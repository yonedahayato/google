from google.cloud import storage
import os

import log
import setting

# google api key setting
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=setting.api_key_json_path

# log
logger = log.logger

# upload file path
upload_file_path = setting.upload_file_path

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
            file_name = os.path.basename(file_path)
            dir_name = file_path.split("/")[-2]
            blob = self.bucket.blob("{}/{}".format(dir_name, file_name))
            blob.upload_from_filename("{}/{}".format(upload_file_path, file_name))
        except Exception as e:
            err_msg = msg.format("fail to upload {}, {}".format(file_path, e))
            self.logging_error(err_msg)
            raise Exception(err_msg)
        else:
            sccs_msg = msg.format("success to update {}".format(file_path))
            self.logging_info(sccs_msg)

    def download(self, file_path):
        msg = "[Google_Cloud_Storage:download]: {}"

        try:
            file_name = os.path.basename(file_path)
            blob = self.bucket.blob(file_path)
            blob.download_to_filename("{}/{}".format(upload_file_path, file_name))
        except Exception as e:
            err_msg = msg.format("fail to download {}, {}".format(file_path, e))
            self.logging_error(err_msg)
            raise Exception(err_msg)
        else:
            sccs_msg = msg.format("success to download {}".format(file_path))
            self.logging_info(sccs_msg)

    def test_print(self):
        print("test")

if __name__ == "__main__":
    gcs = Google_Cloud_Storage()
    gcs.upload("upload_file/test.txt")
