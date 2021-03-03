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
    device_distribution = (IOS_L3_distribution1, IOS_L3_distribution2)
    for device in device_distribution:
        ssh_connection = ConnectHandler(**device)
        print("Connection Establish\n")
        ssh_connection.enable()
        print(ssh_connection.find_prompt())
        configurations_device_port = [
            'int range g0/1-2', 'channel-protocal lacp', 'channel-group 1 mode active', 'exit']
        configurations_etherchannel_port = [
            'interface port-channel 1', 'switchport trunk encapsulation dot1q', 'switchport mode trunk']
        push_device_port_config = ssh_connection.send_config_set(
            configurations_device_port)
        print(push_device_port_config)
        push_etherchannel_port = ssh_connection.send_config_set(
            configurations_etherchannel_port)
        print(push_etherchannel_port)

except:
    print("Connection Failed")


#test SCM for second