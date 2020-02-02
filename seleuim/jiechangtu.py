from selenium import webdriver
'''
使用python3
selenium调用无头浏览器PhantomJS截长屏幕
'''
br = webdriver.PhantomJS()
br.maximize_window()
br.get("https://www.cnblogs.com/Jack-cx/p/9383990.html")

br.save_screenshot("/Volumes/Samsung_T5/huzekang/py_code/py-learnning/app2.png")