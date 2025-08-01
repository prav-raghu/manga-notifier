import requests

def get_latest_chapter(title):
    search = requests.get("https://api.mangadex.org/manga", params={"title": title}).json()
    if not search["data"]:
        return None

    manga_id = search["data"][0]["id"]
    ch_res = requests.get("https://api.mangadex.org/chapter", params={
        "manga": manga_id,
        "translatedLanguage[]": "en",
        "order[chapter]": "desc",
        "limit": 1
    }).json()

    if not ch_res["data"]:
        return None

    ch = ch_res["data"][0]
    return {
        "id": ch["id"],
        "title": title,
        "number": ch["attributes"].get("chapter", "?"),
        "url": f"https://mangadex.org/chapter/{ch['id']}"
    }
