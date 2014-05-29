ruby-wrapper
============

Wrapper for RHSCL ruby


%{scl_prefix}-ruby-wrapper

This is just a tiny wrapper script to be used as a shim where useful. It is
used in OpenShift Origin for RHEL+RHSCL installs and it's been packaged 
independently in hopes it might be useful for others.

You should find an example script in your docdir (most likely
/usr/share/doc/%{scl_prefix}-ruby-wrapper/)


Note: There some modifications happening in the rpm spec file to make this 
SCL agnostic in an attempt to be ready for the future so if you use this at
face value it's not going to work and you need to change FIXMESCL in 
ruby-wrapper and install it as /usr/bin/${SCL_NAME}-ruby (such that SCL_NAME
were treated like a shell variable).
