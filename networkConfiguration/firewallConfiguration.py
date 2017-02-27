import os
import source

# --- 3.6.1 Ensure iptables is installed (Scored) ----#

def check_ip_tables_installed():
    config = '3.6.1 Ensure iptables is installed (Scored)'
    command = 'rpm -q iptables'
    output = 'not installed'
    source.output_isIn_terminal_output_inverse(config,command,output)