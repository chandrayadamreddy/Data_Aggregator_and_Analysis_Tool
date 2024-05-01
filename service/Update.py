from distutils.command.config import config
from urllib import request

import pandas as pd


def upload_file():
    try:
        file = request.files.get("data")
        if file is None:
            return "No file uploaded", 400
        df = pd.read_excel(file)
        json_data = df.to_dict(orient='records')

        conn = config.MongoConfig.get_connect()
        db = conn['my_db']
        collection = db["my_collection"]
        collection.insert_many(json_data)
        conn.close()
        return "Data Uploaded successfully to MongoDB!!!", 200
    except Exception as e:
        print(e)
        return "An error occurred while processing the file", 500
