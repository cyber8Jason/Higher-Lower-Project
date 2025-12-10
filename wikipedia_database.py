import datetime as dt
import random
import requests
from bs4 import BeautifulSoup
import wikipedia

WIKIMEDIA_PAGE_VIEWS = "https://wikimedia.org/api/rest_v1/metrics/pageviews"
TOP = "top"
PER_ARTICLE = "per-article"
PROJECT = "de.wikipedia"
START_DATE = "19700101"
HEADERS = {"User-Agent": "Masterschool SyntaxSquad/1.0"}
FILTER_ELEMENTS = ["/", ".", ":", "special", "spezial", "wikipedia"]


def get_top_titles():
    url = f"{WIKIMEDIA_PAGE_VIEWS}/{TOP}/{PROJECT}/all-access/2024/01/all-days"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise PermissionError()
    data = response.json()
    top_titles = []
    if "items" in data:
        articles = data["items"][0]["articles"]
        for article in articles:
            top_title = article["article"]
            if any(filter_element in top_title.lower() for filter_element in FILTER_ELEMENTS):
                continue
            top_title = top_title.replace("_", " ")
            top_titles.append(top_title)
    return top_titles


def get_random_wikipedia_title(top_titles, excluded=None):
    if not excluded:
        return random.choice(top_titles)

    filtered = [title for title in top_titles if title not in excluded]
    return random.choice(filtered)


def get_page_views(article_title):
    now = dt.datetime.now()
    end_date = f"{now.year + 1}0101"

    url = f"{WIKIMEDIA_PAGE_VIEWS}/{PER_ARTICLE}/{PROJECT}/all-access/all-agents/{article_title}/monthly/{START_DATE}/{end_date}"
    response = requests.get(url, headers=HEADERS)

    if not response.status_code == 200:
        raise ValueError(f"Unable to find page views metric for wikipedia article '{article_title}'.")

    json = response.json()
    items = json.get("items")
    views = 0

    for item in items:
        views += item.get("views")

    return views


def get_random_article(top_titles, excluded=None):
    random_title = get_random_wikipedia_title(top_titles, excluded)
    page_views = get_page_views(random_title)
    return random_title, page_views


def get_geo_datas():
    wikipedia.set_lang("de")
    page = wikipedia.page("Liste_der_Länder_und_Territorien_nach_Einwohnerzahl")

    html = page.html()
    soup = BeautifulSoup(html, 'html.parser')
    table_body = soup.tbody
    table_rows = table_body.find_all("tr")
    geo_datas = []

    for row in table_rows[2:]:
        cols = row.find_all("td")

        if len(cols) >= 3:
            land = cols[1].find_all("a")[1].get_text(strip=True)

            einwohner_str = cols[2].get_text(strip=True)
            einwohner_str = einwohner_str.replace(".", "")
            try:
                einwohner = int(einwohner_str)  # In Integer umwandeln
            except ValueError:
                einwohner = None
            geo_datas.append((land, einwohner))
    return geo_datas


def get_random_country(countries, excluded=None):
    if not excluded:
        return random.choice(countries)

    filtered = [(c, p) for c, p in countries if c not in excluded]
    return random.choice(filtered)


if __name__ == "__main__":
    # article = "New York City"
    # print(f"{article} has {get_page_views(article)} views.")
    # top = get_top_titles()
    # print(top)
    # print(len(top))
    # top_titles = get_top_titles()

    # Test random title
    # titles = []
    # for i in range(100):
    #    title = get_random_wikipedia_title(["Title1", "Title2", "Title3"], excluded=["Title2"])
    #    titles.append(title)
    # print("Title1", len([t for t in titles if t == "Title1"]))
    # print("Title2", len([t for t in titles if t == "Title2"]))
    # print("Title3", len([t for t in titles if t == "Title3"]))

    # Test random country
    # countries = []
    # for i in range(100):
    #    country, population = get_random_country([("DEU", 12), ("USA", 13), ("FR", 2)], excluded=["FR"])
    #    countries.append(country)
    # print("DEU", len([c for c in countries if c == "DEU"]))
    # print("USA", len([c for c in countries if c == "USA"]))
    # print("FR", len([c for c in countries if c == "FR"]))
    pass
