import nmap

scanner=nmap.PortScanner()

ip=input("Digite la direccion ip: ")
print("Esta es la ip selecciono: ", ip)
scanner.scan(ip)

print(scanner.all_hosts)

