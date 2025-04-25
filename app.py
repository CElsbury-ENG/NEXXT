from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# Replace with your actual Apps Script URL
SCRIPT_URL = "https://script.google.com/macros/s/AKfycbwUKcg4miBtaanAF_5tVQwvPeNAJHzkRCOHXqul_NrSqDCmosvsd7z1sGhVIrqbDbkXZw/exec"

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        comment = request.form.get("comment")
        
        data = {
            "name": name,
            "email": email,
            "comment": comment
        }

        try:
            response = requests.post(SCRIPT_URL, data=data)
            print("Script response:", response.text)
        except Exception as e:
            print("Error posting to Google Sheet:", e)

        return redirect("/")  # Redirect after form submit

    return render_template("form.html")