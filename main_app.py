from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates
from job_api import get_saramin_jobs

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 정적 파일 경로 설정
app.mount("/static", StaticFiles(directory="static"), name="static")

# 홈 페이지 경로
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 공고 리스트 페이지 경로
@app.get("/construction_list", response_class=HTMLResponse)
async def construction_list(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 사람인 API에서 공고 데이터 가져오는 엔드포인트
@app.get("/api/get_saramin_jobs")
async def api_get_saramin_jobs(keywords: str = "건설"):
    jobs = get_saramin_jobs(keywords)
    return {"jobs": jobs}