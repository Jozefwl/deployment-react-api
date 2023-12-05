from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

# read API password from file
with open('api_password.txt', 'r') as file:
    API_PASSWORD = file.read().strip()

@app.route('/run-deploy', methods=['POST'])
def run_deploy_script():
    # check if provided password is correct
    data = request.json
    if not data or 'password' not in data or data['password'] != API_PASSWORD:
        return jsonify({'error': 'Unauthorized access'}), 401

    try:
        result = subprocess.run(['./deploy_financio.sh'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output_lines = result.stdout.strip().split('\n')

        # structure the output into JSON array
        deploy_info = {
            "output_lines": output_lines
        }

        return jsonify(deploy_info), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'error': e.stderr}), 500

@app.route('/get-status', methods=['POST'])
def get_status():
    # check if provided password is correct
    data = request.json
    if not data or 'password' not in data or data['password'] != API_PASSWORD:
        return jsonify({'error': 'Unauthorized access'}), 401

    try:
        result = subprocess.run(['./checkStatus.sh'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output_lines = result.stdout.strip().split('\n')

        # parse the output into a structured format
        status_info = {
            "nginx_status": output_lines[1],
            "cpu_usage": output_lines[3].split(": ")[1],
            "ram_usage": output_lines[5]
        }

        return jsonify(status_info), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'error': e.stderr}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
