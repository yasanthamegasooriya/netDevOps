from netmiko import ConnectHandler

IOS_L3_core1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.11',
    'username': 'root',
    'password': 'cisco'}
IOS_L3_distribution1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.12',
    'username': 'root',
    'password': 'cisco'
}
IOS_L3_distribution2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.13',
    'username': 'root',
    'password': 'cisco'
}
IOS_L3_access1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.14',
    'username': 'root',
    'password': 'cisco'}
IOS_L3_access2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.15',
    'username': 'root',
    'password': 'cisco'
}
IOS_L3_access3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.16',
    'username': 'root',
    'password': 'cisco'
}

try:
    ssh_connection = ConnectHandler(**IOS_L3_access1)
    print("connection success\n")
    ssh_connection.enable()
    print(ssh_connection.find_prompt())
    ports = ["gig 0/0", "gig 0/1 ", "gig1/0"]
    for com in ports:
        commands = ['int' + " " + str(com), 'switchport trunk encapsulation dot1q', 'switchport mode trunk', 'exit']
        out = ssh_connection.send_config_set(commands)
        time.sleep(5)
        ssh_connection.save_config(self, 'write mem', False, '')
        print(out)



except:

    print("login failure\n")
    sys.exit()

try:
    ssh_connection = ConnectHandler(**IOS_L3_distribution1)
    print("connection success\n")
    ssh_connection.enable()
    print(ssh_connection.find_prompt())
    ports = ["gig 0/0", "gig 0/1 ", "gig 0/2", "gig 2/1", "gig 2/0", "gig 1/0", "gig 1/1"]
    for com in ports:
        commands = ['int' + " " + str(com), 'switchport trunk encapsulation dot1q', 'switchport mode trunk', 'exit']
        out = ssh_connection.send_config_set(commands)
        time.sleep(5)

        ssh_connection.save_config(self, 'write mem', False, '')
        print(out)
except:
    print("command failure\n")
    sys.exit()

try:
    ssh_connection = ConnectHandler(**IOS_L3_distribution2)
    print("connection success\n")
    ssh_connection.enable()
    print(ssh_connection.find_prompt())
    ports = ["gig 0/0", "gig 0/1 ", "gig 0/2", "gig 2/1", "gig 2/0", "gig 1/0", "gig 1/1"]
    for com in ports:
        commands = ['int' + " " + str(com), 'switchport trunk encapsulation dot1q', 'switchport mode trunk', 'exit']
        out = ssh_connection.send_config_set(commands)
        time.sleep(5)

        ssh_connection.save_config(self, 'write mem', False, '')
        print(out)
except:
    print("command failure\n")
    sys.exit()

try:
    ssh_connection = ConnectHandler(**IOS_L3_core1)
    print("connection success\n")
    ssh_connection.enable()
    print(ssh_connection.find_prompt())
    ports = ["gig 1/2", "gig 1/3 ", "gig 0/2", "gig 2/1", "gig 2/0", "gig 0/2", "gig 1/1"]
    for com in ports:
        commands = ['int' + " " + str(com), 'switchport trunk encapsulation dot1q', 'switchport mode trunk', 'exit']
        out = ssh_connection.send_config_set(commands)
        time.sleep(5)

        ssh_connection.save_config(self, 'write mem', False, '')
        print(out)
except:
    print("command failure\n")
    sys.exit()

try:
    ssh_connection = ConnectHandler(**IOS_L3_access2)
    print("connection success\n")
    ssh_connection.enable()
    print(ssh_connection.find_prompt())
    ports = ["gig 1/1", "gig 1/0 ", "gig 0/1", "gig 0/0", "gig 0/2", "gig 0/3"]
    for com in ports:
        commands = ['int' + " " + str(com), 'switchport trunk encapsulation dot1q', 'switchport mode trunk', 'exit']
        out = ssh_connection.send_config_set(commands)
        time.sleep(5)

        ssh_connection.save_config(self, 'write mem', False, '')
        print(out)
except:
    print("command failure\n")
    sys.exit()

try:
    ssh_connection = ConnectHandler(**IOS_L3_access3)
    print("connection success\n")
    ssh_connection.enable()
    print(ssh_connection.find_prompt())
    ports = ["gig 0/0", "gig 0/1 ", "gig 0/2", "gig 0/3", "gig 1/0", "gig 1/1"]
    for com in ports:
        commands = ['int' + " " + str(com), 'switchport trunk encapsulation dot1q', 'switchport mode trunk', 'exit']
        out = ssh_connection.send_config_set(commands)
        time.sleep(5)

        ssh_connection.save_config(self, 'write mem', False, '')
        print(out)

except:
    print("command failure\n")
    sys.exit()
ssh_connection.disconnect()
