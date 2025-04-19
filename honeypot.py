from flask import Flask, request, render_template_string
from datetime import datetime
import os

app = Flask(__name__)

# Replace this with your actual reCAPTCHA secret key
RECAPTCHA_SECRET = "your-secret-key"

LOGIN_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Secure Login</title>
    <script src="https://www.google.com/recaptcha/api.js" async defer></script>
</head>
<body>
    <h2>Login to Admin Panel</h2>
    <form action="/login" method="POST">
        Username: <input name="username" type="text"><br>
        Password: <input name="password" type="password"><br><br>
        <div class="g-recaptcha" data-sitekey="your-site-key"></div><br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(LOGIN_PAGE)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    ip = request.remote_addr
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("attack_logs.txt", "a") as f:
        f.write(f"{timestamp} - Attempted login from {ip} with username: {username}\n")

    return "🚨 Intrusion Logged. This incident has been reported."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
