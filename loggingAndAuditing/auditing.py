import systemAccounting

def check_system_accounting():
    systemAccounting.check_system_disabled_when_auditLogs_are_full()
    systemAccounting.check_auditLogs_not_auto_deleted()
    systemAccounting.check_audit_service_enabled()

def run():
    check_system_accounting()

run()