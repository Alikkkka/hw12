import json
from config import POST_PATH, UPLOAD_FOLDER
from exceptions import *


def save_picture(picture):
    allowed_types = ["pdf", "jpg", "jpeg", "png"]
    picture_type = picture.filename.split(".")[-1]
    if picture_type not in allowed_types:
        raise WrongImgFile("неверный формат файла")

    picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"
    picture.save(picture_path)
    return picture_path


def add_post(post_list, post):
    post_list.append(post)
    with open(POST_PATH, "w", encoding="utf-8") as file:
        json.dump(post_list, file)
