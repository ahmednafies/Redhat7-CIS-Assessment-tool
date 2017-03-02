import systemAccounting

def check_system_accounting():
    systemAccounting.check_system_disabled_when_auditLogs_are_full()
    systemAccounting.check_auditLogs_not_auto_deleted()
    systemAccounting.check_audit_service_enabled()
    systemAccounting.check_date_time_modifying_events()
    systemAccounting.check_user_group_modifying_events()

def run():
    check_system_accounting()

run()