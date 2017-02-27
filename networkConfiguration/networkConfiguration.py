import hostNetworkParameters
import routerAndHostNetworkParameters
import ipv6
import tcpWrappers
import uncommonNetworkProtocols
import firewallConfiguration


def host_network_parameters_check():
    hostNetworkParameters.check_ip_forwarding_is_disabled()
    hostNetworkParameters.check_packet_redirect_sending_is_disabled()


def router_and_host_network_parameters():
    routerAndHostNetworkParameters.check_source_routed_packets_not_accepted()
    routerAndHostNetworkParameters.check_ICMP_redirects_are_not_accepted()
    routerAndHostNetworkParameters.check_secure_ICMP_redirect_are_not_accepted()
    routerAndHostNetworkParameters.check_suspicious_packets_are_logged()
    routerAndHostNetworkParameters.check_bogus_icmp_requests_ignored()
    routerAndHostNetworkParameters.check_bogus_icmp_requests_ignored()
    routerAndHostNetworkParameters.check_reverse_path_filtering_enabled()
    routerAndHostNetworkParameters.check_tcp_SYN_cookies_is_enabled()


def ipv6_check():
    ipv6.check_IPv6_router_ads_not_accepted()
    ipv6.check_IPv6_redirect_not_accepted()
    ipv6.check_IPv6_is_disabled()


def tcp_wrappers_check():
    tcpWrappers.check_tcp_wrappers_is_installed()
    tcpWrappers.check_etc_hosts_deny_is_configured()
    tcpWrappers.check_permissions_on_etc_hosts_allow_isConfigured()
    tcpWrappers.check_permissions_on_etc_hosts_deny_isConfigured()


def uncommon_network_protocols_check():
    uncommonNetworkProtocols.check_DCCP_is_disabled()
    uncommonNetworkProtocols.check_SCTP_is_disabled()
    uncommonNetworkProtocols.check_rds_is_disabled()
    uncommonNetworkProtocols.check_tipc_is_disabled()


def firewall_configuration_check():
    firewallConfiguration.check_ip_tables_installed()

def run():
    # host_network_parameters_check()
    # router_and_host_network_parameters()
    # ipv6_check()
    # tcp_wrappers_check()
    # uncommon_network_protocols_check()
    firewall_configuration_check()


run()
