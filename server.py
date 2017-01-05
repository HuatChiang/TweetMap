from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from textblob import TextBlob

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
@socketio.on('request')
def test_message(data):

    textData = TextBlob(data['data'])
    senti = float(textData.sentiment.polarity)

    feeling =''

    if senti >= -1 and senti < -.75:
        feeling = 'http://emojipedia-us.s3.amazonaws.com/cache/aa/0d/aa0df8c03f8f383a7a8bf008449d1d24.png' #rage
    
    elif senti >= -.75 and senti < -.5:
        feeling = 'http://emojipedia-us.s3.amazonaws.com/cache/6e/a0/6ea06e1d085a782995ff26a82f729b4c.png' #angry
    
    elif senti >= -.5 and senti < -.25:
        feeling = 'http://emojipedia-us.s3.amazonaws.com/cache/f0/65/f065565eb5f02757858766531476d0dd.png' #worried
    
    elif senti >= -.25 and senti < 0:
        feeling = 'http://emojipedia-us.s3.amazonaws.com/cache/6d/96/6d96631bf73562fea8d80624ee86690e.png' #unamused
    
    elif senti >= 0 and senti < .25:
        feeling = 'http://emojipedia-us.s3.amazonaws.com/cache/cc/ee/ccee6eef2faa53c12fde1bacaf76278c.png' #neutralface
    
    elif senti >= .25 and senti < .5:
        feeling = 'http://emojipedia-us.s3.amazonaws.com/cache/92/ed/92eddc7180737357aa52a876a82f748c.png' #blush
    
    elif senti >= .5 and senti < .75:
        feeling = 'http://emojipedia-us.s3.amazonaws.com/cache/91/01/91019eb02405b1e86e4c10ae92ad4409.png' #smile
    
    elif senti >= .75 and senti <= 1:
        feeling = 'http://emojipedia-us.s3.amazonaws.com/cache/2b/b3/2bb365f6f875e316aed3a7be07b1cec5.png' #smiley
   
    socketio.emit('response', {"sentiment": senti, "emoji": feeling})

@app.route('/')
def index():
    return render_template('index.html')
    
if __name__ == '__main__':
    socketio.run(app)