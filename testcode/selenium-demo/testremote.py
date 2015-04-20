from selenium import webdriver

# remoteUrl = "http://172.17.11.187:4444/wd/hub"
remoteUrl = "http://192.168.0.103:4444/wd/hub"

browserType = webdriver.DesiredCapabilities.INTERNETEXPLORER

driver = webdriver.Remote(remoteUrl, browserType)

driver.get("http://www.baidu.com")

