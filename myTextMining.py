import pandas as pd
import streamlit as st
from konlpy.tag import Komoran
from collections import Counter

def load_corpus_from_csv(filename, column):
    data_df = pd.read_csv(filename)
    if data_df[column].isnull().sum():
        data_df.dropna(subset=[column], inplace=True)
    corpus = list(data_df[column])
    return corpus

def tokenize_data(corpus):
    komo = Komoran()
    my_tags = ['NNP', 'NNG', 'VA']
    my_stopwords = ['없', '같', '많', '영화', "!!"]

    result_tokens = []
    for text in corpus:
        tokens = [word for word, tag in komo.pos(text) if tag in my_tags and word not in my_stopwords]
        result_tokens.extend(tokens)
    return result_tokens

@st.cache_data
def analyze_word_freq(corpus):
    result_tokens = tokenize_data(corpus)
    counter = Counter(result_tokens)
    return counter

def generate_wordcloud(counter, num_words, font_path):
        # 워드클라우드 시각화
    from wordcloud import WordCloud

    # WordCloud 객체 생성
    wordcloud = WordCloud(
        font_path = font_path,
        #max_font_size = 200,
        width = 800, #이미지 너비 지정
        height = 600, #이미지 높이 지정
        max_words=num_words,
        background_color='ivory' #이미지 배경색 지정
    )
    wordcloud=wordcloud.generate_from_frequencies(counter)
    return wordcloud