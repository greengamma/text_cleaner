import pandas as pd
import streamlit as st
import neattext.functions as nfx


def main():
    st.title("Text Cleaner")

    menu = ['TextCleaner', 'About']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'TextCleaner':
        st.subheader('Text Cleaning')
        text_file = st.file_uploader('Upload Txt File', type=['txt'])
        if text_file is not None:

            col1, col2 = st.beta_columns(2)

            with col1:
                with st.beta_expander('Original Text'):
                    raw_text = text_file.read().decode('utf-8')
                    st.write(text_file)



    else:
        st.subheader('About')


if __name__ == '__main__':
    main()
