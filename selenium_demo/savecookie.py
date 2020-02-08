import time
from selenium import webdriver
import json
'''
使用python3
selenium调用chrome进行扫描登录后，将cookie保存到外部文件
'''

driver = webdriver.Chrome('/Users/huzekang/opt/chromedriver')
driver.maximize_window()

# 访问
driver.get("https://weread.qq.com/web/reader/cf1320d071a1a78ecf19254k16732dc0161679091c5aeb1")

# 休眠20s，用微信扫描登录记录cookie
time.sleep(20)

# 保存cookie到外部文件
cookiesFile = '/Volumes/Samsung_T5/huzekang/py_code/py-learnning/selenium_demo/cookies.txt'
with open('%s' % cookiesFile, 'w') as cookief:
    # 将cookies保存为json格式
    print(json.dumps(driver.get_cookies()))
    cookief.write(json.dumps(driver.get_cookies()))
