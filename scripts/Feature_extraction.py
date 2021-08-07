import sklearn
import librosa
import librosa.display
import matplotlib.pyplot as plt

def mfcc(samples, sample_rate):
    mfcc = librosa.feature.mfcc(samples, sr=sample_rate)
    # Center MFCC coefficient dimensions to the mean and unit variance
    mfcc = sklearn.preprocessing.scale(mfcc, axis=1)
    
    print (f'MFCC is of type {type(mfcc)} with shape {mfcc.shape}')
    # MFCC is of type <class 'numpy.ndarray'> with shape (, )
    return mfcc


def mel_scale(samples):
  sgram = librosa.stft(samples)   
  #The STFT represents a signal in the time-frequency domain by computing discrete Fourier transforms (DFT) over short overlapping windows.
  #This function returns a complex-valued matrix D

  sgram_mag, _ = librosa.magphase(sgram)
  #Separate a complex-valued spectrogram D into its magnitude (S) and phase (P) components, so that D = S * P

  mel_scale_sgram = librosa.feature.melspectrogram(S=sgram_mag, sr=sample_rate)
  #Compute a mel-scaled spectrogram.

  mel_sgram = librosa.amplitude_to_db(mel_scale_sgram, ref=np.min)
  #Convert an amplitude spectrogram to dB-scaled spectrogram.

  return mel_sgram