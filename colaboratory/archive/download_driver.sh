FILE_NAME=headless-chromium.zip
FILE_ID=1mwRBDZGZn4ug9JA79EqQNilqhBa6tvuV

cd selenium_helper

curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${FILE_ID}" > /dev/null
CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=${FILE_ID}" -o ${FILE_NAME}

unzip $FILE_NAME
