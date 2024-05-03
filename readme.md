## Nota:
Por las dudas crea el venv, y instala paquetes desde powershell, en git bash no se me registraban bien los comandos de flask luego de instalar.

```
PS python -m venv .\.venv
PS .\.venv\Scripts\Activate.ps1
```


## Iniciar la aplicacion:

```
PS flask --app app run --debug
```

## Incializar Migraciones:
Solo se corre una vez, genera la carpeta migrations de cero.

```
 PS flask db init
```

## Agregar Script de Migracion:

```
 PS flask db migrate -m "xx_Nombre migracion"
```
(recomiendo que le pongas numeros a las migraciones en el xx, porque no te las ordena secuencialmente)

## Ejecutar todas las imgraciones (hasta la ultima):

```
PS flask db upgrade HEAD
```

## Ejecutar todas las imgraciones (hasta una especifica):

```
PS flask db upgrade <revision>
```

## Downgreadear migraciones (hasta una especifica):

```
PS flask db downgrade <revision>
```