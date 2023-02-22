import asyncio
from time import time
from urllib.parse import urljoin

import aiofiles as aiofiles
from bs4 import BeautifulSoup
from httpx import AsyncClient

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import config

BASE_URL = config.url


def get_num_pages(soup: BeautifulSoup) -> int:
    pagination = soup.select_one(".pagination")

    if pagination is None:
        return 1

    return int(pagination.select("li")[-2].text)


def get_single_page(soup: BeautifulSoup) -> list:
    vacancies = soup.select(".profile")

    return [i["href"] for i in vacancies]


async def all_items_href(experience: int, client: AsyncClient, url: str = BASE_URL) -> [str]:
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("-lang=uk")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    experience_dict = {
        0: "Без досвіду",
        1: "1 рік",
        2: "2 роки",
        3: "3 роки",
        4: "3 роки",
        5: "5 років",
    }

    experience_button = driver.find_element(By.LINK_TEXT, experience_dict[experience])
    experience_button.click()

    page_source = driver.page_source
    current_url = driver.current_url

    driver.close()

    first_page_soup = BeautifulSoup(page_source, "lxml")
    num_pages =  get_num_pages(first_page_soup)

    all_hrefs = [*get_single_page(first_page_soup)]

    for number_page in range(2, num_pages + 1):
        page = await client.get(current_url, params={"page": number_page})
        soup = BeautifulSoup(page.content, "html.parser")
        all_hrefs.extend(get_single_page(soup))

    return all_hrefs


async def scrape(experience: int, client: AsyncClient) -> None:

    all_hrefs = await asyncio.gather(all_items_href(experience, client))

    for href in all_hrefs[0]:
        position_url = urljoin(BASE_URL, href[6:])

        page = await client.get(position_url)
        soup = BeautifulSoup(page.content, "html.parser")

        main_text = soup.select_one(".profile-page-section").text.lower()

        async with aiofiles.open("text.txt", "a", encoding="utf-8") as f:
            await f.write(main_text.strip())


async def async_scrape():
    async with AsyncClient() as client:
        await asyncio.gather(*[scrape(2, client)])


if __name__ == "__main__":
    start_time = time()
    asyncio.run(async_scrape())
    end_time = time()

    print(f"Elapsed time: {end_time - start_time}")
