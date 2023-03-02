import os

from google_images_search import GoogleImagesSearch

GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
GOOGLE_API_SECRET = os.environ["GOOGLE_API_SECRET"]


def search_image(event, context):
    print("search_image: {}".format(event))

    # Parse search query from event
    query_params = event.get("queryStringParameters", {})
    q = query_params.get("q")

    print("search_image: {}".format(q))

    # Initialize Google Images Search
    gis = GoogleImagesSearch(GOOGLE_API_KEY, GOOGLE_API_SECRET)

    _search_params = {
        "q": q,
        "num": 1,
        # "fileType": "jpg|gif|png",
        # "rights": "cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived",
    }

    # Define search params
    gis.search(search_params=_search_params)

    # Wait for image results
    gis.wait(1)

    # Get first result image url
    result_url = gis.results()[0]["url"]

    print("search_image: {}".format(result_url))

    # Redirect to result url
    return {
        "statusCode": 302,
        "headers": {"Location": result_url},
    }
