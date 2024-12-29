from flask import Flask, request, jsonify
from translator import translate_to_english
import uuid
import sys
import os

# Add the project root directory to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "C:/Users/ahell/Downloads/ar2enservice")))
from translator import translate_to_english


app = Flask(__name__)


# In-memory store for request statuses
translation_status = {}

@app.route("/translate/ar2en", methods=["POST"])
def translate_ar_to_en():
    try:
        input_text = request.json.get("text", "")
        if not input_text:
            return jsonify({"error": "No text provided"}), 400

        # Generate a unique request ID
        request_id = str(uuid.uuid4())
        translation_status[request_id] = "Processing"

        # Perform translation
        translated_text = translate_to_english(input_text)
        translation_status[request_id] = "Completed"

        return jsonify({"request_id": request_id, "translated_text": translated_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/translate/ar2en/status/<request_id>", methods=["GET"])
def get_status(request_id):
    status = translation_status.get(request_id)
    if not status:
        return jsonify({"error": "Invalid request ID"}), 404

    return jsonify({"request_id": request_id, "status": status})

# Add this to ensure proper multiprocessing handling on Windows
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    