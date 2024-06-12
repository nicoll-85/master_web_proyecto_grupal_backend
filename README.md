# Proyecto Grupal

[User mapping](https://www.figma.com/file/kZV7nxsHS7TOGd4jWaMMc1/GRUPO-01---USER-MAPING-UNEM?type=whiteboard&node-id=0%3A1&t=ReMYZUpIa3m9LJh2-1)

# Indice
- [Proyecto Grupal](#proyecto-grupal)
- [Indice](#indice)
  - [Integrantes del equipo:](#integrantes-del-equipo)
  - [Tecnologías a usar](#tecnologías-a-usar) 
  - [Estructura del proyecto](#estructura-del-proyecto)
  - [Control de versiones](#control-de-versiones)
    - [Ramas](#ramas)

## Integrantes del equipo:
- Cristina de los Ángeles Bosa Sánchez
- Elena Sánchez Jiménez
- Fernando Mencía Labarga
- Nadia Nicoll Aguilar Flores

## Objetivo del proyecto
Realización del `back-end` de el centro de entrenamiento enfocado a CrossFit. Donde los usuarios visitantes podrán visualizar la información detallada del centro, así como registrarse, pagar su cuota mensual y acceder a las clases disponibles.

Por otro lado, habrá un panel de administración donde el gestor se encargará de realizar diferentes funcionalidades internas del centro.

## Tecnologías a usar
- Python
- Django
- Django Rest Framework
- Sqlite

## Estructura del proyecto
Con la finalidad de tener una buena estructura de proyecto que sea fácil de mantener y escalable, se ha apostado por la siguiente estructura:
```
administrator/
|-- migrations/
|-- models/
|-- serializers/
|-- views/
| ...

authentication/
|-- migrations/
|-- models/
|-- serializers/
|-- views/
| ...

gym/
|-- migrations/
|-- management/commands/
|-- models/
|-- serializers/
|-- views/
| ...

master_web_proyecto_grupal_backend/
| ...
```

Módulo de `administrator`: Estará la lógica de negocio de los administradores, para gestionar el centro de HeraFit.
```
administrator/
|-- migrations/ -> Migraciones de la base de datos
|-- views/ -> Viewsets de los modelos creados, que tendrán la lógica de negocio
|       |-- classes.py -> Viewset de la clase (PJ: crear clases, modificar..)
|       |-- classDifficult.py -> Viewset de la clase (PJ: crear clases, modificar..)
|       |-- ...
|admin.py -> Registro de los modelos 
|urls.py -> Rutas de la aplicación (endpoints)
```
Módulo de `authentication`: La capa de autenticación de los usuarios, se registrarán y se logearan.
```
authentication/
|-- migrations/ -> Migraciones de la base de datos
|-- models/ -> Modelos necesarios para la lógica de negocio 
|       |-- users.py
|       |-- ... 
|-- serializers/ -> Serializadores de los modelos creados
|       |-- users.py -> Serializadores de las clases
|-- views/ -> Viewsets de los modelos creados, que tendrán la lógica de negocio
|       |-- users.py -> Viewset de la clase (PJ: crear usuario, modificar, perfil..)
|admin.py -> Registro de los modelos 
|urls.py -> Rutas de la aplicación (endpoints)
```
Módulo de `gym`: La capa de negocio de todos los usuarios independientemente del rol que tengan.
```
gym/
|-- migrations/ -> Migraciones de la base de datos
|-- management/commands -> Comandos para la gestión de la aplicación 
|       |-- seeder_auth.py -> Clases necesarias para la lógica de negocio
|-- models/ -> Modelos necesarios para la lógica de negocio 
|       |-- classes.py -> Clases necesarias para la lógica de negocio
|       |-- classDifficult.py -> Dificultad de las clases 
|       |-- classModality.py -> Modalidad de las clases
|       |-- usersClasses.py -> Clases asignadas a cada usuario
|       |-- billingPlan.py -> Plan de facturación
|       |-- classSchedule.py -> Horario de clases
|-- serializers/ -> Serializadores de los modelos creados
|       |-- classes.py -> Serializadores de las clases
|-- views/ -> Viewsets de los modelos creados, que tendrán la lógica de negocio
|       |-- classes.py -> Viewset de la clase (PJ: consultar clases, inscribirse..)
|admin.py -> Registro de los modelos 
|urls.py -> Rutas de la aplicación (endpoints)
```
Módulo de `master_web_proyecto_grupal_backend` es la configuración del servidor del que depende el resto de módulos mencionados anteriormente.  
```
master_web_proyecto_grupal_backend/
|paginations.py -> Paginaciones del proyecto
|settings.py -> Configuración del proyecto (PJ: configuración de base de datos, middleware...) 
|urls.py -> Rutas de la aplicación (endpoints)
```
## Control de versiones
Este proyecto utliza Git para el control de versiones. A continuación, se detallan las ramas que se usaran para poder gestionar el proyecto y sus diferentes versiones.
### Ramas 
- `main` La rama principal del repositorio. Contiene la versión estable y entregable del proyecto. **No se deben realizar cambios directamente en esta rama**.
- `integration` La rama donde se hará los merges de las ramas de dev-[nombre] para asegurarnos que no haya problemas antes de pasarlo a la rama principal.
- `dev` Se creará una rama dev-[nombre] con la finalidad de que, cada persona haga su constribución al proyecto.
