virtualenv-installed:
    cmd.run:
        - name: mkdir -p /home/vagrant/.virtualenvs
        - user: vagrant

configure-vm:
    cmd.run:
        - name: virtualenv /home/vagrant/.virtualenvs/fotochest
        - user: vagrant
        - unless: ls -nd /home/vagrant/.virtualenvs | grep -q "fotochest"
