import streamlit as st

from matplotlib import font_manager, rc
import matplotlib.pyplot as plt

import os

import myTextMining as tm

def is_running_on_streamlit_cloud():

    #return "STREAMLIT_SERVER_PORT" in os.environ
    
    server_address = os.environ.get("SERVER_NAME", "localhost")
    print(server_address)
    if server_address in ["localhost", "127.0.0.1"]:
        return False
    return True

    #isCloud=False

    #return isCloud

@st.cache_data
def visualize_barhgraph(counter, num_words):

    if is_running_on_streamlit_cloud():
        font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
        font_name = 'NanumGothic'
        font_manager.fontManager.addfont(font_path)
    else:
        font_path = "c:/Windows/Fonts/malgun.ttf"
        font_name = font_manager.FontProperties(fname=font_path).get_name() 

    rc('font', family=font_name)

    word_list = [word for word, _ in counter.most_common(num_words)]
    count_list = [count for _, count in counter.most_common(num_words)]

    fig, ax = plt.subplots()
    ax.barh(word_list[::-1], count_list[::-1])
    st.pyplot(fig)

def visualize_wordcloud(counter, num_words):
        
    if is_running_on_streamlit_cloud():
        font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'      
    else:    
        font_path = "c:/Windows/fonts/malgun.ttf"

    wordcloud = tm.generate_wordcloud(counter, num_words, font_path)

    fig, ax = plt.subplots()
    ax.imshow(wordcloud)
    ax.axis('off')
    st.pyplot(fig)