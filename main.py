import requests
from urllib.parse import urlparse
from urllib.parse import parse_qs


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename


cookie = 'this is where the cookie goes'
url = input()

parsed_url = urlparse(url)
if 'facebook.com/reel/' in url:
    video_id = parsed_url.path.split('/')[2]
else:
    video_id = parse_qs(parsed_url.query)['v'][0]

mobile_page_text = requests.get('https://mbasic.facebook.com/watch?v=' + video_id, cookies=cookie).text

download_file(find_between(mobile_page_text, '<a href="/video_redirect/?src=', 'aria-label'))
