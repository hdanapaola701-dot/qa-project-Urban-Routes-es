# 🚗 Proyecto Urban Routes - Pruebas Automatizadas (Sprint 9)

El propósito de este proyecto es aplicar técnicas de automatización de pruebas web utilizando **Selenium WebDriver** y **Pytest**, validando los flujos críticos de usuario dentro de la plataforma de transporte Urban Routes de principio a fin.

---

## 🎯 Objetivo del Proyecto
Validar que todas las funcionalidades críticas de la aplicación móvil y web (desde la configuración de direcciones hasta la confirmación final del viaje) funcionen correctamente mediante pruebas automatizadas estables, reduciendo tiempos en pruebas de regresión.

---

## 🛠️ Tecnologías y Técnicas Utilizadas

* **Python 3.x**: Lenguaje de programación principal de la suite.
* **Selenium WebDriver**: Framework para la automatización de acciones en el navegador.
* **Pytest**: Framework de testing para estructurar, organizar y ejecutar la suite de pruebas.
* **ChromeDriver**: Driver para automatizar y controlar el navegador Google Chrome.
* **WebDriverWait**: Implementación de esperas explícitas para mejorar la estabilidad ante elementos dinámicos.
* **Page Object Model (POM)**: Patrón de diseño para separar la lógica de la UI de los casos de prueba.

### 🏷️ Estrategias de Localización Utilizadas
* `By.ID`
* `By.CLASS_NAME`
* `By.CSS_SELECTOR`
* `By.XPATH` (Consultas jerárquicas y uso de ejes como `ancestor`)

---

## 🧪 Cobertura de Pruebas Automatizadas (`test_main.py`)

La suite ejecuta 9 casos secuenciales que cubren las siguientes funcionalidades con aserciones (`assert`) rigurosas:

1. **`test_1_set_route`:** Configuración y validación de direcciones de origen y destino.
2. **`test_2_seleccionar_tarifa_comfort`:** Apertura del menú y selección de la tarifa Comfort.
3. **`test_3_fill_in_phone_number`:** Flujo de teléfono y recuperación dinámica de código SMS vía helper.
4. **`test_4_payment_method`:** Apertura de sección de pagos, ingreso y validación de datos de tarjeta bancaria.
5. **`test_5_write_a_message_for_the_driver`:** Envío y comprobación de un mensaje personalizado al conductor.
6. **`test_6_order_blanket_and_tissues`:** Activación y verificación booleana de manta y pañuelos.
7. **`test_7_order_two_ice_cream`:** Clics secuenciales y validación del contador dinámico de helados en "2".
8. **`test_8_the_option_to_search_for_a_taxi_appears`:** Confirmación de la solicitud y aparición del modal "Buscar automóvil".
9. **`test_9_waiting_for_driver_information`:** Espera controlada y asignación exitosa de la información del conductor.

---

## 📐 Patrón de Diseño e Interfaz

El proyecto implementa el patrón **Page Object Model (POM)**, permitiendo separar la lógica de interacción de la interfaz de usuario de los casos de prueba lógicos.

Esto facilita:
* Mejor mantenimiento del código ante cambios visuales.
* Reutilización de métodos de interacción.
* Mayor legibilidad y escalabilidad de los scripts.

### 📁 Estructura del Proyecto
```plaintext
qa-project-Urban-Routes-es/
│
├── data.py          # Almacena los datos y variables estáticas de prueba
├── main.py          # Implementación de clases y localizadores (POM)
├── test_main.py     # Suite de 9 casos de prueba automatizados
├── helpers.py       # Método auxiliar para la recuperación del código telefónico SMS
└── README.md        # Documentación general del proyecto
```

---

## 🚀 Instrucciones de Ejecución

### Prerrequisitos
Antes de ejecutar las pruebas, asegúrate de tener instalado:
1. Python 3.x
2. Google Chrome
3. ChromeDriver compatible con tu versión de Chrome

### Instalación de Dependencias
```bash
pip install selenium pytest webdriver-manager
```

### Ejecución de Pruebas
* **Ejecutar toda la suite:**
  ```bash
  pytest
  ```
* **Ejecutar pruebas con salida detallada:**
  ```bash
  pytest -v
  ```

---

## 🧠 Retos Técnicos y Soluciones

* 🧩 **Contadores Dinámicos (Helados):** Los botones carecían de IDs únicos. Se solucionó mediante consultas XPATH complejas y el eje `ancestor` (`//div[text()='Helado']/ancestor::div...`).
* 🛑 **Elementos Bloqueados por Modales:** El botón de pago fallaba por animaciones de la interfaz. Se solucionó inyectando JavaScript directo con `self.driver.execute_script("arguments[0].click();", payment_botton)`.
* ⌛ **Sincronización Dinámica (Código SMS):** Modales fantasmas rompían el flujo. Se dominó el uso de condiciones inversas con `expected_conditions.invisibility_of_element_located`.

---

## 🎯 Conclusión del Proyecto & Lecciones Aprendidas

La automatización de *Urban Routes* consolidó mi transición práctica en la ingeniería de calidad de software. Este proyecto me enfrentó a dificultades reales en la inspección del DOM y la sincronización de interfaces dinámicas, transformando retos de código en lógica de control estructurada mediante el patrón **POM**.

### 🎉 El Resultado Final
A pesar de la complejidad de los selectores, el mayor éxito fue lograr que la suite completa de **9 casos de prueba secuenciales corriera de principio a fin de manera fluida y limpia**. Ver la suite en verde valida la estabilidad de mis scripts, el control de datos de prueba y la efectividad de las esperas explícitas (`WebDriverWait`). Estas bases técnicas me preparan con total seguridad para enfrentar flujos interactivos en industrias dinámicas como el Game QA y las Plataformas de Streaming. 🐌🚀



Objetivo del proyecto

El propósito de este proyecto es aplicar técnicas de automatización de pruebas web utilizando Selenium y Pytest,
validando flujos críticos de usuario dentro de la plataforma Urban Routes.
