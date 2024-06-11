from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import player

@app.route('/players/new', methods=['POST', 'GET'])
def create_player():
    if request.method == 'POST':
        # create a new instrument and retrieve the id
        player_id = player.Player.create_new_player(request.form)
        if player_id:
            return redirect('/home')
    return render_template('create_instrument.html', data = request.form)