#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages
from finddata import find_package_data

setup(
    name = 'Feedjack',
    version = '0.9.16',
    url = 'http://www.feedjack.org/',
    author = 'Gustavo Picón',
    author_email = 'gpicon@gmail.com',
    license = 'BSD',
    packages = find_packages(),
    package_data = find_package_data(where='feedjack', package='feedjack'),
    scripts = ['feedjack/bin/feedjack_update.py'],
    zip_safe = False,
    description = 'Multisite Feed Agregator (Planet)',
    long_description = '''
Feedjack is a feed aggregator writen in Python using the Django web development
framework.

Like the Planet feed aggregator:

    * It downloads feeds and aggregate their contents in a single site
    * The new aggregated site has a feed of its own (atom and rss)
    * It uses Mark Pilgrim’s excelent FeedParser
    * The subscriber list can be exported as OPML and FOAF

But FeedJack also has some advantages:

    * It handles historical data, you can read old posts
    * It parses a lot more info, including post categories
    * It generates pages with posts of a certain category
    * It generates pages with posts from a certain subscriber
    * It generates pages with posts of a certain category from a certain
       subcriber
    * A cloud tag/folksonomy (hype 2.0 compliant) for every page and every
      subscriber
    * It uses Django templates
    * The administration is done via web (using Django's kickass autogenerated
      and magical admin site), and can handle multiple planets
    * Extensive use of django’s internal cache engine. Most of the time you
      will have no database hits when serving pages.''',
)

