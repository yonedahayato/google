from google.cloud import storage
import os

import log
# log
logger = log.logger

class Uploader:
    def __init__(self, bucket_name):
        self.client = storage.Client()
        self.bucket_name = bucket_name
        self.bucket = self.client.get_bucket(self.bucket_name)

    def upload(self, local_path, gcp_path, public=False):
        msg = "[Google_Cloud_Storage:update]: {}"

        try:
            blob = self.bucket.blob(gcp_path)
            blob.upload_from_filename(local_path)
            if public:
                blob.make_public()

        except Exception as e:
            err_msg = msg.format("fail to upload {}, {}".format(local_path, e))
            logger.exception(err_msg)
            raise Exception(err_msg)

        else:
            sccs_msg = msg.format("success to update {}".format(local_path))
            logger.info(sccs_msg)

    def download(self, file_path):
        msg = "[Google_Cloud_Storage:download]: {}"

        try:
            file_name = os.path.basename(file_path)
            blob = self.bucket.blob(file_path)
            blob.download_to_filename("{}/{}".format(upload_file_path, file_name))
        except Exception as e:
            err_msg = msg.format("fail to download {}, {}".format(file_path, e))
            logger.exception(err_msg)
            raise Exception(err_msg)
        else:
            sccs_msg = msg.format("success to download {}".format(file_path))
            self.logging_info(sccs_msg)

    def test_print(self):
        print("test")

if __name__ == "__main__":
    import setting
    # upload file path
    upload_path = setting.upload_file_path

    # google api key setting
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=setting.api_key_json_path

    uploader = Uploader(bucket_name=setting.bucket_name)
    uploader.upload("upload_file/test.txt", upload_path)
