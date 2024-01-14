from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "https://i.kym-cdn.com/photos/images/newsfeed/002/681/863/ede.gif",
    "https://media1.giphy.com/media/ule4vhcY1xEKQ/giphy.gif",
    "https://cdn.shopify.com/s/files/1/0344/6469/files/cat-gif-loop-wheel_grande.gif?v=1523982721",
    "https://media.tenor.com/n8FLvdqXQ4gAAAAM/plink-cat.gif",
    "https://www.icegif.com/wp-content/uploads/cat-icegif-19.gif",
    "https://i.pinimg.com/originals/9a/3c/3f/9a3c3fb5f73822af8514df07f6676392.gif",
    "https://i0.wp.com/dianaurban.com/wp-content/uploads/2017/07/01-cat-stretching-feet.gif?resize=500%2C399&ssl=1",
    "https://media.tenor.com/YX0vm2HQ_ZsAAAAM/cat.gif",
    "https://www.icegif.com/wp-content/uploads/icegif-341.gif",
    "https://media1.giphy.com/media/yFQ0ywscgobJK/giphy.gif",
    "https://i.pinimg.com/originals/fa/3b/40/fa3b40cabeb38b98d55040e51947a736.gif",
    "https://media0.giphy.com/media/cfuL5gqFDreXxkWQ4o/giphy.gif"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")