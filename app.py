from flask import Flask, render_template, redirect
import os

app = Flask(__name__)
INSTALLER_URL = "https://github.com/herrymonster555-bot/yt-drop-download-site/releases/latest/download/YT-Drop-Setup.exe"

@app.get("/")
def home():
    return render_template("index.html", size_mb=108)

@app.get("/download/windows")
def download_windows():
    return redirect(INSTALLER_URL, code=302)

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "10000")))
