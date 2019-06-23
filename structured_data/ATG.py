import re
import time

import requests
from selenium import webdriver

# to track execution time
start_time = time.time()

# structured data url
url = 'https://www.atg.world/view-article/29016'

# take the screenshot of the page
driver = webdriver.Chrome()
driver.get(url)
driver.execute_script("window.scrollTo(0, 500)")
driver.save_screenshot("screenshot.png")
driver.close()

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
