from flask import Flask, render_template, request
from utilities.find_handler import CheckIfFileExist, FindFiles, FileNameGenerator

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title="Blog")


@app.route("/blog")
def blog():
    # TODO: Change this logic to loop though blog files and get picture, date, and entry text.

    text = open("./blog_entries/this-is-a-test-blog.txt").read()
    text = text.split("|")

    data = {}
    data["title"] = text[0]
    data["date"] = text[1]
    data["image"] = text[2]
    data["content"] = text[3]

    return render_template("blog.html", data=data)


@app.route("/blog/<string:blog_name>")
def blogArticle(blog_name):
    filename = blog_name
    filepath = CheckIfFileExist("./blog_entries/", filename)

    if type(filepath.doesFileExist()) is not str or False:
        return "Page not Found", 404

    text = open(filepath.doesFileExist()).read()
    text = text.split("|")

    data = {}
    data["title"] = text[0]
    data["date"] = text[1]
    data["image"] = text[2]
    data["content"] = text[3]

    return render_template("blog.html", data=data)


@app.route("/get-data", methods=["POST"])
def getData():
    if request.method == "POST":
        data = request.get_json()

        if (
            not data["title"]
            or not data["image"]
            or not data["date"]
            or not data["content"]
        ):
            return "Please enter data in all fields.", 400
        else:
            filename = FileNameGenerator(data["title"])

            write_data = ""
            outfile = open("./blog_entries/" + filename + ".txt", "w")
            write_data = (
                data["title"]
                + "|"
                + data["date"]
                + "|"
                + data["image"]
                + "|"
                + data["content"]
            )
            outfile.write(write_data)
        return data
    else:
        return "No Access.", 400
