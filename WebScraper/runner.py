import requests
import bs4
from WebScraper import Constants, poem_scraper


def write_poets_to_file(poets: list, filename: str):

    for poet in poets:
        print(f"Scraping {poet}")
        current_url = f"{Constants.URL_PREFIX}{Constants.URL_POET}{poet}{Constants.URL_POST}"

        try:
            poem_links = poem_scraper.get_poem_urls(current_url)
        except poem_scraper.UnexpectedResponse as ue:
            print(f"ERROR: {ue.msg} for the poet {poet} at URL: {ue.url}")
            continue
        except Exception as e:
            print(e)
            return

        line_list = []
        for link in poem_links:
            try:
                line_list = line_list + poem_scraper.get_poem_lines(link)
            except poem_scraper.UnexpectedResponse as ue:
                print(f"ERROR: {ue.msg} for the poet {poet} at URL: {ue.url}")
                continue
            except Exception as e:
                print(e)
                return

        clean_lines = poem_scraper.get_clean_poem_lines(line_list)
        poem_scraper.write_poems_to_file(filename, clean_lines, append=True)


if __name__ == "__main__":
    print("Starting to scrape poets...")
    write_poets_to_file(Constants.POETS, "PoetData.txt")

    print("Complete")
