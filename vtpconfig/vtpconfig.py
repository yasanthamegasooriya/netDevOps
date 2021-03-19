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

#connecting to corelayer switch
try:
    ssh_connection = ConnectHandler(**IOS_L3_core1)
    print("connection success\n")
    ssh_connection.enable()
    print(ssh_connection.find_prompt())
    commandos = ['vtp domain corelayerswitch.com', 'vtp password python123', 'vtp mode server', 'vtp version 2']
    outputs = ssh_connection.send_config_set(commandos)
    print(outputs)

except:
    print("login failure\n")
    sys.exit()

distribution_and_access_layer_devices = [IOS_L3_access1,IOS_L3_access2,IOS_L3_access3,IOS_L3_distribution1,IOS_L3_distribution2]
for devices in distribution_and_access_layer_devices:
    try:
        ssh_connection = ConnectHandler(**devices)
        ssh_connection.enable()
        commands = ['vtp domain corelayerswitch.com', 'vtp password python123', 'vtp mode client', 'vtp version 2']
        output = ssh_connection.send_config_set(commands)
        print(output)
        time.sleep(3)
        print("done")

    except:
        print("connection failed to this")



ssh_connection.disconnect()