from selenium_automation import AutoSelenium

def test_navigation():
    auto_selenium = AutoSelenium()
    url = "http://example.com"  # Cambia a una URL válida para pruebas
    auto_selenium.navigate_to(url)
    # Aquí se pueden agregar más aserciones o comprobaciones según sea necesario
    auto_selenium.close()

if __name__ == "__main__":
    test_navigation()
    print("Prueba de navegación completada.")
