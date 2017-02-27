import inetdServices
import timeSynchronization
import serviceClients

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
    timeSynchronization.check_NIS_server_is_not_enabled()
    timeSynchronization.check_rsh_server_not_enabled()
    timeSynchronization.check_talk_server_is_not_enabled()
    timeSynchronization.check_telnet_server_not_enabled()
    timeSynchronization.check_tftp_server_not_enabled()
    timeSynchronization.check_rsync_server_is_not_enabled()

def service_clients_check():
    serviceClients.check_NIS_Client_not_installed()
    serviceClients.check_rsh_client_not_installed()
    serviceClients.check_talk_client_not_installed()
    serviceClients.check_telnet_client_not_installed()
    serviceClients.check_LDAP_client_not_installed()

def run():
#    services_check()
#    special_purpose_services_check()
    service_clients_check()

run()
