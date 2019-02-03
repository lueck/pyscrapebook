# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='pyscrapebook',
      version='0.1',
      description='Tools for scraping the web for text data.',
      url='http://github.com/lueck/pyscrapebook',
      author=u"Christian Lück",
      author_email='cluecksbox@gmail.com',
      license='GPLv3',
      packages=['pyscrapebook'],
      zip_safe=False,
      #test_suite='nose.collector',
      #tests_require=['nose'],
      scripts = ["bin/scrapebook"])
