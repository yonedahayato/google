from google.cloud import storage
import os

import log
import setting

# google api key setting
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=setting.api_key_json_path

# log
logger = log.logger

class Google_Cloud_Storage:
    def __init__(self):
        self.client = storage.Client()
        self.bucket_name = setting.bucket_name
        self.bucket = self.client.get_bucket(self.bucket_name)

    def logging_info(self, msg):
        print(msg)
        logger.info(msg)

    def logging_error(self, msg):
        logger.exception(msg)
        logger.error(msg)

    def upload(self, file_path):
        msg = "[Google_Cloud_Storage:update]: {}"

        try:
            blob = self.bucket.blob(file_path)
            blob.upload_from_filename(file_path)
        except Exception as e:
            err_msg = msg.format("fail to upload {}, {}".format(file_path, e))
            self.logging_error(err_msg)
            raise Exception(err_msg)
        else:
            sccs_msg = msg.format("success to update {}".format(file_path))
            self.logging_info(sccs_msg)

    def test_print(self):
        print("test")

if __name__ == "__main__":
    gcs = Google_Cloud_Storage()
    gcs.upload("upload_file/test.txt")
