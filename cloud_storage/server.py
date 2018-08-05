import tornado.ioloop
import tornado.web

import log
import setting
from uploader import Google_Cloud_Storage

logger = log.logger
port = setting.port

class UploadHander(tornado.web.RequestHandler):
    def post(self):
        msg = "[UploadHander:post]: {}"

        try:
            file_path = self.get_argument("file_path")
            gcs = Google_Cloud_Storage()
            gcs.upload(file_path)
        except Exception as e:
            err_msg = msg.format("fail to upload {}, {}".format(file_path, e))
            logger.exception(err_msg)
            logger.error(err_msg)
            raise Exception(err_msg)
        else:
            sccs_msg = msg.format("success to upload {}".format(file_path))
            logger.info(sccs_msg)

        self.write("success\n")

class DownloadHandler(tornado.web.RequestHandler):
    def post(self):
        msg = "[DownloadHandler:post]: {}"

        try:
            file_path = self.get_argument("file_path")
            gcs = Google_Cloud_Storage()
            gcs.download(file_path)
        except Exception as e:
            err_msg = msg.format("fail to download {}, {}".format(file_path, e))
            logger.exception(err_msg)
            logger.error(err_msg)
            raise Exception(err_msg)
        else:
            sccs_msg = msg.format("success to download {}".format(file_path))
            logger.info(sccs_msg)

        self.write("success\n")

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        logger.info("[TestHandler:get]: test message")
        self.write("test\n")

class Server:
    def __init__(self):
        self.application = tornado.web.Application(
            [
                (r"/upload", UploadHander),
                (r"/test", TestHandler),
                (r"/download", DownloadHandler)
            ]
        )
        self.port = port

    def start(self):
        msg = "[Server:start]: {}"
        self.application.listen(self.port)
        print(msg.format("server is up ..."))
        tornado.ioloop.IOLoop.instance().start()



if __name__ == "__main__":
    server = Server()
    server.start()
