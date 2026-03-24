from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/run-script', methods=['POST'])     #run script wala method run hora 
def run_script():
    data = request.json             #javaScript object notation {string(anydata types)}
    dynamic_variable = data.get('dynamic_variable')     #url =Dynamic varible

    if not dynamic_variable:
        return jsonify({'error': 'No URL provided.'}), 400

    try:
        # Print the received URL for debugging
        print(f"Received URL: {dynamic_variable}")

        # Adjust the path to your Python executable and web scraping script as needed
        command = ['C:\\Program Files\\Python312\\python.exe',
                   'D:/Project/pythonProject - Copy/.venv/backend/WebScrapping.py',
                   dynamic_variable]
        print(f"Running command: {command}")

        result = subprocess.run(command, capture_output=True, text=True)
        output = result.stdout.strip()

        # Print the result for debugging
        print(f"Command output: {output}")

        if result.returncode != 0:
            output += "\n" + result.stderr.strip()
            print(f"Command error: {result.stderr.strip()}")
    except Exception as e:
        output = str(e)
        print(f"Exception: {output}")

    return jsonify({'output': output})


if __name__ == '__main__':
    app.run(debug=True)
