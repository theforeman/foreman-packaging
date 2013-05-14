# Source

https://github.com/domcleal/rkerberos/archive/rkerberos-0.1.1.zip

# To build

* Unzip source
* Move `debian/` into source
* Cd into source
* `sudo pdebuild-<os>`

# Notes

* Builds fine for Wheezy.
* Drop gem2deb requirement to 0.2.0 for Squeeze/Precise
* Add squeeze-backports to pdebuild apt hook for Squeeze
