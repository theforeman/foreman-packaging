FROM centos:8

RUN dnf -y install dnf-utils

RUN mkdir -p /app/repoclosure
WORKDIR /app/repoclosure

ENTRYPOINT ["/usr/bin/dnf", "repoclosure"]
