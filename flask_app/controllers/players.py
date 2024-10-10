from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import player
import openai
# import requests

@app.route('/players/new', methods=['POST', 'GET'])
def create_player():
    if request.method == 'POST':
        player_id = player.Player.create_new_player(request.form)
        if player_id:
            return redirect('/players/all')
    return render_template('create_player.html', data = request.form)

@app.route('/players/all', methods=['GET'])
def show_all_players():
    all_players = player.Player.get_all_players()
    return render_template('display_all.html', players = all_players)

@app.route('/players/<int:id>', methods=['GET'])
def player_card(id):
    this_player = player.Player.get_player_by_id(id)
    height = this_player.height
    feet, inches = divmod(height, 12)
    return render_template('one_player.html', player = this_player, inches = inches, feet = feet)

# create a route from the chatbot that sends input to API
    # form takes text, sends to external chatbot
    # chatbot returns a SQL query in python string format
    # function passes the SQL query to the model and selects data to send back
        # session text or variable to display?
@app.route('/players/chat_query', methods=['POST', 'GET'])
def handle_chat():
    if request.method == 'POST':
        text = request.form['user_input']
        # text passed to chatbot, store returned query
        # chatbot_response = requests.post('http://api', json={'input': text})
        chat_response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': text}]
        )

        query = chat_response.choices[0].message.content.strip()
        # query = chatbot_response.json().get('query')
        # pass query to model and store returned data
        if query:
            try:
                query_result = player.Player.get_players_from_bot(query)
                return render_template('display_all.html', players=query_result, text="I hope this is what you were asking for.")
            except Exception as e:
                return render_template('display_all.html', error="Query execution failed.", text=text)
    return render_template('display_all.html', players = [], text="Enter a query")

# Will I need to program the bot on the host side or do I need to send a prompt from here?