from flask import Flask, request, jsonify, redirect, url_for, render_template_string
from flask_login import LoginManager, login_user, login_required, UserMixin, logout_user
from flask import render_template  # <-- Add this import at the top
import os
import config



app = Flask(__name__, static_url_path='/static', static_folder='static')

app.config['SECRET_KEY'] = config.SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

LOG_FILES = config.LOG_FILES


LINES_PER_PAGE = 100  # Default number of lines per page

class User(UserMixin):
    pass

# This is just a dummy user store. Replace this with your database or other user store.
users = {username: {'password': pwd} for username, pwd in config.USERS.items()}

@login_manager.user_loader
def user_loader(username):
    if username not in users:
        return

    user = User()
    user.id = username
    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('username')
    if (username in users) and (request.form['password'] == users[username]['password']):
        user = User()
        user.id = username
        login_user(user)
        return redirect(url_for('index'))

    return 'Bad login'

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/get_log_files', methods=['GET'])
@login_required
def get_log_files():
    return jsonify({'log_files': LOG_FILES})     

@app.route('/get_log_content', methods=['POST'])
@login_required
def get_log_content():
    log_file = request.form['log_file']
    page = int(request.form.get('page', 1))
    search_term = request.form.get('search_term', '').lower()
    items_per_page = int(request.form.get('items_per_page', LINES_PER_PAGE))
    read_from = request.form.get('read_from', 'top')

    if not os.path.exists(log_file):
        return jsonify({'error': 'Log file not found'}), 404

    with open(log_file, 'r', encoding="utf-8", errors="ignore") as file:
        lines = file.readlines()

    if search_term:
        lines = [line for line in lines if search_term in line.lower()]
    
    # Reverse lines if reading from bottom
    if read_from == 'bottom':
        lines = lines[::-1]

    total_lines = len(lines)
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page

    content = ''.join(lines[start_index:end_index])
    return jsonify({
        'content': content,
        'total_lines': total_lines,
        'lines_per_page': items_per_page
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
