import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from loguru import logger
import os

# [설정] 프로젝트 폴더 및 데이터 경로
PROJECT_DIR = "yes24"
DATA_DIR = os.path.join(PROJECT_DIR, "data")
OUTPUT_FILE = os.path.join(DATA_DIR, "yes24_ai.csv")

# 데이터 디렉토리가 없으면 생성
os.makedirs(DATA_DIR, exist_ok=True)

# [문서화] 네트워크 정보 (GEMINI.md 및 agent_scraping.md 요구사항)
"""
### 네트워크 메뉴를 통해 실제 데이터를 가져오는 URL
Request URL: https://www.yes24.com/product/category/CategoryProductContents
Request Method: GET

### 해당 Request에 대한 Header 정보
- host: www.yes24.com
- referer: https://www.yes24.com/product/category/display/001001003032
- user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36
- x-requested-with: XMLHttpRequest

### Payload (Query Parameters)
- dispNo: 001001003032
- order: SINDEX_ONLY
- addOptionTp: 0
- page: {page}
- size: 120
- statGbYn: N
- usedTp: 0
- elemNo: 0
- elemSeq: 0
- seriesNumber: 0
"""

# 로거 설정
logger.add(os.path.join(PROJECT_DIR, "scraping_{time}.log"), rotation="500 MB")

def scrape_yes24_ai_books():
    base_url = "https://www.yes24.com/product/category/CategoryProductContents"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
        "referer": "https://www.yes24.com/product/category/display/001001003032",
        "x-requested-with": "XMLHttpRequest"
    }
    
    all_books = []
    
    for page in range(1, 11):
        logger.info(f"페이지 {page} 수집 시작 (120개 요청)...")
        
        params = {
            "dispNo": "001001003032",
            "order": "SINDEX_ONLY",
            "addOptionTp": "0",
            "page": page,
            "size": "120",
            "statGbYn": "N",
            "usedTp": "0",
            "elemNo": "0",
            "elemSeq": "0",
            "seriesNumber": "0"
        }
        
        try:
            response = requests.get(base_url, headers=headers, params=params)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            items = soup.select('.itemUnit')
            
            if not items:
                logger.warning(f"페이지 {page}에서 도서 아이템을 찾을 수 없습니다.")
                break
            
            for item in items:
                try:
                    # 제목
                    title_elem = item.select_one('.gd_name')
                    title = title_elem.get_text(strip=True) if title_elem else "N/A"
                    
                    # 상세 페이지 URL
                    detail_url = "https://www.yes24.com" + title_elem['href'] if title_elem and 'href' in title_elem.attrs else "N/A"
                    
                    # 상세 정보 (부제목 등)
                    detail_info_elem = item.select_one('.gd_nameE')
                    detail_info = detail_info_elem.get_text(strip=True) if detail_info_elem else ""

                    # 저자
                    author_elem = item.select_one('.info_auth')
                    author = author_elem.get_text(strip=True).replace(" 저", "") if author_elem else "N/A"
                    
                    # 출판사
                    pub_elem = item.select_one('.info_pub')
                    publisher = pub_elem.get_text(strip=True) if pub_elem else "N/A"
                    
                    # 발행일
                    date_elem = item.select_one('.info_date')
                    pub_date = date_elem.get_text(strip=True) if date_elem else "N/A"
                    
                    # 정가
                    reg_price_elem = item.select_one('.txt_num.dash .yes_m')
                    reg_price = reg_price_elem.get_text(strip=True).replace(",", "").replace("원", "") if reg_price_elem else "0"
                    
                    # 판매가
                    sale_price_elem = item.select_one('.txt_num .yes_b')
                    sale_price = sale_price_elem.get_text(strip=True).replace(",", "").replace("원", "") if sale_price_elem else "0"
                    
                    # 리뷰 수
                    review_elem = item.select_one('.rating_rvCount .txC_blue')
                    review_count = review_elem.get_text(strip=True) if review_elem else "0"
                    
                    # 판매지수
                    sale_num_elem = item.select_one('.saleNum')
                    sales_index = sale_num_elem.get_text(strip=True).replace("판매지수", "").strip().replace(",", "") if sale_num_elem else "0"
                    
                    # 설명
                    desc_elem = item.select_one('.info_read')
                    description = desc_elem.get_text(strip=True) if desc_elem else "N/A"
                    
                    book_data = {
                        "제목": title,
                        "저자": author,
                        "출판사": publisher,
                        "발행일": pub_date,
                        "정가": int(reg_price) if reg_price.isdigit() else 0,
                        "판매가": int(sale_price) if sale_price.isdigit() else 0,
                        "리뷰수": int(review_count) if review_count.isdigit() else 0,
                        "판매지수": int(sales_index) if sales_index.isdigit() else 0,
                        "상세정보": detail_info,
                        "설명": description,
                        "상세페이지URL": detail_url
                    }
                    all_books.append(book_data)
                    
                except Exception as e:
                    logger.error(f"아이템 파싱 중 오류 발생: {e}")
                    continue
            
            logger.info(f"페이지 {page} 수집 완료 (누적 {len(all_books)}개)")
            time.sleep(1.5)  # 1-2초 간격 유지
            
        except Exception as e:
            logger.error(f"페이지 {page} 요청 중 오류 발생: {e}")
            break

    # 데이터프레임 변환 및 저장
    if all_books:
        df = pd.DataFrame(all_books)
        # 중복 제거 (상세페이지URL 기준)
        df = df.drop_duplicates(subset=['상세페이지URL'])
        df.to_csv(OUTPUT_FILE, index=False, encoding='utf-8-sig')
        logger.info(f"전체 수집 완료. 데이터 저장됨: {OUTPUT_FILE}")
        logger.info(f"최종 수집된 도서 수: {len(df)}개")
        print(df.head())
    else:
        logger.warning("수집된 데이터가 없습니다.")

if __name__ == "__main__":
    scrape_yes24_ai_books()
