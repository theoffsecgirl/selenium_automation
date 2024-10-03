from selenium_automation import AutoSelenium

if __name__ == "__main__":
    auto_selenium = AutoSelenium()
    url = input("Ingrese la URL donde desea buscar elementos: ")
    auto_selenium.navigate_to(url)

    # Búsqueda de un elemento por su nombre
    element_name = input("Ingrese el nombre del elemento que desea buscar: ")
    try:
        element = auto_selenium.driver.find_element(By.NAME, element_name)
        print(f"Elemento encontrado: {element.get_attribute('outerHTML')}")
    except Exception as e:
        print(f"Error al buscar el elemento: {e}")

    auto_selenium.close()
