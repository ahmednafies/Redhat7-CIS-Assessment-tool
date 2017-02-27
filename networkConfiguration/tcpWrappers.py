import os,source


# --- 3.4.1 Ensure TCP Wrappers is installed (Scored) ---#

def check_tcp_wrappers_is_installed():
    config = 'Ensure TCP Wrappers is installed (Scored)'

    command1 = 'rpm -q tcp_wrappers'
    command2 = 'rpm -q tcp_wrappers-libs'
    output = 'not installed'

    print('checking "' + config + '" ..... ')

    terminal_variable = os.popen(command1)
    terminal_output1 = terminal_variable.read()

    terminal_variable = os.popen(command2)
    terminal_output2 = terminal_variable.read()

    if output in terminal_output1 and output in terminal_output2:
        print("Your system has NOT been configured correctly")
        print('WARNING: please check the benchmark "' + config + '" ')
        print('-----------------------------------------------------')
        return True
    else:
        print('test was successful ... ')
        print('-----------------------------------------------------')
        return False

# --- 3.4.3 Ensure /etc/hosts.deny is configured (Scored) ---- #

def check_etc_hosts_deny_is_configured():
    config = '3.4.3 Ensure /etc/hosts.deny is configured (Scored)'
    command = 'cat /etc/hosts.deny'
    output = 'ALL: ALL'
    source.output_isIn_terminal_output(config,command,output)

# ---- 3.4.4 Ensure permissions on /etc/hosts.allow are configured (Scored) ---#

def check_permissions_on_etc_hosts_allow_isConfigured():

    config = '3.4.4 Ensure permissions on /etc/hosts.allow are configured (Scored)'
    command = 'stat /etc/hosts.allow'
    output = 'Access:(0644/-rw-r--r--)Uid:(0/root)Gid:(0/root)'

    print('checking "'+ config +'" ..... ')
    terminal_variable = os.popen(command)
    terminal_output = terminal_variable.read().replace(' ','')

    if output in terminal_output:
        print('test was successful ... ')
        print('-----------------------------------------------------')

        return True
    else:
        print("Your system has NOT been configured correctly")
        print('WARNING: please check the benchmark "'+config+'" ')
        print('-----------------------------------------------------')
        return False

# ---- 3.4.4 Ensure permissions on /etc/hosts.deny are configured (Scored) ---#

def check_permissions_on_etc_hosts_deny_isConfigured():

    config = '3.4.5 Ensure permissions on /etc/hosts.deny are configured (Scored)'
    command = 'stat /etc/hosts.allow'
    output = 'Access:(0644/-rw-r--r--)Uid:(0/root)Gid:(0/root)'

    print('checking "'+ config +'" ..... ')
    terminal_variable = os.popen(command)
    terminal_output = terminal_variable.read().replace(' ','')

    if output in terminal_output:
        print('test was successful ... ')
        print('-----------------------------------------------------')

        return True
    else:
        print("Your system has NOT been configured correctly")
        print('WARNING: please check the benchmark "'+config+'" ')
        print('-----------------------------------------------------')
        return False
