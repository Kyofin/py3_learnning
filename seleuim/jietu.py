import json
import time
from selenium import webdriver

'''
使用python3
selenium调用chrome截当前屏
写出登录后的cookie到文件
'''

driver = webdriver.Chrome('/Users/huzekang/opt/chromedriver')
driver.maximize_window()


# 访问
driver.get("https://weread.qq.com/web/reader/cf1320d071a1a78ecf19254k16732dc0161679091c5aeb1")


# 截图（chrome只能截当前屏幕看到的）
driver.save_screenshot("/Volumes/Samsung_T5/huzekang/py_code/py-learnning/app1.png")

# 休眠20s，用微信扫描登录记录cookie
time.sleep(20)

# 保存cookie到外部文件
cookiesFile = '/Volumes/Samsung_T5/huzekang/py_code/py-learnning/seleuim/cookies.txt'
with open('%s' % cookiesFile, 'w') as cookief:
    # 将cookies保存为json格式
    print(json.dumps(driver.get_cookies()))
    cookief.write(json.dumps(driver.get_cookies()))

# 关闭浏览器
driver.close()
