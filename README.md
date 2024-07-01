<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README</title>
</head>
<body>

<h1>Proyecto de Automatización de Pruebas con Selenium - Urban Routes</h1>

<h2>Descripción</h2>
<p>Este proyecto está diseñado para automatizar la prueba de la funcionalidad de rutas urbanas de una aplicación web utilizando Selenium WebDriver y Python. El objetivo es asegurar que las funciones críticas, como la selección de direcciones, la elección de tarifas, la introducción de números de teléfono, la adición de tarjetas de crédito y otras interacciones del usuario, funcionen correctamente.</p>

<h2>Estructura del Proyecto</h2>
<pre>
qa-project-Urban-Routes-es/
│
├── main.py
├── data.py
├── README.md
├── .venv/
│   └── ...
└── tests/
    ├── __init__.py
    ├── test_rutas_urbanas.py
    └── ...
</pre>
<ul>
<li><code>main.py</code>: Contiene la implementación principal de las clases y métodos para interactuar con la aplicación web.</li>
<li><code>data.py</code>: Archivo que contiene los datos utilizados en las pruebas.</li>
<li><code>README.md</code>: Este archivo, que proporciona una descripción detallada del proyecto.</li>
<li><code>.venv/</code>: Entorno virtual para la instalación de dependencias.</li>
<li><code>tests/</code>: Directorio que contiene todos los archivos de prueba.</li>
</ul>

<h2>Configuración del Entorno</h2>
<ol>
<li>Clona el repositorio en tu máquina local:
<pre>
<code>git clone &lt;URL_del_repositorio&gt;
cd qa-project-Urban-Routes-es
</code>
</pre>
</li>
<li>Crea y activa un entorno virtual:
<pre>
<code>python -m venv .venv
source .venv/bin/activate  # Para Linux/Mac
.venv\Scripts\activate     # Para Windows
</code>
</pre>
</li>
<li>Instala las dependencias:
<pre>
<code>pip install -r requirements.txt
</code>
</pre>
</li>
</ol>

<h2>Uso</h2>

<h3>Ejecución de las Pruebas</h3>
<p>Para ejecutar las pruebas, usa el siguiente comando:</p>
<pre>
<code>pytest tests/
</code>
</pre>

<h3>Archivos y Métodos Principales</h3>

<h4><code>data.py</code></h4>
<p>Contiene datos importantes para las pruebas:</p>
<pre>
<code>
urban_routes_url = 'https://cnt-4ec61720-b99f-470c-8b8f-af76913acfbd.containerhub.tripleten-services.com?lng=es'
address_from = 'East 2nd Street, 601'
address_to = '1300 1st St'
phone_number = '+1 123 123 12 12'
card_number, card_code = '1234 5678 9100', '111'
message_for_driver = 'Muéstrame el camino al museo'
</code>
</pre>

<h4><code>main.py</code></h4>
<p>Define la clase <code>UrbanRoutesPage</code> con varios métodos para interactuar con la aplicación web y el método <code>retrieve_phone_code</code> para obtener el código de confirmación del teléfono. Algunos métodos clave incluyen:</p>
<ul>
<li><code>set_from(self, from_address)</code>: Introduce la dirección de origen.</li>
<li><code>set_to(self, to_address)</code>: Introduce la dirección de destino.</li>
<li><code>click_boton_pedir_un_taxi(self)</code>: Hace clic en el botón para pedir un taxi.</li>
<li><code>click_boton_confort(self)</code>: Selecciona la tarifa Comfort.</li>
<li><code>set_tel(self, from_phone)</code>: Introduce el número de teléfono.</li>
<li><code>set_numero_de_tarjeta(self, from_card_number)</code>: Introduce el número de tarjeta de crédito.</li>
<li><code>set_card_code(self, from_card_code)</code>: Introduce el código de la tarjeta de crédito.</li>
<li><code>set_agregar_mensaje_conductor(self, from_message_for_driver)</code>: Introduce un mensaje para el conductor.</li>
<li><code>click_switch_input(self)</code>: Solicita una manta y pañuelos.</li>
<li><code>double_click_counter_plus_disabled(self)</code>: Ordena dos helados.</li>
<li><code>click_boton_iniciar_viaje(self)</code>: Inicia el viaje.</li>
<li><code>is_element_present(self, locator)</code>: Verifica si un elemento está presente.</li>
</ul>

<h4><code>tests/test_rutas_urbanas.py</code></h4>
<p>Contiene las pruebas automatizadas que verifican diversas funcionalidades de la aplicación. Algunas pruebas clave incluyen:</p>
<ul>
<li><code>test_01_set_route(self)</code>: Verifica que las direcciones de origen y destino se establezcan correctamente.</li>
<li><code>test_02_select_comfort_tariff(self)</code>: Verifica la selección de la tarifa Comfort.</li>
<li><code>test_03_fill_phone_number(self)</code>: Verifica la introducción del número de teléfono.</li>
<li><code>test_04_add_credit_card(self)</code>: Verifica la adición de una tarjeta de crédito.</li>
<li><code>test_05_write_message_for_driver(self)</code>: Verifica la introducción de un mensaje para el conductor.</li>
<li><code>test_06_request_blanket_and_tissues(self)</code>: Verifica la solicitud de una manta y pañuelos.</li>
<li><code>test_07_order_ice_creams(self)</code>: Verifica la orden de dos helados.</li>
<li><code>test_08_modal_appears_to_search_taxi(self)</code>: Verifica la aparición del modal para buscar un automóvil.</li>
<li><code>test_09_wait_for_driver_info_modal(self)</code>: Espera la aparición del modal con la información del conductor.</li>
</ul>

<h2>Contribuciones</h2>
<p>Las contribuciones son bienvenidas. Para contribuir, sigue estos pasos:</p>
<ol>
<li>Realiza un fork del repositorio.</li>
<li>Crea una nueva rama (<code>git checkout -b feature/nueva-funcionalidad</code>).</li>
<li>Realiza los cambios necesarios y realiza commits (<code>git commit -m 'Añadir nueva funcionalidad'</code>).</li>
<li>Realiza un push a la rama (<code>git push origin feature/nueva-funcionalidad</code>).</li>
<li>Abre un Pull Request.</li>
</ol>

<h2>Licencia</h2>
<p>Este proyecto está licenciado bajo la Licencia MIT.</p>

</body>
</html>
