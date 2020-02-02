from selenium import webdriver

'''
使用python3
selenium调用chrome截当前屏
'''

driver = webdriver.Chrome('/Users/huzekang/opt/chromedriver')
driver.maximize_window()

# 访问
driver.get("https://weread.qq.com/web/reader/cf1320d071a1a78ecf19254k16732dc0161679091c5aeb1")

# 截图（chrome只能截当前屏幕看到的）
driver.save_screenshot("/Volumes/Samsung_T5/huzekang/py_code/py-learnning/app1.png")

# 关闭浏览器
driver.close()
