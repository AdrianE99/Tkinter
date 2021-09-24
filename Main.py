from tkinter import ttk
from tkinter import *
from tkinter import messagebox

import mysql.connector
from GuardarDatos import *
from Verificar import *
from Temas import *

class Administrador:
    """ 
    Con esta clase definimos tanto la interfaz
     visual de la aplicación, como el llamado 
     de los diferentes módulos.  

    """

    def __init__(self):

        """
        Creación de objeto de clase Tk() 
         la cual será la ventana principal,
         a su vez creamos su título y 
         seguidamente del llamado del método
         "aplicación"

        """
        self.raiz=Tk()
        self.raiz.title('Tarea POO')
        self.raiz.resizable(0,0)   
        self.aplicacion()
        self.raiz.mainloop()


    def aplicacion(self):

        """
        Creación del frame que tendrá la interfaz
         en donde tenemos definido las etiquetas,
         variables, entradas, Treeview y los botones.

        """
        self.miFrame=Frame(self.raiz)
        self.miFrame.pack()

#-------Etiquetas------------------------
        self.barra1=Label(self.miFrame,text='Ingrese sus datos',relief='groove',fg='white',bg='#6133FF')
        self.barra1.grid(row=0,column=0,columnspan=4,sticky=W+E)

        self.barra2=Label(self.miFrame,text='Mostrar registros existentes',relief='groove',fg='black',bg='#D5D1E3')
        self.barra2.grid(row=3,column=0,columnspan=4,sticky=W+E)

        self.barra3=Label(self.miFrame,text='Temas',relief='groove',fg='red',bg='black')
        self.barra3.grid(row=6,column=0,columnspan=4,sticky=W+E)

#-------Variables------------------------

        self.DatoT=StringVar()
        self.DatoD=StringVar()
        self.TemaOpcion=IntVar()


#-------Entrada de datos------------------

        self.tituloLabel=Label(self.miFrame,text='Titulo')
        self.tituloLabel.grid(row=1,column=0,sticky='w')

        self.cuadroTitulo=Entry(self.miFrame,textvariable=self.DatoT)
        self.cuadroTitulo.grid(row=1,column=1)

        self.DescripcionLabel=Label(self.miFrame,text='Descripcion')
        self.DescripcionLabel.grid(row=2,column=0,sticky='w')

        self.cuadroDescripcion=Entry(self.miFrame,textvariable=self.DatoD)
        self.cuadroDescripcion.grid(row=2,column=1)


#-------Treeview---------------------

        self.reg=ttk.Treeview(self.miFrame)
        self.reg['columns']=('col1','col2')
        self.reg.column("#0", width=50, minwidth=50, anchor=W)
        self.reg.column("col1", width=200, minwidth=200)
        self.reg.column("col2", width=200, minwidth=200)
        self.reg.heading('#0',text='ID')
        self.reg.heading('col1',text='Titulo')
        self.reg.heading('col2',text='Descripcion')
        self.reg.grid(column=0,row=5,columnspan=4)


#-------Botones------------------------

        self.BotonBd=Button(self.miFrame,text='Crear bd',width=6,command=self.CreacionBd).grid(row=4,column=0,padx=1,pady=1)
        self.BotonAlta=Button(self.miFrame,text='Alta',width=3,command=self.Registrar).grid(row=4,column=2,padx=1,pady=1)

        self.RadioButton1=Radiobutton(self.miFrame,text='Tema 1',fg='red',variable=self.TemaOpcion,value=1,command=lambda:EleccionTemas(self.miFrame,self.TemaOpcion.get()))
        self.RadioButton1.config(bg ="black")
        self.RadioButton1.grid(row=7,column=0,columnspan=5)

        self.RadioButton2=Radiobutton(self.miFrame,text='Tema 2',fg='red',variable=self.TemaOpcion,value=2,command=lambda:EleccionTemas(self.miFrame,self.TemaOpcion.get()))
        self.RadioButton2.config(bg ="black")
        self.RadioButton2.grid(row=8,column=0,columnspan=5)

        self.RadioButton3=Radiobutton(self.miFrame,text='Tema 3',fg='red',variable=self.TemaOpcion,value=3,command=lambda:EleccionTemas(self.miFrame,self.TemaOpcion.get()))
        self.RadioButton3.config(bg ="black")
        self.RadioButton3.grid(row=9,column=0,columnspan=5)



#---Metodos----------------------------

    def CreacionBd(self):

        """
        Con este método creamos la base de datos
         como así también la tabla en MySQL.

        """

        try:
            #Creación de bases de datos

            mibase=mysql.connector.connect(host='localhost',user='root',passwd='')
            micursor=mibase.cursor()
            micursor.execute('CREATE DATABASE prueba3')
            mibase.close()

            #Creacion de tabla

            mibase=mysql.connector.connect(host='localhost',user='root',passwd='',database='prueba3')
            micursor=mibase.cursor()
            micursor.execute('CREATE TABLE producto( id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, titulo VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, descripcion text COLLATE utf8_spanish2_ci NOT NULL )')
            mibase.close()
            messagebox.showinfo('BBDD','CREACION CON EXITO!')
            


        except:

            messagebox.showwarning('AVISO','La base de datos ya esta creada!!!')

            #Muestra de la base de datos ya existente.
            self.MuestraBBDD(self.reg)



    def Registrar(self):

        """
        En este método realizamos el alta del registro
         pero validando antes los datos.
        Luego registramos los datos en la base de datos,
         y finalmente realizamos la muestra de los datos 
         registrados en la interfaz.

        """

        ValDatoT=Validar(self.DatoT.get())

        if ValDatoT:

            BD=Guardar(self.DatoT.get(),self.DatoD.get())

            if BD==False:

                self.limpiarEntry()
                messagebox.showwarning('AVISO','Debe crear la Base de Datos')
	    
            else:

                self.limpiarEntry()
                self.MuestraBBDD(self.reg)
                messagebox.showinfo('BBDD','Registro exitoso')

        else:

            self.limpiarEntry()
            messagebox.showerror('ERROR','Ingrese solo alfanumericos.')


    def limpiarEntry(self):

        """
        Este método nos permite
         la limpieza de los entry 
         una vez utilizados.


        """

        self.DatoD.set('')
        self.DatoT.set('')

    def MuestraBBDD(self,tabla):

        """
        El método permite mostrar 
         los datos almacenadados, pero antes
         realizamos una limpieza de 
         los mismos en el Treeview.

        """

       
        mibase=mysql.connector.connect(host="localhost", user="root", passwd="", database="prueba3")
        micursor=mibase.cursor()
        sql='SELECT * FROM producto'
        micursor.execute(sql)
        mibase.close()

        Datos=micursor.fetchall()

        for i in tabla.get_children():
            tabla.delete(i)


        for i in Datos:
            tabla.insert('',0,text=i[0],values=(i[1],i[2]))

    
#Creación de objeto de la clase Administrador
App=Administrador()
