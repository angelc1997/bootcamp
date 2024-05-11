#%%
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
import mysql.connector
import datetime


app = FastAPI()

# SETUP MYSQL CONNECTION
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1006",
  database="website"
)

mycursor = mydb.cursor()


app.add_middleware( 
    SessionMiddleware, 
    same_site= "strict" , 
    session_cookie= "MY_SESSION_ID", 
    secret_key= "key" , 
)


app.mount("/public", StaticFiles(directory="public"), name="public")
templates = Jinja2Templates(directory="templates")

def get_comments():
    sql = "SELECT message.*, member.name FROM message INNER JOIN member ON message.member_id = member.id ORDER BY message.time DESC"
    mycursor.execute(sql)
    comments = mycursor.fetchall()
    return comments

# GET HOME
@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):

    sign_in = request.session.get("signin_in", False)

    if sign_in:
        return RedirectResponse("/member", status_code=303)

    return templates.TemplateResponse(request=request, name="index.html", context={"title": "首頁", "header_title": "歡迎光臨，請註冊登入系統"})

# POST SIGNUP
@app.post("/signup", response_class=RedirectResponse)
async def post_signup(request: Request, signup_name: str = Form(None), signup_username: str = Form(None), signup_password: str = Form(None)):

    sql = "SELECT username FROM member WHERE username = %s"
    mycursor.execute(sql, (signup_username,))
    user = mycursor.fetchone()

    if user:
        username = user[0]
        message = "帳號已經被註冊使用"
        return RedirectResponse(f"/error?message={message}&username={username}" , status_code=303)  
    
    sql = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
    val = (signup_name, signup_username, signup_password)
    mycursor.execute(sql, val)
    mydb.commit()
    return RedirectResponse("/", status_code=303)


# POST SIGNIN
@app.post("/signin", response_class=RedirectResponse)
async def post_signin(request: Request, signin_username: str = Form(None), signin_password: str = Form(None)):

    sql = "SELECT id, username, password FROM member WHERE username = %s AND password = %s"
    mycursor.execute(sql, (signin_username, signin_password))
    user = mycursor.fetchone()

    if user[1] == signin_username and user[2] == signin_password:

        sql = "UPDATE member SET last_signin = %s WHERE id = %s"
        signin_time = datetime.datetime.now()
        mycursor.execute(sql, (signin_time, user[0]))
        mydb.commit()

        request.session["signin_in"] = True
        request.session["id"] = user[0]

        return RedirectResponse("/member", status_code=303)
    
    else: 
        message = "帳號或密碼輸入錯誤"
        return RedirectResponse(f"/error?message={message}", status_code=303)
   
    

# GET MEMBER
@app.get("/member", response_class=HTMLResponse)
async def get_member(request: Request):

    sign_in = request.session.get("signin_in", False)

    if not sign_in:
        return RedirectResponse("/", status_code=303)
    

    sql = "SELECT name FROM member WHERE id = %s"
    mycursor.execute(sql, (request.session.get("id"),))
    user = mycursor.fetchone()

    name = user[0]
    comments = get_comments()
  
    return templates.TemplateResponse(
        request=request, 
        name="member.html", 
        context={
            "title": "會員頁面", 
            "header_title": "歡迎光臨，這是會員頁", 
            "member": name, 
            "message": "，歡迎登入系統",
            "comments": comments,
             "member_id": request.session.get("id")
            })
           

# GET ERROR
@app.get("/error", response_class=HTMLResponse)
async def get_error(request: Request, username: str = None, message: str = None):

    if not message:
        return RedirectResponse("/", status_code=303)

    return templates.TemplateResponse(
        request=request, 
        name="error.html", 
        context={
            "title": "錯誤頁面", 
            "header_title": "失敗頁面",
            "username": username,
            "message": message})


# GET SIGNOUT
@app.get("/signout")
async def get_signout(request: Request):

    request.session.clear()
    return RedirectResponse("/", status_code=303)


# POST COMMENT
@app.post("/createMessage", response_class=RedirectResponse)
async def create_comment(request: Request, comment: str = Form(None)):

    user_id = request.session.get("id")
    sql = "INSERT INTO message(member_id , content) VALUES (%s, %s)"
    val = (user_id, comment)
    mycursor.execute(sql, val)
    mydb.commit()

    return RedirectResponse("/member", status_code=303)


# DELETE COMMENT
@app.post("/deleteMessage/{id}")
async def delete_comment(id: int):
    sql = "DELETE FROM message WHERE id = %s"
    mycursor.execute(sql, (id,))
    mydb.commit()

    return RedirectResponse("/member", status_code=303)
# %%
