# 스타벅스 매장 데이터 EDA 보고서

## 0. 기본 분석

### 데이터 로드 성공

데이터 경로: `starbucks_stores/data/starbucks_ai.csv`

### 데이터 구조

|    |   seq |   sido_cd |   sido_nm |   gugun_cd |   gugun_nm |   code_order |   view_yn |   store_num |   sido |   gugun |   address |   new_img_nm |   p_pro_seq |   p_view_yn |   p_sido_cd |   p_gugun_cd |   p_store_nm |   p_theme_cd |   p_wireless_yn |   p_smoking_yn |   p_book_yn |   p_music_yn |   p_terrace_yn |   p_table_yn |   p_takeout_yn |   p_parking_yn |   p_dollar_assent |   p_card_recharge |   p_subway_yn |   stb_store_file_renew |   stb_store_theme_renew |   stb_store_time_renew |   stb_store_lsm |   s_code | s_name   | tel       |   dlvry_call_cntr_phno | fax          |   sido_code | sido_name   |   gugun_code | gugun_name   | addr                          |   park_info | new_state   | theme_state                                                                                   |   new_bool |   search_text |   ins_lat |   ins_lng |   in_distance |   out_distance |   all_search_cnt |   addr_search_cnt |   store_search_cnt |   rowCount |   store_nm |   store_cd |   s_biz_code | new_icon   |   set_user |   favorites |   map_desc |   notice | defaultimage                                          |   etcimage |   in_biz_cd |   in_store_cd |   in_favorites |   in_user_id |   in_biz_cds |   in_biz_arr |   in_biz_arrdata |   in_scodes |   in_scode_arr |   in_scode_arrdata |   disp |   set_date |   hlytag |   hlytag_msg |   vSal |   istart |   iend |   open_dt |   gold_card |   ip_lat |   ip_long |   espresso |   new_store |   premiere_food | doro_address                         |   cold_blew | my_siren_order_store_yn   | whcroad_yn   |   skuNo |   skuName |   skuImgUrl |   stock_count |   store_area_name | store_area_code   |   is_open |   ev_open_yn |   option |   gift_stock_yn |     lat |     lot |   t20 |   t04 |   t03 |   t01 |   t12 |   t09 |   t06 |   t10 |   p10 |   p50 |   p20 |   p60 |   p30 |   p70 |   p40 |   p80 |   t22 |   t21 |   p90 |   p01 |   t05 |   t30 |   t36 |   t27 |   t29 |   t43 |   t48 |   z9999 |   t64 |   t66 |   p02 |
|---:|------:|----------:|----------:|-----------:|-----------:|-------------:|----------:|------------:|-------:|--------:|----------:|-------------:|------------:|------------:|------------:|-------------:|-------------:|-------------:|----------------:|---------------:|------------:|-------------:|---------------:|-------------:|---------------:|---------------:|------------------:|------------------:|--------------:|-----------------------:|------------------------:|-----------------------:|----------------:|---------:|:---------|:----------|-----------------------:|:-------------|------------:|:------------|-------------:|:-------------|:------------------------------|------------:|:------------|:----------------------------------------------------------------------------------------------|-----------:|--------------:|----------:|----------:|--------------:|---------------:|-----------------:|------------------:|-------------------:|-----------:|-----------:|-----------:|-------------:|:-----------|-----------:|------------:|-----------:|---------:|:------------------------------------------------------|-----------:|------------:|--------------:|---------------:|-------------:|-------------:|-------------:|-----------------:|------------:|---------------:|-------------------:|-------:|-----------:|---------:|-------------:|-------:|---------:|-------:|----------:|------------:|---------:|----------:|-----------:|------------:|----------------:|:-------------------------------------|------------:|:--------------------------|:-------------|--------:|----------:|------------:|--------------:|------------------:|:------------------|----------:|-------------:|---------:|----------------:|--------:|--------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|--------:|------:|------:|------:|
|  0 |     0 |       nan |       nan |        nan |        nan |          nan |       nan |         nan |    nan |     nan |       nan |          nan |           0 |         nan |         nan |          nan |          nan |          nan |             nan |            nan |         nan |          nan |            nan |          nan |            nan |            nan |               nan |               nan |           nan |                    nan |                     nan |                    nan |             nan |     1724 | 무교로      | 1522-3232 |                    nan | 02-3789-3955 |           1 | 서울          |          119 | 중구           | 서울특별시 중구 무교동 32-2 남강건설회관빌딩    |         nan | nan         | Z9999@T05@T08@T16@T17@T20@T21@T30@T32@T34@T36@@@T52@T56@T57@T64@T65@T69@P80@P90               |          0 |           nan |       nan |       nan |             0 |           0.06 |               -1 |                -1 |                 -1 |         30 |        nan |          0 |         3969 | N          |        nan |           0 |        nan |      nan | /upload/store/2020/10/[3969]_20201029075346_wbszq.jpg |        nan |         nan |           nan |            nan |          nan |            0 |          nan |              nan |           0 |            nan |                nan |    nan |        nan |      nan |          nan |    nan |        1 |     60 |  20201029 |           0 |      nan |       nan |        nan |         nan |             nan | 서울특별시 중구 무교로 15 (무교동)                |         nan | N                         | nan          |     nan |       nan |         nan |             0 |               nan | A01               |       nan |          nan |      nan |             nan | 37.5672 | 126.979 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |       0 |     0 |     0 |     0 |
|  1 |     0 |       nan |       nan |        nan |        nan |          nan |       nan |         nan |    nan |     nan |       nan |          nan |           0 |         nan |         nan |          nan |          nan |          nan |             nan |            nan |         nan |          nan |            nan |          nan |            nan |            nan |               nan |               nan |           nan |                    nan |                     nan |                    nan |             nan |     1047 | 한국프레스센터  | 1522-3232 |                    nan | 02-722-3264  |           1 | 서울          |          119 | 중구           | 서울특별시 중구 태평로1가 25 프레스센터       |         nan | nan         | Z9999@T05@T08@T16@T17@T20@T21@T30@T32@@@T52@T56@T57@T64@T65@T69@P80@P90@T09                   |          0 |           nan |       nan |       nan |             0 |           0.07 |               -1 |                -1 |                 -1 |         30 |        nan |          0 |         3263 | N          |        nan |           0 |        nan |      nan | /upload/store/2016/03/[3263]_20160328074259_xdpew.jpg |        nan |         nan |           nan |            nan |          nan |            0 |          nan |              nan |           0 |            nan |                nan |    nan |        nan |      nan |          nan |    nan |        1 |     60 |  20160328 |           0 |      nan |       nan |        nan |         nan |             nan | 서울특별시 중구 세종대로 124 (태평로1가)            |         nan | N                         | WHCROAD      |     nan |       nan |         nan |             0 |               nan | A01               |       nan |          nan |      nan |             nan | 37.5672 | 126.978 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |       0 |     0 |     0 |     0 |
|  2 |     0 |       nan |       nan |        nan |        nan |          nan |       nan |         nan |    nan |     nan |       nan |          nan |           0 |         nan |         nan |          nan |          nan |          nan |             nan |            nan |         nan |          nan |            nan |          nan |            nan |            nan |               nan |               nan |           nan |                    nan |                     nan |                    nan |             nan |      513 | 시청       | 1522-3232 |                    nan | 02-319-8504  |           1 | 서울          |          119 | 중구           | 서울특별시 중구 을지로1가 50 삼성화재 삼성빌딩1층 |         nan | Y           | T05@T08@T16@T17@T20@T21@T30@T32@@@T36@T43@T51@T52@@T56@T57@T64@T65@T69@T71@P80                |          0 |           nan |       nan |       nan |             0 |           0.12 |               -1 |                -1 |                 -1 |         30 |        nan |          0 |         9704 | N          |        nan |           0 |        nan |      nan | /upload/store/2022/12/[9704]_20221223075102_3hoe2.jpg |        nan |         nan |           nan |            nan |          nan |            0 |          nan |              nan |           0 |            nan |                nan |    nan |        nan |      nan |          nan |    nan |        1 |     60 |  20120502 |           0 |      nan |       nan |        nan |         nan |             nan | 서울특별시 중구 을지로 19, 삼성화재삼성빌딩 1층 (을지로1가) |         nan | N                         | WHCROAD      |     nan |       nan |         nan |             0 |               nan | A01               |       nan |          nan |      nan |             nan | 37.5663 | 126.98  |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |       0 |     0 |     0 |     0 |
|  3 |     0 |       nan |       nan |        nan |        nan |          nan |       nan |         nan |    nan |     nan |       nan |          nan |           0 |         nan |         nan |          nan |          nan |          nan |             nan |            nan |         nan |          nan |            nan |          nan |            nan |            nan |               nan |               nan |           nan |                    nan |                     nan |                    nan |             nan |      179 | 무교동      | 1522-3232 |                    nan | 02-779-1838  |           1 | 서울          |          119 | 중구           | 서울특별시 중구 무교동 45 코오롱빌딩         |         nan | N           | Z9999@T05@T08@T16@T17@T20@@T30@T32@T34@@@T36@T51@T52@T56@T57@T64@T65@T69@T73@P80@T09          |          0 |           nan |       nan |       nan |             0 |           0.13 |               -1 |                -1 |                 -1 |         30 |        nan |          0 |         9237 | N          |        nan |           0 |        nan |      nan | /upload/store/2021/11/[9237]_20211101080653_2anba.jpg |        nan |         nan |           nan |            nan |          nan |            0 |          nan |              nan |           0 |            nan |                nan |    nan |        nan |      nan |          nan |    nan |        1 |     60 |  20020308 |           0 |      nan |       nan |        nan |         nan |             nan | 서울특별시 중구 무교로 21 (무교동) 코오롱빌딩 1층       |         nan | N                         | WHCROAD      |     nan |       nan |         nan |             0 |               nan | A01               |       nan |          nan |      nan |             nan | 37.5679 | 126.979 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |       0 |     0 |     0 |     0 |
|  4 |     0 |       nan |       nan |        nan |        nan |          nan |       nan |         nan |    nan |     nan |       nan |          nan |           0 |         nan |         nan |          nan |          nan |          nan |             nan |            nan |         nan |          nan |            nan |          nan |            nan |            nan |               nan |               nan |           nan |                    nan |                     nan |                    nan |             nan |      234 | 환구단      | 1522-3232 |                    nan | 02-778-1940  |           1 | 서울          |          119 | 중구           | 서울특별시 중구 소공동 87-10            |         nan | N           | Z9999@T05@T08@T12@T16@T17@T20@T21@T22@T30@T32@T34@@@@T43@T52@@T56@T57@T64@T65@T69@T71@P80@P90 |          0 |           nan |       nan |       nan |             0 |           0.26 |               -1 |                -1 |                 -1 |         30 |        nan |          0 |         9340 | N          |        nan |           0 |        nan |      nan | /upload/store/2024/08/[9340]_20240819073851_1q215.png |        nan |         nan |           nan |            nan |          nan |            0 |          nan |              nan |           0 |            nan |                nan |    nan |        nan |      nan |          nan |    nan |        1 |     60 |  20051020 |           0 |      nan |       nan |        nan |         nan |             nan | 서울특별시 중구 소공로 112 (소공동)               |         nan | N                         | WHCROAD      |     nan |       nan |         nan |             0 |               nan | A01               |       nan |          nan |      nan |             nan | 37.5645 | 126.979 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |       0 |     0 |     0 |     0 |

