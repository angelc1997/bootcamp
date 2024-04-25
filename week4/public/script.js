document.getElementById("login_form").addEventListener("submit", function(event) {
    var checkbox = document.getElementById("checkbox");
    
    if (!checkbox.checked) {
        alert("請勾選同意條款");
        event.preventDefault(); 
    }
});

document.getElementById("count_form").addEventListener("submit", function(event){
    var count = document.getElementById("count").value;

    if (count <= 0 || count % 1 !== 0){
        alert("請輸入正整數");
        event.preventDefault();
    }
});
