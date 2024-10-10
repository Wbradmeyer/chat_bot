from flask import Flask
from dotenv import load_dotenv
import openai
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = "The first rule of secret key is..." 

openai.api_key = os.getenv('API_KEY')
# The secret key is needed to run session
# This is one thing that would usually be kept in your git ignore, along with API keys