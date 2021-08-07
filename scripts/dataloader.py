import torch
import torchaudio
from pathlib import Path
from typing import List, Tuple, Union
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import torchaudio.transforms as T
import librosa
import numpy as np

class Loader(Dataset):
    def __init__(self, 
        folds_location: List
        ) -> None:
        sample_rate = 22050
        n_fft = 1024
        win_length = 512
        hop_length = 512
        n_mels = 128 
        self._walker = []
        self.length = []

        self.mel_spectrogram = T.MelSpectrogram(
                sample_rate=sample_rate,
                n_fft=n_fft,
                win_length=win_length,
                hop_length=hop_length,
                f_min = 0,
                f_max = 22050,
                power = 1,
                n_mels=n_mels,
        )
        self._parse_file(folds_location)

    def __len__(self):
        return len(self._walker)
    
    def _parse_file(self, folds_location: str) -> None:
        for fold_location in folds_location:
            archive = Path(fold_location)
            self._walker.extend(p for p in Path(archive).glob("*.wav")))
    
    def __getitem__(self, index):# -> [torch.Tensor,int]:
        # return self._walker[index]
        fileid = self._walker[index]
        label = torch.tensor(int(fileid.split('-')[1]))
        waveform, sample_rate = torchaudio.load(fileid)
        waveform = waveform.mean(0, keepdim=True)

        spec =  self.mel_spectrogram(waveform)
        padd = torch.zeros(1,128,128)
        if padd.shape[-1] < spec.shape[-1]:
            indices = torch.arange(0, 128)
            padd = torch.index_select(spec, 2, indices)
        else:
            indices = torch.arange(0, spec.shape[-1])
            padd.index_copy_(2,indices,spec)

        return padd, 1

if __name__ == "__main__":
  train_dataset = Loader(["SWH-05-20101124/", "SWH-05-20101211/",
                            "SWH-05-20101222/", "SWH-15-20110203/", "SWH-15-20110311/", "SWH-15-20110323/"])
