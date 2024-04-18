
// 漢堡選單切換按鈕
function showMenu(){
  const menu = document.querySelector('.menu')
  menu.style.display = 'flex'
}


function getData() {
  fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1")
      .then(function(response) {
          return response.json();
      })
      .then(function(data) {
          let results = data.data.results;

          // 清空原本的資料
          document.querySelectorAll('.newdata').forEach(function(element) {
              element.innerHTML = '';
          });
          document.querySelectorAll('.newimg img').forEach(function(imgElement) {
              imgElement.src = '';
          });

          // 顯示新的資料
          results.forEach(function(result, index) {
              let title = result.stitle;
              let element = document.createElement('div');
              element.textContent = title;
              let textelements = document.querySelectorAll('.newdata');
              if (textelements[index]) {
                  textelements[index].appendChild(element);
              }

              let img = result.filelist;
              let imglinks = img.split('https://');
              let link1 = 'https://' + imglinks[1];
              let imgelements = document.querySelectorAll('.newimg img');
              if (imgelements[index]) {
                  imgelements[index].src = link1;
              }
          });
      });
}

// 載入初始資料
getData(); 

// 追蹤點擊次數
var clickCount = 0; 

document.getElementById('btn_load').addEventListener('click', function() {
  
  // 點一次就加一
    clickCount++; 

  // 每次點按鈕都會重新載入資料
  getData();

  var boxes = document.querySelectorAll('.box.d, .box.e, .box.f, .box.g, .box.h, .box.i, .box.j, .box.k, .box.l, .box.m');

  if (clickCount <= 4) {
    var cloneCount = Math.min(boxes.length, 10);
    boxes.forEach(function(box, index) {
        if (index < cloneCount) {

            // cloneNode(true) 複製該元素的所有child，false通常只會複製該節點
            var cloneBox = box.cloneNode(true);

            // 將複製的box新增到wrapper中
            document.querySelector('.wrapper').appendChild(cloneBox);
        }
    });
  } else {
    var boxes = document.querySelectorAll('.box.d, .box.e, .box.f, .box.g, .box.h');
    var cloneCount = Math.min(boxes.length, 5);
    boxes.forEach(function(box, index) {
        if (index < cloneCount) {
            var cloneBox = box.cloneNode(true);
            document.querySelector('.wrapper').appendChild(cloneBox);
        }
    });

    // 更改按鈕的文字
    document.getElementById('btn_load').textContent = 'Refresh';

    // 新增refresh按鈕的功能，重新載入頁面
    document.getElementById('btn_load').addEventListener('click', function(){
      location.reload();
    });
  }
});