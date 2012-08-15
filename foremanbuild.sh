#!/bin/bash

sh foremanbuild-srpms.sh

for distro in el5 el6 f16 f17; do
    #Build foreman-proxy for all distros and archs
    for arch in i386 x86_64; do
        mock -r $distro-$arch ~/rpmbuild/SRPMS/foreman-proxy*
        mv /var/lib/mock/$distro-$arch/result/*src.rpm ~/foreman/$distro/source
        mv /var/lib/mock/$distro-$arch/result/*noarch.rpm  ~/foreman/$distro/$arch
    done
    rm -f ~/rpmbuild/SRPMS/foreman-proxy*
   
    #Build foreman for all distros and archs 
    for arch in i386 x86_64; do
        mock -r $distro-$arch ~/rpmbuild/SRPMS/foreman*
        mv /var/lib/mock/$distro-$arch/result/*src.rpm ~/foreman/$distro/source
        mv /var/lib/mock/$distro-$arch/result/*noarch.rpm  ~/foreman/$distro/$arch
    done
    rm -f ~/rpmbuild/SRPMS/foreman*

    # stash changes to foreman.spec so we can checkout next branch
    git stash

done

rsync -avHpz ~/foreman/ account@shell...

for distro in el5 el6 f16 f17; do
   for arch in source i386 x86_64; do
       ssh account@shell... createrepo .../$distro/$arch 
   done
done

#clean up after ourselves
cd; rm -rf ~/rpmbuild
cd; rm -rf ~/foreman
