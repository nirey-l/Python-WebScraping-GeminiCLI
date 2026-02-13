### 네트워크 메뉴를 통해 실제 데이터를 가져오는 URL
Request URL
https://frontapi.ssg.com/dp/api/v2/page/area
Request Method
POST

 
### 해당 Request에 대한 Header 정보
referer
https://www.ssg.com/page/pc/SpecialPrice.ssg
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
same-site
user-agent
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36


### Payload
{"common":{"aplVer":"","osCd":"","ts":"20260213043422","mobilAppNo":"99","dispDvicDivCd":"10","viewSiteNo":"6005"},"params":{"page":"2","state":"{}","pageId":"100000007533","pageSetId":"2","dispCtgId":null,"pageCmptId":"4"}}


### 응답 예시 (JSON 의 일부 정보)

{
    "cacheStatus": "NOT_STORED",
    "cacheStore": true,
    "resultCode": "200",
    "resultMsg": "SUCCESS",
    "resultDtlCode": null,
    "resultDtlMsg": null,
    "data": {
        "areaList": [
            [
                {
                    "cacheStatus": "NOT_STORED",
                    "cacheStore": true,
                    "unitType": "SPECIALDEAL_ITEM",
                    "dataType": "SPECIALPRICE_HOTDEAL",
                    "pageId": "100000007533",
                    "pageSetId": "2",
                    "pageCmptId": "4",
                    "reactPrefix": "특가|상품_2|",
                    "assocationParam": {
                        "actCtgId": null,
                        "dispCtgLowerId": null,
                        "hu": null,
                        "hr": null,
                        "reu": null,
                        "rer": null,
                        "fi": null,
                        "ru": null,
                        "re": null,
                        "pr": null,
                        "nrcq": null,
                        "dcim": null,
                        "nrcn": null,
                        "nrl": null,
                        "cornrSetId": null,
                        "brandId": null,
                        "dispCtgs": null,
                        "itemIds": null,
                        "frontItems": null,
                        "dti": null,
                        "itemProfId": null
                    },
                    "isAreaMoreFixedUnit": false,
                    "dispOrdr": 3,
                    "cornrSetId": "",
                    "itemList": [
                        {

응답 예시가 위와 같을 때 수집하고자 하는 데이터가  itemList 에 있을 때 itemList 하위의 모든 정보를 수집하는 코드를 작성하고 csv 파일로 저장 할 것                           