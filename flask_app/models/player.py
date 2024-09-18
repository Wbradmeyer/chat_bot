from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session

class Player:
    db = "bball_players_db"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.height = data['height']
        self.weight = data['weight']
        self.country = data['country']
        self.position = data['position']
        self.team = data['team']
        self.points = data['points']
        self.assists = data['assists']
        self.rebounds = data['rebounds']
        self.blocks = data['blocks']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_new_player(cls, data):
        if not cls.validate_player(data):
            return False
        query = """
        INSERT INTO players (first_name, last_name, height, weight,
                    country, position, team, points, assists, rebounds, blocks)
        VALUES (%(first_name)s, %(last_name)s, %(height)s, %(weight)s,
                    %(country)s, %(position)s, %(team)s, %(points)s, %(assists)s, %(rebounds)s, %(blocks)s)
        ;"""
        player_id = connectToMySQL(cls.db).query_db(query, data)
        return player_id
    
    @classmethod
    def get_player_by_id(cls, id):
        data = {'id': id}
        query = """
        SELECT * FROM players
        WHERE id = %(id)s
        ;"""
        result = connectToMySQL(cls.db).query_db(query, data)
        this_player = cls(result[0])
        return this_player
    
    @classmethod
    def get_all_players(cls):
        query = """
        SELECT * FROM players
        ;"""
        results = connectToMySQL(cls.db).query_db(query)
        all_players = []
        if results:
            for row in results:
                this_player = cls(row)
                all_players.append(this_player)
        return all_players
    
    def get_players_from_bot(cls, query):
        try:
            results = connectToMySQL(cls.db).query_db(query)
            sorted_players = []
            if results:
                for row in results:
                    this_player = cls(row)
                    sorted_players.append(this_player)
            return sorted_players
        except Exception as e:
            print(f'Error executing query: {e}')
            return []
    
    @staticmethod
    def validate_player(data):
        is_valid = True

        if len(data['first_name']) < 2:
            flash('First name should be at least 2 characters.')
            is_valid = False
        if int(data['height']) < 1:
            flash('Height must be at least 1 inch.')
            is_valid = False
        if int(data['weight']) < 1:
            flash('Weight must be at least 1 lb.')
            is_valid = False
        if len(data['last_name']) < 2:
            flash('Last name should be at least 2 characters.')
            is_valid = False
        if len(data['country']) < 2:
            flash('Country should be at least 2 characters.')
            is_valid = False
        if len(data['team']) < 2:
            flash('Team should be at least 2 characters.')
            is_valid = False

        return is_valid