### 데이터 정보 (df.info())

```
<class 'pandas.DataFrame'>
RangeIndex: 173 entries, 0 to 172
Columns: 137 entries, seq to p02
dtypes: float64(71), int64(52), str(14)
memory usage: 185.3 KB

```

### 기술 통계

|        |   seq |   sido_cd |   sido_nm |   gugun_cd |   gugun_nm |   code_order |   view_yn |   store_num |   sido |   gugun |   address |   new_img_nm |   p_pro_seq |   p_view_yn |   p_sido_cd |   p_gugun_cd |   p_store_nm |   p_theme_cd |   p_wireless_yn |   p_smoking_yn |   p_book_yn |   p_music_yn |   p_terrace_yn |   p_table_yn |   p_takeout_yn |   p_parking_yn |   p_dollar_assent |   p_card_recharge |   p_subway_yn |   stb_store_file_renew |   stb_store_theme_renew |   stb_store_time_renew |   stb_store_lsm |   s_code | s_name   | tel       |   dlvry_call_cntr_phno | fax   |   sido_code | sido_name   |   gugun_code | gugun_name   | addr                             |   park_info | new_state   | theme_state                                                                     |   new_bool |   search_text |   ins_lat |   ins_lng |   in_distance |   out_distance |   all_search_cnt |   addr_search_cnt |   store_search_cnt |   rowCount |   store_nm |   store_cd |   s_biz_code | new_icon   |   set_user |   favorites |   map_desc |   notice | defaultimage                                          |   etcimage |   in_biz_cd |   in_store_cd |   in_favorites |   in_user_id |   in_biz_cds |   in_biz_arr |   in_biz_arrdata |   in_scodes |   in_scode_arr |   in_scode_arrdata |   disp |   set_date |   hlytag |   hlytag_msg |   vSal |   istart |   iend |         open_dt |   gold_card |   ip_lat |   ip_long |   espresso |   new_store |   premiere_food | doro_address             |   cold_blew | my_siren_order_store_yn   | whcroad_yn   |   skuNo |   skuName |   skuImgUrl |   stock_count |   store_area_name | store_area_code   |   is_open |   ev_open_yn |   option |   gift_stock_yn |        lat |         lot |   t20 |   t04 |   t03 |   t01 |   t12 |   t09 |   t06 |   t10 |   p10 |   p50 |   p20 |   p60 |   p30 |   p70 |   p40 |   p80 |   t22 |   t21 |   p90 |   p01 |   t05 |   t30 |   t36 |   t27 |   t29 |   t43 |   t48 |   z9999 |   t64 |   t66 |   p02 |
|:-------|------:|----------:|----------:|-----------:|-----------:|-------------:|----------:|------------:|-------:|--------:|----------:|-------------:|------------:|------------:|------------:|-------------:|-------------:|-------------:|----------------:|---------------:|------------:|-------------:|---------------:|-------------:|---------------:|---------------:|------------------:|------------------:|--------------:|-----------------------:|------------------------:|-----------------------:|----------------:|---------:|:---------|:----------|-----------------------:|:------|------------:|:------------|-------------:|:-------------|:---------------------------------|------------:|:------------|:--------------------------------------------------------------------------------|-----------:|--------------:|----------:|----------:|--------------:|---------------:|-----------------:|------------------:|-------------------:|-----------:|-----------:|-----------:|-------------:|:-----------|-----------:|------------:|-----------:|---------:|:------------------------------------------------------|-----------:|------------:|--------------:|---------------:|-------------:|-------------:|-------------:|-----------------:|------------:|---------------:|-------------------:|-------:|-----------:|---------:|-------------:|-------:|---------:|-------:|----------------:|------------:|---------:|----------:|-----------:|------------:|----------------:|:-------------------------|------------:|:--------------------------|:-------------|--------:|----------:|------------:|--------------:|------------------:|:------------------|----------:|-------------:|---------:|----------------:|-----------:|------------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|--------:|------:|------:|------:|
| count  |   173 |         0 |         0 |          0 |          0 |            0 |         0 |           0 |      0 |       0 |         0 |            0 |         173 |           0 |           0 |            0 |            0 |            0 |               0 |              0 |           0 |            0 |              0 |            0 |              0 |              0 |                 0 |                 0 |             0 |                      0 |                       0 |                      0 |               0 |  173     | 173      | 173       |                      0 | 173   |         173 | 173         |    173       | 173          | 173                              |           0 | 71          | 173                                                                             |        173 |             0 |         0 |         0 |           173 |      173       |              173 |               173 |                173 |        173 |          0 |        173 |       173    | 173        |          0 |         173 |          0 |        0 | 173                                                   |          0 |           0 |             0 |              0 |            0 |          173 |            0 |                0 |         173 |              0 |                  0 |      0 |          0 |        0 |            0 |      0 |      173 |    173 |   173           |         173 |        0 |         0 |          0 |           0 |               0 | 173                      |           0 | 173                       | 130          |       0 |         0 |           0 |           173 |                 0 | 173               |         0 |            0 |        0 |               0 | 173        | 173         |   173 |   173 |   173 |   173 |   173 |   173 |   173 |   173 |   173 |   173 |   173 |   173 |   173 |   173 |   173 |   173 |   173 |   173 |   173 |   173 |   173 |   173 |   173 |   173 |   173 |   173 |   173 |     173 |   173 |   173 |   173 |
| unique |   nan |       nan |       nan |        nan |        nan |          nan |       nan |         nan |    nan |     nan |       nan |          nan |         nan |         nan |         nan |          nan |          nan |          nan |             nan |            nan |         nan |          nan |            nan |          nan |            nan |            nan |               nan |               nan |           nan |                    nan |                     nan |                    nan |             nan |  nan     | 173      | 1         |                    nan | 151   |         nan | 1           |    nan       | 8            | 172                              |         nan | 2           | 173                                                                             |        nan |           nan |       nan |       nan |           nan |      nan       |              nan |               nan |                nan |        nan |        nan |        nan |       nan    | 1          |        nan |         nan |        nan |      nan | 173                                                   |        nan |         nan |           nan |            nan |          nan |          nan |          nan |              nan |         nan |            nan |                nan |    nan |        nan |      nan |          nan |    nan |      nan |    nan |   nan           |         nan |      nan |       nan |        nan |         nan |             nan | 172                      |         nan | 1                         | 1            |     nan |       nan |         nan |           nan |               nan | 1                 |       nan |          nan |      nan |             nan | nan        | nan         |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |     nan |   nan |   nan |   nan |
| top    |   nan |       nan |       nan |        nan |        nan |          nan |       nan |         nan |    nan |     nan |       nan |          nan |         nan |         nan |         nan |          nan |          nan |          nan |             nan |            nan |         nan |          nan |            nan |          nan |            nan |            nan |               nan |               nan |           nan |                    nan |                     nan |                    nan |             nan |  nan     | 무교로      | 1522-3232 |                    nan | --    |         nan | 서울          |    nan       | 중구           | 서울특별시 종로구 세종로 100 KT 광화문 빌딩 West |         nan | Y           | Z9999@T05@T08@T16@T17@T20@T21@T30@T32@T34@T36@@@T52@T56@T57@T64@T65@T69@P80@P90 |        nan |           nan |       nan |       nan |           nan |      nan       |              nan |               nan |                nan |        nan |        nan |        nan |       nan    | N          |        nan |         nan |        nan |      nan | /upload/store/2020/10/[3969]_20201029075346_wbszq.jpg |        nan |         nan |           nan |            nan |          nan |          nan |          nan |              nan |         nan |            nan |                nan |    nan |        nan |      nan |          nan |    nan |      nan |    nan |   nan           |         nan |      nan |       nan |        nan |         nan |             nan | 서울특별시 종로구 세종대로 178 (세종로) |         nan | N                         | WHCROAD      |     nan |       nan |         nan |           nan |               nan | A01               |       nan |          nan |      nan |             nan | nan        | nan         |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |     nan |   nan |   nan |   nan |
| freq   |   nan |       nan |       nan |        nan |        nan |          nan |       nan |         nan |    nan |     nan |       nan |          nan |         nan |         nan |         nan |          nan |          nan |          nan |             nan |            nan |         nan |          nan |            nan |          nan |            nan |            nan |               nan |               nan |           nan |                    nan |                     nan |                    nan |             nan |  nan     | 1        | 173       |                    nan | 22    |         nan | 173         |    nan       | 54           | 2                                |         nan | 37          | 1                                                                               |        nan |           nan |       nan |       nan |           nan |      nan       |              nan |               nan |                nan |        nan |        nan |        nan |       nan    | 173        |        nan |         nan |        nan |      nan | 1                                                     |        nan |         nan |           nan |            nan |          nan |          nan |          nan |              nan |         nan |            nan |                nan |    nan |        nan |      nan |          nan |    nan |      nan |    nan |   nan           |         nan |      nan |       nan |        nan |         nan |             nan | 2                        |         nan | 173                       | 130          |     nan |       nan |         nan |           nan |               nan | 173               |       nan |          nan |      nan |             nan | nan        | nan         |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |   nan |     nan |   nan |   nan |   nan |
| mean   |     0 |       nan |       nan |        nan |        nan |          nan |       nan |         nan |    nan |     nan |       nan |          nan |           0 |         nan |         nan |          nan |          nan |          nan |             nan |            nan |         nan |          nan |            nan |          nan |            nan |            nan |               nan |               nan |           nan |                    nan |                     nan |                    nan |             nan | 1160.83  | nan      | nan       |                    nan | nan   |           1 | nan         |    117.37    | nan          | nan                              |         nan | nan         | nan                                                                             |          0 |           nan |       nan |       nan |             0 |        2.34012 |               -1 |                -1 |                 -1 |         30 |        nan |          0 |      5807.02 | nan        |        nan |           0 |        nan |      nan | nan                                                   |        nan |         nan |           nan |            nan |          nan |            0 |          nan |              nan |           0 |            nan |                nan |    nan |        nan |      nan |          nan |    nan |        1 |     60 |     2.01574e+07 |           0 |      nan |       nan |        nan |         nan |             nan | nan                      |         nan | nan                       | nan          |     nan |       nan |         nan |             0 |               nan | nan               |       nan |          nan |      nan |             nan |  37.5617   | 126.977     |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |       0 |     0 |     0 |     0 |
| std    |     0 |       nan |       nan |        nan |        nan |          nan |       nan |         nan |    nan |     nan |       nan |          nan |           0 |         nan |         nan |          nan |          nan |          nan |             nan |            nan |         nan |          nan |            nan |          nan |            nan |            nan |               nan |               nan |           nan |                    nan |                     nan |                    nan |             nan |  723.114 | nan      | nan       |                    nan | nan   |           0 | nan         |      4.45541 | nan          | nan                              |         nan | nan         | nan                                                                             |          0 |           nan |       nan |       nan |             0 |        1.5204  |                0 |                 0 |                  0 |          0 |        nan |          0 |      2774.47 | nan        |        nan |           0 |        nan |      nan | nan                                                   |        nan |         nan |           nan |            nan |          nan |            0 |          nan |              nan |           0 |            nan |                nan |    nan |        nan |      nan |          nan |    nan |        0 |      0 | 61504.7         |           0 |      nan |       nan |        nan |         nan |             nan | nan                      |         nan | nan                       | nan          |     nan |       nan |         nan |             0 |               nan | nan               |       nan |          nan |      nan |             nan |   0.014632 |   0.0249322 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |       0 |     0 |     0 |     0 |
| min    |     0 |       nan |       nan |        nan |        nan |          nan |       nan |         nan |    nan |     nan |       nan |          nan |           0 |         nan |         nan |          nan |          nan |          nan |             nan |            nan |         nan |          nan |            nan |          nan |            nan |            nan |               nan |               nan |           nan |                    nan |                     nan |                    nan |             nan |   33     | nan      | nan       |                    nan | nan   |           1 | nan         |    110       | nan          | nan                              |         nan | nan         | nan                                                                             |          0 |           nan |       nan |       nan |             0 |        0.06    |               -1 |                -1 |                 -1 |         30 |        nan |          0 |      3018    | nan        |        nan |           0 |        nan |      nan | nan                                                   |        nan |         nan |           nan |            nan |          nan |            0 |          nan |              nan |           0 |            nan |                nan |    nan |        nan |      nan |          nan |    nan |        1 |     60 |     1.99907e+07 |           0 |      nan |       nan |        nan |         nan |             nan | nan                      |         nan | nan                       | nan          |     nan |       nan |         nan |             0 |               nan | nan               |       nan |          nan |      nan |             nan |  37.5238   | 126.924     |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |       0 |     0 |     0 |     0 |
| 25%    |     0 |       nan |       nan |        nan |        nan |          nan |       nan |         nan |    nan |     nan |       nan |          nan |           0 |         nan |         nan |          nan |          nan |          nan |             nan |            nan |         nan |          nan |            nan |          nan |            nan |            nan |               nan |               nan |           nan |                    nan |                     nan |                    nan |             nan |  491     | nan      | nan       |                    nan | nan   |           1 | nan         |    113       | nan          | nan                              |         nan | nan         | nan                                                                             |          0 |           nan |       nan |       nan |             0 |        0.88    |               -1 |                -1 |                 -1 |         30 |        nan |          0 |      3549    | nan        |        nan |           0 |        nan |      nan | nan                                                   |        nan |         nan |           nan |            nan |          nan |            0 |          nan |              nan |           0 |            nan |                nan |    nan |        nan |      nan |          nan |    nan |        1 |     60 |     2.01203e+07 |           0 |      nan |       nan |        nan |         nan |             nan | nan                      |         nan | nan                       | nan          |     nan |       nan |         nan |             0 |               nan | nan               |       nan |          nan |      nan |             nan |  37.5558   | 126.965     |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |       0 |     0 |     0 |     0 |
| 50%    |     0 |       nan |       nan |        nan |        nan |          nan |       nan |         nan |    nan |     nan |       nan |          nan |           0 |         nan |         nan |          nan |          nan |          nan |             nan |            nan |         nan |          nan |            nan |          nan |            nan |            nan |               nan |               nan |           nan |                    nan |                     nan |                    nan |             nan | 1137     | nan      | nan       |                    nan | nan   |           1 | nan         |    118       | nan          | nan                              |         nan | nan         | nan                                                                             |          0 |           nan |       nan |       nan |             0 |        2.35    |               -1 |                -1 |                 -1 |         30 |        nan |          0 |      4340    | nan        |        nan |           0 |        nan |      nan | nan                                                   |        nan |         nan |           nan |            nan |          nan |            0 |          nan |              nan |           0 |            nan |                nan |    nan |        nan |      nan |          nan |    nan |        1 |     60 |     2.01611e+07 |           0 |      nan |       nan |        nan |         nan |             nan | nan                      |         nan | nan                       | nan          |     nan |       nan |         nan |             0 |               nan | nan               |       nan |          nan |      nan |             nan |  37.5629   | 126.978     |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |       0 |     0 |     0 |     0 |
| 75%    |     0 |       nan |       nan |        nan |        nan |          nan |       nan |         nan |    nan |     nan |       nan |          nan |           0 |         nan |         nan |          nan |          nan |          nan |             nan |            nan |         nan |          nan |            nan |          nan |            nan |            nan |               nan |               nan |           nan |                    nan |                     nan |                    nan |             nan | 1729     | nan      | nan       |                    nan | nan   |           1 | nan         |    119       | nan          | nan                              |         nan | nan         | nan                                                                             |          0 |           nan |       nan |       nan |             0 |        3.85    |               -1 |                -1 |                 -1 |         30 |        nan |          0 |      9409    | nan        |        nan |           0 |        nan |      nan | nan                                                   |        nan |         nan |           nan |            nan |          nan |            0 |          nan |              nan |           0 |            nan |                nan |    nan |        nan |      nan |          nan |    nan |        1 |     60 |     2.02012e+07 |           0 |      nan |       nan |        nan |         nan |             nan | nan                      |         nan | nan                       | nan          |     nan |       nan |         nan |             0 |               nan | nan               |       nan |          nan |      nan |             nan |  37.57     | 126.992     |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |       0 |     0 |     0 |     0 |
| max    |     0 |       nan |       nan |        nan |        nan |          nan |       nan |         nan |    nan |     nan |       nan |          nan |           0 |         nan |         nan |          nan |          nan |          nan |             nan |            nan |         nan |          nan |            nan |          nan |            nan |            nan |               nan |               nan |           nan |                    nan |                     nan |                    nan |             nan | 2519     | nan      | nan       |                    nan | nan   |           1 | nan         |    124       | nan          | nan                              |         nan | nan         | nan                                                                             |          0 |           nan |       nan |       nan |             0 |        4.96    |               -1 |                -1 |                 -1 |         30 |        nan |          0 |      9988    | nan        |        nan |           0 |        nan |      nan | nan                                                   |        nan |         nan |           nan |            nan |          nan |            0 |          nan |              nan |           0 |            nan |                nan |    nan |        nan |      nan |          nan |    nan |        1 |     60 |     2.02602e+07 |           0 |      nan |       nan |        nan |         nan |             nan | nan                      |         nan | nan                       | nan          |     nan |       nan |         nan |             0 |               nan | nan               |       nan |          nan |      nan |             nan |  37.6061   | 127.034     |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |       0 |     0 |     0 |     0 |

