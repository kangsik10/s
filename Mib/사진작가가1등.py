# import pandas as pd

# # Path to the CSV files
# artwork_file_path = 'artwork.csv'  # Replace with your artwork file path
# artist_file_path = 'artist.csv'    # Replace with your artist file path

# # Reading the CSV files into DataFrames
# artwork_df = pd.read_csv(artwork_file_path)
# artist_df = pd.read_csv(artist_file_path)

# # 두 데이터셋을 병합하기 전에 열 이름 변경
# artwork_df = artwork_df.rename(columns={'Nationality': 'ArtworkNationality'})
# artist_df = artist_df.rename(columns={'Nationality': 'ArtistNationality'})

# # 두 데이터셋 병합
# merged_df = pd.merge(artwork_df, artist_df, on='ConstituentID', how='left')

# # Convert the 'ConstituentID' column to string in both DataFrames
# artwork_df['ConstituentID'] = artwork_df['ConstituentID'].astype(str)
# artist_df['ConstituentID'] = artist_df['ConstituentID'].astype(str)

# # Merging the two DataFrames
# merged_df = pd.merge(artwork_df, artist_df, on='ConstituentID', how='left')

# # Display the first few rows of the merged DataFrame
# print(merged_df.head())
import pandas as pd

# Path to the CSV files
artwork_file_path = 'artwork.csv'  # Replace with your artwork file path
artist_file_path = 'artist.csv'    # Replace with your artist file path

# Reading the CSV files into DataFrames
artwork_df = pd.read_csv(artwork_file_path)
artist_df = pd.read_csv(artist_file_path)

# 두 데이터셋을 병합하기 전에 열 이름 변경
artwork_df = artwork_df.rename(columns={'Nationality': 'ArtworkNationality'})
artist_df = artist_df.rename(columns={'Nationality': 'ArtistNationality'})

# Convert the 'ConstituentID' column to string in both DataFrames
artwork_df['ConstituentID'] = artwork_df['ConstituentID'].astype(str)
artist_df['ConstituentID'] = artist_df['ConstituentID'].astype(str)

# 두 데이터셋 병합
merged_df = pd.merge(artwork_df, artist_df, on='ConstituentID', how='left')

# Display the first few rows of the merged DataFrame
print(merged_df.head())

import matplotlib.pyplot as plt
import seaborn as sns

# 화가별 작품 수 계산
artist_production = merged_df['Artist'].value_counts().head(10)

# 화가별 작품 수 시각화
plt.figure(figsize=(10, 6))
sns.barplot(x=artist_production.values, y=artist_production.index)
plt.title('Top 10 Artists by Number of Artworks')
plt.xlabel('Number of Artworks')
plt.ylabel('Artist')
plt.show()