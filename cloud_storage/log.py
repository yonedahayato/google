import logging
import os
from os import path
import sys

import logzero
from logzero import logger

abspath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(abspath)

import setting
log_save_path = setting.log_save_path

# ログのファイル出力先を設定
if not os.path.exists(log_save_path):
    os.mkdir(log_save_path)

log_file = log_save_path + "/google_cloud_storage.log"
if not os.path.exists(log_file):
    f = open(log_file, "a")
    f.close()

logzero.logfile(log_file)
