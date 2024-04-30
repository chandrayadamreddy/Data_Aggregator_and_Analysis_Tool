from urllib import request

from flask import Blueprint
from werkzeug.utils import secure_filename
realtime = Blueprint("realtime", __name__)

ALLOWED_EXTENSIONS = {'json', 'txt', 'xlsx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@realtime.route("/upload", methods=['POST'])

def upload_file():
    try:
        file = request.files.get("data")
        if file is None:
            return "No file uploaded", 400

        if file and allowed_file(file.filename):
            # Proceed with file processing
            filename = secure_filename(file.filename)
            # Here you can handle uploading to MongoDB or any other operations
            return "Data Uploaded successfully to MongoDB!!!", 200
        else:
            return "Invalid file type. Allowed file types are: JSON, TXT, XLSX.", 400
    except Exception as e:
        print(e)
        return "An error occurred while processing the file", 500
