import openai
import os
from dotenv import load_dotenv
from flask import Flask, request, redirect, url_for, json


# load the api key
load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

#add this openai key inside my openai key
openai.api_key=OPENAI_API_KEY
