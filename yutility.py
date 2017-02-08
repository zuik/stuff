import requests

key = "AIzaSyAK76Z9ryYzpjnzDbAMkqAXggcRLkzQ09Y"


def yt_search(query, page_id=None):
    if not page_id:
        r = requests.get("https://www.googleapis.com/youtube/v3/search",params={
            "q": query,
            "key": key, 
            "part":"snippet"})
        return r.json()
    else:
        r = requests.get("https://www.googleapis.com/youtube/v3/search",params={
            "q": query,
            "key": key, 
            "part":"snippet",
            "pageToken": page_id})
        return r.json()

def playlist_data(playlist_id, page_id=None):
    if not page_id:
        r = requests.get("https://content.googleapis.com/youtube/v3/playlistItems",params={
            "playlistId":playlist_id, 
            "key": key, 
            "part":"snippet",
            "maxResults": "50"})
        return r
    else:
        r = requests.get("https://content.googleapis.com/youtube/v3/playlistItems",params={
            "playlistId":playlist_id, 
            "key": key, 
            "part":"snippet",
            "maxResults": "50",
            "pageToken": page_id})
        return r

def all_playlist_data(playlist_id):
    first_page = playlist_data(playlist_id)
    if not first_page:
        print("There is no data")
    else:
        first_page = first_page.json()
        try:
            next_token = first_page['nextPageToken']
        except KeyError as e:
            last_page = True
            return first_page
        else:
            last_page = False
            pages = []
            print(pages)
            pages.append(first_page)
            while(not last_page):
                try:
                    r = playlist_data(playlist_id, next_token)
                    if not r:
                        print("There is no data")
                        return pages
                    else:
                        pages.append(r)
                        next_token = r.json()['nextPageToken']
                except KeyError as e:
                    return pages