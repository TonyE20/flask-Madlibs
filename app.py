from flask import Flask, request, render_template
from stories import story1, story2
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "ninjaswordstyle"
debug = DebugToolbarExtension(app)

@app.route("/")
def home():
    return render_template("chooseStory.html")

@app.route("/questions1")
def homepage():
    questions = story1.prompts
    return render_template("homepage.html", questions=questions)

@app.route("/questions2")
def homepage2():
    questions = story2.prompts
    return render_template("homepage2.html", questions=questions)

@app.route("/story1")
def your_story():
    my_story = story1.generate(request.args)
    return render_template("story.html", my_story=my_story)

@app.route("/story2")
def your_story2():
    my_story = story2.generate(request.args)
    return render_template("story2.html", my_story=my_story)