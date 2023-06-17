from flask import render_template
from app.posts import bp
from app.models.post import Post


# Flask ieskos blueprint su keliu templates/posts/index.html
@bp.route("/")
def index():
    posts = Post.query.all()
    return render_template("posts/index.html", posts=posts)


@bp.route("/categories")
def categories():
    return render_template("posts/categories.html")
