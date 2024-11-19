from flask import Flask, render_template

import requests


app = Flask(__name__)

blog_endpoint = 'https://api.npoint.io/c790b4d5cab58020d391'
blog_response = requests.get(blog_endpoint)
blog_data = blog_response.json()

@app.route('/')
def home():
    return render_template("index.html", posts=blog_data)

@app.route('/post/<int:index>')
def blog(index):
    for post in blog_data:
        if post['id'] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
