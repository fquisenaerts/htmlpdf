from flask import Flask, request, jsonify, send_file
from weasyprint import HTML
import os

app = Flask(__name__)

@app.route("/convert_to_pdf", methods=["POST"])
def convert_to_pdf():
    data = request.json
    html_content = data.get("html", "")

    if not html_content:
        return jsonify({"error": "Aucun HTML fourni"}), 400

    pdf_path = "/tmp/output.pdf"
    HTML(string=html_content).write_pdf(pdf_path)

    return send_file(pdf_path, as_attachment=True, download_name="cv.pdf")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
