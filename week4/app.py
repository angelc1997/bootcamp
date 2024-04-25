from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware


app = FastAPI()


app.add_middleware( 
    SessionMiddleware, 
    same_site= "strict" , 
    session_cookie= "MY_SESSION_ID", 
    secret_key= "key" , 
)


app.mount("/public", StaticFiles(directory="public"), name="public")
templates = Jinja2Templates(directory="template")

# GET HOME
@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    sign_in = request.session.get("signin_in", False)

    if sign_in:
        return RedirectResponse("/member", status_code=303)
    
    return templates.TemplateResponse(request=request, name="home.html", context={"title": "首頁", "header_title": "歡迎光臨，請輸入帳號密碼"})

# POST SIGNIN
@app.post("/signin", response_class=RedirectResponse)
async def post_signin(request: Request, username: str = Form(None), password: str = Form(None)):
    if username == "test" and password == "test":
        request.session["signin_in"] = True
        return RedirectResponse("/member", status_code=303)
    if username is None or password is None:
        message = "帳號及密碼不能為空"
        return RedirectResponse(f"/error?message={message}", status_code=303)
    else:
        message = "帳號、或密碼錯誤"
        return RedirectResponse(f"/error?message={message}", status_code=303)

# GET MEMBER
@app.get("/member", response_class=HTMLResponse)
async def get_member(request: Request):
    sign_in = request.session.get("signin_in", False)
    if not sign_in:
        return RedirectResponse("/", status_code=303)
    return templates.TemplateResponse(request=request, name="member.html", context={"title": "會員頁面", "header_title": "歡迎光臨，這是會員頁", "message": "恭喜您，成功登入系統"})

# GET ERROR
@app.get("/error", response_class=HTMLResponse)
async def get_error(request: Request, message: str):
    return templates.TemplateResponse(request=request, name="error.html", context={"title": "錯誤頁面", "header_title": "失敗頁面", "message": message})

# GET SIGNOUT
@app.get("/signout")
async def get_signout(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=303)

# POST SQUARE
@app.post("/square", response_class=RedirectResponse)
async def post_square(request: Request, count: str = Form(...)):
    return RedirectResponse(f"/square/{count}", status_code=303)

# GET SQUARE
@app.get("/square/{count}", response_class=HTMLResponse)
async def get_square(request: Request, count: str):
    count = int(count)
    square = count * count
    return templates.TemplateResponse(request=request, name="square.html", context={"title": "計算頁面", "header_title": "正整數平方計算結果", "square": square})
