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
import json
import time
import threading

DHCP_SERVER_PORT = 23457
BUFFER_SIZE = 1024

# 模拟主机类
class Host:
    def __init__(self, client_id):
        self.client_id = client_id
        self.config = None

    def request_dhcp(self):
        # 广播DHCP请求
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
            client_socket.settimeout(2)  # 超时设置2秒
            client_socket.sendto(self.client_id.encode('utf-8'), ('<broadcast>', DHCP_SERVER_PORT))

            # 等待多个DHCP响应，以优先到达为准
            start_time = time.time()
            while time.time() - start_time < 2:
                try:
                    data, _ = client_socket.recvfrom(BUFFER_SIZE)
                    config = json.loads(data.decode('utf-8'))
                    if not self.config:
                        self.config = config  # 设置第一个到达的响应
                        print(f"[Host] Configured with IP {config['ip']} from DHCP server {config['dhcp_server_ip']}")
                        break
                except socket.timeout:
                    break

    def run(self):
        print("[Host] Sending DHCP request...")
        self.request_dhcp()
        if not self.config:
            print("[Host] No response from DHCP servers.")

# 启动主机请求线程
client = Host("client1")
client_thread = threading.Thread(target=client.run)
client_thread.start()
client_thread.join()
