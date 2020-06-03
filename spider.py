import requests
import re
from bs4 import BeautifulSoup
from parsel import Selector
import collections
import  time

def getHTMLText_and_Links(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }
        r = requests.get(url, timeout=30,headers=headers)
        r.encoding = r.apparent_encoding

        selector=Selector(r.text)
        title=selector.xpath("//title/text()").get()
        links=selector.css("body").xpath('//@href').getall()
        return url,title,links
    except:
        return "","",""

def create_start_url():
    start_url=[
        'https://www.hao123.com/',
    ]
    return start_url

def find_new_url(text):
    html=BeautifulSoup.prettify(text,'html.parser')
    print(html)



def find_text():
    pass


def save_file(text, count):
    root = "D:/spider_text/"
    s = root + "file" + str(count) + ".txt"
    print(s)
    with open(root + str(count) + ".txt", 'w',encoding='utf-8') as f:
        f.write(text)
        f.close()


def start():

    dq=collections.deque()
    start_url=create_start_url()
    for url in start_url:
        dq.append(url)

    while len(dq)>0:
        next_url=dq.popleft()

        url,title,links=getHTMLText_and_Links(next_url)
        print("即将访问:",url)

        if len(links) ==0:
            pass
        else:
            try:
                # txt format :1.url 2.title 3. length of links 4.
                with open('C:/Users/lenovo/Desktop/gjr/毕业设计/数据收集/5_25_test/1.TXT', 'a',encoding='utf-8') as f:
                    f.writelines(url+'\n'+title.strip()+'\n')
                    f.close()
                print("网站链接:",url)
                print("网页标题:",title.strip(),"链接个数",len(links))
                print("队列的长度为:",len(dq))
                if len(dq)<100000:
                    for l in links:
                        dq.append(l)
                else:
                    with open('C:/Users/lenovo/Desktop/gjr/毕业设计/数据收集/5_25_test/links.TXT', 'a', encoding='utf-8') as f:
                        for i in dq:
                            f.writelines(i+'\n')
                    f.close()
                    break
            except:
                pass
        #time.sleep(2)

start()
