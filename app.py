import streamlit as st
from PIL import Image

st.title('初めてのWebアプリ')
st.caption('これはテストアプリです')
st.subheader('自己紹介')
st.text('プログラミングの勉強してます！\n'
        'サミー健司です！！')

code = '''
import streamlit as st

st.title('テストアプリ')
'''
st.code(code, language = 'python')

#画像
image = Image.open('zou.png')
st.image(image, width=200)

with st.form(key='prifile_form'):
        #テキストボックス
        name = st.text_input('名前')
        
        #セレクトボックス
        age_category = st.radio('年齢層',('子供','大人'))
        
        #複数選択
        hobby = st.multiselect(
                '趣味',
                ('スポーツ','読書','プログラミング','アニメ','映画','釣り','料理'))


        #ボタン
        submit_btn = st.form_submit_button('送信')
        cancel_btn = st.form_submit_button('キャンセル')
if submit_btn:
        st.text(f'ようこそ!{name}さん!')
        st.text(f'年齢層：{age_category}')
        st.text(f'趣味：{", ".join(hobby)}')

