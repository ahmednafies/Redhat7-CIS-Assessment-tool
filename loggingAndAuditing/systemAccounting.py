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