Proyecto del Sprint 9: Urban Routes - Pruebas Automatizadas

 Descripción del proyecto:

Este proyecto contiene pruebas automatizadas para la aplicación web Urban Routes, enfocándose en el flujo completo de
solicitud de taxi. Las pruebas cubren desde la configuración de direcciones hasta la confirmación del viaje, incluyendo
funcionalidades como selección de tarifa, métodos de pago y servicios adicionales.

El objetivo principal es validar que todas las funcionalidades críticas de la aplicación funcionen correctamente mediante
pruebas automatizadas utilizando Selenium WebDriver.


Tecnologías y técnicas utilizadas

* **Python 3.x**: lenguaje de programación principal.
* **Selenium WebDriver**: framework para automatización de navegadores web.
* **Pytest**: framework de testing para ejecutar y organizar las pruebas.
* **ChromeDriver**: driver utilizado para automatizar el navegador Google Chrome.
* **WebDriverWait**: utilizado para implementar esperas explícitas y mejorar la estabilidad de las pruebas.
* **Page Object Model (POM)**: patrón de diseño utilizado para organizar y mantener el código.

Estrategias de localización utilizadas

* `By.ID`
* `By.CLASS_NAME`
* `By.CSS_SELECTOR`
* `By.XPATH`

Funcionalidades automatizadas

Las pruebas automatizadas cubren las siguientes funcionalidades:

* Configuración de dirección de origen y destino.
* Selección de tarifa Comfort.
* Ingreso de número telefónico.
* Agregar método de pago.
* Registro de tarjeta bancaria.
* Envío de mensaje al conductor.
* Solicitud de manta y pañuelos.
* Pedido de helado.
* Confirmación del viaje.

---
 Patrón de diseño utilizado

El proyecto implementa el patrón **Page Object Model (POM)**, permitiendo separar la lógica de interacción con la
interfaz de usuario de los casos de prueba.

Esto facilita:

* Mejor mantenimiento del código.
* Reutilización de métodos.
* Mayor legibilidad.
* Escalabilidad de las pruebas automatizadas.

Estructura del proyecto

```plaintext
qa-project-Urban-Routes-es/
│
├── data.py
├── main.py
├── test_main.py
├── README.md
```
 Archivos principales

* UrbanRoutesPage`: contiene la clase principal y los métodos de interacción con la página.
* `test_main.py`: contiene los casos de prueba automatizados.
* `data.py`: almacena los datos utilizados durante las pruebas.
*helpers.py: contiene un metodo para las pruebas relacionadas con el telefóno
* `README.md`: documentación general del proyecto.


 Instrucciones para ejecutar las pruebas

Prerrequisitos

Antes de ejecutar las pruebas, asegúrate de tener instalado:

1. Python 3.x
2. Google Chrome
3. ChromeDriver compatible con la versión de Chrome instalada

---

## Instalación de dependencias

Ejecuta el siguiente comando para instalar las dependencias necesarias:

```bash
pip install selenium pytest
```

---

Ejecución de pruebas

Ejecutar todas las pruebas

```bash
pytest
```

Ejecutar una prueba específica

```bash
pytest test_main.py
```
 Ejecutar pruebas con salida detallada

```bash
pytest -v
```

 Esperas explícitas

El proyecto utiliza `WebDriverWait` para mejorar la estabilidad de las pruebas automatizadas y evitar errores relacionados con tiempos de carga, renderizado dinámico y animaciones dentro de la aplicación.

Ejemplo:

```python
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(locator)
)



Objetivo del proyecto

El propósito de este proyecto es aplicar técnicas de automatización de pruebas web utilizando Selenium y Pytest,
validando flujos críticos de usuario dentro de la plataforma Urban Routes.
