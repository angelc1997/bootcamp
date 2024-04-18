console.log("===第一題===")
// Never change existing code.

// We just received message`s from 5 friends in JSON format, and we want to take the green
// line, including Xiaobitan station, of Taipei MRT to meet one of them. Write code to find out
// the nearest friend and print name, based on any given station currently located at and
// station count between two stations.



function findAndPrint(messages, currentStation){
    // your code here
    
    // 找出朋友訊息中的車站位置
        // 如果是'小碧潭'站，優先處理(程式先跑到)
            // 取出小碧潭車站名稱
            // 將小碧潭視為大坪林或新店區公所
            // 算出兩邊與目前位置差的最大正整數
            // 回傳姓名與距離到distance陣列
        
        // 其他車站都可在車站陣列找到
            // 提取車站位置index
            // 算出每站與目前位置差的正整數
            // 回傳姓名與距離到distance陣列
            
    // 比較distance陣列中，所有距離
        // 將所有內容傳到friendDistance中
        // 按照升序排列
        // 回傳最小的距離index 0 

    
    // 車站陣列
    const stations = ["Songshan", "Nanjing Sanmin", "Taipei Arena", "Nanjing Fuxing", "Songjiang Nanjing","Zhongshan", "Beimen", "Ximen", "Xiaonanmen", "Chiang Kai-Shek Memorial Hall", "Guting", "Taipower Building", "Gongguan", "Wanlong", "Jingmei", "Dapinglin", "Qizhang", "Xindian City Hall", "Xindian"]
 
    
    
    let friendDistances = [];
    let currentIndex = stations.indexOf(currentStation);

    for(let name in messages){
        let message = messages[name];
        let distances = [];

        for(let i = 0 ; i < stations.length; i++){
            if(message.includes("Xiaobitan")){
                let branch1 = stations.indexOf("Dapinglin");
                let branch2 = stations.indexOf("Xindian City Hall");

                let branchDistance = Math.abs(currentIndex - branch1) > Math.abs(currentIndex - branch2) ? Math.abs(currentIndex - branch1): Math.abs(currentIndex - branch2);

                distances.push({name: name, distance:branchDistance});

            } else if (message.includes(stations[i])){
                let distance = Math.abs(currentIndex - i);
                distances.push({name: name, distance:distance});
            }
        }
        if (distances.length > 0 ) {
            friendDistances.push(...distances);
        }
    }

    friendDistances.sort((a,b) => a.distance - b.distance);
    console.log(friendDistances[0].name)
}


    const messages={
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.",
    "Copper":"I just saw a concert at Taipei Arena.",
    "Leslie":"I'm at home near Xiaobitan station.",
    "Vivian":"I'm at Xindian station waiting for you."
    };


    findAndPrint(messages, "Wanlong"); // print Mary
    findAndPrint(messages, "Songshan"); // print Copper
    findAndPrint(messages, "Qizhang"); // print Leslie
    findAndPrint(messages, "Ximen"); // print Bob
    findAndPrint(messages, "Xindian City Hall"); // print Vivian


console.log("===第二題===")
    // Assume we have consultants for consulting services. Help people book the best matching
// consultant in a day, based on hours, service durations, and selection criteria.
// 1. Booking requests are one by one, order matters.
// 2. A consultant is only available if there is no overlapping between already booked time and an incoming request time.
// 3. If the criteria is "price", choose the available consultant with the lowest price.
// 4. If the criteria is "rate", choose the available consultant with the highest rate.
// 5. If every consultant is unavailable, print "No Service".


//1.紀錄完整預約名單，以便排除重疊
//2.逐一確認每位顧問的時間
    //預約採先預約先記錄
    //2-1如果預約衝突，跳出換評估下一位
    //2-2如果預約不衝突，將顧問推送至free狀態
//3.如果都衝突，無法提供服務
//4.free顧問們按照顧客條件篩選(此階段是從逐一挑選空檔顧問進行篩選)
    //條件:價格採最低價、評價採最高價
    //4-1價格或是評價篩選
    //4-2回傳最合適的顧問
//5.推送並記錄顧問名稱、時間至預約清單中


// your code here, maybe
function book(consultants, hour, duration, criteria){
    // your code here
    // 創建可以放有空的顧問
    let freeList = [];

    // 逐一確認每位顧問的時間是否有衝突
    for (const consultant of consultants) {

        // 初始先假設大家都有空
        let free = true;

        // consultant陣列中多一個管理預約時間的array
            // 逐一檢查bookingTime裡面的每個order時間是否有衝突
        if (consultant.bookingTime) {
            for (const order of consultant.bookingTime) {
                if (hour < order.end && hour + duration > order.start) {
                    // 產生衝突跳出
                    free = false;
                    break;
                }
            }
        }
        // 如果不衝突，將顧問加入空閒清單
        if (free) {
            freeList.push(consultant);
        }
    }
    // 如果全部衝突，無法提供服務
    if (freeList.length === 0) {
        console.log("No service");
        return;
    }

    // 從freeList裡面的顧問們，按照條件篩選最適合的
    let bestChoice;
    if (criteria === "price") {
        //價 格，須符合低價優先
        freeList.sort((a, b) => a.price - b.price);
    } else if (criteria === "rate") {
        // 評價，須符合高評優先
        freeList.sort((a, b) => b.rate - a.rate);
    }
    // 最佳人選會排在第一位置
    bestChoice = freeList[0];

    // 確認bookingTime有無空值
    bestChoice.bookingTime = bestChoice.bookingTime || [];
    // 新增預約到最適合人選的預約清單中
    bestChoice.bookingTime.push({ "start": hour, "end": hour + duration });
    // 輸出
    console.log(bestChoice.name);
    }
    const consultants=[
    {"name":"John", "rate":4.5, "price":1000},
    {"name":"Bob", "rate":3, "price":1200},
    {"name":"Jenny", "rate":3.8, "price":800}
    ];
    book(consultants, 15, 1, "price"); // Jenny
    book(consultants, 11, 2, "price"); // Jenny
    book(consultants, 10, 2, "price"); // John
    book(consultants, 20, 2, "rate"); // John
    book(consultants, 11, 1, "rate"); // Bob
    book(consultants, 11, 2, "rate"); // No Service
    book(consultants, 14, 3, "price"); // John
    


    
