import pandas as pd
import streamlit as st
import neattext.functions as nfx
import base64
import time
timestr = time.strftime('%Y%m%d-%H%M%S')

def text_downloader(raw_text):
    b64 = base64.b64encode(raw_text.encode()).decode()
    new_filename = 'clean_text_result_{}_.txt'.format(timestr)
    st.markdown('### Download File ###')
    href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">click here</a>'
    st.markdown(href, unsafe_allow_html=True)


def main():
    st.title("Text Cleaner")

    menu = ['TextCleaner', 'About']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'TextCleaner':
        st.subheader('Text Cleaning')
        text_file = st.file_uploader('Upload .txt File', type=['txt'])
        normalise_case = st.sidebar.checkbox('Normalised Case')
        clean_stopwords = st.sidebar.checkbox('Stopwords')
        clean_punctuation = st.sidebar.checkbox('Punctuations')
        clean_emails = st.sidebar.checkbox('Emails')
        clean_special_char = st.sidebar.checkbox('Special Characters')
        clean_numbers = st.sidebar.checkbox('Numbers')
        clean_urls = st.sidebar.checkbox('URLs')

        if text_file is not None:
            file_details = {'File name': text_file.name,
                            'File size': text_file.size,
                            'File type': text_file.type}
            st.write(file_details)

            # Decode the text
            raw_text = text_file.read().decode('utf-8')

            col1, col2 = st.columns(2)

            with col1:
                with st.expander('Original Text'):
                    st.write(raw_text)

            with col2:
                with st.expander('Processed Text'):
                    if normalise_case:
                        raw_text = raw_text.upper()

                    if clean_stopwords:
                        raw_text = nfx.remove_stopwords(raw_text)

                    if clean_numbers:
                        raw_text = nfx.remove_numbers(raw_text)

                    if clean_urls:
                        raw_text = nfx.remove_urls(raw_text)

                    if clean_punctuation:
                        raw_text = nfx.remove_punctuations(raw_text)

                    if clean_emails:
                        raw_text = nfx.remove_emails(raw_text)

                    if clean_special_char:
                        raw_text = nfx.remove_special_characters(raw_text)

                    st.write(raw_text)
                    text_downloader(raw_text)




    else:
        st.subheader('About')


if __name__ == '__main__':
    main()
