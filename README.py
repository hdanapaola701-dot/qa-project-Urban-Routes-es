# 🚗 Proyecto Urban Routes - Pruebas Automatizadas (Sprint 9)

Urban Routes es una plataforma integral diseñada para la planificación de movilidad urbana y la gestión de logística, permitiendo a los usuarios gestionar viajes y entregas en una interfaz unificada. Sus funcionalidades clave incluyen la configuración de perfiles, un selector modular de tarifas, reserva de vehículos en tiempo real, gestión de pagos y persistencia de datos para asegurar la consistencia del servicio. Para más detalles técnicos, consulte la documentación del proyecto Urban Routes.

El sistema integra funcionalidades de planificación de rutas con la solicitud de taxis, ofreciendo opciones avanzadas como la selección de tarifas, comunicación con el conductor y la inclusión de artículos adicionales durante el viaje.

---

## 🎯 Objetivo del Proyecto

Validar que todas las funcionalidades críticas de la aplicación web (desde la configuración de direcciones hasta la confirmación final del viaje) funcionen correctamente mediante pruebas automatizadas estables, reduciendo tiempos en pruebas de regresión.

---

## 🦹 Alcance de las pruebas

Las pruebas cubren el flujo completo de reserva de un taxi, incluyendo:

📍 **Configuración de la ruta**
* Ingreso de dirección en los campos "Desde" y "Hasta".
* Validación de campos y visualización de puntos en el mapa cuando las direcciones son válidas.
* Verificación de comportamiento ante datos válidos e inválidos y eliminación automática de espacios innecesarios.

Selector **Modos de ruta y tarifas**
* Selección automática de la mejor combinación de transporte en función del tiempo y costo (Óptimo, Flash y Comfort).
* Validación de actualización dinámica de opciones disponibles según el modo seleccionado.

🔐 **Autenticación del usuario**
* Ingreso de número telefónico en la interfaz.
* Captura automática del código SMS mediante logs del navegador y helpers dinámicos.
* Validación del flujo de verificación e ingreso de código en el sistema.

💳 **Gestión de pago**
* Adición de tarjeta de crédito (ingreso de datos de tarjeta bancaria).
* Validación de formularios y almacenamiento seguro de datos en la pasarela.

💬 **Interacción con el conductor**
* Envío de mensajes personalizados y comprobación de persistencia de la información en pantalla.

🧳 **Servicios adicionales y confirmación**
* Selección de artículos extra en el viaje como Mantas, Pañuelos y Helados (incluyendo validación del contador de cantidad).
* Confirmación del servicio con la aparición del modal de búsqueda de taxi ("Buscar automóvil").
* Espera controlada, verificación de la asignación del conductor y validación de la información mostrada al usuario.

---

## 🟣 Lógica de funcionamiento

* En el estado inicial, los campos de dirección están vacíos y las opciones adicionales se encuentran desactivadas.
* La ruta solo se genera cuando ambos puntos (origen y destino) son válidos dentro de la plataforma.
* En modos automáticos (Óptimo y Flash), el sistema decide el transporte de manera autónoma; en modo Personal, el usuario tiene control total sobre la configuración.
* Cualquier cambio en los datos del formulario provoca la actualización dinámica de la ruta, el tiempo estimado y el costo del viaje.
* La adición de elementos extra actualiza síncronamente el precio total antes de la confirmación del servicio.
* La asignación del conductor interrumpe el estado de búsqueda y transiciona de forma limpia a la pantalla de información del chofer.

## 🪶 Contenido del Proyecto

Este proyecto contiene la automatización de pruebas end-to-end (E2E) para la aplicación Urban Routes, enfocada en validar el flujo completo de solicitud de un servicio de taxi y sus funcionalidades asociadas.

El objetivo principal es garantizar que la aplicación funcione correctamente desde la perspectiva del usuario, validando tanto la interacción con la interfaz como la correcta ejecución de la lógica de negocio en cada etapa del proceso.

### 📁 Estructura de Archivos
```plaintext
qa-project-Urban-Routes-es/
│
├── data.py          # Almacena los datos del usuario y variables estáticas de prueba
├── main.py          # Implementación de clases de páginas y localizadores (POM)
├── test_main.py     # Suite con los 9 casos de prueba automatizados
├── helpers.py       # Método auxiliar para la recuperación del código telefónico SMS
└── README.md        # Documentación general y guía del proyecto
```

## 🧩 Tecnologías y Herramientas

* **Lenguaje:** Python 3.x
* **Framework de testing:** Pytest
* **Automatización:** Selenium WebDriver
* **Patrón de diseño:** Page Object Model (POM) para separar la lógica de la UI de los casos de prueba.
* **Gestión de datos:** Diccionarios centralizados y archivos de configuración independientes (`data.py`).
* **Logs y debugging:** Performance Logs del navegador para captura dinámica de eventos (como códigos SMS).

