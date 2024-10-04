from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
json_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
all_posts = []
for post in json_posts:
    all_posts.append(Post(post["id"], post["title"], post["subtitle"], post["body"]))

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:blog_id>')
def blog(blog_id):
    requested_post = None
    for any_post in all_posts:
        if any_post.post_id == blog_id:  # Correct comparison
            requested_post = any_post    # Assign the matching post
        return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
