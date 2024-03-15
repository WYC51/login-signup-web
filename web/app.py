from flask import Flask, render_template, request, redirect, url_for
from mysql.connector import (connection)
app = Flask(__name__)

# Route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    users = get_user_data()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            # Redirect to logged-in page if credentials are correct
            return redirect(url_for("logged_in"))
        else:
            error = 'Invalid username or password. Please try again.'
    return render_template('index.html', error=error)

# Route for the sign-up page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        inser_user_data_to_db(username, password)
        return redirect(url_for("login"))
    return render_template('signup.html')

# Route for the logged-in page
@app.route('/login')
def logged_in():
    return render_template('login_in.html')

def get_user_data(sql = '''SELECT * from EMPLOYEE'''):
    cnx = connection.MySQLConnection(user='root', password='password',
                                 host='db',
                                 port=3306, database = "mysql")
    try:
        with cnx.cursor() as cursor:
            cursor.execute("USE mysql;")
            cursor.execute(sql)
            users = {}
            for acc, pwd in cursor.fetchall():
                users[acc] = pwd
        return users
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()

def inser_user_data_to_db(account, pwd):
    cnx = connection.MySQLConnection(user='root', password='password',
                                 host='db',
                                 port=3306, database = "mysql")
    try:
        with cnx.cursor() as cursor:
            cursor.execute("USE mysql;")
            sql = f"INSERT INTO EMPLOYEE(ACCOUNT, PWD) VALUES('{account}', '{pwd}');"
            cursor.execute(sql)
            cnx.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5050")