from flask import Flask, render_template
import psutil
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    cpu_usage = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    memory_usage = mem.percent
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    network_devices = [
        {"name": "Router", "status": "Online"},
        {"name": "Printer", "status": "Online"},
        {"name": "Server", "status": "Online"}
    ]

    return render_template('index.html', cpu=cpu_usage, memory=memory_usage,
                           time=time, devices=network_devices)

if __name__ == "__main__":
    app.run(debug=True)
