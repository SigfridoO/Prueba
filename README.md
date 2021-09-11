# Resolución de la prueba técnica

## Componentes de la aplicación

- Base de datos gestionada por Django
- La app 'core', restiona los enlaces generales para para la pantalla de inicio '/'
- La app 'productos' gestiona el modelo e incluye vistas en el endpoint 'productos/' para administrar los productos ingresados
- La app 'registrousuarios', permite crear cuentas de usuarios, e incluye un login para ingresar a la panel de administración para administrar la sección de productos, así como restauración de contraseña 
- Para la restauración de la contraseña se envia un email con en enlace para hacerlo utiliza un correo de prueba, ssi se quiere utilizar un correo rreal, es necesario ingresar las credenciales
- La app 'api' se utiliza para la integración de la api rest, para el modelo productos, en la url 'api/v1'

- La documentación de la api se encuentra en el siguiente enlace
  https://app.swaggerhub.com/apis/SigfridoO/Prueba/1.0.0

### Creación de usuarios

- auth/registration/
- auth/login/
- auth/logout/

curl -X POST http://127.0.0.1:8000/api/v1/auth/registration/ -d "password1=TEST1234A&password2=TEST1234A&email=prueba4@test2.com"
curl -X POST http://127.0.0.1:8000/api/v1/auth/login/ -d "password=TEST1234A&email=test2@test2.com" 
curl -X POST http://127.0.0.1:8000/api/v1/auth/logout/

### Perfil de usuario
- 



### end points productos

### Operaciones de compra venta