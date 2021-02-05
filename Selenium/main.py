#Navegadores: Chrome, Firefox
from selenium.webdriver import Firefox
import time

browser = Firefox()
browser.get('https://curso-python-selenium.netlify.app/aula_03.html')

time.sleep(2)

a = browser.find_element_by_tag_name('a')


for click in range(10):
    p = browser.find_elements_by_tag_name('p')
    a.click()
    print(f'Valor do ultimo p: {p[-1].text} valor do click: {click}')

    print(f'Os valores são iguais {p[-1].text == str(click)}')
# browser.quit()
