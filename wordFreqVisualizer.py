
import streamlit as st
import pandas as pd
import os

import myTextMining as tm
import mySTVisualizer as sv

#######################################
# 웹 대시보드
#######################################

st.set_page_config(
    page_title="Word Frequency Visualizer",
    page_icon="📊",
    #layout="wide"
    #initial_sidebar_state="expanded"
)

st.sidebar.write("## 설정")
with st.sidebar.form('my_form'):
    data_file = st.file_uploader("파일 선택", type=['csv'])
    column_name = st.text_input('데이터가 있는 컬럼명', value='review')
    freq = st.checkbox('빈도수 그래프', value=True)
    num_freq_words = st.slider('단어 수', 10, 50, 20, 1)
    wc = st.checkbox('워드클라우드')
    num_wc_words = st.slider('단어 수', 20, 500, 50, 10)
    submitted = st.form_submit_button('분석 시작')

st.title('단어 빈도수 시각화')
status = st.info('분석할 파일을 업로드하고, 시각화 수단을 선택한 후 "분석 시작" 버튼을 클릭하세요.')

# 메인 화면에 결과 출력

if submitted:
    if data_file:
        status.info('데이터를 분석 중입니다.')
        #data_file = "./data/daum_movie_review.csv"
        corpus = tm.load_corpus_from_csv(data_file, column_name)  
        counter = tm.analyze_word_freq(corpus)
        status.info('분석이 완료되었습니다.')

        if freq: sv.visualize_barhgraph(counter, num_freq_words)
        if wc: sv.visualize_wordcloud(counter, num_wc_words)
        if not freq and not wc:
            st.warning('빈도수 그래프 또는 워드클라우드 중 하나 이상을 선택하세요.')
            # df = pd.DataFrame(counter.most_common(20), columns=['단어', '빈도수'])
            # df
    else:
        st.warning('분석할 데이터 파일을 업로드 한 후 분석 시작하세요.')
    