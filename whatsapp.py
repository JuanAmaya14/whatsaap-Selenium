#importa selenium que es el encargado de hacer la automatizacion

from time import sleep
import unittest
from selenium import webdriver


name = input('Nombre de contacto o grupo: ') #Pedir nombre del un grupo o contacto (no se puede con caracteres especiales como emojis)


#clase de pasos a seguir
class SendMessage(unittest.TestCase):
    
    def setUp(self): #funcion encargada de ejecutar chromedriver y direccionar a la pagina
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe') #declara la variable driver
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window() #abre la ventana completa
        driver.get('https://web.whatsapp.com/') #entra a la pagina indicada
        

    def test_find_chat_and_seen_text(self): #funcion de lo que tiene que hacer en esa pagina    
        driver = self.driver

        sleep(10) #espera mientras escaneas el codigo QR 

        #busca el contacto o grupo que pusiste anteriormente
        chat = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        self.assertTrue(chat.is_enabled()) #verifica que este habilitado
        chat.click() #le da click al primer chat que encuentra

        Encontrado = 0

       
        #Busca la barra para escribir el mensaje
        Text = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')     
        Text.click()
        Text.send_keys('this message was sent by Selenium in python') #En esa misma barra escribe el texto

        #busca el boton para enviar el mensaje
        send = driver.find_element_by_class_name('_4sWnG')
        

        sleep(3) #espera

        self.assertTrue(send.is_enabled()) #verifica que el boton para enviar este habilitado
        send.click() #Le da click al boton de enviar

        sleep(3) #espera

    #funcion para acabar el proceso
    def tearDown(self):
        self.driver.quit()


#comienza todo el codigo
if __name__ == "__main__":
    unittest.main(verbosity=2)