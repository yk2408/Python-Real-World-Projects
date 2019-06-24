import re
import time

import imgkit
import requests

# to track execution time
start_time = time.time()

# structured data url
url = 'https://www.atg.world/view-article/29016'

# take the screenshot of the page
imgkit.from_url(url, 'screenshot.png')

# get structred data and retrieve status code and title of the post
req = requests.get(url)
status_code = req.status_code
title_pattern = re.compile(r'"name": "[\w ]+"')
title = title_pattern.findall(req.text)
title_text = title[0].split(':')[1].strip().strip('"')
print('HTTP Status Code: {}'.format(status_code))
print('Title: {}'.format(title_text))

# track total execution time
end_time = time.time()
print('Execution completed in {} sec'.format(end_time - start_time))
