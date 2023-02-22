import os
import re
from collections import Counter
from urllib.parse import urljoin
from datetime import datetime

import matplotlib as mpl
from PIL import Image
from matplotlib import pyplot as plt

import config


def create_dict_tech() -> dict:
    stop_words = config.stop_words

    with open("text.txt", "r", encoding="utf-8") as file:
        text = file.read()
        text = " ".join(re.findall("[a-zA-Z]+", text))

        words = text.split()

        result = [word for word in words if word not in stop_words]

    most_popular = Counter(result).most_common(10)

    open("text.txt", "w").close()

    return dict(most_popular)


def create_statistic_img(experience: int) -> None:
    mpl.use("TkAgg")  # !IMPORTANT
    dict_technologies = create_dict_tech()

    if not os.path.exists(os.path.join(os.getcwd(), "statistic_img")):
        os.mkdir(os.path.join(os.getcwd(), "statistic_img"))

    os.chdir(os.path.join(os.getcwd(), "statistic_img"))

    techs = list(dict_technologies.keys())
    values = list(dict_technologies.values())

    plt.figure(figsize=(11, 9))
    plt.xticks(rotation="vertical")
    plt.title(f"Python technologies statistics for {experience} years experience")

    plt.bar(techs, values, color="#7eb54e", width=0.4)

    timedate = datetime.now()
    img_path = urljoin(
        os.getcwd(),
        f"{str(timedate.year)}_{str(timedate.month)}_{str(timedate.day)} {str(timedate.hour)}_{str(timedate.minute)}.png",
    )

    plt.savefig(img_path)

    img = Image.open(img_path)
    img.show()


if __name__ == "__main__":
    create_statistic_img(experience=1)
