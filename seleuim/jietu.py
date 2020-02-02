from selenium import webdriver
'''
使用python3
selenium调用chrome截当前屏
'''
br = webdriver.Chrome('/Users/huzekang/opt/chromedriver')
br.maximize_window()
br.get("https://www.cnblogs.com/Jack-cx/p/9383990.html")

br.save_screenshot("/Volumes/Samsung_T5/huzekang/py_code/py-learnning/app1.png")