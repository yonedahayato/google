import os
from exec_gcolab import main as exec_gcolab

def main(request):
    url = os.environ["COLAB_URL"]
    login_id = os.environ["GOOGLE_ID"]
    pas = os.environ["GOOGLE_PASS"]

    exec_gcolab(url, login_id, pas)
