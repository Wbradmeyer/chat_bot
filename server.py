from flask_app import app
from flask_app.controllers import users, players

if __name__=="__main__":   
    app.run(debug=True) 

# debug needs to be set to False when deployed.
# We shared a video showing how the information leaked by this feature and help hackers.