import requests

def get_saramin_jobs(keywords="건설"):
    url = "https://oapi.saramin.co.kr/job-search"
    headers = {
        "Accept": "application/json"
    }
    params = {
        "access-key": "YOUR_ACCESS_KEY",  # 발급받은 API 키로 대체
        "keywords": keywords,
        "bbs_gb": 1  # 공채 여부 (1로 설정 시 공채만 가져옴)
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        jobs = []
        for item in data.get("jobs", {}).get("job", []):
            job_info = {
                "title": item["position"]["title"],
                "company": item["company"]["name"]["value"],
                "date": item["expiration_date"]
            }
            jobs.append(job_info)
        return jobs
    else:
        raise Exception("사람인 API 요청 실패")