# /****************************************************************************
# * Author: Neuron-to-open
# * Date: 2024/11/12
# * Python : 3.11
# * 系统版本： Windows 11 家庭版 20H2
# * IDE: Pycharm
# * 编程语言: Python
# * =========== ====== ===== ==============================================
# * @Copyright (C) Yijiayi All Rights reserved
# *****************************************************************************/
import socket
import threading
import json
import time

DHCP_SERVER_PORT = 23456  # 自定义端口避免权限问题
BUFFER_SIZE = 1024

# DHCP服务器配置
default_config = {
    "subnet_mask": "255.255.255.0",
    "gateway": "192.168.1.1",
    "dhcp_server_ip": "",
}

# 模拟租约记录
lease_table = {}


# DHCP服务器类
class DHCPServer:
    def __init__(self, server_ip, server_id):
        self.server_ip = server_ip
        self.server_id = server_id
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((server_ip, DHCP_SERVER_PORT))

    def handle_request(self, data, client_address):
        client_id = data.decode('utf-8')

        # 如果之前有分配过IP，返回之前的配置，否则使用默认配置
        if client_id in lease_table:
            config = lease_table[client_id]
        else:
            assigned_ip = f"192.168.1.{100 + self.server_id}"  # 简单生成一个IP
            config = {
                "ip": assigned_ip,
                "subnet_mask": default_config["subnet_mask"],
                "gateway": default_config["gateway"],
                "dhcp_server_ip": self.server_ip,
            }
            lease_table[client_id] = config

        # 发送响应给客户端
        response = json.dumps(config)
        self.socket.sendto(response.encode('utf-8'), client_address)
        print(f"[DHCP Server {self.server_id}] Assigned IP {config['ip']} to {client_id}")

    def run(self):
        while True:
            data, client_address = self.socket.recvfrom(BUFFER_SIZE)
            self.handle_request(data, client_address)


# 启动DHCP服务器线程
def start_dhcp_server(server_ip, server_id):
    server = DHCPServer(server_ip, server_id)
    server.run()


# 启动两个DHCP服务器
server_thread_1 = threading.Thread(target=start_dhcp_server, args=("127.0.0.1", 1))
server_thread_2 = threading.Thread(target=start_dhcp_server, args=("127.0.0.2", 2))
server_thread_1.start()
server_thread_2.start()
