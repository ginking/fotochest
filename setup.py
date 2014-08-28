#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


readme = open('README.md').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'django==1.6.5',
    'south==0.8.4',
    'Pillow==2.4.0',
    'sorl-thumbnail==11.12',
    'django-celery==3.1.10',
    'django-kombu==0.9.4',
    'python-memcached==1.53',
    'sphinx==1.2.2',
    'factory_boy==2.4.1',
    'django-crispy-forms==1.4.0',
    'django-haystack==2.1.0',
    'whoosh==2.5.7',
    'celery==3.1.12',
    'django-bootstrap-static==2.0.2',
    'django-braces==1.4.0',
    'django-chosen==0.1',
    'gunicorn==18.0',
    'django-picklefield',
    'django-locations',
    'django-constance',
]

dep_links = ['http://github.com/dstegelman/django-locations/tarball/master#egg=locations',
             'http://github.com/comoga/django-constance/tarball/master#egg=constance']
test_requirements = requirements + ['coverage==3.7.1', 'pytest']

setup(
    name='fotochest',
    version='3.0.5',
    description='',
    long_description=readme + '\n\n' + history,
    author='Derek Stegelman',
    author_email='email@stegelman.com',
    url='https://github.com/dstegelman/fotochest',
    dependency_links=dep_links,
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='photo',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
    ],
    test_suite='tests',
    tests_require=test_requirements
)