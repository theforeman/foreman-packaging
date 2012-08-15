#!/bin/bash

for distro in el5 el6 f16 f17; do
    #Build foreman-proxy for each arch and distro
    for arch in i386 x86_64; do
        mkdir -p /var/lib/mock/$distro-$arch/result
        sudo mock -r $distro-$arch ~/rpmbuild/SRPMS/foreman-proxy*
        scp /var/lib/mock/$distro-$arch/result/*src.rpm account@shell.../$distro/source
        scp /var/lib/mock/$distro-$arch/result/*noarch.rpm  account@shell.../$distro/$arch
    done
    rm -f ~/rpmbuild/SRPMS/foreman-proxy*

    #Build foreman for each arch and distro
    for arch in i386 x86_64; do
        mock -r $distro-$arch ~/rpmbuild/SRPMS/foreman*
        scp /var/lib/mock/$distro-$arch/result/*src.rpm account@shell.../$distro/source
        scp /var/lib/mock/$distro-$arch/result/*noarch.rpm account@shell.../$distro/$arch
    done


   #Update repo files for each arch and distro
   for arch in source i386 x86_64; do
       ssh account@shell createrepo .../$distro/$arch 
   done

   # stash changes to foreman.spec so we can checkout next branch
   git stash
done

#clean up after ourselves
cd; rm -rf ~/rpmbuild
