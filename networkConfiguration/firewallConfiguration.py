import os
import source

# --- 3.6.1 Ensure iptables is installed (Scored) ----#

def check_ip_tables_installed():
    config = '3.6.1 Ensure iptables is installed (Scored)'
    command = 'rpm -q iptables'
    output = 'not installed'
    source.output_isIn_terminal_output_inverse(config,command,output)

# ---- 3.6.2 Ensure default deny firewall policy (Scored) ---#

def check_default_deny_firewall_policy():

    config = 'Ensure default deny firewall policy (Scored)'
    command = 'sudo iptables -L'

    print('checking "'+ config +'" ..... ')

    output1 = 'Chain INPUT (policy DROP)'
    output2 = 'Chain FORWARD (policy DROP)'
    output3 = 'Chain OUTPUT (policy DROP)'

    terminal_variable = os.popen(command)
    terminal_output = terminal_variable.read()


    if (output1 in terminal_output and
        output2 in terminal_output and
        output3 in terminal_output):

        source.return_function(True,config)
    else:
        source.return_function(False,config)