### 🏷️ Estrategias de Localización Utilizadas
* `By.ID` y `By.CLASS_NAME` para elementos estáticos comunes.
* `By.CSS_SELECTOR` para búsquedas estructurales de interfaz de usuario.
* `By.XPATH` (Consultas jerárquicas avanzadas y uso de ejes como `ancestor` para elementos dinámicos).

---

## 🪄 Enfoque de testing

Se utiliza un enfoque de automatización E2E, simulando el comportamiento real del usuario en la aplicación desde el navegador Chrome.

Incluye:
* Interacción directa con los elementos de la interfaz mediante Selenium.
* Uso de Page Object Model (POM) para estructurar el código de manera limpia y escalable.
* Implementación de esperas explícitas (`WebDriverWait`) para manejar asincronías sin recurrir a pausas inestables.
* Captura de datos dinámicos (como códigos SMS de verificación) desde logs del navegador en tiempo real.

## ⚡ Aspectos destacados

* **Cobertura completa:** Cobertura del 100% del flujo principal (9/9 escenarios secuenciales ejecutados limpiamente).
* **Ejecución eficiente:** Suite optimizada con tiempos de respuesta ágiles (~11 segundos totales de ejecución).
* **Alta mantenibilidad:** Arquitectura desacoplada gracias al patrón POM, facilitando actualizaciones ante cambios visuales en el DOM.
* **Automatización robusta:** Scripts estables desarrollados sin dependencias de tiempos fijos o comandos inestables (`sleep`).

## 🎯 Objetivo

Garantizar que la experiencia de usuario en Urban Routes sea fluida, confiable y libre de errores, validando cada punto crítico del proceso de solicitud de transporte mediante pruebas automatizadas escalables.

---

## 🚀 Instrucciones de Ejecución

### Prerrequisitos
Antes de ejecutar las pruebas, asegúrate de contar con:
1. Python 3.x instalado en tu sistema.
2. Google Chrome instalado.
3. ChromeDriver compatible con tu versión de Chrome (gestionado automáticamente).

### Instalación de Dependencias
Ejecuta el siguiente comando en tu terminal para preparar el entorno:
```bash
pip install selenium pytest webdriver-manager
```

### Ejecución de la Suite
* **Ejecución estándar:**
  ```bash
  pytest
  ```
* **Ejecución con salida detallada (Verbose):**
  ```bash
  pytest -v
  ```

---

## 🧠 Retos Técnicos y Soluciones

* 🧩 **Contadores Dinámicos (Helados):** Los botones carecían de identificadores únicos. Se solucionó mediante consultas XPATH complejas utilizando el eje `ancestor` (`//div[text()='Helado']/ancestor::div...`).
* 🛑 **Elementos Bloqueados por Modales:** El botón de pago fallaba debido a superposiciones de animaciones de la interfaz. Se solucionó inyectando JavaScript directo con `self.driver.execute_script("arguments.click();", payment_button)`.
* ⌛ **Sincronización Dinámica (Código SMS):** Modales transitorios rompían el flujo asincrónico. Se dominó el uso de condiciones inversas con `expected_conditions.invisibility_of_element_located`.

---

## 🏅 Conclusión y Lecciones Aprendidas

La automatización de *Urban Routes* consolidó mi transición práctica en la ingeniería de calidad de software. Este proyecto me enfrentó a dificultades reales en la inspección del DOM y la sincronización de interfaces dinámicas, transformando retos de código en lógica de control estructurada mediante el patrón **POM**.

El mayor éxito fue lograr que la suite completa de **9 casos de prueba secuenciales corriera de principio a fin de manera fluida, limpia y en verde**. Ver la suite exitosa valida la estabilidad de mis scripts, el control de datos de prueba y la efectividad de las esperas explícitas. Estas bases técnicas me preparan con total seguridad para enfrentar flujos interactivos en industrias dinámicas como el Game QA y las Plataformas de Streaming. 🐌🚀


La automatización de *Urban Routes* consolidó mi transición práctica en la ingeniería de calidad de software. Este proyecto me enfrentó a dificultades reales en la inspección del DOM y la sincronización de interfaces dinámicas, transformando retos de código en lógica de control estructurada mediante el patrón **POM**.

El mayor éxito fue lograr que la suite completa de **9 casos de prueba secuenciales corriera de principio a fin de manera fluida, limpia y en verde**. Ver la suite exitosa valida la estabilidad de mis scripts, el control de datos de prueba y la efectividad de las esperas explícitas. Estas bases técnicas me preparan con total seguridad para enfrentar flujos interactivos en industrias dinámicas como el Game QA y las Plataformas de Streaming. 🐌🚀
