# /****************************************************************************
# * Author: Neuron-to-open
# * Date: 2024/6/3
# * Python : 3.11
# * 系统版本： Windows 11 家庭版 20H2
# * IDE: Pycharm
# * 编程语言: Python
# * =========== ====== ===== ==============================================
# * @Copyright (C) Yijiayi All Rights reserved
# *****************************************************************************/
import csv

def csv_to_txt(csv_file, txt_file):
    with open(csv_file, 'r', encoding='gbk') as csvfile, open(txt_file, 'w', newline='', encoding='utf-8') as txtfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            txtfile.write(' '.join(row) + '\n')

# 使用函数转换文件
csv_to_txt('D:\\projects_Dealing\\PersonalDevelopment\\asset\\medical.csv', 'asset/output.txt')
