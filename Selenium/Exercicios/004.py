from selenium.webdriver import Firefox
from pprint import pprint
from time import sleep

browser = Firefox()
browser.get('https://selenium.dunossauro.live/aula_04.html')

sleep(2)

def getLinks(browser, elemento): # dicionário
    element = browser.find_element_by_tag_name(elemento)
    ancoras = element.find_elements_by_tag_name('a')
    resultado = {}

    for ancora in ancoras:
        resultado[ancora.text] = ancora.get_attribute('href')

    return resultado


pprint(getLinks(browser,'aside'))
pprint(getLinks(browser,'main'))