#FotoChest

[![Build Status](https://secure.travis-ci.org/fotochest/fotochest.png?branch=master)](http://travis-ci.org/fotochest/fotochest)

![Progress](http://progressed.io/bar/60)

FotoChest is a open source photo sharing/gallery solution that you can host yourself.  One of the primary goals
in developing FotoChest is to always provide easy access to your photos and data through APIs.

FotoChest is a Python application that runs on Python3

## Developing

Development is done using Salt and Vagrant so you'll need vagrant, salty-vagrant, and virtualbox to get started.

To get the development environment up and running simply:

```
vagrant up
```

This will take a while so go grab some coffee.

```
vagrant ssh
source .virtualenvs/fotochest/bin/activate
./manage.py runserver 0.0.0.0:8000

```

### Run the Test Suite

```
vagrant ssh
source .virtualenvs/fotochest/bin/activate
cd fotochest


py.test fotochest --flakes
```


For more detailed documentation:


http://readthedocs.org/docs/fotochest/en/latest/


##In Action

http://photos.stegelman.com/

##Road Map

https://github.com/fotochest/fotochest/wiki/Roadmap

###Thanks

* https://github.com/blueimp/Bootstrap-Image-Gallery/
* https://github.com/blueimp/jQuery-File-Upload/