### 결측치 및 단일 값 컬럼 제거

#### 제거 전 결측치 비율

```
seq                          0.000000
sido_cd                    100.000000
sido_nm                    100.000000
gugun_cd                   100.000000
gugun_nm                   100.000000
code_order                 100.000000
view_yn                    100.000000
store_num                  100.000000
sido                       100.000000
gugun                      100.000000
address                    100.000000
new_img_nm                 100.000000
p_pro_seq                    0.000000
p_view_yn                  100.000000
p_sido_cd                  100.000000
p_gugun_cd                 100.000000
p_store_nm                 100.000000
p_theme_cd                 100.000000
p_wireless_yn              100.000000
p_smoking_yn               100.000000
p_book_yn                  100.000000
p_music_yn                 100.000000
p_terrace_yn               100.000000
p_table_yn                 100.000000
p_takeout_yn               100.000000
p_parking_yn               100.000000
p_dollar_assent            100.000000
p_card_recharge            100.000000
p_subway_yn                100.000000
stb_store_file_renew       100.000000
stb_store_theme_renew      100.000000
stb_store_time_renew       100.000000
stb_store_lsm              100.000000
s_code                       0.000000
s_name                       0.000000
tel                          0.000000
dlvry_call_cntr_phno       100.000000
fax                          0.000000
sido_code                    0.000000
sido_name                    0.000000
gugun_code                   0.000000
gugun_name                   0.000000
addr                         0.000000
park_info                  100.000000
new_state                   58.959538
theme_state                  0.000000
new_bool                     0.000000
search_text                100.000000
ins_lat                    100.000000
ins_lng                    100.000000
in_distance                  0.000000
out_distance                 0.000000
all_search_cnt               0.000000
addr_search_cnt              0.000000
store_search_cnt             0.000000
rowCount                     0.000000
store_nm                   100.000000
store_cd                     0.000000
s_biz_code                   0.000000
new_icon                     0.000000
set_user                   100.000000
favorites                    0.000000
map_desc                   100.000000
notice                     100.000000
defaultimage                 0.000000
etcimage                   100.000000
in_biz_cd                  100.000000
in_store_cd                100.000000
in_favorites               100.000000
in_user_id                 100.000000
in_biz_cds                   0.000000
in_biz_arr                 100.000000
in_biz_arrdata             100.000000
in_scodes                    0.000000
in_scode_arr               100.000000
in_scode_arrdata           100.000000
disp                       100.000000
set_date                   100.000000
hlytag                     100.000000
hlytag_msg                 100.000000
vSal                       100.000000
istart                       0.000000
iend                         0.000000
open_dt                      0.000000
gold_card                    0.000000
ip_lat                     100.000000
ip_long                    100.000000
espresso                   100.000000
new_store                  100.000000
premiere_food              100.000000
doro_address                 0.000000
cold_blew                  100.000000
my_siren_order_store_yn      0.000000
whcroad_yn                  24.855491
skuNo                      100.000000
skuName                    100.000000
skuImgUrl                  100.000000
stock_count                  0.000000
store_area_name            100.000000
store_area_code              0.000000
is_open                    100.000000
ev_open_yn                 100.000000
option                     100.000000
gift_stock_yn              100.000000
lat                          0.000000
lot                          0.000000
t20                          0.000000
t04                          0.000000
t03                          0.000000
t01                          0.000000
t12                          0.000000
t09                          0.000000
t06                          0.000000
t10                          0.000000
p10                          0.000000
p50                          0.000000
p20                          0.000000
p60                          0.000000
p30                          0.000000
p70                          0.000000
p40                          0.000000
p80                          0.000000
t22                          0.000000
t21                          0.000000
p90                          0.000000
p01                          0.000000
t05                          0.000000
t30                          0.000000
t36                          0.000000
t27                          0.000000
t29                          0.000000
t43                          0.000000
t48                          0.000000
z9999                        0.000000
t64                          0.000000
t66                          0.000000
p02                          0.000000
```

