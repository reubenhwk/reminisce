#!/usr/bin/env python

from setuptools import setup

setup(name='HelloFlask',
    version='0.1',
    packages=['helloflask'],
    include_package_data=True,
    zip_safe=False,
    data_files=[
        ('/var/www/helloflask', ['helloflask.wsgi']),
        ('/etc/httpd/conf.d', ['helloflask.conf']),
    ]
)

