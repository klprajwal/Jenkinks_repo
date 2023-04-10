import unittest
from netmiko import ConnectHandler
import re

class RouterTests(unittest.TestCase):
    def test_loopback_ip_add(self):
        device = {
            'device_type': 'cisco_ios',
            'ip': '198.51.100.13',
            'username': 'netman',
            'password': 'netman',
            'secret': 'my_secret',  
	}
        net_connect = ConnectHandler(**device)
        net_connect.enable()
        output = net_connect.send_command('show running-config interface loopback99')
#        print(output)
        output_lines = output.splitlines() 
        ip_address=()
        subnet_mask=()
        for line in output_lines:
            if 'ip address' in line:
                ip_mask = line.split(' ')[-2:]  
                ip_address = ip_mask[0]
                subnet_mask = ip_mask[1]
                break
        ip_subnet = "{} {}".format(ip_address, subnet_mask)
        net_connect.disconnect()
        print(ip_subnet)
#        print("check R3 loopback")
        self.assertEqual(ip_subnet, "10.1.3.1 255.255.255.0")

    def test_R1_area_configuration(self):
        device = {
            'device_type': 'cisco_ios',
            'ip': '198.51.100.11',
            'username': 'netman',
            'password': 'netman',
            'secret': 'my_secret',  
	}
        net_connect = ConnectHandler(**device)
        net_connect.enable()
        output = net_connect.send_command('show ip protocols')
#       print(output)
        start_index = output.find("Number of areas in this router is") + len("Number of areas in this router is")
        end_index = output.find(".", start_index)
        number_of_areas = output[start_index:end_index].strip()
#        print(number_of_areas)
        net_connect.disconnect()
        # Scenario 2: If R1 is configured only for a single area
#        r1_area_configuration = "Single"
        self.assertEqual(number_of_areas, "1")

    def test_ping_router2_to_router5(self):
        device = {
            'device_type': 'cisco_ios',
            'ip': '198.51.100.12',  
            'username': 'netman',  
            'password': 'netman', 
        }
        net_connect = ConnectHandler(**device)
        ping_result = net_connect.send_command('ping 10.1.5.1')
        if 'Success rate is 100 percent' in ping_result:
            ping_success = True
        else:
            ping_success = False
        net_connect.disconnect()
#        router2_ping_result = True
        self.assertTrue(ping_success)

if __name__ == '__main__':
    unittest.main()

