Make this changes in /etc/salt/master which is the configuration file of salt master

# The address of the interface to bind to:
interface: your_master_machine's_IP (eg : 192.100.11.10)

# modified files cause conflicts, set verify_env to False.
user: root (necessary for eauth to function) 

# The external auth system uses the Salt auth modules to authenticate and
# validate users to access areas of the Salt system.
external_auth:
  pam:
    user1:
      - .*
      - '@runner'
      - '@wheel'
      - '@jobs'

rest_cherrypy:
  port: 8000 (port of your choice)
  disable_ssl: True

netapi_enable_clients:
    - local
    - local_async
    - runner
    - wheel
    
Make this changes in /etc/salt/minion which is the configuration file of salt minion

# resolved, then the minion will fail to start.
master: your_master's_IP_address

# same machine but with different ids, this can be useful for salt compute
# clusters.
id: Minion1 (give your Minion name for ease)

Documentations referred :
https://docs.saltproject.io/en/latest/ref/netapi/all/salt.netapi.rest_cherrypy.html
https://docs.saltproject.io/en/latest/ref/modules/all/salt.modules.schedule.html 
