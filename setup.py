#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
 
setup(
    name='django-scheduler',
    version='0.5b',
    description='A calendaring app for Django.',
    author='Michael Shestakov',
    author_email='mshestakov57@gmail.com',
    url='https://github.com/jellojunkie/django-scheduler',
    packages=[
        'schedule',
        'schedule.feeds',
        'schedule.management',
        'schedule.management.commands',
        'schedule.models',
        'schedule.templatetags',
        'schedule.tests',
    ],
    include_package_data=True,
    zip_safe=False,
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Utilities'],
    install_requires=['setuptools', 'vobject', 'python-dateutil'],
    license='BSD',
    test_suite = "schedule.tests",
)
