from selenium.webdriver import Firefox
import time

def SearchUser(namesUsr):

    browser = Firefox()   
    usersFound = []
    usersNotFound = []
    for name in namesUsr:
        browser.get('https://github.com/')      

        time.sleep(2)
        src = browser.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/div/div/div/form/label/input[1]')
        src.send_keys(name)

        time.sleep(2)
        srcBtn = browser.find_element_by_xpath('//*[@id="jump-to-results"]')
        srcBtn.click()

        time.sleep(2)
        resulUsers = browser.find_element_by_xpath('/html/body/div[4]/main/div/div[2]/nav[1]/a[10]/span')

        if resulUsers.text == str(0):
            usersNotFound.append(name)
            time.sleep(1)
        else:
            usersFound.append(name)
            resulUsers = browser.find_element_by_xpath('/html/body/div[4]/main/div/div[2]/nav[1]/a[10]')
            resulUsers.click()

    alert = "alert('Usuários encontrados: {} | Usuários não encontrados: {} ');".format(len(usersFound),len(usersNotFound))
    browser.execute_script(alert)
    
    time.sleep(10)
    browser.quit()

users = ['MichaelDouglasdoAmarante','MichaelDouglasAmarante']
SearchUser(users)
exit()