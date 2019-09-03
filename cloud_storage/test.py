import os

import setting
from uploader import Uploader

def test_upload():
    # google api key setting
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=setting.api_key_json_path

    uploader = Uploader(bucket_name="yoneda-tmp")
    uploader.upload("./test.txt")


if __name__ == "__main__":
    test_upload()
