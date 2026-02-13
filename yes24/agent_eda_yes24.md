# YES24 AI 도서 데이터 분석 리포트

본 문서는 `yes24_ai.csv` 데이터를 바탕으로 AI 관련 도서 시장의 트렌드를 분석하고 시각화한 리포트입니다.

## 1. 환경 설정 및 데이터 로드

분석을 위해 `pandas`, `matplotlib`, `seaborn`, `koreanize_matplotlib` 등을 임포트합니다.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib
from wordcloud import WordCloud
from loguru import logger

# 데이터 불러오기
file_path = 'data/yes24_ai.csv'
df = pd.read_csv(file_path)

logger.info(f"데이터 로드 완료: {len(df)}개의 도서 정보")
```

## 2. 데이터 요약 및 전처리

데이터의 구조를 파악하고 수치형 데이터의 타입을 정제합니다.

```python
# 기본 정보 확인
print(df.info())

# 발행일에서 연도/월 추출 (예: 2025년 11월 -> 2025, 11)
df['발행연도'] = df['발행일'].str.extract(r'(\d{4})년').astype(float)
df['발행월'] = df['발행일'].str.extract(r'(\d{2})월').astype(float)

# 결측치 확인
print(df.isnull().sum())
```

## 3. 시각화 분석

### 3.1 판매가 분포 분석
AI 관련 도서들의 실제 판매 가격대를 확인합니다.

```python
plt.figure(figsize=(10, 6))
plt.hist(df['판매가'], bins=20, color='skyblue', edgecolor='black')
plt.title('AI 도서 판매가 분포')
plt.xlabel('판매가(원)')
plt.ylabel('도서 수')
plt.grid(axis='y', alpha=0.3)
plt.show()
```

### 3.2 주요 출판사 순위 (Top 10)
어떤 출판사에서 AI 관련 도서를 활발하게 출간하고 있는지 분석합니다.

```python
top_publishers = df['출판사'].value_counts().head(10)

plt.figure(figsize=(12, 6))
top_publishers.plot(kind='bar', color='salmon')
plt.title('AI 도서 출간 상위 10개 출판사')
plt.xlabel('출판사')
plt.ylabel('출간 종수')
plt.xticks(rotation=45)
plt.show()
```

### 3.3 판매지수와 리뷰수의 상관관계
판매지수가 높은 책이 실제로 리뷰도 많이 달리는지 산점도를 통해 확인합니다.

```python
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='리뷰수', y='판매지수', alpha=0.5)
plt.title('리뷰수와 판매지수의 상관관계')
plt.xlabel('리뷰수')
plt.ylabel('판매지수')
plt.show()

correlation = df['리뷰수'].corr(df['판매지수'])
logger.info(f"리뷰수와 판매지수의 상관계수: {correlation:.2f}")
```

### 3.4 발행일 기준 출간 트렌드
최근 AI 도서의 출간량이 어떻게 변하고 있는지 분석합니다.

```python
trend = df.groupby('발행연도').size()

plt.figure(figsize=(10, 6))
trend.plot(kind='line', marker='o', color='green', linewidth=2)
plt.title('연도별 AI 도서 출간 추이')
plt.xlabel('발행연도')
plt.ylabel('출간 종수')
plt.grid(True, alpha=0.3)
plt.show()
```

## 4. 제목 키워드 분석 (Word Cloud)

도서 제목에서 가장 많이 등장하는 핵심 키워드를 시각화합니다.

```python
titles = " ".join(df['제목'].values)
wordcloud = WordCloud(
    font_path='malgun.ttf', # Windows 기준
    background_color='white',
    width=800,
    height=400
).generate(titles)

plt.figure(figsize=(15, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('AI 도서 제목 핵심 키워드')
plt.show()
```

## 5. 분석 결과 요약
1. **가격대:** 대부분의 AI 실무/입문 도서는 1만원 후반에서 2만원 중반대에 형성되어 있음.
2. **시장 트렌드:** 2024년과 2025년에 걸쳐 출간량이 급증하며 생성형 AI 관련 도서가 주류를 이룸.
3. **인기 요인:** 판매지수는 리뷰수와 양의 상관관계를 보이며, 특히 입문서(`된다!`, `누구나 아는` 시리즈 등)의 판매지수가 높게 나타남.
