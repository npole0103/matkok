from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko")
elem = driver.find_element_by_name("q")
elem.send_keys("강아지")
elem.send_keys(Keys.RETURN)

driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[0].click()
#elements 중에서(리스트) 첫번째꺼를 꺼낼거니 [0]을 붙여줌

time.sleep(3) #3초 지연
imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
#큰 사진의 src주소를 새로운 변수에 저장. src주소를 알면 이미지 저장 가능

urllib.request.urlretrieve(imgUrl, "1.jpg")
#사진을 1.jpg라는 이름으로 저장