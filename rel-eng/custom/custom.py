# Copyright (c) 2008-2014 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public License,
# version 2 (GPLv2). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#
# Red Hat trademarks are not licensed under GPLv2. No permission is
# granted to use or replicate Red Hat trademarks that are incorporated
# in this software or its documentation.

from datetime import datetime
import json
import os
import os.path
import re
import shutil
import urllib
from zipfile import ZipFile

from tito.builder.fetch import SourceStrategy
from tito.common import error_out, debug, run_command


class JenkinsSourceStrategy(SourceStrategy):
    """
    Downloads the source files from Jenkins, from a job that produces them as
    artifacts.  Will follow the version number present in the filename and
    adds a timestamp & SHA if available from the Jenkins job start reasons.

    Designed to be used for nightly or pull request builds only.

    It first copies source files from git, then downloads the Jenkins
    artifacts over the top, so they're merged (patches etc can then be stored
    in git).

    Takes the following arguments:
      jenkins_url: base URL of Jenkins ("http://ci.theforeman.org")
      jenkins_job: name of job ("test_develop")
      jenkins_job_id: job number or alias ("123", "lastSuccessfulBuild")
    """
    def fetch(self):
        url_base = self.builder.args['jenkins_url']
        job_name = self.builder.args['jenkins_job']
        if 'jenkins_job_id' in self.builder.args:
            job_id = self.builder.args['jenkins_job_id']
        else:
            job_id = "lastSuccessfulBuild"
        job_url_base = "%s/job/%s/%s" % (url_base, job_name, job_id)
        json_url = "%s/api/json" % job_url_base

        job_info = json.loads(urllib.urlopen(json_url).read())
        if "number" in job_info:
            job_id = job_info["number"]

        if "runs" in job_info:
            run_idx = 0
            for idx, run in enumerate(job_info["runs"]):
                if run["number"] == job_id:
                    run_idx = idx
                    break
            job_url_base = job_info["runs"][run_idx]["url"]
        elif "url" in job_info:
            job_url_base = job_info["url"]

        url = "%s/artifact/*zip*/archive.zip" % job_url_base
        debug("Fetching from %s" % url)

        (zip_path, zip_headers) = urllib.urlretrieve(url)
        zip_file = ZipFile(zip_path, 'r')
        try:
            zip_file.extractall(self.builder.rpmbuild_sourcedir)
        finally:
            zip_file.close()

        # Copy the live spec from our starting location. Unlike most builders,
        # we are not using a copy from a past git commit.
        self.spec_file = os.path.join(self.builder.rpmbuild_sourcedir,
                    '%s.spec' % self.builder.project_name)
        shutil.copyfile(
            os.path.join(self.builder.start_dir, '%s.spec' %
                self.builder.project_name),
            self.spec_file)
        for s in os.listdir(self.builder.start_dir):
            if os.path.exists(os.path.join(self.builder.start_dir, s)):
                shutil.copyfile(
                    os.path.join(self.builder.start_dir, s),
                    os.path.join(self.builder.rpmbuild_sourcedir, os.path.basename(s)))
        print("  %s.spec" % self.builder.project_name)

        i = 0
        replacements = []
        src_files = run_command("find %s -type f" %
              os.path.join(self.builder.rpmbuild_sourcedir, 'archive')).split("\n")
        for s in src_files:
            base_name = os.path.basename(s)
            debug("Downloaded file %s" % base_name)
            if ".tar" not in base_name and ".gem" not in base_name:
                debug("Skipping %s as it isn't a source archive" % base_name)
                continue

            dest_filepath = os.path.join(self.builder.rpmbuild_sourcedir,
                    base_name)
            shutil.move(s, dest_filepath)
            self.sources.append(dest_filepath)

            # Add a line to replace in the spec for each source:
            source_regex = re.compile("^(source%s:\s*)(.+)$" % i, re.IGNORECASE)
            new_line = "Source%s: %s\n" % (i, base_name)
            replacements.append((source_regex, new_line))
            i += 1

        # Replace version in spec:
        version_regex = re.compile("^(version:\s*)(.+)$", re.IGNORECASE)
        self.version = self._get_version()
        print("Building version: %s" % self.version)
        replacements.append((version_regex, "Version: %s\n" % self.version))
        self.replace_in_spec(replacements)

        rel_date = datetime.utcnow().strftime("%Y%m%d%H%M")
        gitrev = ""
        for action in job_info["actions"]:
            if "lastBuiltRevision" in action:
                gitrev = "git%s" % action["lastBuiltRevision"]["SHA1"][0:7]
        self.release = rel_date + gitrev
        print("Building release: %s" % self.release)
        run_command("sed -i '/^Release:/ s/%%/.%s%%/' %s" % (self.release, self.spec_file))

    def _get_version(self):
        """
        Get the version from the builder.
        Sources are configured at this point.
        """
        # Assuming source0 is a tar.gz we can extract a version from:
        base_name = os.path.basename(self.sources[0])
        debug("Extracting version from: %s" % base_name)

        # Example filename: tito-0.4.18.tar.gz:
        simple_version_re = re.compile(".*-(.*).(tar.gz|tgz|zip|tar.bz2|gem)")
        match = re.search(simple_version_re, base_name)
        if match:
            version = match.group(1)
        else:
            error_out("Unable to determine version from file: %s" % base_name)

        return version

    def replace_in_spec(self, replacements):
        """
        Replace lines in the spec file using the given replacements.

        Replacements are a tuple of a regex to look for, and a new line to
        substitute in when the regex matches.

        Replaces all lines with one pass through the file.
        """
        in_f = open(self.spec_file, 'r')
        out_f = open(self.spec_file + ".new", 'w')
        for line in in_f.readlines():
            for line_regex, new_line in replacements:
                match = re.match(line_regex, line)
                if match:
                    line = new_line
            out_f.write(line)

        in_f.close()
        out_f.close()
        shutil.move(self.spec_file + ".new", self.spec_file)
