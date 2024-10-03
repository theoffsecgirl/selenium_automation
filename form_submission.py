from selenium_automation import AutoSelenium

if __name__ == "__main__":
    auto_selenium = AutoSelenium()
    url = input("Ingrese la URL del formulario: ")
    auto_selenium.navigate_to(url)

    # Datos del formulario (ejemplo)
    form_data = {
        "username": "tu_usuario",
        "password": "tu_contraseña"
    }
    
    auto_selenium.fill_form(form_data)
    auto_selenium.submit_form()
    auto_selenium.close()
