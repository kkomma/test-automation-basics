import pytube
import subprocess
import random
import string
import os.path
# ss=''.join(random.choices(string.ascii_uppercase, k=5))

# https://platform.openai.com/docs/guides/speech-to-text/longer-inputs
# from pydub import AudioSegment
# song = AudioSegment.from_mp3("good_morning.mp3")
# # PyDub handles time in milliseconds
# ten_minutes = 10 * 60 * 1000
# first_10_minutes = song[:ten_minutes]
# first_10_minutes.export("good_morning_10.mp3", format="mp3")

video_urls = ['https://www.youtube.com/watch?v=HjpwGgmt57U']        
s=video_urls[-1]
vv=s.split('?v=')
print(vv[1])
f1=f'{vv[1]}.mp4'
f2=f'{vv[1]}.flac'
path = f'./{f1}'
check_file = os.path.isfile(path)
print(check_file)
if check_file:
    print(f'exiting as file {f1} exists..')
    exit(0)

# Create an instance of YouTube video
video_instance = pytube.YouTube(s)
print('downloading plz wait..')
stream = video_instance.streams.get_highest_resolution()

# download 🚀 
stream.download(filename=f1)
crop = f"/Users/veeranica/Downloads/ffmpeg -i {f1} {f2}"
subprocess.call(crop, shell=True)
