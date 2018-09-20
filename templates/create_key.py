import sys

connect('{{ weblogic_admin }}','{{ weblogic_password }}','{{ t3_url }}')
storeUserConfig('{{ config_file }}','{{ key_file }}')
disconnect()
exit()

