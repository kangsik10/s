import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터셋 로드 (경로는 실제 파일 위치에 맞게 수정해야 합니다)
artwork_df = pd.read_csv('artwork.csv')

# 'Medium' 열에서 각 매체의 빈도 계산
medium_counts = artwork_df['Medium'].value_counts()

# 시각화 (상위 20개의 매체)
plt.figure(figsize=(10, 8))
sns.barplot(y=medium_counts.index[:20], x=medium_counts.values[:20])
plt.title('Top 20 Mediums Used in Artworks')
plt.xlabel('Counts')
plt.ylabel('Mediums')
plt.show()