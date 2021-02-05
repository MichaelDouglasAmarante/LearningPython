from selenium.webdriver import Firefox
import time
import re

browser = Firefox()

browser.get('https://curso-python-selenium.netlify.app/exercicio_02.html')
time.sleep(2)

a = browser.find_element_by_tag_name('a')
numEsperado = browser.find_element_by_xpath('/html/body/p[2]')
numEsperado = re.sub('[^0-9]','',numEsperado.text)

p = browser.find_elements_by_tag_name('p')

while True:
    a.click()
    p = browser.find_elements_by_tag_name('p')
    if re.sub('[^0-9]','',p[-1].text) == str(numEsperado):
        break
