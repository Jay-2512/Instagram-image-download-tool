from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from os import system, name
import os
import wget
import time
class extras:
    def clear(Fore): 
        if name == 'nt': 
            _ = system('cls') 
        else: 
            _ = system('clear') 

        print(Fore.CYAN  + "-"*34)
        print('INSTAGRAM -- IMAGE DOWNLOADER TOOL              -- github.com/Jay-2512')
        print("-"*34)

class cnct:

    def insta_login(uname, passw, browser, keyword):
        if browser == '1':
            path = os.getcwd()
            path = path+'\\web_drivers\\chromedriver.exe'
            driver = webdriver.Chrome(executable_path=path)
            driver.get('https://www.instagram.com/')

            username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
            password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))


            username.clear()
            password.clear()

            username.send_keys(uname)
            password.send_keys(passw)

            log_in =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

            #not save pass

            not_now =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

            #turn off notifications
            noti_off =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click() 

            #search
            search_content = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder= 'Search']")))
            search_content.clear()

            search_content.send_keys(keyword) 
            
            search_content.send_keys(Keys.RETURN)
            time.sleep(2)
            search_content.send_keys(Keys.DOWN)
            time.sleep(1)
            search_content.send_keys(Keys.RETURN)

            time.sleep(10)

            driver.execute_script("window.scrollTo(0,4000);")
            images = driver.find_elements_by_tag_name('img')

            images = [image.get_attribute('src') for image in images]

            time.sleep(10)

            path = os.getcwd()

            path = os.path.join(path, keyword[1:])

            os.mkdir(path)

            counter = 0

            for image in images:
                save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
                wget.download(image, save_as)
                counter += 1

            print("DOWNLOAD COMPLETE CHECK THE DIR : " + path)

        elif browser == '2':
            path = os.getcwd()
            path = path+'\\web_drivers\\geckodriver.exe'
            driver = webdriver.Firefox(executable_path=path)
            driver.get('https://www.instagram.com/')

            username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
            password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))


            username.clear()
            password.clear()

            username.send_keys(uname)
            password.send_keys(passw)

            log_in =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

            #not save pass

            not_now =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

            #turn off notifications
            noti_off =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click() 

            #search
            search_content = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder= 'Search']")))
            search_content.clear()

            search_content.send_keys(keyword) 
            
            search_content.send_keys(Keys.RETURN)
            time.sleep(2)
            search_content.send_keys(Keys.DOWN)
            time.sleep(1)
            search_content.send_keys(Keys.RETURN)

            time.sleep(10)

            driver.execute_script("window.scrollTo(0,4000);")
            images = driver.find_elements_by_tag_name('img')

            images = [image.get_attribute('src') for image in images]

            time.sleep(10)

            path = os.getcwd()

            path = os.path.join(path, keyword[1:])

            os.mkdir(path)

            counter = 0

            for image in images:
                save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
                wget.download(image, save_as)
                counter += 1

            print("DOWNLOAD COMPLETE CHECK THE DIR : " + path)

        else:
            print('Oh! More Browsers will be added soon! :)')

    def fb_login(uname, passw, browser, keyword):
        if browser == '1':
            path = os.getcwd()
            path = path+'\\web_drivers\\chromedriver.exe'
            driver = webdriver.Chrome(executable_path=path)
            driver.get('https://www.instagram.com/')

            click_fb_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='sqdOP yWX7d    y3zKF     ']"))).click()
            
            username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
            password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))  

            username.clear()
            password.clear()

            username.send_keys(uname)
            password.send_keys(passw)

            log_in =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click() 

            #turn off notifications
            noti_off =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click() 

            #search

            search_content = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class ='LWmhU _0aCwM']")))
            search_content.clear()

            search_content.send_keys('alan__v__john') 

            search_content.send_keys(Keys.RETURN)
            time.sleep(2)
            search_content.send_keys(Keys.DOWN)
            time.sleep(1)
            search_content.send_keys(Keys.RETURN)

            time.sleep(10)

            driver.execute_script("window.scrollTo(0,4000);")
            images = driver.find_elements_by_tag_name('img')

            images = [image.get_attribute('src') for image in images]

            time.sleep(10)

            path = os.getcwd()

            path = os.path.join(path, keyword[1:])

            os.mkdir(path)

            counter = 0

            for image in images:
                save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
                wget.download(image, save_as)
                counter += 1

            print("DOWNLOAD COMPLETE CHECK THE DIR : " + path)
        elif browser == '2':
            path = os.getcwd()
            path = path+'\\web_drivers\\geckodriver.exe'
            driver = webdriver.Firefox(executable_path=path)
            driver.get('https://www.instagram.com/')

            click_fb_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='sqdOP yWX7d    y3zKF     ']"))).click()
            
            username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
            password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))  

            username.clear()
            password.clear()

            username.send_keys(uname)
            password.send_keys(passw)

            log_in =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click() 

            #turn off notifications
            noti_off =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click() 

            #search

            search_content = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class ='LWmhU _0aCwM']")))
            search_content.clear()

            search_content.send_keys('alan__v__john') 

            search_content.send_keys(Keys.RETURN)
            time.sleep(2)
            search_content.send_keys(Keys.DOWN)
            time.sleep(1)
            search_content.send_keys(Keys.RETURN)

            time.sleep(10)

            driver.execute_script("window.scrollTo(0,4000);")
            images = driver.find_elements_by_tag_name('img')

            images = [image.get_attribute('src') for image in images]

            time.sleep(10)

            path = os.getcwd()

            path = os.path.join(path, keyword[1:])

            os.mkdir(path)

            counter = 0

            for image in images:
                save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
                wget.download(image, save_as)
                counter += 1

            print("DOWNLOAD COMPLETE CHECK THE DIR : " + path)

        else:
            print('Oh! More Browsers will be added soon! :)')
