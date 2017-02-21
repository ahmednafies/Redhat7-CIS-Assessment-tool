import os
import source

#------ 1.6.1.1 Ensure SELinux is not disabled in bootloader configuration-----#

def check_SElinux_notDisabled_in_bootloader():

    config = '1.6.1.1 Ensure SELinux is not disabled in bootloader configuration'
    command = 'sudo grep "^\s*linux" /boot/grub2/grub.cfg'
    output1 = 'selinux=0'
    output2 = 'enforcing=0'

    print('checking "' + config + '" ..... ')
    terminal_variable = os.popen(command)
    terminal_output = terminal_variable.read()


    if (output1 in terminal_output) or (output2 in terminal_output):
        print("Your system has NOT been configured correctly")
        print('WARNING: please check the benchmark "' + config + '" ')
    else:
        print('test was successful ... ')

    print('-----------------------------------------------------')

# ----- 1.6.1.2 Ensure the SELinux state is enforcing (Scored) ---#

def check_SELinux_state_enforcing():
    config = '1.6.1.2 Ensure the SELinux state is enforcing (Scored)'
    command1 = 'grep SELINUX=enforcing /etc/selinux/config'
    output1 = 'SELINUX=enforcing'
    command2= 'sestatus'

    output2 = 'SELinuxstatus:enabled'
    output3 = 'Currentmode:enforcing'
    output4 = 'Modefromconfigfile:enforcing'

    print('checking "' + config + '" ..... ')
    terminal_variable = os.popen(command1)
    terminal_output1 = terminal_variable.read()

    terminal_variable = os.popen(command2)
    terminal_output2 = terminal_variable.read().replace(' ','')


    if (output1 in terminal_output1 and output2 in terminal_output2):
        if (output3 in terminal_output2 and output4 in terminal_output2):
            print('test was successful ... ')
    else:
        print("Your system has NOT been configured correctly")
        print('WARNING: please check the benchmark "' + config + '" ')

    print('-----------------------------------------------------')

#----- 1.6.1.3 Ensure SELinux policy is configured (Scored) ----#

def check_SELinux_policy_configured():

    config = '1.6.1.3 Ensure SELinux policy is configured (Scored)'
    command1 = 'grep SELINUXTYPE=targeted /etc/selinux/config'
    command2 = 'sestatus'

    output1 = 'SELINUXTYPE=targeted'
    output2 = 'SELINUXTYPE=mls'
    output3 = 'Loadedpolicyname:targeted'
    output4 = 'Loadedpolicyname:mls'

    print('checking "' + config + '" ..... ')

    terminal_variable = os.popen(command1)
    terminal_output1 = terminal_variable.read()

    terminal_variable = os.popen(command2)
    terminal_output2 = terminal_variable.read().replace(' ', '')

    if (output1 in terminal_output1 or output2 in terminal_output1):

        if (output3 in terminal_output2 or output4 in terminal_output2):
            print('test was successful ... ')
        else:
            print("Your system has NOT been configured correctly")
            print('WARNING: please check the benchmark "' + config + '" ')

    else:
        print("Your system has NOT been configured correctly")
        print('WARNING: please check the benchmark "' + config + '" ')

    print('-----------------------------------------------------')

#------1.6.1.4 Ensure SETroubleshoot is not installed (Scored)-----#

def check_setTroubleShoot_notInstalled():

    config = '1.6.1.4 Ensure SETroubleshoot is not installed (Scored)'
    command = 'rpm -q setroubleshoot'
    output = 'package setroubleshoot is not installed'
    source.output_isIn_terminal_output(config,command,output)

#----- 1.6.1.5 Ensure the MCS Translation Service (mcstrans) is not installed ---#

def check_mcstrans_notInstalled():
    config = '1.6.1.5 Ensure the MCS Translation Service (mcstrans) is not installed'
    command = 'rpm -q mcstrans'
    output = 'package mcstrans is not installed'
    source.output_isIn_terminal_output(config,command,output)

#----------1.6.1.6 Ensure no unconfined daemons exist (Scored)--------#


def check_noConfined_deamons_exist():

    config = '1.6.1.6 Ensure no unconfined daemons exist (Scored)'
    command = 'ps -eZ | egrep "initrc" | egrep -vw '+'"tr|ps|egrep|bash|awk" | ' + "tr ':' ' ' | awk '{print $NF }'"
    output = ''
    source.output_isEqualTo_terminal_output(config,command,output)

# ------ 1.6.2 Ensure SELinux is installed (Scored) --------#

def check_SElinux_installed():
    config = '1.6.2 Ensure SELinux is installed (Scored)'
    command = 'rpm -q libselinux'
    output = 'not installed'
    source.output_isIn_terminal_output_inverse(config,command,output)

#--------------------------------------------------------------------#