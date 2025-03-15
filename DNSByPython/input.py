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

DNS_SERVER_IP = "127.0.0.1"
DNS_PORT = 53535

def query_domain(domain):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.sendto(domain.encode('utf-8'), (DNS_SERVER_IP, DNS_PORT))
        data, _ = client_socket.recvfrom(512)
        print(f"Response from DNS server: {data.decode('utf-8')}")

if __name__ == "__main__":
    domain = input("Enter domain name to query: ")
    query_domain(domain)
