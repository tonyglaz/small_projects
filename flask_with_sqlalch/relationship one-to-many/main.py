from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dota.db"
db = SQLAlchemy(app)


class Player(db.Model):
    """Таблица игрока"""
    __tablename__ = "player"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    nickname = db.Column(db.String(100))
    position = db.Column(db.Integer)
    group_id = db.Column(db.Integer, db.ForeignKey("team.id"))

    team = relationship("Team")


class Team(db.Model):
    """Таблица команды"""
    __tablename__ = "team"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),unique=True)

    players = relationship("Player")


@app.route('/')
def create_app():
    db.create_all()

    team_TS = Team(id=1, name="Team Spirit")
    player_denis = Player(id=1, name="Denis", age=21, nickname="Larl", position=2, team=team_TS)
    player_yatoro = Player(id=2, name="Ilya", age=19, nickname="Yatoro", position=1, team=team_TS)

    db.session.add(player_denis)
    db.session.add(player_yatoro)

    player_nightfall = Player(id=3, name="Egor", age=20, nickname="Nightfall", position=3)
    player_torontotokyo = Player(id=4, name="Alexander", age=25, nickname="TORONTOTOKYO", position=5)
    team_BB = Team(id=2, name="BetBoom", players=[player_nightfall, player_torontotokyo])

    db.session.add(team_BB)

    player_with_team = Player.query.get(1)
    return player_with_team.team.name


if __name__ == "__main__":
    app.run(debug=True)
