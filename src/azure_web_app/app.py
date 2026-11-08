from datetime import datetime

from dotenv import find_dotenv, load_dotenv
from flask import Flask, abort, render_template

from azure_web_app import auth, db, sessions
from azure_web_app._constants import SECRET_ENV_FILE
from azure_web_app.sessions import login_required


FAVORITES = [
    {"id": 1, "title": "Intergalactic", "why": "The beat!"},
    {"id": 2, "title": "I Like It", "why": "It makes me want to dance"},
    {"id": 3, "title": "Since U Been Gone", "why": "The perfect breakup song"},
    {"id": 4, "title": "En la Ciudad de la Furia", "why": "My dad's favorite song"},
]

GAMES = [
    {"id": 1, "title": "Valorant", "why": "Me and my friends grinded to Immortal on this game, it took up all of my high school years"},
    {"id": 2, "title": "NBA 2K27", "why": "My current favorite game to play with my friends"},
    {"id": 3, "title": "Tetris", "why": "I used to grind tetr.io in highschool as well, but I was not too good"},
    {"id": 4, "title": "Ghost of Yotei", "why": "The best game ever created, cmon now"},
]



def create_app():
    load_dotenv(find_dotenv(SECRET_ENV_FILE))
    app = Flask(__name__)
    db.setup_for_app(app)
    sessions.setup_sessions(app)
    auth.setup_auth(app)
    setup_routes(app)
    return app



def index():
    return render_template(
        "index.html",
        name="Brandon Valadez",
        hobby="Playing Video Games",
        hours_per_week=15, 
        fun_fact="I can play the accordion",
        hour=datetime.now().hour,
        show_counter=True,
        favorites=FAVORITES,
    )


def favorite_detail(favorite_id: int):
    for favorite in FAVORITES:
        if favorite["id"] == favorite_id:
            return render_template("favorite.html", favorite=favorite)
    abort(404)


def games():
    return render_template("games.html", games=GAMES)


def game_detail(game_id: int):
    for game in GAMES:
        if game["id"] == game_id:
            return render_template("game.html", game=game)
    abort(404)

@login_required
def account():
    return render_template("account.html")

@login_required
def game_night():
    return render_template("game_night.html", games=GAMES)

def setup_routes(app):
    app.route("/")(index)
    app.route("/favorites/<int:favorite_id>")(favorite_detail)
    app.route("/games")(games)
    app.route("/games/<int:game_id>")(game_detail)
    app.route("/account")(account)
    app.route("/game-night")(game_night)

def run_app(debug: bool = True) -> None:
    app = create_app()
    app.run(debug=debug)


if __name__ == "__main__":
    run_app(debug=True)