#### 제거된 컬럼: `['seq', 'sido_cd', 'sido_nm', 'gugun_cd', 'gugun_nm', 'code_order', 'view_yn', 'store_num', 'sido', 'gugun', 'address', 'new_img_nm', 'p_view_yn', 'p_sido_cd', 'p_gugun_cd', 'p_store_nm', 'p_theme_cd', 'p_wireless_yn', 'p_smoking_yn', 'p_book_yn', 'p_music_yn', 'p_terrace_yn', 'p_table_yn', 'p_takeout_yn', 'p_parking_yn', 'p_dollar_assent', 'p_card_recharge', 'p_subway_yn', 'stb_store_file_renew', 'stb_store_theme_renew', 'stb_store_time_renew', 'stb_store_lsm', 'dlvry_call_cntr_phno', 'sido_code', 'park_info', 'new_bool', 'search_text', 'ins_lat', 'ins_lng', 'in_distance', 'all_search_cnt', 'addr_search_cnt', 'store_search_cnt', 'rowCount', 'store_nm', 'store_cd', 'new_icon', 'set_user', 'favorites', 'map_desc', 'notice', 'etcimage', 'in_biz_cd', 'in_store_cd', 'in_favorites', 'in_user_id', 'in_biz_cds', 'in_biz_arr', 'in_biz_arrdata', 'in_scodes', 'in_scode_arr', 'in_scode_arrdata', 'disp', 'set_date', 'hlytag', 'hlytag_msg', 'vSal', 'istart', 'iend', 'gold_card', 'ip_lat', 'ip_long', 'espresso', 'new_store', 'premiere_food', 'cold_blew', 'my_siren_order_store_yn', 'whcroad_yn', 'skuNo', 'skuName', 'skuImgUrl', 'stock_count', 'store_area_name', 'store_area_code', 'is_open', 'ev_open_yn', 'option', 'gift_stock_yn', 'z9999']`

