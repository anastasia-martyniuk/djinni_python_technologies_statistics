import asyncio
from time import time

import inquirer
from httpx import AsyncClient

from analysis import create_statistic_img
from scrape_with_async import scrape


async def main() -> None:
    question = [
        inquirer.List(
            "practice", message="Choose your experience:", choices=[0, 1, 2, 3, 4, 5]
        ),
    ]

    experience = inquirer.prompt(question)["practice"]

    start_time = time()

    async with AsyncClient() as client:
        await asyncio.gather(*[scrape(experience, client)])

    create_statistic_img(experience)

    end_time = time()

    print(f"Elapsed time: {end_time - start_time}")


if __name__ == "__main__":
    asyncio.run(main())
