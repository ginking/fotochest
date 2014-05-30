mysql:
  server:
    root_password: 'somepass'
    bind-address: 127.0.0.1
    port: 3306
    user: mysql

  # Manage databases
  database:
    - fotochest

  # Manage users
  user:
    - name: dstegelman
      password: '1234'
      host: localhost
      databases:
        - database: fotochest
          grants: ['all privileges']

  # Override any names defined in map.jinja
  lookup:
    server: mysql-server
    client: mysql-client
    service: mysql-service
    config: /etc/mysql/my.cnf
    python: python-mysqldb