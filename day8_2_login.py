from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # React 개발 서버만 허용(허용할 출처)
    allow_credentials=True,  #(인증정보 허용, 쿠키, jWT토큰 등등)
    allow_methods=["*"],     #허용할 HTTP메서드(get, post, patch, put, delete)
    allow_headers=["*"],     #허용할 http헤더(Content-Type, Authorization)
)

user = {'dkdlel':'qlqjs'}

class Login(BaseModel):
    userid : str
    password : str

@app.post('/login/')
async def login(login:Login):
    if login.userid not in user:
        return {'message':'없는 아이디'}
    if login.password != user[login.userid]:
        return {'message':'비번 틀림'}
    return {'message':'로그인 성공!'}