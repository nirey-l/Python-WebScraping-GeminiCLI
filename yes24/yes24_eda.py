import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib
from wordcloud import WordCloud
from loguru import logger
import os

# 디렉토리 설정
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, 'data', 'yes24_ai.csv')
image_dir = os.path.join(base_dir, 'images')

if not os.path.exists(image_dir):
    os.makedirs(image_dir)

logger.info(f"데이터 분석 시작: {data_path}")

# 1. 데이터 로드
try:
    df = pd.read_csv(data_path)
    logger.info(f"데이터 로드 완료: {len(df)}개의 도서 정보")
except Exception as e:
    logger.error(f"데이터 로드 실패: {e}")
    exit(1)

# 2. 데이터 요약 및 전처리
# 발행일에서 연도/월 추출
df['발행연도'] = df['발행일'].str.extract(r'(\d{4})년').astype(float)
df['발행월'] = df['발행일'].str.extract(r'(\d{2})월').astype(float)

# 기본 통계 정보 출력
print("\n[데이터 요약]")
print(df[['정가', '판매가', '리뷰수', '판매지수']].describe())

# 3. 시각화 분석

# 3.1 판매가 분포 분석
plt.figure(figsize=(10, 6))
plt.hist(df['판매가'], bins=20, color='skyblue', edgecolor='black')
plt.title('AI 도서 판매가 분포')
plt.xlabel('판매가(원)')
plt.ylabel('도서 수')
plt.grid(axis='y', alpha=0.3)
plt.savefig(os.path.join(image_dir, '01_price_distribution.png'))
logger.info("판매가 분포 차트 저장 완료")

# 3.2 주요 출판사 순위 (Top 10)
top_publishers = df['출판사'].value_counts().head(10)
plt.figure(figsize=(12, 6))
top_publishers.plot(kind='bar', color='salmon')
plt.title('AI 도서 출간 상위 10개 출판사')
plt.xlabel('출판사')
plt.ylabel('출간 종수')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(image_dir, '02_top_publishers.png'))
logger.info("출판사 순위 차트 저장 완료")

# 3.3 판매지수와 리뷰수의 상관관계
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='리뷰수', y='판매지수', alpha=0.5)
plt.title('리뷰수와 판매지수의 상관관계')
plt.xlabel('리뷰수')
plt.ylabel('판매지수')
plt.savefig(os.path.join(image_dir, '03_review_sales_corr.png'))
logger.info("상관관계 산점도 저장 완료")

correlation = df['리뷰수'].corr(df['판매지수'])
print(f"\n리뷰수와 판매지수의 상관계수: {correlation:.2f}")

# 3.4 발행일 기준 출간 트렌드
trend = df.groupby('발행연도').size()
plt.figure(figsize=(10, 6))
trend.plot(kind='line', marker='o', color='green', linewidth=2)
plt.title('연도별 AI 도서 출간 추이')
plt.xlabel('발행연도')
plt.ylabel('출간 종수')
plt.grid(True, alpha=0.3)
plt.savefig(os.path.join(image_dir, '04_annual_trend.png'))
logger.info("출간 트렌드 차트 저장 완료")

# 4. 제목 키워드 분석 (Word Cloud)
titles = " ".join(df['제목'].values)
# 폰트 경로 설정 (Windows 기준 Malgun Gothic)
font_path = 'C:/Windows/Fonts/malgun.ttf' 

try:
    wordcloud = WordCloud(
        font_path=font_path,
        background_color='white',
        width=800,
        height=400
    ).generate(titles)

    plt.figure(figsize=(15, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('AI 도서 제목 핵심 키워드')
    plt.savefig(os.path.join(image_dir, '05_wordcloud.png'))
    logger.info("워드클라우드 저장 완료")
except Exception as e:
    logger.warning(f"워드클라우드 생성 실패 (폰트 문제 등): {e}")

logger.info("모든 분석 및 시각화 작업 완료")
