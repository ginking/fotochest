"""
FotoChest

"""

from setuptools import setup, find_packages

from fotochest.defaults import VERSION_NUMBER

version = VERSION_NUMBER

install_requires = [
    'django==1.4.1',
    'south==0.7.6',
    'hadrian==1.1.4',
    'PIL==1.1.7',
    'sorl-thumbnail==11.12',
    'django-celery==2.5.5',
    'django-kombu==0.9.4',
    'django-tastypie==0.9.11',
    'python-memcached==1.48',
    'sphinx==1.1.3',
    'django-api-docs==1.1.1',
    'django-mail-queue==1.1.0',
    'django-taggit==0.9.3',
    'django-crispy-forms==1.1.4',
    'django-debug-toolbar==0.9.4',
    'django-haystack==1.2.7',
    'whoosh==2.4.1',
    'celery==2.5.5',
    'django-extensions==0.9',
    'django-site-notifications==0.1',
    'django-downtime==0.2',
    'django-bootstrap-static==2.0.2',
    'django-braces==0.1.7',
]

setup(name='fotochest',
    version=version,
    description="A Django driven Photo Sharing application",
    long_description=open("README.md", "r").read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        ],
    keywords='',
    author='Derek Stegelman',
    author_email='dstegelman@gmail.com',
    url='http://github.com/fotochest/fotochest',
    license='MIT',
    packages=find_packages(),
    install_requires = install_requires,
    include_package_data=True,
    zip_safe=False,
)
