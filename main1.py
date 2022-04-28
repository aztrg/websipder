import requests,os
from bs4 import BeautifulSoup
def getHtml(url):
    try:
        r=requests.get(url)
        html=r.text
        return html
    except:
        print("error")
def getcontent(html):
    book_url = {}
    soup=BeautifulSoup(html,'html.parser')
    target=soup.select('.co3 a')
    book=[item.string for item in target]
    url=[item.attrs['href'] for item in target]
    for i,url in zip(book,url):
        book_url[i]='http://www.wuxia.net.cn/'+url

    return book_url
if __name__=='__main__':
    author=str(input('please input the author'))
    url='http://www.wuxia.net.cn/author/{}.html'.format(author)
    html=getHtml(url)
    a=getcontent(html)
    f=open('new.txt','w')
    f.write(str(a))
    f.close()
    os.system("python 2.py {}")











