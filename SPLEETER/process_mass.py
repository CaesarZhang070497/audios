import glob
import os
import numpy as np
import soundfile as sf

def pad_audio(audio):
    template = np.zeros([44100*20,])
    template[0:audio.shape[0],]=audio
    return template

directories = 'Mass/*/*/*/'
paths = glob.glob(directories)
for path in paths:
    new_filename = path.split('\\')[2]+ '_'+path.split('\\')[3]
    path +='*'
    files = glob.glob(path)
    left = []
    right = []
    for a_file in files:
        content,freq = sf.read(a_file)
        left.append(content[:,0])
        right.append(content[:,1])
    left = np.sum(np.array(left),0)
    right = np.sum(np.array(right),0)
    mono = left+ right
    if len(mono)<44100*20:
        left = pad_audio(left)
        right = pad_audio(right)
        mono = pad_audio(mono)
    writing_dir = 'mass_dataset\\'+new_filename+'\\'
    os.makedirs(writing_dir)
    sf.write(writing_dir+'left.wav',left,samplerate=44100)
    sf.write(writing_dir + 'right.wav', right, samplerate=44100)
    sf.write(writing_dir + 'mono.wav', mono, samplerate=44100)
