#%%

import urllib.request as req
from bs4 import BeautifulSoup

def getData(url):

     # 使用者行為資訊
    headers = {   
        'Cookie': 'over18=1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36'}

    # request時需要模仿使用者，加上headers資訊
    request = req.Request(url, headers=headers)

    # 打開、讀取、解碼
    with req.urlopen(request) as response:
        data = response.read().decode('utf-8')

    # 解析html格式
    root = BeautifulSoup(data, 'html.parser')

    # 找到所有使用class = title 的 div 標籤
    titles = root.find_all('div', class_='title')
    pushes = root.find_all('div', class_='nrec') 

    art_list = []

        # 進入每個標題連結
    for title, push in zip(titles,pushes):

        # 取標題連結，若為空則跳過
        if title.a is None:
            continue

        else:
            push_span = push.find('span', class_='hl')
            if push_span:
                push_text = push_span.text
            else:
                push_text = ''

            link = title.a.get('href')
            full_link = "https://www.ptt.cc/" + link
            
            # 進入標題頁面，重新"打開、讀取、解碼、解析html格式"
            art_req = req.Request(full_link, headers=headers)
            with req.urlopen(art_req) as art_res:
                art_page = art_res.read().decode('utf-8')
            art_root = BeautifulSoup(art_page, 'html.parser')


            # 找到time
            time = [title.text for title in art_root.find_all('span', class_='article-meta-value')][3:4] 
            
            art_list.append({'title': title.text.strip(), 'push': push_text, 'time': time})

    #取完該頁面，前往上一頁面，找到上一頁的連結
    next_link = root.find('a', string='‹ 上頁')
    if next_link:
        next_link = "https://www.ptt.cc/" + next_link.get('href')
        
    return next_link, art_list


url = 'https://www.ptt.cc/bbs/Lottery/index.html'

art_lists = []

# 用來控制取的頁面次數
count = 0 
while count < 3:
    next_link, art_list = getData(url)
    art_lists.extend(art_list)
    count += 1
    url = next_link

# 打開檔案寫入內容
with open('article.csv', 'w', encoding='utf-8-sig') as file:
    
    # 寫入header，後面加入內容
    file.write('Article Title, Like/DislikeCount, PublishTime\n')

    for item in art_lists:
        if 'time' in item and item['time']:
            file.write(f"{item['title']},{item['push']},{item['time'][0]}\n")
        else:
            file.write(f"{item['title']},{item['push']},''\n")
        






# %%
