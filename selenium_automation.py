from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Definición de colores
VERDE = "\033[92m"
ROJO = "\033[91m"
AMARILLO = "\033[93m"
RESET = "\033[0m"

# Banner ASCII
def banner():
    print(f"{VERDE}\
     _____   _             ___     __    __   ___               ___   _         _ \n\
    |_   _| | |_    ___   / _ \   / _|  / _| / __|  ___   __   / __| (_)  _ _  | |\n\
      | |   | ' \  / -_) | (_) | |  _| |  _| \__ \ / -_) / _| | (_ | | | | '_| | |\n\
      |_|   |_||_| \___|  \___/  |_|   |_|   |___/ \___| \__|  \___| |_| |_|   |_|\n\
    {RESET}")

class AutoSelenium:
    def __init__(self):
        # Mostrar banner
        banner()
        
        # Configuración del navegador
        self.driver = self.setup_driver()

    def setup_driver(self):
        """Configura el controlador de Selenium."""
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Ejecutar en modo headless (sin GUI)
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    def navigate_to(self, url):
        """Navega a la URL especificada."""
        try:
            self.driver.get(url)
            print(f"{AMARILLO}Navegando a {url}...{RESET}")
            time.sleep(2)  # Espera a que la página cargue
        except Exception as e:
            print(f"{ROJO}Error al navegar a {url}: {e}{RESET}")

    def fill_form(self, form_data):
        """Llena un formulario con los datos especificados."""
        try:
            for field_name, value in form_data.items():
                field = self.driver.find_element(By.NAME, field_name)
                field.clear()
                field.send_keys(value)
            print(f"{AMARILLO}Formulario llenado correctamente.{RESET}")
        except Exception as e:
            print(f"{ROJO}Error al llenar el formulario: {e}{RESET}")

    def submit_form(self):
        """Envía el formulario."""
        try:
            submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
            submit_button.click()
            print(f"{AMARILLO}Formulario enviado.{RESET}")
        except Exception as e:
            print(f"{ROJO}Error al enviar el formulario: {e}{RESET}")

    def close(self):
        """Cierra el navegador."""
        self.driver.quit()
        print(f"{AMARILLO}Navegador cerrado.{RESET}")

if __name__ == "__main__":
    auto_selenium = AutoSelenium()
    
    # Ejemplo de uso
    url = input(f"{AMARILLO}Ingrese la URL a la que desea navegar: {RESET}")
    auto_selenium.navigate_to(url)

    # Datos del formulario (ejemplo)
    form_data = {
        "username": "tu_usuario",
        "password": "tu_contraseña"
    }
    
    auto_selenium.fill_form(form_data)
    auto_selenium.submit_form()
    auto_selenium.close()
