import socket

def get_ip_addresses(url):
    try:
        ipv4_address = socket.gethostbyname(url)
    except socket.gaierror:
        ipv4_address = None

    try:
        ipv6_info = socket.getaddrinfo(url, None, socket.AF_INET6)
        ipv6_address = ipv6_info[0][4][0]
    except (socket.gaierror, IndexError):
        ipv6_address = None

    return ipv4_address, ipv6_address

if __name__ == "__main__":
    url = input("Enter the URL: ")
    ipv4, ipv6 = get_ip_addresses(url)
    
    if ipv4 is not None:
        print(f"The IPv4 address of {url} is {ipv4}")
    else:
        print(f"No IPv4 address found for {url}")
    
    if ipv6 is not None:
        print(f"The IPv6 address of {url} is {ipv6}")
    else:
        print(f"No IPv6 address found for {url}")
