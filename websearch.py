import webbrowser
def search():
    s=str(input("请输入关键词:\n\t\t\t\t\t\t"))
    print("正在为您打开搜索界面..")
    url = 'http://www.baidu.com/s?wd=' + s + '&amp;cl=3&amp;t=12&amp;fr=news' # 接收一个关键字
    webbrowser.open(url)   # webbrowser.open()打开浏览器