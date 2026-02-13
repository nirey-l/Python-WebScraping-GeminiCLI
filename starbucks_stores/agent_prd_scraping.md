## 스타벅스 매장정보 수집
https://www.starbucks.co.kr/store/store_map.do

## 네트워크 메뉴를 통해 실제 데이터를 가져오는 URL
Request URL
https://www.starbucks.co.kr/store/getStore.do?r=I59I8PGZM9
Request Method
POST

## 해당 Request에 대한 Header 정보
host
www.starbucks.co.kr
origin
https://www.starbucks.co.kr
referer
https://www.starbucks.co.kr/store/store_map.do
sec-ch-ua
"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"
sec-ch-ua-mobile
?0
sec-ch-ua-platform
"Windows"
sec-fetch-dest
empty
sec-fetch-mode
cors
sec-fetch-site
same-origin
user-agent
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36


## Payload

in_biz_cds=0&in_scodes=0&ins_lat=37.56682&ins_lng=126.97865&search_text=&p_sido_cd=&p_gugun_cd=&isError=true&in_distance=5&in_biz_cd=&iend=30&searchType=A&set_date=&rndCod=041ECH5TRI


## 응답 예시 (JSON 의 일부 정보)
{
    "list": [
        {

"list"하위의 모든 정보 수집하기

## 수집 내역
p_sido_cd=01 부터 17까지 전국 스타벅스 매장 정보를 수집하는 파이썬 코드 starbucks_stores/starbucks_scraper.py를 작성할 것 
중간에 수집되는 내역을 확인할 수 있게 로그를 남길 것
수집한 내용을 현재 폴더 하위에 있는 data에 저장하고 파일명은 starbucks_stores/data/starbucks_ai.csv로 저장할 것 
