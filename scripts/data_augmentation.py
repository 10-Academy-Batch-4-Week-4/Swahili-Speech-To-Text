import numpy

def time_shift(data, shift):
  return np.roll(data,int(shift))

def add_noise(data, noise_levels=(0, 0.3)):
    noise_level = np.random.uniform(*noise_levels)

    noise = np.random.randn(len(data))
    data_noise = data + noise_level * noise  

    return data_noise

def change_speed(data, speed_factor):
    return librosa.effects.time_stretch(data, speed_factor)

def change_pitch(data, sampling_rate):
    n_steps = np.random.randint(-1, 2)
    return librosa.effects.pitch_shift(data, sampling_rate, n_steps)