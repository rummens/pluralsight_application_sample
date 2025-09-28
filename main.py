from flask import Flask, render_template_string
import subprocess
import os

app = Flask(__name__)

@app.route("/")
def index():
    # Get installed packages
    result = subprocess.run(["pip", "freeze"], capture_output=True, text=True)
    packages = result.stdout.splitlines()

    print("Found packages:", packages)  # Debugging line

    # Try to read the timestamp file
    timestamp_path = "/app/timestamp.txt"
    if os.path.exists(timestamp_path):
        with open(timestamp_path, "r") as f:
            timestamp_content = f.read().strip()
            timestamp_error = None
    else:
        timestamp_content = None
        timestamp_error = f"No build time found at path {timestamp_path}"

    print("Image was built at:", timestamp_content)  # Debugging line

    # HTML template
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello Pluralsight</title>
        <style>
            #packages { display: none; margin-top: 10px; }
            button { margin-top: 20px; }
            #timestamp { margin-top: 30px; color: #555; }
            #error { color: red; margin-top: 30px; }
        </style>
        <script>
            function togglePackages() {
                var x = document.getElementById('packages');
                x.style.display = x.style.display === 'none' ? 'block' : 'none';
            }
        </script>
    </head>
    <body>
        <h1>Hello Pluralsight</h1>
        <button onclick="togglePackages()">Show/Hide Installed Packages</button>
        <div id="packages">
            <ul>
                {% for pkg in packages %}
                    <li>{{ pkg }}</li>
                {% endfor %}
            </ul>
        </div>
        {% if timestamp_content %}
            <div id="timestamp">
                <strong>Build Timestamp:</strong> {{ timestamp_content }}
            </div>
        {% elif timestamp_error %}
            <div id="error">{{ timestamp_error }}</div>
        {% endif %}
    </body>
    </html>
    """
    return render_template_string(
        html,
        packages=packages,
        timestamp_content=timestamp_content,
        timestamp_error=timestamp_error
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)