import os

class GetIP():
    def get_Ip(self):
        result = os.popen("ipconfig")
        ret = result.read()
        for line in ret.splitlines():

            #字符串也可以使用in方法进行判断
            if "IPv4 地址" in line:
                ipaddr = line.split(":")[-1].strip()
        return ipaddr


import socket
import uuid

class GetIp2():
    def info(self):
        #获取主机名
        hostname = socket.gethostname()

        #获取IP
        Ip = socket.gethostbyname(hostname)

        #获取主机的mac地址
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        mac_addr = ":".join([mac[i:i+2] for i in range(0, 11, 2)])


        return hostname, Ip, mac_addr










if __name__ == '__main__':

    IP = GetIP()
    print(IP.get_Ip())

    info = GetIp2()
    hostname, Ip, mac_addr = info.info()
    print(f"主机名：{hostname}", end="\n")
    print(f"Ip地址：{Ip}", end="\n")
    print(f"mac地址：{mac_addr}", end="\n")