#### 제거 후 데이터 구조

|    |   p_pro_seq |   s_code | s_name   | tel       | fax          | sido_name   |   gugun_code | gugun_name   | addr                          | new_state   | theme_state                                                                                   |   out_distance |   s_biz_code | defaultimage                                          |   open_dt | doro_address                         |     lat |     lot |   t20 |   t04 |   t03 |   t01 |   t12 |   t09 |   t06 |   t10 |   p10 |   p50 |   p20 |   p60 |   p30 |   p70 |   p40 |   p80 |   t22 |   t21 |   p90 |   p01 |   t05 |   t30 |   t36 |   t27 |   t29 |   t43 |   t48 |   t64 |   t66 |   p02 |
|---:|------------:|---------:|:---------|:----------|:-------------|:------------|-------------:|:-------------|:------------------------------|:------------|:----------------------------------------------------------------------------------------------|---------------:|-------------:|:------------------------------------------------------|----------:|:-------------------------------------|--------:|--------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
|  0 |           0 |     1724 | 무교로      | 1522-3232 | 02-3789-3955 | 서울          |          119 | 중구           | 서울특별시 중구 무교동 32-2 남강건설회관빌딩    | nan         | Z9999@T05@T08@T16@T17@T20@T21@T30@T32@T34@T36@@@T52@T56@T57@T64@T65@T69@P80@P90               |           0.06 |         3969 | /upload/store/2020/10/[3969]_20201029075346_wbszq.jpg |  20201029 | 서울특별시 중구 무교로 15 (무교동)                | 37.5672 | 126.979 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |
|  1 |           0 |     1047 | 한국프레스센터  | 1522-3232 | 02-722-3264  | 서울          |          119 | 중구           | 서울특별시 중구 태평로1가 25 프레스센터       | nan         | Z9999@T05@T08@T16@T17@T20@T21@T30@T32@@@T52@T56@T57@T64@T65@T69@P80@P90@T09                   |           0.07 |         3263 | /upload/store/2016/03/[3263]_20160328074259_xdpew.jpg |  20160328 | 서울특별시 중구 세종대로 124 (태평로1가)            | 37.5672 | 126.978 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |
|  2 |           0 |      513 | 시청       | 1522-3232 | 02-319-8504  | 서울          |          119 | 중구           | 서울특별시 중구 을지로1가 50 삼성화재 삼성빌딩1층 | Y           | T05@T08@T16@T17@T20@T21@T30@T32@@@T36@T43@T51@T52@@T56@T57@T64@T65@T69@T71@P80                |           0.12 |         9704 | /upload/store/2022/12/[9704]_20221223075102_3hoe2.jpg |  20120502 | 서울특별시 중구 을지로 19, 삼성화재삼성빌딩 1층 (을지로1가) | 37.5663 | 126.98  |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |
|  3 |           0 |      179 | 무교동      | 1522-3232 | 02-779-1838  | 서울          |          119 | 중구           | 서울특별시 중구 무교동 45 코오롱빌딩         | N           | Z9999@T05@T08@T16@T17@T20@@T30@T32@T34@@@T36@T51@T52@T56@T57@T64@T65@T69@T73@P80@T09          |           0.13 |         9237 | /upload/store/2021/11/[9237]_20211101080653_2anba.jpg |  20020308 | 서울특별시 중구 무교로 21 (무교동) 코오롱빌딩 1층       | 37.5679 | 126.979 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |
|  4 |           0 |      234 | 환구단      | 1522-3232 | 02-778-1940  | 서울          |          119 | 중구           | 서울특별시 중구 소공동 87-10            | N           | Z9999@T05@T08@T12@T16@T17@T20@T21@T22@T30@T32@T34@@@@T43@T52@@T56@T57@T64@T65@T69@T71@P80@P90 |           0.26 |         9340 | /upload/store/2024/08/[9340]_20240819073851_1q215.png |  20051020 | 서울특별시 중구 소공로 112 (소공동)               | 37.5645 | 126.979 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |     0 |

