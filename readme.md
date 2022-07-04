# Entrega del Proyecto Final - BASSIN, Walter Daniel 

## Descarga
    Desde una consola o el bash de git usar el siguiente comando en una carpeta nueva:
        git clone https://github.com/walterbassin/EntregaFinal-BASSIN.git
    

## Instalacion:
    * Acceder a 'EntregaFinal-BASSIN.git'
    * pip install -r requirements.txt
    * python manage.py migrate
    * python manage.py runserver

## Funcionalidades:

    - NavBar con acceso a los templates principales y búsqueda de productos.

    - Template de Inicio: Con fotos de portada y descripción. Al final de la portada, se cuenta con un acceso al "Acerca de mí'.

    - Templates de Pizzas/Empanadas/Bebidas/Postres: Se visualizan en forma de 'cards' las características principales de los productos de cada modelo, (incluyendo foto) ya cargados en la base de datos del proyecto.

    - Detalle de Productos: En cada producto se visualiza un botón para acceder al detalle. Para acceder al detalle, hay que estar logueado en el sistema. Si el usuario es 'superuser', se brinda la posibilidad de editar y eliminar el producto.
    Para el caso que no sea 'superuser', se muestra un botón de 'comprar'(sin acceso posterior).

    - Cada template del producto cuenta con la funcionalidad de agregar el producto que corresponde.

    - Funcionalidad de agregar producto: Luego de agregado, se muestra una pantalla con una 'card' del producto. En caso de coincidir el nombre exacto del producto ya agregado, se muestra un mensaje de error notificando el motivo.

    - Funcionalidad de buscar producto: Muestra los productos encontrados de cada modelo del proyecto (pizza, empanada, bebida y postre). Se agrega en cada tarjeta de producto  encontrado, el nombre del tipo de modelo que corresponde al producto encontrado. En caso de no encontrar producto alguno, se visualiza un mensaje notificando que no se encontró un producto con el texto ingresado. 

    - Perfil de Usuario: Con acceso en el Navbar, se puede hacer login, logout y register.  Cuenta también con foto de perfil en el Navbar, con una foto por defecto en caso que no tenga foto el usuario. También se puede modificar el perfil de usuario (cualquier dato menos el nombre de usuario) haciendo click en el nombre de usuario de la Navbar. 

    - Modificación de fotos y descripción de la portada. Si el usuario es 'superuser', se muestran botones de 'Editar' en cada una de las portadas. 
