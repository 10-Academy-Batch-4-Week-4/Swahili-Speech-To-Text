import librosa
import torch
import torchaudio
import numpy as np
import pandas as pd
import os

from scripts.channel import channels_check
from scripts.Feature_extraction import mel_scale
from scripts.data_augmentation import time_shift
from scripts.load_text import loading
from scripts.resize import resize_

file = "../SWH-05-20101106/SWH-05-20101106_16k-emission_swahili_05h30_-_06h00_tu_20101106_part2.wav"
#files = os.listdir(parent_dir)
audio, fs = librosa.load(file)
meta_df = pd.read_csv('../metadata.csv')


class testSwahlli():
    def __init__(self):
        pass

    def feature_extraction_(self):
        s = mel_scale(audio)
        assert type(
            s) == np.ndarray, f"Function should return the value {np.ndarray}, it is returning the value {type(s)}"

    def channel_(self, data: pd.DataFrame, col: str):
        ch = channels_check(data: pd.DataFrame, col: str)
        assert set(ch) == {
            1, 2}, f"Function should return the value {[1, 2]}, it is returning the value {ch}"

    def data_augimentation_(self):
        sh = time_shift(audio, shift)
        assert int(sh.shape[1]) == (int(data.shape[1]) + shift), \
            f"Function should return the value {(int(np.shape(data)) + shift)}, it is returning the value {int(sh.shape[1])}"

    def load_text_(self):
        txt = 'rais wa tanzania jakaya mrisho kikwete'
        t = loading(text_path)
        assert t.iloc[0] == txt, f"Function should return the value {txt}, it is returning the value {t}"

    def resize(self):
        re = resize_(audio, max_length)
        assert int(re.shape[1]) == (int(signal.shape[1]) + max_length), \
            f"Function should return the value {(int(signal.shape[1]) + max_length)}, it is returning the value {int(re.shape[1])}"


if __name__ == '__main__':
	testSwahlli.main()
