import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import pandas as pd

def get_word_count(url):
    # 페이지의 내용을 가져옴
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    # 페이지의 텍스트를 가져와 소문자로 변환하고, 단어만 추출
    words = re.findall(r'\b\w+\b', soup.get_text().lower())

    # 단어의 빈도수를 계산
    word_count = Counter(words)

    return word_count

def print_top_words(word_count, num=5):
    # 빈도수가 높은 단어를 출력
    top_words = word_count.most_common(num)

    # DataFrame 생성
    df = pd.DataFrame(top_words, columns=['Word', 'Frequency'])

    # DataFrame 출력
    print(df)

if __name__ == "__main__":
    url = "https://quotes.toscrape.com/tag/life/"
    word_count = get_word_count(url)
    print_top_words(word_count)
