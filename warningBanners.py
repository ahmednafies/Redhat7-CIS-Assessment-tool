import os
import source
import shlex
from subprocess import Popen,PIPE
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

# ----- 1.7.2 Ensure GDM login banner is configured (Scored) ---- #

def check_file_exits():
    command = 'ls /etc/dconf/profile/ | grep gdm'
    output = 'gdm'
    terminal_variable = os.popen(command)
    terminal_output = terminal_variable.read()

    if output in terminal_output:
        return True
    else:
        return False


def check_file_contents():
    command = "egrep -r 'user-db:user|system-db:gdm|file-db:/usr/share/gdm/greeter-dconf-defaults' /etc/dconf/profile/gdm"
    output1 = 'user-db:user'
    output2 = 'system-db:gdm'
    output3 = 'file-db:/usr/share/gdm/greeter-dconf-defaults'

    terminal_variable = os.popen(command)
    terminal_output = terminal_variable.read()

    if output1 in terminal_output:
        if output2 in terminal_output:
            if output3 in terminal_output:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def check_gdm_login_banner_configured():

    config = '1.7.2 Ensure GDM login banner is configured (Scored)'
    print('checking "' + config + '" ..... ')


    gdm_file_exits = check_file_exits()
    gdm_file_contents = check_file_contents()

    if (gdm_file_exits == False):
        print('gdm file does not exist')
        return False
    else:
        if (gdm_file_contents == False):
            print("Your system has NOT been configured correctly")
            print('WARNING: please check the benchmark "' + config + '" ')
            print('-----------------------------------------------------')
            return False
        else:
            print('test was successful ... ')
            print('-----------------------------------------------------')

# ----- 1.8 Ensure updates, patches, and additional security software are installed (Not Scored) ----#
def check_updates_patches_installed():

    config = '1.8 Ensure updates, patches, and additional security software are installed (Not Scored)'
    print('checking "' + config + '" ..... ')

    command = 'yum check-update'

    process = Popen(shlex.split(command), stdout=PIPE)
    process.communicate()  # execute it, the output goes to the stdout
    exit_code = str(process.wait())

    if '100' in exit_code:
        source.return_function(False,config)
    elif '0' in exit_code:
        source.return_function(True,config)
    else:
        print('error')


