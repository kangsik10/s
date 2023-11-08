from wordcloud import WordCloud, STOPWORDS
from matplotlib import pyplot as plt

text = ['안녕하세요 이진범 입니다', '안녕하세요 홍길동 입니다']

wordcloud = WordCloud(max_font_size=200, font_path='./NanumGothic.ttf', stopwords=STOPWORDS, background_color='#FFFFFF', width=1200, height=800).generate(''.join(text))

plt.figure(figsize=(5,5))
plt.imshow(wordcloud)
plt.tight_layout(pad=0)
plt.axis('off')
plt.show()

