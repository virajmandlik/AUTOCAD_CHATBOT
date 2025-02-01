from flask import Flask, request, jsonify, send_file, render_template
import os
from generate_dwg import create_dwg
import time
import threading

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate_dwg():
    data = request.json  

    if not data or "rooms" not in data:
        return jsonify({"error": "Invalid input"}), 400
        
    if len(data["rooms"]) == 0:
        return jsonify({"error": "At least one room required"}), 400

    try:
        filename = "floor_plan.dwg"
        file_path = create_dwg(data["rooms"], filename)
        
        # Send the file as a response
        return send_file(
            file_path,
            as_attachment=True,
            download_name=filename
        )

    finally:
        # Start a background thread to delete the file after a delay
        threading.Thread(target=delete_file_after_delay, args=(file_path,)).start()


def delete_file_after_delay(file_path):
    # Wait for 2 seconds to ensure the file download is completed
    time.sleep(2)
    if os.path.exists(file_path):
        os.remove(file_path)


if __name__ == '__main__':
    os.makedirs(app.config['STATIC_FOLDER'], exist_ok=True)
    app.run(debug=True)
