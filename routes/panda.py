from urllib import request

from flask import Blueprint
from pymongo import auth
from werkzeug.utils import secure_filename
import json
from flask import request
from pymongo import MongoClient
realtime = Blueprint("realtime", __name__)

ALLOWED_EXTENSIONS = {'json', 'txt', 'xlsx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'json', 'txt'}

@realtime.route("/upload_file", methods=['POST'])

def upload_file():
    try:
        file = request.files.get("data")
        if file is None:
            return "No file uploaded", 400

        if file and allowed_file(file.filename):
            # Proceed with file processing
            filename = secure_filename(file.filename)
            # Connect to MongoDB
            client = MongoClient("mongodb://localhost:27017/")
            db = client["your_database_name"]  # Replace "your_database_name" with your database name
            collection = db["your_collection_name"]  # Replace "your_collection_name" with your collection name

            if filename.endswith('.json'):
                # If JSON file, parse and upload data to MongoDB
                data = json.load(file)
                collection.insert_many(data)
            elif filename.endswith('.txt'):
                # If TXT file, read lines and upload each line to MongoDB
                lines = file.readlines()
                for line in lines:
                    collection.insert_one({"text": line.decode("utf-8").strip()})
            else:
                return "Invalid file type. Allowed file types are: JSON, TXT.", 400

            return "Data Uploaded successfully to MongoDB!!!", 200
        else:
            return "Invalid file type. Allowed file types are: JSON, TXT.", 400
    except Exception as e:
        print(e)
        return "An error occurred while processing the file", 500
