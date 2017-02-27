import os
import source

# --- 2.3.1 Ensure NIS Client is not installed (Scored) ---#
def check_NIS_Client_not_installed():

    config = '2.3.1 Ensure NIS Client is not installed (Scored)'
    command = 'rpm -q ypbind'
    output = 'not installed'
    source.output_isIn_terminal_output(config,command,output)

#---- 2.3.2 Ensure rsh client is not installed (Scored) --- #
def check_rsh_client_not_installed():
    config = '2.3.2 Ensure rsh client is not installed (Scored)'
    command = 'rpm -q rsh'
    output = 'not installed'
    source.output_isIn_terminal_output(config,command,output)

# ---- 2.3.3 Ensure talk client is not installed (Scored) --- #

def check_talk_client_not_installed():
    config = '2.3.3 Ensure talk client is not installed (Scored)'
    command = 'rpm -q talk'
    output = 'not installed'
    source.output_isIn_terminal_output(config,command,output)

# --- 2.3.4 Ensure telnet client is not installed (Scored) --- #

def check_telnet_client_not_installed():
    config = '2.3.4 Ensure telnet client is not installed (Scored)'
    command = 'rpm -q telnet'
    output = 'not installed'
    source.output_isIn_terminal_output(config,command,output)


# ---- 2.3.5 Ensure LDAP client is not installed (Scored) ---#

def check_LDAP_client_not_installed():
    config = '2.3.5 Ensure LDAP client is not installed (Scored)'
    command = 'rpm -q openldap-clients'
    output = 'not installed'
    source.output_isIn_terminal_output(config,command,output)

#------------------------------------------------------------------------#