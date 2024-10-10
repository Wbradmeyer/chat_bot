from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user
import openai

# Create Users Controller



# Read Users Controller

@app.route('/')
def index():
    # text = """
    #     I'd like you to output SQL queries that I can use on my database. 
    #     I have a MySQL schema with a table called players that includes the following columns: 
    #     id(INT), first_name(VARCHAR), last_name(VARCHAR), height(INT), weight(INT), country(VARCHAR),
    #     position(VARCHAR), team(VARCHAR), points(FLOAT), assists(FLOAT), rebounds(FLOAT), blocks(FLOAT),
    #     created_at(DATETIME), updated_at(DATETIME). 
    #     Please only answer with SQL queries in a Python string format. 
    #     Could I get a list of all the players in the database?
    # """

    # chat_response = openai.ChatCompletion.create(
    #     model='gpt-3.5-turbo',
    #     messages=[{'role': 'user', 'content': text}]
    # )

    # query = chat_response.choices[0].message.content.strip()
    # print(query)
    return render_template('index.html')


# Update Users Controller



# Delete Users Controller


# Notes:
# 1 - Use meaningful names
# 2 - Do not overwrite function names
# 3 - No matchy, no worky
# 4 - Use consistent naming conventions 
# 5 - Keep it clean
# 6 - Test every little line before progressing
# 7 - READ ERROR MESSAGES!!!!!!
# 8 - Error messages are found in the browser and terminal




# How to use path variables:
# @app.route('/<int:id>')
# def index(id):
#     user_info = user.User.get_user_by_id(id)
#     return render_template('index.html', user_info)

# Converter -	Description
# string -	Accepts any text without a slash (the default).
# int -	Accepts integers.
# float -	Like int but for floating point values.
# path 	-Like string but accepts slashes.