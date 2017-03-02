import source
import os
# --- 4.1.1.2 Ensure system is disabled when audit logs are full (Scored) ---#

def check_system_disabled_when_auditLogs_are_full():

    config = '4.1.1.2 Ensure system is disabled when audit logs are full (Scored)'

    command1 = 'sudo grep space_left_action /etc/audit/auditd.conf'
    command2 = 'sudo grep action_mail_acct /etc/audit/auditd.conf'
    command3 = 'sudo grep admin_space_left_action /etc/audit/auditd.conf'

    output1 = 'space_left_action = email'
    output2 = 'action_mail_acct = root'
    output3 = 'admin_space_left_action = halt'

    print('checking "' + config + '" ..... ')

    terminal_variable1 = os.popen(command1)
    terminal_output1 = terminal_variable1.read()

    terminal_variable2 = os.popen(command2)
    terminal_output2 = terminal_variable2.read()

    terminal_variable3 = os.popen(command3)
    terminal_output3 = terminal_variable3.read()


    if (output1 in terminal_output1
        and output2 in terminal_output2
        and output3 in terminal_output3):

        source.return_function(True,config)

    else:
        source.return_function(False,config)

# -- 4.1.1.3 Ensure audit logs are not automatically deleted (Scored) ---#

def check_auditLogs_not_auto_deleted():
    config = '4.1.1.3 Ensure audit logs are not automatically deleted (Scored)'
    command = 'sudo grep max_log_file_action /etc/audit/auditd.conf'
    output = 'max_log_file_action = keep_logs'
    source.output_isIn_terminal_output(config,command,output)

# --- 4.1.2 Ensure auditd service is enabled (Scored) ----#

def check_audit_service_enabled():
    config = '4.1.2 Ensure auditd service is enabled (Scored)'
    command = 'systemctl is-enabled auditd'
    output = 'enabled'
    source.output_isEqualTo_terminal_output(config,command,output)

# --- 4.1.4 Ensure events that modify date and time information are collected(Scored)---#

def check_date_time_modifying_events():
    config = '4.1.4 Ensure events that modify date and time information are collected (Scored)'
    command = 'sudo grep time-change /etc/audit/audit.rules'

    arch = source.check_platform()

    if arch == '64bit':
        output = '-a always,exit -F arch=b64 -S adjtimex -S settimeofday -k time-change ' \
                 '-a always,exit -F arch=b32 -S adjtimex -S settimeofday -S stime -k time-change ' \
                 '-a always,exit -F arch=b64 -S clock_settime -k time-change ' \
                 '-a always,exit -F arch=b32 -S clock_settime -k time-change ' \
                 '-w /etc/localtime -p wa -k time-change'
    else:
        output = '-a always,exit -F arch=b32 -S adjtimex -S settimeofday -S stime' \
                 ' -k time-change-a always,exit -F arch=b32 -S clock_settime -k ' \
                 'time-change-w /etc/localtime -p wa -k time-change'

    source.output_isIn_terminal_output(config,command,output)


#---- 4.1.5 Ensure events that modify user/group information are collected (Scored) ---- #

def check_user_group_modifying_events():

    config = '4.1.5 Ensure events that modify user/group information are collected (Scored)'
    command = 'sudo grep identity /etc/audit/audit.rules'
    output = '-w /etc/group -p wa -k identity ' \
             '-w /etc/passwd -p wa -k identity ' \
             '-w /etc/gshadow -p wa -k identity ' \
             '-w /etc/shadow -p wa -k identity ' \
             '-w /etc/security/opasswd -p wa -k identity'

    source.output_isIn_terminal_output(config,command,output)

# --- 4.1.6 Ensure events that modify the system's network environment are collected (Scored)

def check_system_network_enviroment_events():

    config = "4.1.6 Ensure events that modify the system's network environment are collected (Scored)"
    command = ' sudo grep system-locale /etc/audit/audit.rules'

    arch = source.check_platform()
    if arch == '64bit':
        output = '-a always,exit -F arch=b64 -S sethostname -S setdomainname -k system-locale ' \
                 '-a always,exit -F arch=b32 -S sethostname -S setdomainname -k system-locale ' \
                 '-w /etc/issue -p wa -k system-locale ' \
                 '-w /etc/issue.net -p wa -k system-locale ' \
                 '-w /etc/hosts -p wa -k system-locale ' \
                 '-w /etc/sysconfig/network -p wa -k system-locale'
    else:
        output = '-a always,exit -F arch=b32 -S sethostname -S setdomainname -k system-locale ' \
                 '-w /etc/issue -p wa -k system-locale ' \
                 '-w /etc/issue.net -p wa -k system-locale ' \
                 '-w /etc/hosts -p wa -k system-locale ' \
                 '-w /etc/sysconfig/network -p wa -k system-locale'

    source.output_isIn_terminal_output_inverse(config,command,output)
    