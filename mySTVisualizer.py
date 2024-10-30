import streamlit as st

from matplotlib import font_manager, rc
import matplotlib.pyplot as plt

import os

import myTextMining as tm

def get_korean_font_info():
    # fontNames = [f.name for f in font_manager.fontManager.ttflist if 'Nanum' in f.name]
    font_path = os.getcwd() + '/myFonts'
    font_file = font_path + '/NanumGothic.ttf'
    font_name = 'NanumGothic'
    return font_path, font_file, font_name

#@st.cache_data
def regist_korean_font():

    font_path, _, _ = get_korean_font_info()
    font_files = font_manager.findSystemFonts(fontpaths=[font_path])

    for font_file in font_files:
        font_manager.fontManager.addfont(font_file)
    font_manager._load_fontmanager(try_read_cache=False) 

@st.dialog("데이터 확인하기")
def view_raw_data_dialog(data_file):
    data_df = tm.get_dataframe_from_csv(data_file)
    st.write(data_df.head())

@st.cache_data
def visualize_barhgraph(counter, num_words):

    _, _, font_name = get_korean_font_info()
    plt.rc('font', family=font_name)

    word_list = [word for word, _ in counter.most_common(num_words)]
    count_list = [count for _, count in counter.most_common(num_words)]

    fig, ax = plt.subplots()
    ax.barh(word_list[::-1], count_list[::-1])
    st.pyplot(fig)

def visualize_wordcloud(counter, num_words):

    _, font_file, _ = get_korean_font_info()
    wordcloud = tm.generate_wordcloud(counter, num_words, font_file)

    fig, ax = plt.subplots()
    ax.imshow(wordcloud)
    ax.axis('off')
    st.pyplot(fig)