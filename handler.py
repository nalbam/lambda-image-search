import os

from google_images_search import GoogleImagesSearch

GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
GOOGLE_API_SECRET = os.environ["GOOGLE_API_SECRET"]


def search_image(event, context):
    # Parse search query from event
    query = event["query"]

    # Initialize Google Images Search
    gis = GoogleImagesSearch(GOOGLE_API_KEY, GOOGLE_API_SECRET)

    # Define search params
    gis.search({"q": query})

    # Wait for image results
    gis.wait(1)

    # Get first result image url
    result_url = gis.results()[0]["url"]

    # Redirect to result url
    return {
        "statusCode": 302,
        "headers": {"Location": result_url},
    }
