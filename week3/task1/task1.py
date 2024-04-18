#%%

# 導入處理url的模組(urllib)
import urllib.request as request

# 本次資料源為json格式
import json

# 連線網址
src1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
src2 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"

# 打開連線網址，讀取內容，將讀取內容存在res
with request.urlopen(src1) as res1:    
# 將儲存的res內容從json轉為python對象   
    data1 = json.load(res1)

with request.urlopen(src2) as res2:
    data2 = json.load(res2)
   
# 要使用的資料位置
    data1 = data1["data"]["results"]
    data2 = data2["data"]

# 將資料寫到csv檔案中，
with open("spot.csv", "w", encoding="utf-8-sig") as file:
    # 先把Header寫進，才寫入數據
    file.write("SpotTitle,District,Longitude,Latitude,ImageURL\n")  

    for i in data1:
        for j in data2:
            if i["SERIAL_NO"] == j["SERIAL_NO"]:
               
                # 取回image所有連結
                img_links = i['filelist']

                # 取出第一個link
                img_link = 'https://' + img_links.split('https://')[1]

                  # 把內容寫入檔案中
                file.write(f'{i['stitle']},{j['address'][4:8]},{i['longitude']},{i['latitude']},{img_link}\n') 



with open("mrt.csv", "w", encoding="utf-8-sig") as file:
    file.write("StationName,AttractionTitle\n")  

    data = {}

    # serialno = serialno 
    for i in data1:
        for j in data2:
            if i["SERIAL_NO"] == j["SERIAL_NO"]:
                mrt = j['MRT']
                attr = i['stitle']

                # 如果mrt有在data中，就新增attr
                if mrt in data:
                    data[mrt].append(attr)

                else:
                    data[mrt] = [attr] #將值（value）加入到字典（dictionary）中

    for mrt, attrs in data.items():
        attr = ", ".join(attrs) # 將景點列表轉換成字串
        file.write(f"{mrt},{attr}\n")   





        




# %%
