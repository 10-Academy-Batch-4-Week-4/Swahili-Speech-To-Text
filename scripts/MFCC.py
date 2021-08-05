import sklearn
import librosa
import librosa.display

def mfcc(samples, sample_rate):
    mfcc = librosa.feature.mfcc(samples, sr=sample_rate)
    # Center MFCC coefficient dimensions to the mean and unit variance
    mfcc = sklearn.preprocessing.scale(mfcc, axis=1)
    librosa.display.specshow(mfcc, sr=sample_rate, x_axis='time')
    print (f'MFCC is of type {type(mfcc)} with shape {mfcc.shape}')
    # MFCC is of type <class 'numpy.ndarray'> with shape (, )
    return mfcc
