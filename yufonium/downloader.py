import requests


def download(url, filename):
    req = requests.get(url, stream=True)
    with open(filename, "wb") as f:
        for chunk in req.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    return filename


if __name__ == "__main__":
    """Test for the downloader function with Konosuba's wallpaper"""
    download("https://images7.alphacoders.com/782/thumb-1920-782943.png", "konosuba_wall.png")
