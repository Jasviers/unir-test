# Memoria Actividad 2: Automatización de pruebas con Python

La actividad propone el desarrollo de una calculadora y la batería de test unitarios y de API para esta.
Se sigue la base de [https://github.com/jafraileni/unir-test](https://github.com/jafraileni/unir-test) implementando
la funcionalidad faltante de la calculadora, los endpoints correspondientes de la API y para el dominio, los test unitarios
y los test de API para cada endpoint.

## Desarrollo de las funcionalidades

En el fichero calc.py se ha desarrollado el dominio se pedía implementar métodos para el cálculo de suma, resta, multiplicación, división, potenciación, raíz cuadrada y logaritmo en base 10, algunas de estas funcionalidades ya estaban implementadas. También se
han contemplado los casos de fallo más comunes para cada operación, como la division por 0 ó las raíces cuadradas negativas, en estos casos
de fallo siempre se lanza un error (TypeError); en todos los casos se comprueba con la función auxiliar "check_type" o  "check_types" el los valores de entrada
sean enteros o decimales.
Para las operaciones básicas se ha utilizado directamente el conjunto de instrucciones de Python
mientras para algunas más avanzadas, la librería por defecto de operaciones matemáticas "math".

En el caso de desarrollo de la API, en el fichero api.py, se han implementado los correspondientes métodos para que cada funcionalidad de la calculadora tenga un endpoint.
La API utiliza la librería de flask que permite definir en un decorador por cada función el path y el metodo CRUD para los recursos. En todos los casos se utiliza el método GET
con un primer path llamado "/calc" que indica la calculadora, un segundo path para indicar la operación, por ejemplo "/add" o "/divide", y por último uno o dos paths que indican los
valores a calcular. Las funciones se encargan de transformar los valores a enteros o decimales, realizar el calculo correspondiente y retornar la respuesta. La respuesta consistirá en el resultado de la operación, junto al código http "ok" y las cabeceras, en caso de error manda en mensaje, el código http de "bad request" y las cabeceras.

## Desarrollo y ejecución de los test unitarios

Para la implementación de los test unitarios se ha intentado cubrir la mayor cantidad de líneas de código posibles obteniendo una cobertura mayor al 90% y buscando
comprobar tanto los casos de acierto como de fallo. Se ha utilizado la librería unit test de python junto a la librería de pytest que permite realizar de forma sencilla sets de pruebas
tiene funcionalidades para realizar mocks, aunque solo se ha usado para la comprobación de permisos de multiply. Para el "happy path" se ha intentado verificar con una variedad
de números tanto positivos como negativos en todos los casos posibles. Para los casos de fallo se han comprobado todos los fallos por uso de valores que no son números enteros o decimales
y en las operaciones que tienen casos especiales como la división por 0 se ha comprobado que al realizar ese tipo de operaciones se obtenía un fallo.

Como se mencionaba para la ejecución de las pruebas y obtener los informes de resultados primero se usa "make build" para crear un contenedor y después se procede con un "make test-unit" que tiene configurado utilizar el módulo pytest de python para realizar las pruebas unitarias y luego generar un informe CML con la cobertura y la información de cada test, y otra ejecución para generar el formato HTML.

El set de pruebas podría ser más exhaustivo comprobando también más casos como operaciones con decimales o pruebas de precisión en el cálculo, casos límites como números que rocen el tamaño máximo de los enteros, entre otras pruebas posibles.

## Desarrollo y ejecución de los test de API

De forma similar a los test unitarios se han implementado pruebas para todos los endpoints de la API tanto para casos de fallo como de funcionamiento correcto. Para las pruebas se hacen peticiones de API con la librería httpclient y pytest, por lo que será necesario tener desplegado el servicio antes de probarlo, con el makefile se consigue desplegar un contenedor antes de lanzar las pruebas. Para el desarrollo de los casos de acierto, se comprueba el estado de la respuesta asegurando que el valor sea un ok y en los casos de fallo al contrario se espera que salte una excepción con la respuesta de "bad request" en la respuesta.

Con el "make build" se genera una imagen con la API, el comando "make test-api" permite levantantar un contenedor que ejecute la API con el dominio apiserver en el puerto 5000, posteriormente ejecuta la batería de pruebas contra el servicio desplegado y se encarga de una vez finalizadas las pruebas destruir los recursos y dejar un informe en la carpeta results.

El set de pruebas se podría ampliar de forma similar al de los test unitarios con más casos de calculos concretos. También al tratarse de una API se pueden contemplar casos como
llamar con metodos CRUD no implementados y verificar que falla la llamada.

---

**Autor:** Javier Antonio Román López

**Asignatura:** Entornos de integración y entrega continua

**Fecha:** 02 de noviembre de 2025
