import pandas as pd
import string

def loading(text_path):
    df=pd.read_csv(text_path,sep="\t",header=None)
    df = df.drop([0],axis=1)
    df.columns=['text']
    
    #clean data
    words_list=[' UNK ', ' music ', ' laughter ']
    df = df[~df['text'].isin(words_list)]
    for row in df['text']:
        for punctuation in string.punctuation:
            row = row.replace(punctuation," ")
    return df