## 1. 기본 정보 요약

주요 필드(매장명, 시/도, 시/군/구, 주소, 오픈일) 요약

|    | s_name   | sido_name   | gugun_name   | doro_address                         | open_dt             |     lat |     lot |
|---:|:---------|:------------|:-------------|:-------------------------------------|:--------------------|--------:|--------:|
|  0 | 무교로      | 서울          | 중구           | 서울특별시 중구 무교로 15 (무교동)                | 2020-10-29 00:00:00 | 37.5672 | 126.979 |
|  1 | 한국프레스센터  | 서울          | 중구           | 서울특별시 중구 세종대로 124 (태평로1가)            | 2016-03-28 00:00:00 | 37.5672 | 126.978 |
|  2 | 시청       | 서울          | 중구           | 서울특별시 중구 을지로 19, 삼성화재삼성빌딩 1층 (을지로1가) | 2012-05-02 00:00:00 | 37.5663 | 126.98  |
|  3 | 무교동      | 서울          | 중구           | 서울특별시 중구 무교로 21 (무교동) 코오롱빌딩 1층       | 2002-03-08 00:00:00 | 37.5679 | 126.979 |
|  4 | 환구단      | 서울          | 중구           | 서울특별시 중구 소공로 112 (소공동)               | 2005-10-20 00:00:00 | 37.5645 | 126.979 |

