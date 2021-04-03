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
        device_distribution=(IOS_L3_distribution1,IOS_L3_distribution2)
        for device in device_distribution:
                ssh_connection=ConnectHandler(**device)
                print("Connection Establish\n")
                ssh_connection.enable()
                print(ssh_connection.find_prompt())
                for n in range(2,21):
                        print ("Creating VLAN " + str(n))
                        config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
                        push_device_vlan_config=ssh_connection.send_config_set(config_commands)
                        print(push_device_vlan_config)
except :
    print("Connection Failed")

