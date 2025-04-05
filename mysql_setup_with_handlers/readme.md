#### Command:

ansible-playbook mysql_playbook.yaml 
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [Mysql Setup] **************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************
ok: [localhost]

TASK [mysql_setup : Install MySQL Server] ***************************************************************************************************
ok: [localhost]

TASK [mysql_setup : Ensure MySQL is running] ************************************************************************************************
ok: [localhost]

PLAY RECAP **********************************************************************************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
