# Resolución de la prueba técnica

## Componentes de la aplicación

- Base de datos gestionada por Django
- La app 'core', restiona los enlaces generales para para la pantalla de inicio '/'
- La app 'productos' gestiona el modelo e incluye vistas en el endpoint 'productos/' para administrar los productos ingresados
- La app 'registrousuarios', permite crear cuentas de usuarios, e incluye un login en el servidor web para ingresar a la panel de administración para administrar la sección de productos, así como restauración de contraseña 
- Para la restauración de la contraseña se envia un email con en enlace para hacerlo utiliza un correo de prueba, ssi se quiere utilizar un correo rreal, es necesario ingresar las credenciales
- La app 'api' se utiliza para la integración de la api rest, para el modelo productos, en la url 'api/v1', la api utliza un autenticación por medio de token, permite tambien el registro de usuarios, el login y logout para poder interactuar con la API

- Cuando se crea el usuario este inicia con un saldo de $ 1000

- La documentación de la api se encuentra en el siguiente enlace
  https://app.swaggerhub.com/apis/SigfridoO/Prueba/1.0.0

### Creación de usuarios

- auth/registration/
- auth/login/
- auth/logout/

+ curl -X POST http://127.0.0.1:8000/api/v1/auth/registration/ -d "password1=holamundo1234&password2=holamundo1234&email=correo1@correo.com"
+ curl -X POST http://127.0.0.1:8000/api/v1/auth/login/ -d "password=holamundo1234&email=correo1@correo.com" 
+ curl -X POST http://127.0.0.1:8000/api/v1/auth/logout/

### Perfil de usuario
+ curl -X GET http://127.0.0.1:8000/api/v1/profile/ -H "Authorization: Token 25eeee5809784e3896143e4191656d810ede4219" -d "id=1"

### Productos
+ curl -X GET http://127.0.0.1:8000/api/v1/productos/

+ curl -X POST http://127.0.0.1:8000/api/v1/productos/ -d "nombre=computadora2&descripcion=computadora+de+escritorio&precio=200.00&categoria=Electronica&cantidad=3&usuario=1&"

+ curl -X GET http://127.0.0.1:8000/api/v1/productos/1/

+ curl -X PUT http://127.0.0.1:8000/api/v1/productos/1/ -d "nombre=camisa&descripcion=camisa+roja&precio=50.00&categoria=Abarrotes&cantidad=5&usuario=1&"

+ curl -X DELETE http://127.0.0.1:8000/api/v1/productos/1/


### Operacion de compra

curl -X POST http://127.0.0.1:8000/api/v1/operacion-de-compra -H "Authorization: Token 25eeee5809784e3896143e4191656d810ede4219" -d "id=1&idproducto=1&cantidad=3&operacion=compra"


curl -X POST http://127.0.0.1:8000/api/v1/operacion-de-compra -H "Authorization: Token 25eeee5809784e3896143e4191656d810ede4219" -d "id=1&idproducto=2&cantidad=3&operacione=venta"