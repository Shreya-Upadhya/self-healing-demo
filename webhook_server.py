from flask import Flask, request, jsonify
import subprocess
import json
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        alert_data = request.json
        logging.info(f"📨 Received webhook: {json.dumps(alert_data, indent=2)}")
        
        if alert_data.get('status') == 'firing':
            alerts = alert_data.get('alerts', [])
            for alert in alerts:
                if alert.get('labels', {}).get('alertname') == 'NginxDown':
                    logging.info("🚨 NGINX down alert detected! Triggering recovery...")
                    
                    # Run Ansible playbook
                    result = subprocess.run(
                        ['ansible-playbook', 'restart-nginx.yml'],
                        capture_output=True,
                        text=True
                    )
                    
                    logging.info(f"Recovery output: {result.stdout}")
                    
                    if result.returncode == 0:
                        logging.info("✅ Recovery completed successfully")
                    else:
                        logging.error(f"❌ Recovery failed: {result.stderr}")
        
        return jsonify({"status": "received"}), 200
    
    except Exception as e:
        logging.error(f"❌ Error: {e}")
        return jsonify({"status": "error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

### This Flask application acts as a webhook receiver for Alertmanager notifications, enabling automated recovery of monitored services. It listens for incoming HTTP POST requests containing alert data, logs the received alerts for auditing and debugging, and checks whether the alert corresponds to an `NginxDown` event. When such an alert is detected in the firing state, the application automatically executes an Ansible playbook (`restart-nginx.yml`) to restart the affected NGINX container. The execution results, including success or failure messages, are recorded through the logging system to provide visibility into the recovery process. By integrating Alertmanager, Flask, and Ansible, this service implements a self-healing mechanism that minimizes downtime and restores the monitored application without manual intervention.
