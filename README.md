# pyrdapd
Python RDAP Daemon

Implementation of [rfc7482](https://datatracker.ietf.org/doc/html/rfc9082) in python

With tests.

RDAP is an HTTP service which takes input as GET and HEAD.  It emits JSON as per [rfc9083](https://datatracker.ietf.org/doc/html/rfc9083)

Let us consider implementing the HTTP server as a [Web Server Gateway Interface](https://www.fullstackpython.com/wsgi-servers.html) application.  

The command line interface to launching WSGI applications for development purposes is called [uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/)

## Creating a virtual environment

Use [virtualenv](https://docs.python.org/3/library/venv.html) to create somewhere to build and install python packages.

```
c:> cd %HOME%\Desktop\src\
c:> pip3 install virtualenv
c:> virtualenv pyrdapd-venv
c:> pyrdapd-venv\Scripts\activate.bat
```

Into the newly created virtualenv, you should install the uwsgi package

```
c:> pip3 install uwsgi
c:> uwsgi --http :43 --wsgi-file pyrdapd.py
```
