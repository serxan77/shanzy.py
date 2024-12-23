import socket

def port_scan(target, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

target = '192.168.1.1'  # Skan ediləcək IP
ports = [22, 80, 443, 8080]  # Skan ediləcək portlar
open_ports = port_scan(target, ports)
print(f"Açıq portlar: {open_ports}")
