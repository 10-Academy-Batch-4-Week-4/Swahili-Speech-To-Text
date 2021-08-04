import pandas as pd
import librosa
def channels_check(data:pd.DataFrame,col:str):
  chan=[]
  for i in df['audio']:
    sig, sr = librosa.load(i)
    sig_shape=sig.shape[0]
    chan.append(sig_shape)
    set_channel=set(chan)
  print('Unique sound signals',set_channel)