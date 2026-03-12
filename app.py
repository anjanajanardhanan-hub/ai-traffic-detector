from flask import Flask, render_template, request, redirect, url_for, session
from model import detect
from graph import create_graph
import requests
import random

app = Flask(__name__)
app.secret_key = "secret123"

blocked_ips = []

fake_ips = [
    "8.8.8.8",
    "1.1.1.1",
    "103.21.244.0",
    "185.199.108.153",
    "45.33.32.156"
]

# LOGIN PAGE
@app.route('/', methods=['GET','POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username == "admin" and password == "1234":
            session['user'] = username
            return redirect('/dashboard')
        else:
            return render_template("login.html", error="Invalid login")

    return render_template("login.html")


# DASHBOARD
# @app.route('/dashboard')
# def home():

#     if 'user' not in session:
#         return redirect('/')

#     create_graph()
#     return render_template("index.html", blocked=blocked_ips)

@app.route('/dashboard')
def home():

    if 'user' not in session:
        return redirect('/')

    create_graph()

    return render_template(
        "index.html",
        blocked=blocked_ips,
        show_blocked=False
    )

# DETECTION
# @app.route('/detect', methods=['POST'])
# def detect_traffic():

#     if 'user' not in session:
#         return redirect('/')

#     requests_value = int(request.form['requests'])
#     failed_value = int(request.form['failed'])

#     ip = random.choice(fake_ips)

#     result, risk_score, level = detect(requests_value, failed_value)

#     create_graph(requests_value)

#     try:
#         response = requests.get(f"http://ip-api.com/json/{ip}")
#         data = response.json()

#         city = data.get("city", "Unknown")
#         country = data.get("country", "Unknown")

#     except:
#         city = "Unknown"
#         country = "Unknown"

#     if "Anomaly" in result:
#         blocked_ips.append(ip)
#         message = f"⚠ Suspicious activity detected. IP {ip} blocked."
#     else:
#         message = f"✅ Traffic from {ip} is normal."

#     return render_template(
#         "index.html",
#         result=result,
#         req=requests_value,
#         fail=failed_value,
#         risk=risk_score,
#         level=level,
#         message=message,
#         blocked=blocked_ips,
#         ip=ip,
#         city=city,
#         country=country
#     )

@app.route('/detect', methods=['POST'])
def detect_traffic():

    if 'user' not in session:
        return redirect('/')

    requests_value = int(request.form['requests'])
    failed_value = int(request.form['failed'])

    ip = random.choice(fake_ips)

    result, risk_score, level = detect(requests_value, failed_value)

    create_graph(requests_value)

    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        city = data.get("city", "Unknown")
        country = data.get("country", "Unknown")

    except:
        city = "Unknown"
        country = "Unknown"

    show_blocked = False

    if level != "LOW":
        blocked_ips.append(ip)
        message = f"⚠ Suspicious activity detected. IP {ip} blocked."
        show_blocked = True
    else:
        message = f"✅ Traffic from {ip} is normal."

    return render_template(
    "index.html",
    result=result,
    req=requests_value,
    fail=failed_value,
    risk=risk_score,
    level=level,
    message=message,
    blocked=blocked_ips,
    show_blocked=show_blocked,
    ip=ip,
    city=city,
    country=country
)

# LOGOUT
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True) 