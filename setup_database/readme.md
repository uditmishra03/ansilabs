## Problem Statement:

Values of variables

Make sure to create hosts.ini file like this:

[all]  # This group name should match the group used in your playbook
server1 ansible_host=server1 ansible_user=server1_admin ansible_ssh_pass='server1_admin@123!' ansible_become=true ansible_become_pass='server1_admin@123!'

In order to configure mysql and postgress properly, make sure to create this mysql.cnf.j2 and postgresql.conf.j2 in /home/user:

vi mysql.cnf.j2

# MySQL configuration settings
[mysqld]
bind-address = 0.0.0.0
max_connections = 150

vi postgresql.conf.j2

# PostgreSQL Configuration File
listen_addresses = '*'
max_connections = 100
shared_buffers = 128MB

Write a playbook named setup_db.yaml that performs different tasks based on the values of variables:

    If the variable db_engine is set to mysql, install MySQL and configure it using MySQL-specific settings.
    If the variable db_engine is set to postgresql, install PostgreSQL and configure it with PostgreSQL-specific settings.
    Ensure that the database-specific tasks are executed based on the value of db_engine.


### Command to run: 

* ansible-playbook setup_db.yaml -i hosts.ini 
