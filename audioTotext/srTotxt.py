# -*- coding: utf-8 -*-
# -------------------------------

# @软件：PyCharm
# @PyCharm：3.4.1
# @Python：3.11
# @项目：PersonalDevelopment

# -------------------------------

# @文件：srTotxt.py
# @时间：2025/3/15 23:53
# @作者：Neuron-to-opens

# -------------------------------
import pyaudio
from vosk import Model, KaldiRecognizer

# 加载模型
MODEL_PATH = 'vosk-model-cn-0.22\\vosk-model-cn-0.22d'
model = Model(MODEL_PATH)

# 初始化语音识别器和音频流
recognizer = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

print('Listening Ctrl+C to exit')

try:
    # 持续监听麦克风输入并进行语音识别
    while True:
        # 从音频流中读取数据块，避免溢出错误
        data = stream.read(4000, exception_on_overflow=False)

        # 如果识别器接受当前音频块，则获取识别结果
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            print(result)

except KeyboardInterrupt:
    # 捕获用户中断信号（Ctrl+C），退出程序
    print('\nExit')

finally:
    # 停止音频流并释放资源
    stream.stop_stream()
    stream.close()
    p.terminate()
