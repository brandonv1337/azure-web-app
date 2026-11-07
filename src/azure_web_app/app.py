from flask import Flask, abort, render_template
from datetime import datetime
FAVORITES = [
    {"id": 1, "title": "Intergalactic", "why": "The beat!"},
    {"id": 2, "title": "I Like It", "why": "It makes me want to dance"},
    {"id": 3, "title": "Since U Been Gone", "why": "The perfect breakup song"},
    {"id": 4, "title": "En la Ciudad de la Furia", "why": "My dad's favorite song"},
]


    
def create_app():
    app = Flask(__name__)
    setup_routes(app)
    return app


def index():
    return render_template(
        "index.html",
        name="Brandon Valadez",
        hobby="Playing Video Games",
        hours_per_week=15,  # roughly how many hours a week you spend on it
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


def setup_routes(app):
    app.route("/")(index)
    app.route("/favorites/<int:favorite_id>")(favorite_detail)


def run_app(debug: bool = True) -> None:
    app = create_app()
    app.run(debug=debug)



if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
