FROM --platform=linux/amd64 quay.io/centos/centos:stream10

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en

RUN dnf install -y epel-release && \
    dnf -y install nodejs npm vim git rpmdevtools git-annex wget ruby jq ruby-devel make gcc-c++ mock postgresql-devel libxml2-devel libcurl-devel systemd-devel rpmlint \
    python3 python3-pip python3-ruamel-yaml python3-requests python3-packaging python3-semver

RUN npm install npm2rpm --global

RUN gem install gem2rpm

RUN pip3 install rpmspectool obal

RUN mkdir -p /opt/foreman-packaging
WORKDIR /opt/foreman-packaging
