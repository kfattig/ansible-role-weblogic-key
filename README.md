Weblogic key
=========

This role creates weblogic authentication keys using the provided username and password.

Requirements
------------

This role requires WLST on the target host.  It's designed to be run on the AdminServer host, but could be run anywhere with WLST installed.

Role Variables
--------------

Below are the variables in use,  see the defaults file for defaults.

Name|Description
---|---
weblogic_admin|Username to authenticate with Weblogic (must be Admin user)
weblogic_password|Password to authenticate with Weblogic
t3_url|T3 URL to connect to Weblogic AdminServer
script_temp_location|Location to stage WLST scripts
oracle_user|User that owns weblogic installation (used for ownership of WLST scripts)
oracle_group|Group that owns weblogic installation (used for ownership of WLST scripts)
domain_name|Name of the weblogic domain
wlst_script|Path to WLST script
key_file |Path to store key file
config_file|Path to store config file

Dependencies
------------

No Dependencies

Example Playbook
----------------

This sample creates files in tmp

    - name: create files
    hosts: weblogic_admin_host
    become: yes
    become_user: mwadmin
    roles:
    - role: weblogic_key
    vars:
      config_file: /tmp/config_file
      key_file: /tmp/key_file


Author Information
------------------

kyle.fattig@zirous.com