## 2. 매장 특성 분석 (theme_state)

### 매장별 제공 서비스/특징 (상위 10개)

|    | 특징   |   매장 수 |
|---:|:-----|-------:|
|  0 | T57  |    173 |
|  1 | T69  |    173 |
|  2 | T20  |    171 |
|  3 | T30  |    169 |
|  4 | T65  |    168 |
|  5 | T08  |    166 |
|  6 | T05  |    165 |
|  7 | T16  |    165 |
|  8 | T32  |    165 |
|  9 | T17  |    164 |

### 상위 10개 매장 서비스/특징

![상위 10개 매장 서비스/특징](images\top10_features.png)

|    | 특징   |   매장 수 |
|---:|:-----|-------:|
|  0 | T57  |    173 |
|  1 | T69  |    173 |
|  2 | T20  |    171 |
|  3 | T30  |    169 |
|  4 | T65  |    168 |
|  5 | T08  |    166 |
|  6 | T05  |    165 |
|  7 | T16  |    165 |
|  8 | T32  |    165 |
|  9 | T17  |    164 |

## 3. 주변 위치적 특징 분석

### 시/도별 매장 분포

### 시/도별 매장 분포

![시/도별 매장 분포](images\stores_by_sido.png)

| sido_name   |   count |
|:------------|--------:|
| 서울          |     173 |

