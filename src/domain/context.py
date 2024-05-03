
#aca tenemos que importar todos los objetos de dominio que queremos que sean levantados por las migraciones, aunque no se use.
#Fijate que si lo comentas y generas una migracion, ignora completamente a la clase.
from src.domain import students



#importamos db aca, para luego importarlo desde este archivo en el app.
from app_base import db

#si importaramos directo desde app_base en el app.py, no se engancharian los modelos que declaramos aca.



