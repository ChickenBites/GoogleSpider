from selenium import webdriver
import urllib
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('/home/guy/Git/Web_Scrape/Google/chromedriver')
word="NAture"
url="http://images.google.com/search?q="+word+"&tbm=isch&sout=1"
driver.get(url)
imageXpathSelector='//*[contains(concat( " ", @class, " " ), concat( " ", "tx8vtf", " " ))]'
img=driver.find_element_by_xpath(imageXpathSelector)
src=(img.get_attribute('src'))
urllib.urlretrieve(src, word+".jpg")
driver.close()