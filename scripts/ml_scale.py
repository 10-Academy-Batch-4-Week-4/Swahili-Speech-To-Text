import librosa 
import matplotlib.pyplot as plt

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

  librosa.display.specshow(mel_sgram, sr=sample_rate, x_axis='time', y_axis='mel')
  #Display a spectrogram

  plt.colorbar(format='%+2.0f dB')
  return mel_sgram