# define simple flask app
from flask import Flask, render_template
from controller.game_handler import GameHandler
app = Flask(__name__)
game_handler = GameHandler()


@app.route('/')
def home():
    """
    Process the get home request
    """
    return render_template('index.html')


@app.route('/start_game')
def start_game():
    """
    Start game
    """
    status = game_handler.start_game()
    return render_template('game_started.html', status=status)


@app.route('/movement', methods=["POST"])
def movement():
    """
    Movement handler function
    """
    return render_template('game_started.html', value="X")




if __name__ == "__main__":
    app.run()
