# Net ping and scan examples

from net import Net

# ping a server(or an IP)
t = Net.ping("www.bing.com")  # return milliseconds, return -1 means not available
print('milliseconds', t)

# get IP address of current computer
my_ip = Net.local_ip()

# create an IP range (a list of IP address)
ip_list = Net.ip_range(my_ip, 1, 100)
print(ip_list)

# Scan the IPs, return a list of pingable IPs
exists_ips = Net.ip_scan(ip_list)
print(exists_ips)

# Scan the IPs, return a list of not-pingable IPs
exists_ips = Net.ip_scan(ip_list, exists=False)
print(exists_ips)

# Scan the IPs, return a list, whose item is a tuple of (ip, mac_address)
exists_ips = Net.ip_scan(ip_list, mac=2)
print(exists_ips)

# Scan the IPs, return a list, whose item is a tuple of (ip, mac_address, manufacturer)
exists_ips = Net.ip_scan(ip_list, mac=3)
print(exists_ips)


# detect whether specified port of specified IP is opened
if Net.is_port_open(my_ip, 80):
    print('port 80 of', my_ip, 'opened')
else:
    print('port 80 of', my_ip, 'not opened')


# scan a list of port on specified IP address, return opened port list
port_list = Net.port_scan(my_ip, [80, 8080, 21, 22, 443, 445])
print('opened ports', port_list)
