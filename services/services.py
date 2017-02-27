import inetdServices
import specialPurposeServices

def services_check():
    inetdServices.check_charge_services_not_enabled()
    inetdServices.check_daytime_services_not_enabled()
    inetdServices.check_discard_services_not_enabled()
    inetdServices.check_echo_services_not_enabled()
    inetdServices.check_time_services_not_enabled()
    inetdServices.check_tftp_server_not_enabled()
    inetdServices.check_xinetd_not_enabled()

def special_purpose_services_check():
    specialPurposeServices.check_time_sync_is_used()
    specialPurposeServices.check_ntp_configured()
    specialPurposeServices.check_x_window_system_not_installed()
    specialPurposeServices.check_Avahi_server_not_enabled()
    specialPurposeServices.check_CUPS_is_not_enabled()

def run():
#    services_check()
    special_purpose_services_check()

run()
