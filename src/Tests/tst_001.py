'''
Created on 20 sep. 2023

@author: Alejandro

'''
import time
from getch import getch
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException

import unittest


class Test_001(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome() #Abrir Chrome
        self.driver.implicitly_wait(10) #Esperamos 10 segundos para continuar (para que se cargue por completo)
        self.driver.maximize_window() #Maximizamos la ventana
        #Ingresamos en la app de Spotify
        self.driver.get("https://www.spotify.com/ar/signup?forward_url=https%3A%2F%2Fwww.spotify.com%2Far%2Fdownload%2F")
        
        #Email
        email= self.driver.find_element(By.ID, value='email')
        time.sleep(1)
        email.send_keys("Alejandro$7@gmail.com")
        email.send_keys(Keys.RETURN)
       
        #Contraseña:
        contraseña = self.driver.find_element(By.ID, value='password')
        time.sleep(1)
        contraseña.send_keys("Ale!$1234")
        contraseña.send_keys(Keys.RETURN)
        
        #Visibilidad Contraseña:
        time.sleep(1)
        visibilidad = self.driver.find_element(By.XPATH, value='//*[@id="__next"]/main/div/div/form/div[2]/div[3]/div/button')
        visibilidad.click()
        
        #Nombre Usuario:
        nick = self.driver.find_element(By.ID, value='displayname')
        nick.send_keys('User_Alejandro')
        nick.send_keys(Keys.RETURN)
        
        #Día Fecha Nacimiento:
        fecha = self.driver.find_element(By.ID, value='day')
        fecha.send_keys('26')
        fecha.send_keys(Keys.RETURN)
        time.sleep(1)
        
        #Mes Fecha Nacimiento:
        mes = self.driver.find_element(By.XPATH, value= '//*[@id="month"]')
        mes.click()
        time.sleep(1)
        mes_check = self.driver.find_element(By.XPATH, value= '//*[@id="month"]/option[11]')
        mes_check.click()
        
        #Año Fecha de Nacimiento:
        time.sleep(1)
        año = self.driver.find_element(By.XPATH, value='//*[@id="year"]')
        año.send_keys('1994')
        año.send_keys(Keys.RETURN)
        
        #Genero:
        genero = self.driver.find_element(By.XPATH, value='//*[@id="__next"]/main/div/div/form/fieldset/div/div[1]/label/span[2]')
        genero.click()
        
        #Check Publicidad Spotify:
        publicidadSp = self.driver.find_element(By.XPATH, value='//*[@id="__next"]/main/div/div/form/div[5]/div/label/span[2]')
        publicidadSp.click()
        
        #Check Marketing Spotify:
        marketingSp = self.driver.find_element(By.XPATH, value= '//*[@id="__next"]/main/div/div/form/div[6]/div/label/span[2]')
        marketingSp.click()
        
        #Registro:
        registro = self.driver.find_element(By.XPATH, value='//*[@id="__next"]/main/div/div/form/div[7]/div/button/span[1]')
        registro.click()
        
        
        getch()


    def testName(self):
        pass
    
    
    def tearDown(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    
    
    
    