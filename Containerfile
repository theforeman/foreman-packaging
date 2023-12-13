FROM centos:stream8

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en

RUN echo "[git-annex]" >> /etc/yum.repos.d/git-annex.repo \
         && echo "name=git-annex" >> /etc/yum.repos.d/git-annex.repo \
         && echo "baseurl='https://downloads.kitenet.net/git-annex/linux/current/rpms/'" >> /etc/yum.repos.d/git-annex.repo \
         && echo "gpgcheck=0" >> /etc/yum.repos.d/git-annex.repo \
         && echo "enabled=1" >> /etc/yum.repos.d/git-annex.repo

RUN dnf -y module enable nodejs:14 ruby:2.7
RUN dnf -y install nodejs vim git rpmdevtools git-annex-standalone wget python3 ruby jq ruby-devel make gcc-c++ postgresql-devel libvirt-devel libxml2-devel libcurl-devel systemd-devel

RUN npm install npm2rpm --global

RUN pip3 install packaging requests ruamel-yaml

RUN mkdir -p /opt/foreman-packaging
WORKDIR /opt/foreman-packaging
