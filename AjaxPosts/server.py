from flask import Flask, request, redirect, render_template, session, flash, jsonify
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)

app.secret_key = "SecretKeyDont"
mysql = MySQLConnector(app, 'ajax_posts')


@app.route('/')
def show_posts():
    # posts = query_posts()
    # query = "SELECT * FROM posts"
    return render_template('index.html')

@app.route('/create/post', methods=['POST'])
def create_post():
    post = request.form['message']
    post_insert = "INSERT INTO posts (post, created_at, updated_at) VALUES(:post, NOW(), NOW())"
    post_data = {
        'post': post
    }
    posts = mysql.query_db(post_insert, post_data)
    new_line_query = "SELECT * FROM posts WHERE id = {}".format(posts)
    new_line = mysql.query_db(new_line_query)
    return jsonify(new_line)

@app.route('/posts/index_json')
def get_posts():
    query = "SELECT * FROM posts"
    posts = mysql.query_db(query)
    return jsonify(posts)

def query_posts():
    query = "SELECT * FROM posts"
    posts = mysql.query_db(query)
    return jsonify(posts)

if __name__ == "__main__":
    app.run(port=8000, debug=True)



# app.run(debug=True)
#
