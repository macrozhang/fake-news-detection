import re
import pandas as pd

from utils.contractions import contractions


def clean_text(text):
    '''Remove unwanted characters, stopwords, and format the text to create fewer nulls word embeddings'''
    
    # Convert words to lower case
    text = text.lower()
    
    # Replace contractions with their longer forms 
    if True:
        text = text.split()
        new_text = []
        for word in text:
            if word in contractions:
                new_text.append(contractions[word])
            else:
                new_text.append(word)
        text = " ".join(new_text)
    
    # Format words and remove unwanted characters
    text = re.sub(r'https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
    text = re.sub(r'\<a href', ' ', text)
    text = re.sub(r'&amp;', '', text) 
    text = re.sub(r'[_"\-;%()|+&=*%.,!?:#$@\[\]/]', ' ', text)
    text = re.sub(r'<br />', ' ', text)
    text = re.sub(r'\'', ' ', text)
    
    return text



def clean_text_col(df):
    clean_data = []
    for line in df['title']:
        clean_data.append(clean_text(line))

    return clean_data


def clean_df(spark_df):
    pd_df = spark_df.toPandas()
    preprocessed_df = pd.DataFrame(columns=['clean_title', 'category'])

    cleaned_titles = clean_text_col(pd_df)

    preprocessed_df['clean_title'] = cleaned_titles
    preprocessed_df['category'] = pd_df['category']
    preprocessed_df['Y'] = pd_df['Y']

    return preprocessed_df
