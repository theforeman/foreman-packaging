#!/bin/bash

#clone rpm spec files, patches, and sources, and stage everything
cd; git clone https://github.com/skottler/foreman-rpms.git rpmbuild
cd rpmbuild; git config user.name nightly
rpmdev-setuptree
cd ~/rpmbuild/SOURCES; git clone https://github.com/theforeman/foreman.git -b develop; git clone git://github.com/theforeman/smart-proxy.git -b develop ./foreman-proxy; tar jcvf foreman-proxy-1.0.0.tar.bz2 foreman-proxy; tar jcvf foreman-1.0.0.tar.bz2 foreman; 

for distro in el5 el6 f16 f17; do
    mkdir -p ~/foreman/$distro/{source,i386,x86_64}
    git checkout $distro

    #Build the SRPMS for mock to work with
    rpmbuild -bs --define "_source_filedigest_algorithm md5" --define "_binary_filedigest_algorithm md5" ~/rpmbuild/SPECS/foreman.spec
    rpmbuild -bs --define "_source_filedigest_algorithm md5" --define "_binary_filedigest_algorithm md5" ~/rpmbuild/SPECS/foreman-proxy.spec

    # stash changes to foreman.spec so we can checkout next branch
    git stash

done
