# Resolución de la prueba técnica

## Componentes de la aplicación

- Base de datos gestionada por Django
- La app 'core', restiona los enlaces generales para para la pantalla de inicio '/'
- La app 'productos' gestiona el modelo e incluye vistas en el endpoint 'productos/' para administrar los productos ingresados
- La app 'registrousuarios', permite crear cuentas de usuarios, e incluye un login para ingresar a la panel de administración para administrar la sección de productos, así como restauración de contraseña 
- Para la restauración de la contraseña se envia un email con en enlace para hacerlo utiliza un correo de prueba, ssi se quiere utilizar un correo rreal, es necesario ingresar las credenciales
- La app 'api' se utiliza para la integración de la api rest, para el modelo productos, en la url 'apip/v1'

