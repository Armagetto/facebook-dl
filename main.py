import os
import requests
from urllib.parse import urlparse
from urllib.parse import parse_qs


url = input()

# get video id
parsed_url = urlparse(url)
if 'facebook.com/reel/' in url:
    video_id = parsed_url.path.split('/')[2]
    print('reel')
else:
    video_id = parse_qs(parsed_url.query)['v'][0]
    print('not reel')

print(video_id)
print(parsed_url)


