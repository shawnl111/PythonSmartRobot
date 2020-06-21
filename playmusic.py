import os

def playmusic():
    print("正在为您打开音乐播放器...\n\t\t\t\t\t\t")
    app_dir = r'D:\Music\QQMusic\QQMusic.exe'#指定应用程序目录
    os.startfile(app_dir) #os.startfile（）打开外部应该程序，与windows双击相同
