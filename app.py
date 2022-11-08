import pandas as pd
import streamlit as st
import neattext.functions as nfx
import base64
import time
import spacy
from spacy import displacy
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
from wordcloud import WordCloud


def plot_wordcloud(my_text):
    my_wordcloud = WordCloud().generate(my_text)
    fig = plt.figure()
    plt.imshow(my_wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot(fig)


def text_analyzer(my_text):
	docx = nlp(my_text)
	allData = [(token.text,token.shape_,token.pos_,token.tag_,token.lemma_,token.is_alpha,token.is_stop) for token in docx]
	df = pd.DataFrame(allData,columns=['Token','Shape','PoS','Tag','Lemma','IsAlpha','Is_Stopword'])
	return df


timestr = time.strftime('%Y%m%d-%H%M%S')
def text_downloader(raw_text):
	b64 = base64.b64encode(raw_text.encode()).decode()
	new_filename = "clean_text_result_{}_.txt".format(timestr)
	st.markdown("### ⬇️ Download as .txt file")
	href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Click here!</a>'
	st.markdown(href, unsafe_allow_html=True)


def make_downloadable(data):
    csvfile = data.to_csv(index=False)
    b64 = base64.b64encode(csvfile.encode()).decode()
    new_filename = "nlp_result_{}_.csv".format(timestr)
    st.markdown("### ⬇️ Download as .csv file")
    href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Click here!</a>'
    st.markdown(href, unsafe_allow_html=True)

nlp = spacy.load("en_core_web_sm")


def main():
    st.title("Text Cleaner")

    menu = ['TextCleaner', 'About']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'TextCleaner':
        st.subheader('Text Cleaning')
        text_file = st.file_uploader('Upload .txt File', type=['txt'])
        normalise_case = st.sidebar.checkbox('Upper/lower Case')
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

            with st.expander('Text Analysis'):
                token_result_df = text_analyzer(raw_text)
                st.dataframe(token_result_df)
                make_downloadable(token_result_df)

            with st.expander('Wordcloud'):
                plot_wordcloud(raw_text)

            with st.expander('POS Tags'):
                fig = plt.figure()
                sns.countplot(token_result_df['PoS'])
                plt.xticks(rotation=45)
                st.pyplot(fig)


    else:
        st.subheader('About')
        st.write('This is a simple app that cleans a .txt file. It converts to upper case, removes stopwords, \
                 punctuations, e-mails, special characters, numbers and/or URLs. The cleaned version can be downloaded \
                 as a .txt file.')


if __name__ == '__main__':
    main()
