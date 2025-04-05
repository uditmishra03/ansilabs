## Problem statement:

Write a playbook that performs different tasks based on the values of variables:

    If the variable db_engine is set to mysql, install MySQL and configure it using MySQL-specific settings.
    If the variable db_engine is set to postgresql, install PostgreSQL and configure it with PostgreSQL-specific settings.
    Ensure that the database-specific tasks are executed based on the value of db_engine.
