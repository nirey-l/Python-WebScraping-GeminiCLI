import requests
import pandas as pd
import os
from loguru import logger
from datetime import datetime

# 디렉토리 설정
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, 'data')
log_dir = os.path.join(base_dir, 'log')

# 로그 설정
log_filename = f"scraping_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logger.add(os.path.join(log_dir, log_filename), rotation="500 MB")

def scrape_starbucks():
    url = "https://www.starbucks.co.kr/store/getStore.do?r=I59I8PGZM9"
    headers = {
        "host": "www.starbucks.co.kr",
        "origin": "https://www.starbucks.co.kr",
        "referer": "https://www.starbucks.co.kr/store/store_map.do",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8"
    }

    all_stores = []

    # p_sido_cd 01 (서울) ~ 17 (세종) 까지 순회
    for sido_cd in range(1, 18):
        sido_str = str(sido_cd).zfill(2)
        logger.info(f"시/도 코드 {sido_str} 수집 시작...")

        payload = {
            "in_biz_cds": "0",
            "in_scodes": "0",
            "ins_lat": "37.56682",
            "ins_lng": "126.97865",
            "search_text": "",
            "p_sido_cd": sido_str,
            "p_gugun_cd": "",
            "isError": "true",
            "in_distance": "5",
            "in_biz_cd": "",
            "iend": "2000",  # 한 번에 모든 매장을 가져오기 위해 넉넉하게 설정
            "searchType": "C", # Sido 기반 검색을 위해 C로 설정 (A는 현재위치 중심)
            "set_date": "",
            "rndCod": "041ECH5TRI"
        }

        try:
            response = requests.post(url, data=payload, headers=headers)
            response.raise_for_status()
            data = response.json()
            
            store_list = data.get("list", [])
            logger.info(f"시/도 코드 {sido_str}: {len(store_list)}개 매장 발견")
            all_stores.extend(store_list)
            
        except Exception as e:
            logger.error(f"시/도 코드 {sido_str} 수집 중 에러 발생: {e}")

    if all_stores:
        df = pd.DataFrame(all_stores)
        output_path = os.path.join(data_dir, 'starbucks_ai.csv')
        df.to_csv(output_path, index=False, encoding='utf-8-sig')
        logger.success(f"수집 완료! 총 {len(df)}개 매장 정보가 '{output_path}'에 저장되었습니다.")
    else:
        logger.warning("수집된 데이터가 없습니다.")

if __name__ == "__main__":
    scrape_starbucks()