### 서울시 내 구별 매장 분포 (가장 많은 시/도 기준)

### 서울 내 구별 매장 분포

![서울 내 구별 매장 분포](images\stores_by_gugun_top_sido.png)

| gugun_name   |   count |
|:-------------|--------:|
| 중구           |      54 |
| 종로구          |      42 |
| 용산구          |      23 |
| 서대문구         |      20 |
| 마포구          |      20 |
| 성북구          |       7 |
| 성동구          |       6 |
| 동대문구         |       1 |

가장 매장이 많은 지역은 **서울**이며, 특히 **중구**에 매장이 집중되어 있어 중심 상권일 가능성이 높습니다.

## 4. 오픈일 기반 통계 분석

### 연도별 매장 오픈 트렌드

### 연도별 매장 오픈 트렌드

![연도별 매장 오픈 트렌드](images\open_trend_by_year.png)

|   open_year |   count |
|------------:|--------:|
|        1999 |       1 |
|        2001 |       1 |
|        2002 |       6 |
|        2003 |       2 |
|        2004 |       2 |
|        2005 |       1 |
|        2006 |       3 |
|        2007 |       2 |
|        2008 |       8 |
|        2009 |       2 |
|        2010 |       5 |
|        2011 |       8 |
|        2012 |       6 |
|        2013 |       6 |
|        2014 |      12 |
|        2015 |      10 |
|        2016 |      14 |
|        2017 |      11 |
|        2018 |      14 |
|        2019 |       8 |
|        2020 |       9 |
|        2021 |      11 |
|        2022 |      10 |
|        2023 |       3 |
|        2024 |       7 |
|        2025 |      10 |
|        2026 |       1 |

최근 연도로 올수록 매장 오픈 수가 증가하는 경향을 보입니다.

## 5. 주요 비즈니스 인사이트 및 6. 데이터 품질 검증

)
- **입지 경쟁력**: 매장은 주로 '서울', '경기' 등 수도권에 집중되어 있으며, 특히 강남구, 서초구, 중구 등 오피스 및 상업 중심지에 밀집되어 있습니다. 이는 유동인구가 많은 핵심 상권을 타겟으로 하는 전략으로 해석됩니다.
- **고객 편의성**: `t01`(무선인터넷), `t03`(테라스) 등의 편의 시설 제공 여부를 통해 고객 경험을 향상시키려는 노력을 엿볼 수 있습니다.
- **데이터 품질**:
  - `open_dt`에서 일부 날짜 변환에 실패한 데이터(NaT)가 존재할 수 있어 확인이 필요합니다.
  - `lat`, `lot` 좌표의 경우, 대한민국 범위를 벗어나는 값이 있는지 확인하여 데이터의 신뢰성을 검증해야 합니다. (예: 위도 33-39, 경도 124-132 범위)
  - `sido_code`, `gugun_code`는 각각 `sido_name`, `gugun_name`과 일관성을 유지하는지 검증이 필요합니다.


### 좌표계 이상치 검사: 대한민국 범위 내에 모든 매장이 위치합니다.

## 7. 추가 분석 제안

)
- **경쟁사 분석**: 공공데이터포털의 타 커피 전문점 데이터를 활용하여, 특정 지역 내 스타벅스와 경쟁사의 분포를 비교 분석할 수 있습니다.
- **유동인구 데이터 결합**: 서울시 열린데이터광장의 '지하철 승하차 인원', '유동인구' 데이터와 매장 위치를 결합하여, 유동인구와 매장 수의 상관관계를 분석할 수 있습니다.
- **매장 클러스터링**: `tXX`, `pXX`와 같은 매장 특성 데이터를 기반으로 K-Means 등의 클러스터링 알고리즘을 사용하여 매장을 '업무 중심형', '주거 지역형', '대학가형' 등으로 유형화할 수 있습니다.
- **매출 예측 모델**: 매장 위치, 오픈 연도, 주변 인구 밀도, 경쟁사 수 등의 변수를 활용하여 신규 매장의 예상 매출을 예측하는 회귀 모델을 개발할 수 있습니다.


