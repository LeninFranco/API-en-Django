# API RESTful de Punto de Venta con Inventarios

Este proyecto es una API RESTful para un sistema de punto de venta con gestión de inventarios. Proporciona operaciones CRUD para manejar productos, categorías, proveedores, clientes, compras y ventas. La autenticación se maneja mediante tokens, y los permisos se configuran mediante grupos y usuarios en Django.

## Estructura del Proyecto

El proyecto sigue la estructura predeterminada de Django y contiene las siguientes aplicaciones:

- **autenticacion**: Maneja el login, logout y generación de tokens. Además, soluciona la gestión de permisos para operaciones `GET`.
- **productos**: Gestiona el CRUD y las operaciones para los modelos de categoría, producto e inventario.
- **compras**: Maneja el CRUD y las operaciones para los modelos de proveedores y compras.
- **ventas**: Gestiona el CRUD y las operaciones para los modelos de clientes y ventas.

## Modelos Principales

El proyecto incluye los siguientes modelos:

- **Categoría**: Categorías de productos.
- **Producto**: Información sobre productos.
- **Inventario**: Movimientos de inventario (entradas y salidas).
- **Proveedor**: Información sobre proveedores.
- **Compra**: Registro de compras de mercancía.
- **Cliente**: Información sobre clientes.
- **Venta**: Registro de ventas a clientes.

Se incluye en el repositorio un diagrama principal de la base de datos en formato PNG para ilustrar las relaciones entre los modelos.

## Endpoints de la API

Los endpoints de la API están definidos utilizando `ModelViewSet` de Django Rest Framework (DRF), lo que permite operaciones CRUD completas en cada modelo. Los métodos HTTP disponibles son GET, POST, PUT y DELETE.

## Autenticación y Permisos

La autenticación se maneja mediante el módulo `authtoken` de DRF. Los usuarios deben incluir un token de autenticación en el encabezado de sus solicitudes para acceder a los endpoints.

- **Admin (Superusuario)**: Tiene acceso completo a todas las operaciones en todos los modelos.
- **Empleados**: Pueden visualizar todos los modelos y realizar operaciones de adición en compras y ventas. Solo pueden iniciar sesión y cerrar sesión.

Los permisos se configuran y gestionan a través del panel de administración de Django.