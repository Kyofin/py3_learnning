from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

'''
使用python3
selenium调用无头浏览器PhantomJS截长屏幕
'''
br = webdriver.PhantomJS()
br.maximize_window()
# 访问微信读书网页
br.get("https://weread.qq.com/web/reader/cf1320d071a1a78ecf19254ke4d32d5015e4da3b7fbb1fa")

# 页码计数
i = 0
while True:
    # 休眠时间
    time.sleep(4)
    # 截长图
    # 保存地址
    filePath = "/Users/huzekang/Downloads/jvmbook/%(name)s.png" % {'name': str(i)}
    br.save_screenshot(filePath)
    print(filePath)
    # 点击下一章
    try:
        if WebDriverWait(br, 3).until(lambda x: x.find_element_by_xpath(
                '//*[@id="routerView"]/div[1]/div[3]/div/a')):
            print('找到下一章按钮')
            br.find_element_by_xpath(
                '//*[@id="routerView"]/div[1]/div[3]/div/a').click()
        else:
            # 找不到下一章就结束
            break
    except:
        pass
    # 计数加1
    i = i + 1
