

import subprocess, winreg, re, time, wmi
import netifaces
import random as rd
import urllib.request

class IP():
    def __init__(self):
        self.gws=netifaces.gateways()
        self.nic_configs=wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
        self.nic=self.nic_configs[0]
        self.gateway=self.gws['default'][netifaces.AF_INET][0]
        self.newIP=self.gateway.split(".")
        self.newIP[-1]=str(rd.randint(5,150))
        self.newIP=".".join(self.newIP)
        self.subnetmask=u"255.255.255.0"
        self.DNS=['208.67.222.222','208.67.220.220']
    def change_IP(self):        
        try:
            self.nic.EnableStatic(IPAddress=[self.newIP],SubnetMask=[self.subnetmask])
            self.nic.SetGateways(DefaultIPGateway=[self.gateway])
            self.nic.SetDNSServerSearchOrder(DNSServerSearchOrder = self.DNS)
            print("Chuyển đổi IP thành công. IP mới:",self.newIP)
        except:
            print("Chuyển đổi IP thất bại")
        time.sleep(10)
    def show_IP(self):
        for i in netifaces.interfaces():
            try:
                if(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']!="127.0.0.1"):
                    print("IP Address: ", netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
                    print("Mask: ", netifaces.ifaddresses(i)[netifaces.AF_INET][0]['netmask'])
                    print("Gateway: ", netifaces.gateways()['default'][netifaces.AF_INET][0])

            except:pass



class MAC():
    def __init__(self):
        self.list_2letter=["0A","0E","02","06"]
        self.other_letter="".join([str(rd.randint(0,9)) for i in range(10)])
        self.genMAC=self.list_2letter[rd.randint(0,3)]+self.other_letter
        gws = netifaces.gateways()
        self.TN=gws['default'][list(gws['default'].keys())[0]][1]
        self.macAddRegex =re.compile(r"([A-Za-z0-9]{2}[:-]){5}([A-Za-z0-9]{2})")
        self.transportName =re.compile("({.+})")
        self.adapterIndex =re.compile("([0-9]+)")
        self.getmac_output=subprocess.run("getmac",capture_output=True).stdout.decode().split('\n')
        self.mac_addresses=[]
        for macAdd in self.getmac_output:
            macFind = self.macAddRegex.search(macAdd)
            transportFind=self.transportName.search(macAdd)
            if macFind == None or transportFind == None:
                continue
            self.mac_addresses.append((macFind.group(0),transportFind.group(0)))
    def show_MAC(self):
        for index,item in enumerate(self.mac_addresses):
            print(f"{index} - Địa chỉ MAC: {item[0]} - Transport Name: {item[1]}")

    def change_MAC(self):
        controller_key_part=r"SYSTEM\ControlSet001\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}"
        with winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE) as hkey:
            controller_key_folders =[("\\000"+str(item) if item < 10 else "\\00"+str(item))for item in range(0,21)]
            for key_folder in controller_key_folders:
                try:
                    with winreg.OpenKey(hkey,controller_key_part+key_folder,0,winreg.KEY_ALL_ACCESS) as regkey:
                        try:
                            count=0
                            while True:
                                name,value,type=winreg.EnumValue(regkey,count)
                                count=count+1
                                if name=="NetCfgInstanceId" and value==self.mac_addresses[0][1]:
                                    new_mac_address = self.genMAC
                                    winreg.SetValueEx(regkey, "NetworkAddress", 0, winreg.REG_SZ, new_mac_address)
                                    print("Sửa địa chỉ MAC trên Registry thành công: {","-".join([(self.genMAC[i:i+2]) for i in range(0, len(self.genMAC), 2)]),"}")
                                    break
                        except:
                            pass
                except:
                    pass

    def restart_Wifi(self):
        run_last_part=True
        while run_last_part:
            network_adapters = subprocess.run(["wmic", "nic", "get", "name,index"], capture_output=True).stdout.decode('utf-8', errors="ignore").split('\r\r\n')
            for adapter in network_adapters:
                adapter_index_find = self.adapterIndex.search(adapter.lstrip())
                if adapter_index_find and "Wireless" in adapter:
                    disable = subprocess.run(["wmic", "path", "win32_networkadapter", "where", f"index={adapter_index_find.group(0)}", "call", "disable"],capture_output=True)
                    if(disable.returncode == 0):
                        print("Vô hiệu hóa",adapter.lstrip())
                    enable = subprocess.run(["wmic", "path", f"win32_networkadapter", "where", f"index={adapter_index_find.group(0)}", "call", "enable"],capture_output=True)
                    if (enable.returncode == 0):
                        print("Kích hoạt",adapter.lstrip())
                getmac_output = subprocess.run("getmac", capture_output=True).stdout.decode()
                mac_add = "-".join([(self.genMAC[i:i+2]) for i in range(0, len(self.genMAC), 2)])
                if mac_add in getmac_output:
                    print("Chuyển đổi địa chỉ MAC thành công.\nĐịa chỉ MAC mới: {","-".join([(self.genMAC[i:i+2]) for i in range(0, len(self.genMAC), 2)]),"}")
                    run_last_part=False
                    break
            break


class IP_MAC(MAC,IP):
    def __init__(self):
        self.ip=IP()
        self.mac=MAC()
    def run(self):
        try:
            self.mac.change_MAC()
            self.mac.restart_Wifi()
        except:
            print("Chuyển địa chỉ MAC thất bại")
            
        flag=True
        count=0
        while(flag):
            for i in netifaces.interfaces():
                try:
                    if(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']!="127.0.0.1"):
                        print("Wifi is connected")
                        flag=False
                        break
                except:
                    pass
            count=count+1
            if(count==50000):
                flag=False
        try:
            time.sleep(1)
            urllib.request.urlopen('https://www.google.com')
            print("Internet has connected")
        except:
            pass
            
        try:
            self.ip.change_IP()
            self.ip.show_IP()
        except:
            print("Chuyển IP thất bại")
        

        flag=True
        count=0
        while(flag):
            for i in netifaces.interfaces():
                try:
                    if(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']!="127.0.0.1"):
                        print("Wifi is connected")
                        flag=False
                        break
                except:
                    pass
            count=count+1
            if(count==50000):
                print("")
                flag=False
        try:
            time.sleep(1)
            urllib.request.urlopen('https://www.google.com')
            print("Internet has connected")
        except:
            print("Kết nối thất bại")
            print(1/0)
    def get_IP(self):
        return self.ip.newIP
    def get_MAC(self):
        return "-".join([(self.mac.genMAC[i:i+2]) for i in range(0, len(self.mac.genMAC), 2)])
    def is_connect(self):
        try:
            time.sleep(1)
            urllib.request.urlopen('https://www.google.com')
            return True
        except:
            print("No Internet")
            return 1/0