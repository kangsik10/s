import pandas as pd

directors_df = pd.read_csv("MoMADirectorsDepartmentHeads.csv")

import pandas as pd

exhibitions_df = pd.read_csv("MoMAExhibitions1929to1989.csv", encoding='iso-8859-1')

import pandas as pd
import matplotlib.pyplot as plt

# Loading and processing the MoMA Exhibitions data
exhibitions_df['ExhibitionBeginDate'] = pd.to_datetime(exhibitions_df['ExhibitionBeginDate'], errors='coerce')
exhibitions_df['ExhibitionEndDate'] = pd.to_datetime(exhibitions_df['ExhibitionEndDate'], errors='coerce')
exhibitions_df['Year'] = exhibitions_df['ExhibitionBeginDate'].dt.year

# Calculating the number of exhibitions and average duration per year
exhibitions_per_year = exhibitions_df.groupby('Year')['ExhibitionID'].nunique()
exhibitions_df['Duration'] = (exhibitions_df['ExhibitionEndDate'] - exhibitions_df['ExhibitionBeginDate']).dt.days
average_duration_per_year = exhibitions_df.groupby('Year')['Duration'].mean()

# Loading and processing the MoMA Directors and Department Heads data
directors_df['PositionBeginYear'] = pd.to_numeric(directors_df['PositionBeginYear'], errors='coerce')
directors_df['PositionEndYear'] = pd.to_numeric(directors_df['PositionEndYear'], errors='coerce')
directors_df['Tenure'] = directors_df['PositionEndYear'] - directors_df['PositionBeginYear']
average_tenure_per_year = directors_df.groupby('PositionBeginYear')['Tenure'].mean()

# Visualization
plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
exhibitions_per_year.plot(title='Number of Exhibitions per Year', ylabel='Number of Exhibitions')
plt.subplot(1, 2, 2)
average_duration_per_year.plot(title='Average Duration of Exhibitions per Year', ylabel='Average Duration (days)', color='orange')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
average_tenure_per_year.plot(title='Average Tenure of Directors/Department Heads per Start Year', ylabel='Average Tenure (years)', color='green')
plt.show()
