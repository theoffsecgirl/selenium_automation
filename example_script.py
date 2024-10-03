from selenium_automation import AutoSelenium

if __name__ == "__main__":
    auto_selenium = AutoSelenium()
    url = input("Ingrese la URL a la que desea navegar: ")
    auto_selenium.navigate_to(url)
    auto_selenium.close()
