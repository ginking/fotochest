from setuptools import setup

version = '3.2.0'

REQUIREMENTS = ['django>=1.7.1,<1.8',
                'django-locations-base==0.2.2',
                'Pillow>=2.5.0,<3.0.0',
                'sorl-thumbnail==12.2',
                'django-crispy-forms==1.4.0',
                'celery[redis]==3.1.17',
                'django-bootstrap-static==2.0.2',
                'django-braces==1.4.0',
                'django-constance==1.0.1',
                'django-chosen==0.1',
                'djangorestframework==3.0.5',
                'markdown==2.6',
                'django-picklefield==0.3.1',
                'gunicorn==19.2.1',
                'mysqlclient==1.3.5',
                'django-redis_cache==0.13.0',
                'hiredis==0.1.6']

setup(name='fotochest',
      version=version,
      description="Photo Sharing with Django",
      long_description=open("README.md", "r").read(),
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Web Environment",
          "Intended Audience :: End Users/Desktop",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Framework :: Django",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License",
          ],
      keywords='',
      author='Derek Stegelman',
      author_email='dstegelman@gmail.com',
      url='http://github.com/dstegelman/fotochest',
      license='MIT',
      packages=['fotochest'],
      include_package_data=True,
      zip_safe=False,
      scripts=['manage.py'],
      install_requires=REQUIREMENTS
)