from flask import Flask, render_template_string
from goprocam import GoProCamera, constants

app = Flask(__name__)
cam = None
HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>GoPro Controller</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { background: #1a1a1a; color: white; font-family: Arial; text-align: center; padding: 20px; }
        h1 { color: #00aaff; }
        .btn { display: block; width: 80%; margin: 15px auto; padding: 20px; font-size: 24px; border: none; border-radius: 15px; cursor: pointer; }
        .photo { background: #00aaff; }
        .record { background: #ff0000; }
        .stop { background: #888; }
        .download { background: #00cc66; }
        .battery { background: #ffaa00; }
    </style>
</head>
<body>
    <h1>GoPro Controller</h1>
    <a href="/photo"><button class="btn photo">📷 Take Photo</button></a>
    <a href="/start"><button class="btn record">🔴 Start Recording</button></a>
    <a href="/stop"><button class="btn stop">⏹ Stop Recording</button></a>
    <a href="/download"><button class="btn download">📥 Download Last File</button></a>
    <a href="/battery"><button class="btn battery">🔋 Battery Level</button></a>
</body>
</html>
'''
@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/photo")
def photo():
    cam.take_photo()
    return render_template_string(HTML.replace("GoPro Controller</h1>", "GoPro Controller</h1><p style='color:#00aaff'>Photo taken!</p>"))

@app.route("/start")
def start():
    cam.shoot_video()
    return render_template_string(HTML.replace("GoPro Controller</h1>", "GoPro Controller</h1><p style='color:#ff0000'>Recording started!</p>"))

@app.route("/stop")
def stop():
    cam.shoot_video(0)
    return render_template_string(HTML.replace("GoPro Controller</h1>", "GoPro Controller</h1><p style='color:#888'>Recording stopped!</p>"))

@app.route("/battery")
def battery():
    level = cam.getStatus(constants.Status.Status, constants.Status.STATUS.BatteryLevel)
    return render_template_string(HTML.replace("GoPro Controller</h1>", "GoPro Controller</h1><p style='color:#ffaa00'>Battery: " + str(level) + "</p>"))

@app.route("/download")
def download():
    cam.downloadLastMedia()
    return render_template_string(HTML.replace("GoPro Controller</h1>", "GoPro Controller</h1><p style='color:#00cc66'>File downloaded!</p>"))

if __name__ == "__main__":
    print("Connecting to GoPro...")
    cam = GoProCamera.GoPro(constants.gpcontrol)
    print("Connected! Open Chrome and go to http://localhost:5000")
    app.run(host="0.0.0.0", port=5000)