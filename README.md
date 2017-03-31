# TweetMap
Summary

TweetMap is a robust web based application that pulls tweets in from Twitter and analyzes each word/emoji of every tweet. By analyzing this data, TweetMap is able to determine the overall emotion/mood of a tweet. The main purpose of the application is to display a map scattered with various emojis that represent the estimated mood of a tweet. This application is the result of a group project with 4 outher students from the University of Nebraska-Lincoln.

![Alt text](https://github.com/Sarcastick/TweetMap/blob/master/TweetMap.PNG) 

Directions for runnning program

    Uncompress all of the source code (if not compressed)
    Move all files to local C drive.
    Find the server.py and right click. Then go to properties on the opens section and chose python.exe
    Open cmd and type "pip install --user flask pip install --user flask_socketio pip install --user textblob"
    Type "server.py" and hit enter. 
    Navigate to chrome and type in "127.0.0.1:5000" hit play and observe the program and when you are done.
    Exit the tab press ctrl + c to stop the stream.

Features

      - Play and Stop for twitter stream
 	
      - Clicking on an emoji on the map will display the tweet
  
      - Use the “+” and “-“ buttons on the upper left corner to zoom in and zoom out
  
      - Click and drag on the map to move the map in any direction

Troubleshooting

    1. Map does not load emojis
 
     - Make sure that there is only one server.py program running in the command prompt 

    2. Map becomes very slow and unresponsive
 
     - Refresh the page

