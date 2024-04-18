print("===第一題===")
#%%

def find_and_print(messages, current_station):
# your code here

    stations = ["Songshan", "Nanjing Sanmin", "Taipei Arena", "Nanjing Fuxing", "Songjiang Nanjing","Zhongshan", "Beimen", "Ximen", "Xiaonanmen", "Chiang Kai-Shek Memorial Hall", "Guting", "Taipower Building", "Gongguan", "Wanlong", "Jingmei", "Dapinglin", "Qizhang", "Xindian City Hall", "Xindian"]

    friend_distance = []
    current_index = stations.index(current_station)

    # 在迴圈內直接使用name和message
    for name, message in messages.items():
        distances = []

        # 在迴圈內直接使用index和station
        for i, station in enumerate(stations):

            if "Xiaobitan" in message:
                branch1 = stations.index("Dapinglin")
                branch2 = stations.index("Xindian City Hall")
                
                branch_distance = max(abs(current_index - branch1), abs(current_index - branch2))
                
                distances.append({"name": name, "distance":branch_distance})

            elif station in message:
                distance = abs(current_index - i) 
                distances.append({"name": name, "distance": distance})


        if distances:
               # 改為使用extend而非append
               friend_distance.extend(distances)

    friend_distance.sort(key=lambda x:x["distance"])
    print(friend_distance[0]["name"])



messages={
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Vivian":"I'm at Xindian station waiting for you."
}
find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian

# %%

print("===第二題===")
# your code here, maybe

#%%
def book(consultants, hour, duration, criteria):
# your code here

    # 判斷每位顧問的時間
    # 選出有空檔的人
        # 空檔的人按照條件篩選
        # 輸出合適的人
    # 完全沒空檔print("No service")

    freeList = []

    for consultant in consultants:
            free = True

            if consultant.get("bookingTime"):
                 for order in consultant["bookingTime"]:
                    if hour < order["end"] and hour + duration > order["start"]:
                          free = False
                          break
                    
            if free:
                freeList.append(consultant)

    if not freeList:
         print("No service")
         return

    if criteria == "price":
         freeList.sort(key=lambda x:x["price"])
    elif criteria == "rate":
         freeList.sort(key=lambda x:x["rate"], reverse=True)

    best = freeList[0]
    best.setdefault("bookingTime", []).append({"start":hour , "end": hour + duration})
    print(best["name"])


consultants=[
    {"name":"John", "rate":4.5, "price":1000},
    {"name":"Bob", "rate":3, "price":1200},
    {"name":"Jenny", "rate":3.8, "price":800}
]

book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John

# %%


print("===第三題===")
#  Never change existing code.

#  Find out whose middle name is unique among all the names, and print it. You can assume
#  every input is a Chinese name with 2 ~ 5 words. If there are only 2 words in a name, the
#  middle name is defined as the second word. If there are 4 words in a name, the middle name
#  is defined as the third word.


# %%
def func(*data):
# your code here

    # 放中間名
    letters = []

    # 取中間名
    for name in data:
        middleIndex = len(name)//2
        middleName = name[middleIndex]
        letters.append(middleName)    

    # 放出現一次的中間名
    uniqueName = []
    
    for name in letters:
        if letters.count(name) == 1:
            uniqueName.append(name)
        
    # 取回只出現一次的姓名，並輸出
    for fullName in data:
        middleIndex = len(fullName)//2
        if fullName[middleIndex] in uniqueName:
            print(fullName)
            break
    else:
        print("沒有")          
    



func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安

# %%


print("===第四題===")
# Never change existing code.

# There is a number sequence: 0, 4, 8, 7, 11, 15, 14, 18, 22, 21, 25, …
# Find out the nth term in this sequence.

#1//3(4-1+4)+4(1%3)
# 2//3(4-1+4)+4(2%3)
# 3//3(4-1+4)+4(3%3)
# 4//3(4-1+4)+4
# 5//3(4-1+4)+4+4
# 6//3(4-1+4)+0

def get_number(index):
# your code here
    print(index // 3 * 7 + 4 *(index % 3))

get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70


print("===第五題===")
#%%

def find(spaces, stat, n):
# your code here

    # 把需要的條件lsit放在一起: spaces, stat
    relation = list(zip(spaces,stat))

    # 找出有服務的車廂，並計算位置是否夠用
    
    carList = []

    for spaces, stat in relation:
        if stat == 1:
            diff = spaces - n
            if diff >= 0:
                 carList.append({"spaces":spaces, "stat": stat, "diff": diff})
    
    # 判斷carList列表中有無元素             
    if carList:
            closeDiff = min(carList, key=lambda x:x["diff"])
            closeIndex = relation.index((closeDiff["spaces"], closeDiff["stat"]))

            print(closeIndex)
    else:
            print(-1)


find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2
# %%


