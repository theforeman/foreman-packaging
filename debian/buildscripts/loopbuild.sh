#!/bin/bash

# Sample script to loop over a set of package builds

# Debian 6
sudo ./buildpackage.sh squeeze64 debian/squeeze/stable/foreman-proxy
sudo ./buildpackage.sh squeeze32 debian/squeeze/stable/foreman-proxy

sudo ./buildpackage.sh squeeze64 debian/squeeze/nightly/foreman-proxy
sudo ./buildpackage.sh squeeze32 debian/squeeze/nightly/foreman-proxy

# Ubuntu 12.04 LTS
sudo ./buildpackage.sh precise64 debian/precise/stable/foreman-proxy
sudo ./buildpackage.sh precise32 debian/precise/stable/foreman-proxy

sudo ./buildpackage.sh precise64 debian/precise/nightly/foreman-proxy
sudo ./buildpackage.sh precise32 debian/precise/nightly/foreman-proxy
