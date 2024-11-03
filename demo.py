# how to use whisper model
import openai
import os
from dotenv import load_dotenv


# load the api key
load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

#add this openai key inside my openai key
openai.api_key=OPENAI_API_KEY


#open that audio file (rb=read binary)
audio_file= open("recorded.mp3","rb")


# get the transcript used that openai whisper model(pass the model and audio)
output=openai.Audio.translate("whisper-1",audio_file)


print(output)
