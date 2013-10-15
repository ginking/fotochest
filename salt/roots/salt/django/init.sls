include:
- python
- users

/home/vagrant/.virtualenvs/fotochest:
    virtualenv.managed:
        - no_site_packages: True
        - runas: vagrant
        - require:
            - pkg: python-virtualenv
            - pkg: libxml2-dev
            - pkg: libxslt-dev
            - pkg: libevent-dev