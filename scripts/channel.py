import pandas as pd
import librosa
# def channels_check(data:pd.DataFrame,col:str):
#   chan=[]
#   for i in data[col]:
#     sig, sr = librosa.load(i)
#     sig_shape=sig.shape[0]
#     chan.append(sig_shape)
#     set_channel=set(chan)
#   print('Unique sound signals',set_channel)

def channels_check(file):
    set_Channel = []
    for i in file:
        sig, sr = librosa.load(i)
        set_Channel.append(len(sig.shape))
    return set(set_Channel)
