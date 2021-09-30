import glob
import os
import numpy as np
import soundfile as sf
import sounddevice as sd
def pad_audio(audio):
    template = np.zeros([44100*20,])
    template[0:audio.shape[0],]=audio
    return template

directories = 'ccmixter_corpus/*/'
paths = glob.glob(directories)
for path in paths:
    new_filename = path.split('\\')[1]+ '_'+path.split('\\')[2]
    path +='*'
    files = glob.glob(path)
    left = []
    right = []
    file_dir = None
    content =None
    for a_file in files:
        print(a_file)
        file_dir = a_file.split('\\')[1]
        if file_dir == 'mindmapthat_-_The_Scuffle_of_Mouth_Sounds_and_the_Magnificent_Uke':
            continue
        os.makedirs('ccmixter\\'+file_dir,exist_ok=True)
        filename = a_file[-7:-4]

        content,freq = sf.read(a_file)

        if filename == 'mix':
            sf.write('ccmixter\\'+file_dir+'\\mix.wav',content,samplerate=freq)
        else:
            left.append(content[:,0])
            right.append(content[:,1])

    left = np.sum(np.array(left),0)
    right = np.sum(np.array(right),0)

    if file_dir != 'mindmapthat_-_The_Scuffle_of_Mouth_Sounds_and_the_Magnificent_Uke' and len(content)<44100*20 :
        left = pad_audio(left)
        right = pad_audio(right)
        mono = pad_audio(mono)
    if file_dir != 'mindmapthat_-_The_Scuffle_of_Mouth_Sounds_and_the_Magnificent_Uke':
        sf.write('ccmixter\\'+file_dir+'\\left.wav',left,samplerate=44100)
        sf.write('ccmixter\\'+file_dir+'\\right.wav', right, samplerate=44100)
