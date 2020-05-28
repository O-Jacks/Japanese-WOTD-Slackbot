from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/Users/ollyp/anaconda3/envs/ml-agents/Lib/site-packages/notebook/tests/selenium/chromedriver.exe", chrome_options=options)
