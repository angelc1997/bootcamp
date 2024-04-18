function showMenu(){
  const menu = document.querySelector('.menu')
  menu.style.display = 'flex'
}

function hideMenu(){
  const menu = document.querySelector('.menu')
  menu.style.display = 'none'
}


// 使用fetch發送請求
fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1")
.then(function(response){
    return response.json();
  })

.then(function(data){
    for (let i = 0 ; i < data.data.results.length ; i++) {

      // 找到json中的stitle => title
      let title = data.data.results[i].stitle;
  
      // 新增一個div，將title文字新增進div中
      element = document.createElement('div');
      element.textContent = title;
      textelements = document.querySelectorAll('.newdata'); 
      textelements[i].appendChild(element); 

       // 找到json中的filelist => img
      img = data.data.results[i].filelist;

      // 處理連結字串
      imglinks = img.split('https://');
      link1 = 'https://' + imglinks[1];

      // 使用 class 選取元素中的 img
      let imgelements = document.querySelectorAll('.newimg img'); 

      // 換掉img的src
      imgelements[i].src = link1; 
    }
  });


// function getData(){
// fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1").then(function(response){
//   return response.json();
// }).then(function(data){

//   var title = data.data.results[0].stitle
  

//   var element = document.createElement('div');
//       element.textContent = title;

//   var sboxTextElement = document.querySelector('.sbox_text');
//   sboxTextElement.appendChild(element);

// })

