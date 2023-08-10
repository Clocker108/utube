# Alternative Youtube Search Website, UTube
#### Introduction Video: [Youtube](https://youtu.be/zXcTdVq7xCA)
#### Description: Simple youtube videos search alternative

### Lightweight python, flask based Open-Source. UTube allows **searching youtube videos** without using youtube's official API, and using unofficial API, InnerTube.

#### Features
- Search videos on youtube
- Go directly to youtube video that you searched
Watch TODO, and those features will come soon!

#### How to use
Use your python and flask to start the server.
0. Of course, open your python3.
1. Move to your folder.
2. Enter "flask run" to start your server with flask.
WARNING : YOU NEED TO INSTALL INNERTUBE AND FLASK IN ORDER TO RUN THIS PROGRAM! TO INSTALL:
"pip install innertube"
"pip install flask"
3. Go into your server, there will be a logo and simple search bar.
4. Search what you want to search on youtube, and press Enter or click Search button.
5. Your results are here!

#### Why should I use this? or Why is it developed?
As you know, youtube website recently increased ads amount and annoying shorts.
Their youtube website also includes various trackers, which takes away your privacy.

UTube can allow you visit and enjoy youtube without all of those ads, shorts, and trackers.
Although there is TODO(As you can see below) left, when its done,
it can be alternative frontend enough.

#### What's difference between ~~~~ ?
1. Invidious
Invidious uses its own developed invidious API, while UTube uses innertube API.
Invidious API is getting problems with google, with too many requests(that's how google tries to block them)
Innertube API in the other hand, is a bit free for that problem, since innertube simulates web experience.
(As you can see through python, it can be simulated into IOS client, too!)

2. Piped
Piped also uses innertube API, and they proxy everything. What this means is the user will never connect to Google.
However, its problem with google is even more serious than invidious.
Their instances tend to go down several times in a day.

In order to combine these two services' advantages(Innertube API with local connection that won't get problem with google at least),
UTube is here.

#### TODO
- Having session to website
Session is needed in order to implement login, register, user playlists saving.
- Adding SQL Database
Database is for saving users id and playlists.
- Channel Tab
Currently, UTube is only searching for youtube videos. Channels can be searched through innertube API.
So we need another html to give channel result to users.