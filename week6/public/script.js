
document.getElementById("signup_form").addEventListener("submit", function(event) {
    var name = document.getElementById("signup_name").value.trim();
    var username = document.getElementById("signup_username").value.trim();
    var password = document.getElementById("signup_password").value.trim();

    
    if (!name || !username || !password) {
        alert("請填寫所有欄位資訊");
        event.preventDefault(); 
    }
});

document.getElementById("login_form").addEventListener("submit", function(event) {
    var username = document.getElementById("signin_username").value.trim();
    var password = document.getElementById("signin_password").value.trim();

    console.log(username, password);
    
    if (!username || !password) {
        alert("請輸入帳號及密碼");
        event.preventDefault(); 
    }
});

document.getElementById("signup_form").addEventListener("submit", function(event) {
    var checkbox = document.getElementById("checkbox");
    
    if (!checkbox.checked) {
        alert("請勾選同意條款");
        event.preventDefault(); 
    }
});


