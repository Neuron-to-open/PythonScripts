# /****************************************************************************
# * Author: Neuron-to-open
# * Date: 2024/11/11
# * Python : 3.11
# * 系统版本： Windows 11 家庭版 20H2
# * IDE: Pycharm
# * 编程语言: Python
# * =========== ====== ===== ==============================================
# * @Copyright (C) Yijiayi All Rights reserved
# *****************************************************************************/
import socket
import json
import dns.resolver  # 使用 dnspython 库来做互联网 DNS 查询
import os

DNS_PORT = 53535  # 自定义端口避免冲突
BUFFER_SIZE = 512
DNS_TABLE_FILE = "dnsrelay.txt"


# 加载域名-IP对照表
def load_dns_table(file_path):
    if not os.path.exists(file_path):
        print(f"{file_path} not found.")
        return {}
    with open(file_path, "r") as file:
        try:
            dns_table = json.load(file)
        except json.JSONDecodeError:
            print("Invalid JSON format in DNS table file.")
            dns_table = {}
    return dns_table


# DNS查找功能
def dns_lookup(domain, dns_table):
    # 本地表查找
    if domain in dns_table:
        ip = dns_table[domain]
        if ip == "0.0.0.0":
            return "Error: Domain not found"  # 不良网站拦截
        return ip  # 本地解析结果

    # 本地表中没有该域名，向因特网DNS查询
    try:
        answers = dns.resolver.resolve(domain, 'A')
        return answers[0].address
    except dns.resolver.NoAnswer:
        return "Error: No answer from internet DNS"
    except dns.resolver.NXDOMAIN:
        return "Error: Domain does not exist"
    except dns.exception.Timeout:
        return "Error: DNS query timeout"


# 处理客户端请求
def handle_dns_request(server_socket, dns_table):
    while True:
        # 接收数据
        data, client_addr = server_socket.recvfrom(BUFFER_SIZE)
        domain = data.decode('utf-8').strip()

        # 查找IP地址
        ip = dns_lookup(domain, dns_table)

        # 发送结果到客户端
        server_socket.sendto(ip.encode('utf-8'), client_addr)


def main():
    # 加载域名-IP对照表
    dns_table = load_dns_table(DNS_TABLE_FILE)

    # 创建UDP套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("", DNS_PORT))

    print(f"DNS server is running on port {DNS_PORT}...")

    try:
        handle_dns_request(server_socket, dns_table)
    except KeyboardInterrupt:
        print("\nDNS server shutting down.")
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()
