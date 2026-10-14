from flask import Flask, render_template

app = Flask(__name__)

BOT_NAME = "𝒍𝒆𝒚𝒏𝒂"
CREATOR = "@lmegax3"
CLIENT_ID = "1546657642062020628"

INVITE_URL = (
    f"https://discord.com/oauth2/authorize?client_id={CLIENT_ID}"
    "&permissions=8&scope=bot%20applications.commands"
)

FEATURES = [
    {"title": "Voice", "desc": "Bring the bot into your voice channels."},
    {"title": "Daily Rewards", "desc": "Claim a reward every day and keep your streak."},
    {"title": "Profiles", "desc": "Show off your stats with a personal profile."},
    {"title": "Ranking", "desc": "Level up and climb the server leaderboard."},
]

COMMANDS = [
    {"name": "/join", "desc": "Make the bot join your voice channel"},
    {"name": "/daily", "desc": "Claim your daily reward"},
    {"name": "/profile", "desc": "View your profile and stats"},
    {"name": "/rank", "desc": "Check your rank and level"},
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        bot_name=BOT_NAME,
        creator=CREATOR,
        invite=INVITE_URL,
        features=FEATURES,
        commands=COMMANDS,
    )

if __name__ == "__main__":
    app.run(debug=True)