from kiroku.db import insert_update
from kiroku.requester import get


class Reddit:
    """
    Encapsulate the Reddit site
    """

    @staticmethod
    def get_new(**kwargs):
        """
        Get the newest threads of the reddit site.
        :return: <list <dict> > List of threads
        """
        threads = _get_newest(None, **kwargs)
        return threads

    @staticmethod
    def get_new_sr(slash_r, **kwargs):
        """
        Get the newest of (a) subreddit
        :param slash_r: [String] Name of the subreddit, after /r/
        :return: <list <dict> > List of threads
        """
        threads = _get_newest("r/{}".format(slash_r), **kwargs)
        return threads

    @staticmethod
    def get_new_domain(domain_name, **kwargs):
        """
        Get the newest threads of a domain
        :param domain_name: Domain name without protocol. E.g. "google.com"
        :return: <list <dict> > List of threads
        """
        threads = _get_newest("domain/{}".format(domain_name), **kwargs)
        return threads


def _get_all(endpoint, limit=100):
    """
    Get the newest threads until we see an old thread in the database.
    :param endpoint: <str> The endpoint, either "r/...", "domain/...", or None. If None, we assumed you mean the
    whole Reddit.
    :param limit: <int> How many items return per page, max 100
    :return: <list <dict>> Newest threads
    """
    after = None
    threads = []
    if endpoint:
        endpoint_url = "{endpoint}/new".format(endpoint=endpoint)
    else:
        endpoint_url = "new"
    new = True
    while new:
        if not after:
            r = get(endpoint_url, params={"limit": limit})
        else:
            r = get(endpoint_url, params={"limit": limit, "after": after})
        for thread in r["data"]["children"]:
            thread["_id"] = thread["data"]["name"]
            threads.append(thread)
            new = insert_update(thread, "reddit")
        after = r["data"]["after"]
    return threads


def _get_newest(endpoint, limit=25, page=1):
    """
    Get the newest threads in a subreddit.
    :param endpoint: <str> The endpoint, either "r/...", "domain/...", or None. If None, we assumed you mean the
    whole Reddit.
    :param limit: <int> How many items return per page, max 100
    :param page: <int> How many pages you want to return. Reddit's API limits us to 1000 items per listing,
    so we can do max 10 pages.
    :return: <list <dict> > Newest threads
    """
    after = None
    threads = []
    if endpoint:
        endpoint_url = "{endpoint}/new".format(endpoint=endpoint)
    else:
        endpoint_url = "new"
    while page > 0:
        page -= 1
        if not after:
            r = get(endpoint_url, params={"limit": limit})
        else:
            r = get(endpoint_url, params={"limit": limit, "after": after})
        for thread in r["data"]["children"]:
            thread["_id"] = thread["data"]["name"]
            threads.append(thread)
        after = r["data"]["after"]
    return threads


def scrape_subreddit(slash_r, limit=100, page=2):
    sr = Reddit.get_new_sr(slash_r, limit=limit, page=page)
    return [insert_update(thread, "reddit") for thread in sr.threads]


def scrape_domain(domain_name, limit=100, page=2):
    dm = Reddit.get_new_domain(domain_name, limit=limit, page=page)
    return [insert_update(thread, "reddit") for thread in dm.threads]


def scrape_site(limit=100, page=2):
    reddit = Reddit.get_new(limit=limit, page=page)
    return [insert_update(thread, "reddit") for thread in reddit.threads]
