from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.3'
desired_caps['deviceName'] = 'Xiaomi HM 1S'
desired_caps['appPackages'] = 'com.oneiter.android.appiumdemoapp'
# desired_caps['deviceName'] = '8696258e'
desired_caps['app'] = '/home/tima/AndroidStudioProjects/AppiumDemoApp/app/build/outputs/apk/app-release-unsigned.apk'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

et_username = driver.find_element_by_id('com.oneiter.android.appiumdemoapp:id/et_username')
# et_username.set_text('First Demo')
et_username.send_keys('First Demo')

# Click Sign In Button
btn_signin = driver.find_element_by_id('com.oneiter.android.appiumdemoapp:id/btn_signin')
btn_signin.click
