from flask import Flask, request, jsonify

app_notify = Flask(__name__)

@app_notify.route('/notifications/', methods=['POST'])
def post_notification():
    data = request.json
    print(f"Received Notification: {data['message']}")  # Affiche la notification sur la console
    return jsonify({"message": "Notification sended successfully"}), 200

if __name__ == '__main__':
    app_notify.run(port=5001)
