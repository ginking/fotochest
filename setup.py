from setuptools import setup, find_packages

version = '2.3'

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
    install_requires = ['django==1.4',],
    include_package_data=True,
    zip_safe=False,
)
