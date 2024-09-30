from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Use a strong secret key

# In-memory user storage (for demonstration purposes)
users = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username]['password'] == password:
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if username in users:
            flash('Username already exists', 'error')
        elif password != confirm_password:
            flash('Passwords do not match', 'error')
        else:
            users[username] = {'password': password}
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)
