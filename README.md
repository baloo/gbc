Git buildpackage CI
===================

This tool is a wrapper around the excellent git-buildpackage:
  https://honk.sigxcpu.org/piki/projects/git-buildpackage/


It will build a package with jenkins (or any other CI-service) if the package respects the following scheme:

```

[] marks branches
() marks tags

   o
   |
   o (0.0.1)
   |\
   | \
   |  o (debian/0.0.1-1)
   o  |
   |  |
   |  o [debian/0.0.1-x]
   o  |
   |  |
   o  |  (0.0.2)
   |\ |
   | \|
   |  o (debian/0.0.2-1) [debian/0.0.2-x] [debian/master]
   |
   o [master]

```

Consider a tag named "T", then gbc will build a package with T as upstream and tag debian/T-N as debian.
N beeing a increment for the debian package version. This package will be put in the stable output directory

Consider a tag named "T", then gbc will build a package with T as upstream and debian/T-x as debian branch
The output will be put in testing output directory

Condider a branch named "B" then gbc will build a package with B as upstream and debian/B as debian branch
the output will be put in unstable output directory


Development environment
-----------------------

```
virtualenv env

. env/bin/activate

python setup.py develop
```




cowbuilder --create --distribution squeeze --debootstrapopts --arch --debootstrapopts amd64 --debootstrap cdebootstrap --basepath /var/cache/pbuilder/base-squeeze-amd64.cow

