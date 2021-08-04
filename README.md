# Swahili-Speech-To-Text
Speech recognition technology allows for hands-free control of smartphones, speakers,
and even vehicles in a wide variety of languages. Companies have moved towards the
goal of enabling machines to understand and respond to more and more of our
verbalized commands. There are many matured speech recognition systems available,
such as Google Assistant, Amazon Alexa, and Apple’s Siri. However, all of those voice
assistants work for limited languages only.


# Data
● Dataset for Swahili [here] (https://github.com/getalp/ALFFA_PUBLIC)

#  Data pre-processing
    - Load audio file
    - Load transcriptions
    - Convert into channels
            -  Some of the sound files are mono (ie. 1 audio channel) while most of them
               are stereo (ie. 2 audio channels). Since the Neural network model expects
               all items to have the same dimensions, we will convert the mono files to
               stereo, by duplicating the first channel to the second
    -  Standardize sampling rate
            - We must standardize and convert all audio to the same sampling rate so
              that all arrays have the same dimensions.
    - Resize to the same length
            - Resize to get an equal-sized audio sample by extending duration by
              padding it with silence, or by truncating it.



