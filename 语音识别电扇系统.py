from aip import AipSpeech
import pyaudio  #语音识别部分所需模块
import wave     #语音识别部分所需模块
import tkinter as tk

'''百度API'''
APP_ID = '28918225'
API_KEY = 'AY0HTIFBWQxilfo1FI6BXEbr'
SECRET_KEY = 'lUM8pETdG2ImXmbTRSxPbkjEOBxrW5qx' 
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
 
'''语音识别函数'''
def Speech():
    def get_file_content(filePath):
        with open(filePath, "rb") as fp:
            return fp.read()
    keyword = client.asr(get_file_content('output.wav'), 'pcm', 16000, {'dev_ped':1536})
    print("识别的录音文字为："+keyword['result'][0])          #打印录音文字
    if "一" in keyword['result'][0]:
        print("系统做出相应行动："+"风扇调到一档\n")
        print("*"*30+"分割线"+"*"*30)
        labelfive.place(x=105,y=80)
    elif "二" in keyword['result'][0]:
        print("系统做出相应行动："+"风扇调到二档\n")
        print("*"*30+"分割线"+"*"*30)
        labelfive.place(x=105,y=135)
    elif "三" in keyword['result'][0]:
        print("系统做出相应行动："+"风扇调到三档\n")
        print("*"*30+"分割线"+"*"*30)
        labelfive.place(x=105,y=195)
    elif "关闭" in keyword['result'][0]:
        print("系统做出相应行动："+"风扇关闭\n")
        print("*"*30+"分割线"+"*"*30)
        labelfive.place(x=105,y=20)      
    else:
        print("系统未识别到关键字，请重新录音\n")
        
    
'''语音采集函数'''
def get_audio():
        CHUNK = 256
        FORMAT = pyaudio.paInt16
        CHANNELS = 1                # 声道数
        RATE = 11025                # 采样率
        RECORD_SECONDS = 5          # 录音时间（s）
        WAVE_OUTPUT_FILENAME ="output.wav"  # 输出文件名和路径
        p = pyaudio.PyAudio() 
        stream = p.open(format=FORMAT,          #打开数据流
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK) 
        print("开始录音：请在5秒内输入语音")
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)   
        print("录音结束\n") 
        stream.stop_stream()    #停止数据流
        stream.close()
        p.terminate()           #关闭PyAudio 
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')      #写入录音文件
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
       


window = tk.Tk()
window.geometry("500x400")
window.title("基于语音识别的电扇开关系统")
canvas = tk.Canvas(window, bg='white',width=400, height=320)  # 设置画布
canvas.pack()  # 显示画布
labelone=tk.Label(canvas,text='电风扇关闭',bg='yellow',width=20,height=2,bd='2')
labelone.place(x=135,y=10)
labeltwo=tk.Label(canvas,text='电风扇一档',bg='yellow',width=20,height=2,bd='2')
labeltwo.place(x=135,y=70)
labelthree=tk.Label(canvas,text='电风扇二档',bg='yellow',width=20,height=2,bd='2')
labelthree.place(x=135,y=130)
labelfour=tk.Label(canvas,text='电风扇三档',bg='yellow',width=20,height=2,bd='2')
labelfour.place(x=135,y=190)
labelfive=tk.Label(canvas,bg='red',width=1,height=1)   #小红块用作挡位标识
labelfive.place(x=105,y=20)
btnone=tk.Button(window, text="开始录音", command=get_audio)
btntwo=tk.Button(window, text="开始识别", command=Speech)
btnone.pack()
btntwo.pack()
window.mainloop()




    
