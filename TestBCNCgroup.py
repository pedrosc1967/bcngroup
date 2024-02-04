from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configura la ruta del controlador WebDriver, se puede elegir entre Chrome y Firefox
# gecko_driver_path = '/Users/pedrosantangelocalvo/Downloads'
chrome_driver_path = '/Users/pedrosantangelocalvo/Downloads'

# Inicializa el navegador
# driver = webdriver.Firefox()
driver = webdriver.Chrome()

# Abrir la URL de la página web
path = 'https://bcncgroup.com/'
driver.get(path)

try:
    # Acepta las condiciones
    driver.find_element(By.XPATH, "//a[normalize-space()='Accept']").click()

    # Función para extraer el valor de los párrafos dentro de los divs con la clase "text"
    def extract_paragraph_text(section):
        div_elements = driver.find_elements(By.CLASS_NAME, 'text')
        paragraph_texts = []

        for div in div_elements:
            paragraph = div.find_element(By.TAG_NAME, 'p')
            paragraph_texts.append(paragraph.text)

        return paragraph_texts

    # Navega a la sección "HOME"
    home_link = driver.find_element(By.LINK_TEXT, 'HOME')
    driver.execute_script("arguments[0].click();", home_link)

    # Espera a que la página cargue completamente
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Cookie Policy')))

    # Extrae el valor de los párrafos en la sección "HOME"
    home_paragraphs = extract_paragraph_text('HOME')
    print("Párrafos en la sección HOME:", home_paragraphs)

    # Navega a la sección "WHO WE ARE"
    who_we_are_link = driver.find_element(By.LINK_TEXT, 'WHO WE ARE')
    driver.execute_script("arguments[0].click();", who_we_are_link)

    # Espera a que la página cargue completamente
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Cookie Policy')))

    # Extrae el valor de los párrafos en la sección "WHO WE ARE"
    who_we_are_paragraphs = extract_paragraph_text('WHO WE ARE')
    print("Párrafos en la sección WHO WE ARE:", who_we_are_paragraphs)

finally:
    # Cierra el navegador al finalizar las pruebas
    driver.quit()
    print("Hasta la próxima")

