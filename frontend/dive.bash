IMAGE_NAME="${1}"
TMP_FILE=/tmp/dive-tmp-image.tar
docker save "$IMAGE_NAME" > $TMP_FILE && dive $TMP_FILE --source=docker-archive && rm $TMP_FILE
