import json

def canonicalize_url(url):
    try:
        url = url.split('://')[1]
    except IndexError:
        return None
    url = url.split('/')[0]
    url = url.lower().strip()
    return url

def make_is_fake_source():
    """Load the the source file of fake urls, and provide a function which can validate a provided link"""
    with open("fake_sites.json", "r") as f:
        blob = f.read().strip()
    blob.decode("utf-8")
    data = json.loads(blob)
    fake_urls = [datum["siteUrl"].lower().strip() for datum in data]
    #get the roots of the urls
    fake_url_roots = set([canonicalize_url(url) for url in fake_urls])
    def is_fake_source(url):
        root = canonicalize_url(url)
        return root in fake_url_roots
    return is_fake_source

if __name__ == '__main__':
    is_fake_source = make_is_fake_source()
    assert is_fake_source('http://21stcenturywire.com/'), True
    assert is_fake_source('http://shareblue.com/'), True
