from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse
browser = Firefox()
browser.get('http://selenium.dunossauro.live/aula_04_b.html')

def find_by_text(browser, tag, text):
    """Encontrar o elemento com texto `text`
    
    Argumentos:
        - browser = Instancia do browser [Firefox, Chrome, ...]
        - texto = conteúdo que deve estar na tag
        -tag = tag onde o texto será procurado
    """
    elementos = browser.find_elements_by_tag_name(tag)

    for elemento in elementos:
        if elemento.text == text:
            return elemento

sleep(2)

nome_das_caixas = ['um','dois','tres','quatro']

for texto in nome_das_caixas:
    find_by_text(browser, 'div', texto).click()        


for texto in nome_das_caixas:
    sleep(0.3)
    browser.back()  

for texto in nome_das_caixas:
    sleep(0.3)
    browser.forward()


# browser.refresh()
# browser.title

# Captura URL
url_parse = urlparse(browser.current_url)