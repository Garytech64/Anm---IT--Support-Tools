from flask import Flask, render_template, jsonify
import psutil
import socket
from threading import Timer
import webbrowser

app = Flask(__name__)

def get_network_info():
    """Return hostname and local IP address."""
    hostname = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip_address = "Unavailable"
    return hostname, ip_address

@app.route("/")
def dashboard():
    # Initial values for template
    cpu_percent = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('C:\\')
    hostname, ip_address = get_network_info()
    
    return render_template(
        "index.html",
        cpu=cpu_percent,
        ram_used=ram.used // (1024**3),
        ram_total=ram.total // (1024**3),
        disk_total=disk.total // (1024**3),
        disk_used=disk.used // (1024**3),
        disk_free=disk.free // (1024**3),
        hostname=hostname,
        ip_address=ip_address
    )

@app.route("/api/stats")
def api_stats():
    cpu_percent = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('C:\\')
    return jsonify({
        "cpu": cpu_percent,
        "ram_used": ram.used // (1024**3),
        "ram_total": ram.total // (1024**3),
        "disk_total": disk.total // (1024**3),
        "disk_used": disk.used // (1024**3),
        "disk_free": disk.free // (1024**3)
    })

if __name__ == "__main__":
    url = "http://127.0.0.1:5000/"
    Timer(1, lambda: webbrowser.open(url)).start()  # Open browser automatically
    app.run(debug=True)
