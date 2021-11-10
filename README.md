# pyrdapd
Python RDAP Daemon

Implementation of [rfc7482](https://datatracker.ietf.org/doc/html/rfc9082) in python

With tests.

RDAP is an HTTP service which takes input as GET and HEAD.  It emits JSON as per [rfc9083](https://datatracker.ietf.org/doc/html/rfc9083)

Let us consider implementing the HTTP server using the [Web Server Gateway Interface](https://www.fullstackpython.com/wsgi-servers.html)

## Creating a virtual environment

Use [virtualenv](https://docs.python.org/3/library/venv.html) to create somewhere to build and install python packages.

```
c:> cd %HOME%\Desktop\src\
c:> pip install virtualenv
c:> virtualenv pyrdapd-venv
c:> pyrdapd-venv\Scripts\activate.bat
```