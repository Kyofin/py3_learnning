import time
from selenium import webdriver

'''
使用python3
selenium调用chrome浏览器使用无头模式截长屏幕
'''

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--dns-prefetch-disable')
options.add_argument('--no-referrers')
options.add_argument('--disable-gpu')
options.add_argument('--disable-audio')
options.add_argument('--no-sandbox')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-insecure-localhost')

driver = webdriver.Chrome(executable_path='/Users/huzekang/opt/chromedriver', options=options)
driver.get('https://weread.qq.com/web/reader/cf1320d071a1a78ecf19254kecc32f3013eccbc87e4b62e')

time.sleep(6)
width = driver.execute_script(
    "return Math.max(document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth);")
height = driver.execute_script(
    "return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
print('width:%s,height:%s' % (width, height))
driver.set_window_size(width + 100, height + 100)
driver.save_screenshot('weixindushu.png')
driver.close()
