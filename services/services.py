import inetdServices


def services_check():
    inetdServices.check_charge_services_not_enabled()
    inetdServices.check_daytime_services_not_enabled()
    inetdServices.check_discard_services_not_enabled()
    inetdServices.check_echo_services_not_enabled()
    inetdServices.check_time_services_not_enabled()


def run():
    services_check()


run()
