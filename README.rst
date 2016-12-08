PonyORM integration for Morepath
===================================

Demonstrate PonyORM integration with Morepath.

Installation
------------

You can use pip in a virtual env::

  $ virtualenv env
  $ source env/bin/activate
  (env) $ pip install -Ue .

Then to run the web server::

  (env) $ run-app

You can now access the application through http://localhost:5000

For installing the test suite and running the tests use::

  (env) $ pip install -e '.[test]'
  (env) $ py.test
