from flask import Flask, render_template, jsonify
import psutil
import shutil

app = Flask(__name__)

# Keep previous network counters for speed calculation
prev_counters = psutil.net_io_counters()

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/stats")
def stats():
    global prev_counters

    # CPU usage
    cpu_percent = psutil.cpu_percent(interval=0.5)

    # RAM usage
    ram = psutil.virtual_memory()
    ram_total = ram.total // (1024**3)
    ram_used = ram.used // (1024**3)
    ram_percent = ram.percent

    # Disk C: usage
    total, used, free = shutil.disk_usage("C:/")
    disk_total = total // (1024**3)
    disk_used = used // (1024**3)
    disk_free = free // (1024**3)
    disk_percent = int((used / total) * 100)

    # Network speeds (KB/s)
    current_counters = psutil.net_io_counters()
    upload_speed = (current_counters.bytes_sent - prev_counters.bytes_sent) / 1024
    download_speed = (current_counters.bytes_recv - prev_counters.bytes_recv) / 1024
    prev_counters = current_counters

    return jsonify({
        "cpu_percent": cpu_percent,
        "ram_total": ram_total,
        "ram_used": ram_used,
        "ram_percent": ram_percent,
        "disk_total": disk_total,
        "disk_used": disk_used,
        "disk_free": disk_free,
        "disk_percent": disk_percent,
        "upload_speed": round(upload_speed, 2),
        "download_speed": round(download_speed, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)
