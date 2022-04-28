import requests,re,os
from bs4 import BeautifulSoup   #库导入



def getHtml(url):
    try:
        r=requests.get(url)
        html=r.text
        return html
    except:
        print("error")
def getchaptercontent(html):
    chapter_url={}
    soup = BeautifulSoup(html,'html.parser')
    target2 = soup.select('.book a')
    chapter_name=[it.string for it in target2]
    url = [it.attrs['href'] for it in target2]





    for i,url in zip(chapter_name,url) :
        chapter_url[i] = 'http://www.wuxia.net.cn/' + url
    return chapter_url
def get_txt(html):

    soup = BeautifulSoup(html, 'html.parser')
    target=soup.select('.text p')
    target2=soup.select('.topnav ')
    book = [item.string for item in target]
    return book
if __name__ == '__main__':  # 主程序获取内容
    with open('new.txt', 'r') as fp:
        a = fp.read()
    b = eval(a)           #读取爬取信息
    os.remove('new.txt')
    list1 = b.keys()
    for i in list1:
        s = b[i]
        print(i)         #书名目录
    root_path1 = '小说'
    if not os.path.exists(root_path1):       #创建文件
        os.mkdir(root_path1)
    z = 0
    number = int(input('how many books do you want to download：'))
    for z in range(1, number + 1):
        xvhao = input('which book do you want to download')
        book_path = root_path1 + '/' + xvhao
        if not os.path.exists(book_path):
            os.mkdir(book_path)
        url2 = b[xvhao]
        html = getHtml(url2)
        txt = getchaptercontent(html)
        m = 0
        for k, v in txt.items():  #文本处理
            html3 = getHtml(v)
            content2 = get_txt(html3)
            comtent4 = str(content2).strip("'[]'")
            comtent4=comtent4.replace("","")

            content3 = str(comtent4).strip("(ā á ō，英： )")
            r = str(k)

            res2 = re.sub('[a-zA-Z]', '', content3)
            with open(book_path + '/' + str(m) + '.txt', 'w') as fp:   #文本写入
                fp.write("{}{}   "
                         "".format(xvhao, r))
                fp.write(res2)
                fp.close()
            m += 1

