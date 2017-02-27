import inetdServices
import timeSynchronization

def services_check():
    inetdServices.check_charge_services_not_enabled()
    inetdServices.check_daytime_services_not_enabled()
    inetdServices.check_discard_services_not_enabled()
    inetdServices.check_echo_services_not_enabled()
    inetdServices.check_time_services_not_enabled()
    inetdServices.check_tftp_server_not_enabled()
    inetdServices.check_xinetd_not_enabled()

def special_purpose_services_check():
    timeSynchronization.check_time_sync_is_used()
    timeSynchronization.check_ntp_configured()
    timeSynchronization.check_chrony_is_configured()
    timeSynchronization.check_x_window_system_not_installed()
    timeSynchronization.check_Avahi_server_not_enabled()
    timeSynchronization.check_CUPS_is_not_enabled()
    timeSynchronization.check_DHCP_server_is_not_enabled()
    timeSynchronization.check_LDAP_server_is_not_enabled()
    timeSynchronization.check_NFS_and_RPC_not_installed()
    timeSynchronization.check_DNS_server_not_enabled()
    timeSynchronization.check_ftp_server_not_enabled()
    timeSynchronization.check_http_server_not_enabled()
    timeSynchronization.check_IMAP_and_POP3_server_not_enabled()
    timeSynchronization.check_samba_is_not_enabled()
    timeSynchronization.check_http_proxy_is_not_enabled()
    timeSynchronization.check_SNMP_server_not_enabled()
    

def run():
#    services_check()
    special_purpose_services_check()

run()
