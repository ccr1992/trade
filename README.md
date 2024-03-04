# trade

## Instalación del Entorno Python

Este repositorio contiene un archivo environment.yml que especifica las dependencias necesarias para el entorno Python. A continuación se muestran las instrucciones para crear y activar el entorno, así como para arrancar el servicio y ejecutar los tests.


## Ejemplo con conda
```
conda env create -f environment.yml
```

Activa el entorno:

```
conda activate trade
```


## Creación del esquema y carga inicial de datos

He añadido unos pocos datos, para que se puedan usar directamente los endpoints que se piden con `user_id`=1 y `trade_id`=1234.
También hay endpoints de create y get de estos dos objetos.
El script resetea la base de datos por si se quieren hacer distintas pruebas desde 0.

```
python scripts/create_database_schema.py
```

## Ejecución

```
uvicorn api.main:app --host 0.0.0.0
```

Visita la web en tu navegador.


```
http://localhost:8000/docs
```

Desde aquí se pueden lanzar los endpoints de manera amigable.

- El endpoint '/public_methods/create_payment_pipeline' registra las transacciones en Base de Datos y calcula el pago de tasas que hacen los usuarios.

- El endpoint /public_methods/get_user_resume/{user_id} Solicita el balance de un usuario

Los endpoints dentro del tag *database* ayudarán a hacer las distintas pruebas.

##  Ejecutar los tests

Para ejecutar los tests, usa el siguiente comando:

```
python -m unittest
```
