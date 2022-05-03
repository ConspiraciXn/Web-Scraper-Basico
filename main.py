# Librerias.
from cgitb import text
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Inicializar driver desde caché o instalar (primera vez).
service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

# Constantes.
URL = 'https://www.google.com/' # URL a scrapear.
BUSQUEDA = "Fotos de gatitos."

# Navegar a sitio web.
driver.implicitly_wait(10) # Esperar a que carguen los objetos.
driver.get(URL)


# Ubicar elementos (por name)
barraBusqueda = driver.find_element(By.NAME, 'q')
botonBusqueda = driver.find_element(By.NAME, 'btnK')

# Realizar acciones en el sitio.
barraBusqueda.send_keys(BUSQUEDA)
botonBusqueda.click()

sleep(30)