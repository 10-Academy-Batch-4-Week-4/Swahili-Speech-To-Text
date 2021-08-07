import os
import pandas as pd
import string

class audio_prep():
    def __init__(self):
        print("Preprocessing audio data...")

    def load_data(self,dataset_path):
        print("Loading the audio files")
        labels=[]
        # dictionary to store files
    
        # loop through all sub-folders
        for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):

            # ensure we're processing at sub-folder level
            if dirpath is not dataset_path:

                # save label (i.e., sub-folder name) in the mapping eg SWH-05-20101106
                label = dirpath#.split("/")[-1]

                # process all audio files in the sub-directory
                for f in filenames:

                    # load audio file
                    filename=label+"/"+f
                    labels.append(filename)
        return labels

    def load_text(self,text_path):
        print("Loading the transcriptions...")
        df=pd.read_csv(text_path,sep="\t",header=None)
        df = df.drop([0],axis=1)
        df.columns=['text']
        
        #clean data
        words_list=[' UNK ', ' music ', ' laughter ']
        df = df[~df['text'].isin(words_list)]
        for row in df['text']:
            for punctuation in string.punctuation:
                row = row.replace(punctuation," ")
        print('Done!')
        return df