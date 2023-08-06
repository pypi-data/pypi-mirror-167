import ipaddress


def is_qiwi_api(ip: str) -> bool:
    """
    Список ip адресов взят со страницы https://developer.qiwi.com/ru/qiwi-wallet-personal/#webhook
    """
    ip_networks = [
        ipaddress.IPv4Network("79.142.16.0/20"),
        ipaddress.IPv4Network("195.189.100.0/22"),
        ipaddress.IPv4Network("91.232.230.0/23"),
        ipaddress.IPv4Network("91.213.51.0/24")
    ]
    allowed_ip_addresses = []
    for ip_network in ip_networks:
        allowed_ip_addresses.extend(ip_network.hosts())

    return ipaddress.IPv4Address(ip) in allowed_ip_addresses
