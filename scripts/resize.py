import random
import torch

# ----------------------------
# Pad (or truncate) the signal to a fixed length 'max_ms' in milliseconds
# ----------------------------
def pad_trunc(aud, max_ms):
    sig, sr = openf(aud)
    num_rows, sig_len = sig.shape
    max_len = sr//1000 * max_ms

    if (sig_len > max_len):
    # Truncate the signal to the given length
        sig = sig[:,:max_len]

    elif (sig_len < max_len):
    # Length of padding to add at the beginning and end of the signal
        pad_begin_len = random.randint(0, max_len - sig_len)
        pad_end_len = max_len - sig_len - pad_begin_len

    # Pad with 0s
        pad_begin = torch.zeros((num_rows, pad_begin_len))
        pad_end = torch.zeros((num_rows, pad_end_len))

        sig = torch.cat((pad_begin, sig, pad_end), 1)

    return (sig, sr)

"""
We can also use below one if we want to resize after we change the Audio file
to spectrogram/mel-spectrogram
"""

# def resize(spec):
#     padd = torch.zeros(1,128,128) # we can change it to the size we want
#     if padd.shape[-1] < spec.shape[-1]:
#         indices = torch.arange(0, 128)
#         padd = torch.index_select(spec, 2, indices)
#     else:
#         indices = torch.arange(0, spec.shape[-1])
#         padd.index_copy_(2, indices,spec)

#     return padd

#     return spec
