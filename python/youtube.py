#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

url = "https://www.youtube.com/user/muse/videos"

# Initialize WebDriver
driver_path = './chromedriver.exe'
driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get(url)

idx = 1

img_xpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer['+str(idx)+']/div[1]/ytd-thumbnail/a/yt-img-shadow/img'
title_xpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer['+str(idx)+']/div[1]/div[1]/div[1]/h3/a'

image = WebDriverWait(driver, 20).until(Ec.presence_of_all_elements_located((By.XPATH, img_xpath)))

if image is None:
    print('image is None:', idx)
    exit(0)

driver.execute_script('window.scrollBy(0, 1080)')

image = driver.find_element_by_xpath(img_xpath)
image_url = image.get_attribute('src')
print('image_url:', image_url)

"""
import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/user/muse/videos?view=0&sort=dd&shelf_id=0"
channel = "muse"

result = requests.get(url)
soup = BeautifulSoup(result.content, "html.parser", from_encoding="utf-8")
"""
