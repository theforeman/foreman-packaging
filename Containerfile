FROM --platform=linux/amd64 quay.io/centos/centos:stream9

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en

RUN echo "[git-annex]" >> /etc/yum.repos.d/git-annex.repo \
         && echo "name=git-annex" >> /etc/yum.repos.d/git-annex.repo \
         && echo "baseurl='https://downloads.kitenet.net/git-annex/linux/current/rpms/'" >> /etc/yum.repos.d/git-annex.repo \
         && echo "gpgcheck=0" >> /etc/yum.repos.d/git-annex.repo \
         && echo "enabled=1" >> /etc/yum.repos.d/git-annex.repo

RUN dnf -y module enable nodejs:18

RUN dnf install -y epel-release && \
    dnf -y install nodejs vim git rpmdevtools git-annex-standalone wget ruby jq ruby-devel make gcc-c++ mock postgresql-devel libxml2-devel libcurl-devel systemd-devel rpmlint \
    python3 python3-pip python3-ruamel-yaml python3-requests python3-packaging

RUN npm install npm2rpm --global

RUN gem install gem2rpm

RUN pip3 install rpmspectool obal

RUN mkdir -p /opt/foreman-packaging
WORKDIR /opt/foreman-packaging
