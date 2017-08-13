======================
Anime Related Crawlers
======================

A collection of self-using anime-related crawlers.

Supported sites:

- Image crawler for danbooru.donmai.us, deviantart.com
- File crawler for sakugabooru.com
- Torrent crawler for nyaa.si, share.dmhy.org, acg.rip, bangumi.moe
- Anime infomation crawler for bangumi.tv


Structure
=========

.. code-block::

    .
    ├── Pipfile             # Python package management
    ├── README.rst
    ├── Pipfile.lock
    ├── scrapy.cfg          # scrapy config file
    ├── anime_spiders       # Spiders
    ├── manage.py           # Django manage.py
    ├── exhibition          # Django backend application
    ├── db.sqlite3
    ├── package.json        # Frontend package management
    ├── package-lock.json
    ├── node_modules        # Frontend dependencies
    ├── index.html          # index.html of frontend
    ├── src                 # Frontend application source
    ├── build               # Frontend build
    ├── config              # Frontend code build configs
    ├── dist                # Distribution code of frontend
    └── static              # Frontend related static files


Usage
=====

Development
-----------

* Run frontend: ``npm run dev``;
* Run backend: ``./manage.py runserver``;
* Run a spider:
    * Start a ElasticSearch server at ``192.168.2.10``;
    * Install requirements: ``pipenv install && pipenv install --dev && pipenv shell``;
    * Run spider ``scrapy crawl [spider_name]``;

Terminal
--------

Only scrapy commands supported for now.

Library
-------

You can use it as normal scrapy.Spider of course.

Scrapyd
-------

Not supported yet.

