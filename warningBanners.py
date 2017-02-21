import os
import source

#----------1.7.1.1 Ensure message of the day is configured properly (Scored)------#

def check_message_of_the_day_configured():
    config = '1.7.1.1 Ensure message of the day is configured properly (Scored)'
    command = "egrep '(\\v|\\r|\\m|\\s)' /etc/motd"
    output = ''
    source.output_isEqualTo_terminal_output(config,command,output)

# ------ 1.7.1.2 Ensure local login warning banner is configured properly (Not Scored)----#

def check_localLogin_warningBanner_configured():
    config = '1.7.1.2 Ensure local login warning banner is configured properly (Not Scored)'
    command = "egrep '(\\v|\\r|\\m|\\s)' /etc/issue"
    output = ''
    source.output_isEqualTo_terminal_output(config,command,output)

#----- 1.7.1.3 Ensure remote login warning banner is configured properly (Not Scored)------#

def check_remotelogin_warningBanner_configured():
    config = '1.7.1.3 Ensure remote login warning banner is configured properly (Not Scored)'
    command = "egrep '(\\v|\\r|\\m|\\s)' /etc/issue.net"
    output = ''
    source.output_isEqualTo_terminal_output(config,command,output)

# ---- 1.7.1.4 Ensure permissions on /etc/motd are configured (Not Scored) ---- #
def check_permissions_on_etc_motd():

    config = '1.7.1.4 Ensure permissions on /etc/motd are configured (Not Scored)'
    command = 'stat /etc/motd'
    output = 'Uid:(0/root)Gid:(0/root)'

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

## --1.7.1.5 Ensure permissions on /etc/issue are configured (Scored)---#

def check_permissions_on_etc_issue():

    config = '1.7.1.5 Ensure permissions on /etc/issue are configured (Scored)'
    command = 'stat /etc/issue'
    output = 'Uid:(0/root)Gid:(0/root)'

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

# ---- 1.7.1.6 Ensure permissions on /etc/issue.net are configured (Not Scored) --#

def check_permissions_on_etc_issue_net():

    config = '1.7.1.5 Ensure permissions on /etc/issue.net are configured (Scored)'
    command = 'stat /etc/issue.net'
    output = 'Uid:(0/root)Gid:(0/root)'

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
