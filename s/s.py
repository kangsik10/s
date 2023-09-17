import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import sys, os
os.chdir(sys.path[0])

text = open('jeff_bezos_speech.txt', mode='r', encoding='utf-8').read()
stopwords = STOPWORDS

wc = WordCloud(
    background_color='white',
    stopwords = stopwords,
    height = 600,
    width=400    
)

# from wordcloud import WordCloud, STOPWORDS

# text = ["안녕하세요 서강식입니다.", "안녕하세요 서강식입니다."]
# wordcloud = WordCloud(max_font_size=200,
#                       font_path='./NanumGothic.ttf',
#                     #   font_path='',
#                       stopwords=STOPWORDS,
#                       background_color='#FFFFFF',
#                     #   background_color='',
#                       width=1200,
#                       height=800),generate(''.join(text))

# plt.figure(figsize=(5,5))
# plt.imshow(wordcloud)
# plt.tight_layout(pad=0)
# plt.axis('off')
# plt.show()

# import csv
# file = open("outputs.csv", mode="w", encoding="utf-8", newline="")
# writer = csv.writer(file)
# writer.writerow(["데이터1","데이터2", "데이터3" ])
# writer.writerow(["데이터1","데이터2", "데이터3" ])
# writer.writerow(["데이터1","데이터2", "데이터3" ])
# file.close()