console.log("===第三題===")
// Never change existing code.

// Find out whose middle name is unique among all the names, and print it. You can assume
// every input is a Chinese name with 2 ~ 5 words. If there are only 2 words in a name, the
// middle name is defined as the second word. If there are 4 words in a name, the middle name
// is defined as the third word.

// 姓名包含2~5個字元，對比中間字不同，2個字以第二個為主、4個字以第三個為主
// 取出中間名字
// 對比取出的中間名字是否一樣
// (不一樣)print完整名；(都有相同)print沒有


function func(...data){
    // your code here
    // 定義空陣列存放中間字
    let letters = [];
    
    // 將每個姓名的中間字取出
    for (let str of data){
        // 取出中間名字的參數    
        let middleIndex = Math.floor(str.length / 2);
        // 按照參數位置取回中文單名
        let middleName = str.charAt(middleIndex);
        // 把單名推至空陣列(letters)
        letters.push(middleName);
    }

    // 找出不同的單名
    let uniqueName = [];
    for (let str of letters) {
        if (letters.indexOf(str) === letters.lastIndexOf(str)) {
            uniqueName.push(str);
        }
    }

    // 回去選取原本的姓名
    let compare = false;
    for (let str of uniqueName) {
        for (let name of data) {
            if (str === name.charAt(Math.floor(name.length / 2))) {
                console.log(name);
                compare = true;
                break; // 找到符合條件的姓名就跳出內層迴圈
            }
        }
        if (compare) {
            break; // 找到符合條件的姓名就跳出外層迴圈
        }
    }
    // 如果都沒有找到匹配的名字
    if (!compare) {
        console.log("沒有");
    }
}

func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安

console.log("===第四題===")
// Never change existing code.

// There is a number sequence: 0, 4, 8, 7, 11, 15, 14, 18, 22, 21, 25, …
// Find out the nth term in this sequence.


// 規律為 
// 1 4 
// 2 4+4 
     // 3 4+4-1 
// 4 4+4-1+4  4+1(4-1+4)
// 5 4+4-1+4+4 4+4(-1+4+4)
    // 6 4+4-1+4+4-1 
// 7 4+4-1+4+4-1+4 4+2(4-1+4)
// 8 4+4-1+4+4-1+4+4  4+4+2(-1+4+4)


function getNumber(index){
    // your code here
    let sum;

    if (index % 3 === 0) {
        sum = Math.floor(index / 3) * (4 + 4 - 1);
    } else if (index % 3 === 1) {
        sum = 4 + Math.floor(index / 3) * (4 - 1 + 4);
    } else {
        sum = 4 + 4 + Math.floor(index / 3) * (-1 + 4 + 4);
    }
    console.log(sum)

}    
    getNumber(1); // print 4
    getNumber(5); // print 15
    getNumber(10); // print 25
    getNumber(30); // print 70

console.log("===第五題===")
// Never change existing code.

// Given available spaces for each car of a train, status bitmap, and number of incoming
// passengers, writing a procedure to find out the index of the most fitted car to serve
// passengers. Print -1 if there is no car which can serve incoming passengers.
// - Available Spaces: list/array containing number of available seats for each car.
// - Status Bitmap: list/array containing only 0 or 1. 1 means the corresponding car can
// serve passengers for now.
// - Passenger Number: number of incoming passengers.
// We can assume all incoming passengers should be served in the same car. 所有乘客需要在同一個車廂


function find(spaces, stat, n) {
    // 創建陣列存放車廂所有資訊
    const relation = [];
    
    // 將 spaces 跟 stat 狀態存放至 relation
    for (let i = 0; i < spaces.length; i++) {
        relation.push({"spaces": spaces[i], "stat": stat[i]});
    }
    
    // 找出狀態為1(有服務)車廂，計算 spaceDiff
    for (let i = 0; i < relation.length; i++) {
        if (relation[i].stat === 1) {
            relation[i].spaceDiff = relation[i].spaces - n;
        }
    }
    
    // 找出 spaceDiff 最小的車廂的索引位置
    const closeDiff = relation.reduce((prev, curr) => prev.spaceDiff < curr.spaceDiff ? prev : curr);
    const closeIndex = relation.findIndex(car => car === closeDiff);
    
    // 判斷最小的車廂，它的車廂位置有沒有為正數或剛好(0)
    if (closeDiff.spaceDiff >= 0) {
        console.log(closeIndex);
    } else {
        console.log(-1);
    }
}
    

    find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2); // print 5
    find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1
    find([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2
