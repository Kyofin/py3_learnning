from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import time

'''
使用python3
selenium调用无头浏览器PhantomJS截长屏幕
'''


def print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False))


# # 设置请求头
# dcap = dict(DesiredCapabilities.PHANTOMJS)
# dcap["phantomjs.page.settings.userAgent"] = (
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3786.0 Safari/537.36"
# )
# driverver = webdriver.PhantomJS(desired_capabilities=dcap)
driver = webdriver.PhantomJS()

# 必须首先加载网站，这样selenium才知道cookie是属于哪个网站的
driver.get("https://weread.qq.com/web/reader/cf1320d071a1a78ecf19254ke4d32d5015e4da3b7fbb1fa")
# 一旦加载网站，即使没登录，也会产生一个cookie，所以这个cookie被删除了
driver.delete_all_cookies()

# 从文件加载cookie
cookiesFile = '/Volumes/Samsung_T5/huzekang/py_code/py-learnning/selenium_demo/cookies.txt'

with open('%s' % cookiesFile, 'r') as cookief:
    # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
    cookieslist = json.load(cookief)
    print('打印文件加载的cookies:')
    print_json(cookieslist)

    # 这个expiry它是cookie的生命周期，也就是失效时间，为什么在这里会报错呢？我们有两种解决办法
    # 方法1 将expiry类型变为int（其实不太清楚为什么变为int就可以）
    # 方法2删除该字段
    for cookie in cookieslist:
        try:
            # 并不是所有cookie都含有expiry 所以要用dict的get方法来获取
            if isinstance(cookie.get('expiry'), float):
                cookie['expiry'] = int(cookie['expiry'])
            driver.add_cookie(cookie)
            print('加载成功cookie：' + str(cookie))
        except:
            print('加载失败cookie：' + str(cookie))
            pass

print('打印driver加载的cookie:')
print_json(driver.get_cookies())

time.sleep(4)
driver.maximize_window()
# 访问微信读书网页
driver.get("https://weread.qq.com/web/reader/cf1320d071a1a78ecf19254ke4d32d5015e4da3b7fbb1fa")

# 页码计数
i = 0
while True:
    # 休眠时间
    time.sleep(6)
    # 截长图
    # 保存地址
    filePath = "/Users/huzekang/Downloads/jvmbook/%(name)s.png" % {'name': str(i)}
    driver.save_screenshot(filePath)
    print(filePath)
    # 点击下一章
    try:
        if WebDriverWait(driver, 3).until(lambda x: x.find_element_by_xpath(
                '//*[@id="routerView"]/div[1]/div[3]/div/a')):
            print('找到下一章按钮')
            driver.find_element_by_xpath(
                '//*[@id="routerView"]/div[1]/div[3]/div/a').click()
        else:
            # 找不到下一章就结束
            break
    except:
        break
    # 计数加1
    i = i + 1

# 退出循环，关闭
driver.close()
