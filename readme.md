# Entrega intermedia del Proyecto Final - BASSIN, Walter Daniel 

## Descarga
    Desde una consola o el bash de git usar el siguiente comando
        git clone https://github.com/walterbassin/pizzeria.git


## Instalacion:
    * pip install -r requirements.txt
    * python manage.py migrate
    * python manage.py runserver

## Funcionalidades:

    - NavBar con acceso a los templates principales y búsqueda de productos.

    - Template de Inicio: Bienvenida a Pizza Web.

    - Templates de Pizzas/Empanadas/Bebidas/Postres: Se visualizan en forma de 'cards' las características principales de los productos de cada modelo, ya cargados en la base de datos del proyecto.

    - Cada template del producto cuenta con la funcionalidad de agregar el producto que corresponde.

    - Funcionalidad de agregar producto: Luego de agregado, se muestra una pantalla con una 'card' del producto. En caso de coincidir el nombre exacto del producto ya agregado (respetando mayúsculas y acentos), se muestra un mensaje de error notificando el motivo.

    - Funcionalidad de buscar producto: Muestra los productos encontrados de cada modelo del proyecto (pizza, empanada, bebida y postre). Se agrega en cada tarjeta de producto  encontrado, el nombre del tipo de modelo que corresponde al producto encontrado. En caso de no encontrar producto alguno, se visualiza un mensaje notificando que no se encontró un producto con el texto ingresado. 
