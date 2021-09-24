
import mysql.connector



def Guardar(T,D):
    """
    El método admite los datos 
    validados y realiza el alta
     en la base de datos.
    """
    try:

        mibase=mysql.connector.connect(host='localhost',  user='root', passwd='', database='prueba3')
        micursor=mibase.cursor()

        sql='INSERT INTO producto(titulo,descripcion) VALUES (%s,%s)'

        datos=(T,D)
        micursor.execute(sql,datos)

        mibase.commit()

        mibase.close()
        return True
    except:
        return False


