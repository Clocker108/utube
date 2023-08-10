from flask import Flask, render_template, request, redirect
from innertube import InnerTube

# Start innertube with web searching
client = InnerTube("WEB")

# Start flask session
app = Flask(__name__)

@app.route("/")
def search():
    return render_template("index.html")

@app.route("/result_video", methods=["GET", "POST"])
def result():
    if request.method == "GET":
        return redirect("/")
    else:
        QUERY = request.form.get("query")

        # Return to home when the user searched nothing
        if QUERY == "":
            return redirect("/")

        # Get the result from what user asked into dictionary
        data = client.search(query=QUERY)

        n = 0
        videoId = []
        title = []
        channel = []
        date = []
        view = []

        for video in data["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"]:
            try:
                o = video["videoRenderer"]

                videoId.append(o["videoId"])
                title.append(o["title"]["runs"][0]["text"])
                channel.append(o["longBylineText"]["runs"][0]["text"])
                date.append(o["publishedTimeText"]["simpleText"])
                view.append(o["viewCountText"]["simpleText"])

                n += 1

            except KeyError:
                pass

        # Redirect to result.html with results
        return render_template("result_video.html", query = QUERY, videoId = videoId, title = title, channel = channel, date = date, view = view, n = n)