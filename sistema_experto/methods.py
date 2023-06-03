import tkinter as tk
from tkinter import messagebox
from tkinter import *
import os
import shutil

class METHODS_LOGIC:

    file_actual       = "" # archivo seleccionado
    dict_file_actual  = {} # estructura del dicionario actual
    list_file_actual  = [] # structura de la lista actual
    list_file_actual2 = [] # structura de la lista actual

# ======== [ Cargar Regras ] ========
    def FileSave(filesave):
        actualPath = os.path.dirname(os.path.abspath(__file__)) + "/" + "bc"
        if not os.path.isdir(actualPath):
            try:
                os.mkdir(actualPath)
            except OSError:
                messagebox.showerror('ERROR', 'La carpeta bc No se creo')
            else:
                messagebox.showinfo('ENHORABUENA', 'La carpeta bc se creo correctamente')
        shutil.copy(filesave,actualPath)



# ======== [ Usar Regras ] ========
    # Agrega el contenido del archivo a una estructura
    def StructureFile(structure_file,mdirs):
        path       = structure_file
        bc_file    = ""
        actualPath = os.path.dirname(os.path.abspath(__file__)) + "/" + mdirs
        filee      = actualPath + path

        if os.path.isdir(actualPath): #Exixte la carpeta
            if os.path.isfile(filee): #Existe el archivo
                bc_file = open(filee)
                # --- variables para la estructura ---
                si          = []
                entonces    = ""
                id_number   = ""
                id_rules    = []
                si_entonces = ""
                asks_init   = ""

                for line in bc_file:

                    for character in line:
                        if character.isnumeric():
                            id_number += character
                        else:
                            break

                    # obtener el idicador de pregunta y respuesta
                    if line.find(id_number+'|SI') != -1:
                        si_entonces = "SI"

                    if line.find(id_number+'|ENTONCES') != -1:
                        si_entonces = "ENTONCES"

                    # almacenamos los varores de las preguntas y respuestas
                    if si_entonces == 'SI' and line.find(id_number+'|SI') == -1:
                        aux = line.replace(id_number,'')
                        aux = aux.replace('|','')
                        aux = aux.replace('SI\n','')
                        aux = aux.replace('\n','')
                        if aux != '':
                            si.append([aux,0])

                    if si_entonces == 'ENTONCES' and line.find(id_number+'|ENTONCES') == -1:
                        aux         = line.replace(id_number,'')
                        aux         = aux.replace('|','')
                        aux         = aux.replace('\n','')
                        entonces    = aux
                        si_entonces = ""

                    if line.find(id_number+'|True') != -1:
                        asks_init  = '1'

                    # valida que haya un salto de linea para agregar la siguiente regla
                    if line != '\n':
                        if len(id_rules) != 0:
                            if id_rules[len(id_rules)-1] != id_number:
                                id_rules.append(id_number)
                        else:
                            id_rules.append(id_number)
                    else:
                        METHODS_LOGIC.dict_file_actual = {
                                'id'          : id_rules[len(id_rules)-1],
                                'si'          : si,
                                'entonces'    : entonces,
                                'estadistica' : 0,
                                'bandera'     : '',
                                'asks_init'  : asks_init 
                        }
                        METHODS_LOGIC.list_file_actual.append(METHODS_LOGIC.dict_file_actual)
                        si         = []
                        asks_init  = ''
                    id_number = ""
                bc_file.close()
        else:
            messagebox.showwarning('ALERTA', 'La carpeta bc NO extiste')

    
    # Agrega el contenido del archivo a una estructura
    def StructureFile2(structure_file,mdirs):
        path       = structure_file
        bc_file    = ""
        actualPath = os.path.dirname(os.path.abspath(__file__)) + "/" + mdirs
        filee      = actualPath + path

        if os.path.isdir(actualPath): #Exixte la carpeta
            if os.path.isfile(filee): #Existe el archivo
                bc_file = open(filee)
                # --- variables para la estructura ---
                si          = []
                entonces    = ""
                id_number   = ""
                id_rules    = []
                si_entonces = ""

                for line in bc_file:

                    for character in line:
                        if character.isnumeric():
                            id_number += character
                        else:
                            break
                    
                    # obtener el idicador de pregunta y respuesta
                    if line.find(id_number+'|SI') != -1:
                        si_entonces = "SI"

                    if line.find(id_number+'|ENTONCES') != -1:
                        si_entonces = "ENTONCES"

                    # almacenamos los varores de las preguntas y respuestas
                    if si_entonces == 'SI' and line.find(id_number+'|SI') == -1:
                        aux = line.replace(id_number,'')
                        aux = aux.replace('|','')
                        aux = aux.replace('SI\n','')
                        aux = aux.replace('\n','')
                        if aux != '':
                            si.append([aux,0])

                    if si_entonces == 'ENTONCES' and line.find(id_number+'|ENTONCES') == -1:
                        aux         = line.replace(id_number,'')
                        aux         = aux.replace('|','')
                        aux         = aux.replace('\n','')
                        entonces    = aux
                        si_entonces = ""

                    # valida que haya un salto de linea para agregar la siguiente regla
                    if line != '\n':
                        if len(id_rules) != 0:
                            if id_rules[len(id_rules)-1] != id_number:
                                id_rules.append(id_number)
                        else:
                            id_rules.append(id_number)
                    else:
                        METHODS_LOGIC.dict_file_actual = {
                                'id'          : id_rules[len(id_rules)-1],
                                'si'          : si,
                                'entonces'    : entonces,
                                'estadistica' : 0,
                                'bandera'     : ''
                        }
                        METHODS_LOGIC.list_file_actual2.append(METHODS_LOGIC.dict_file_actual)
                        si         = []
                    id_number = ""
                bc_file.close()
        else:
            messagebox.showwarning('ALERTA', 'La carpeta bc NO extiste')

    # regresa el nombre del archivo seleccionado
    def FileEvent(event,mdirs):
        messagebox.showinfo('SELECIONATES',event)
        if mdirs == "bc/":
            print("cacacacac: ",mdirs)
            METHODS_LOGIC.StructureFile(event,mdirs)
        
        if mdirs == "bc2/":
            print("entro: ",mdirs)
            METHODS_LOGIC.StructureFile2(event,mdirs)
        return event

    # lee la carpeta bc para ver las bases de conocimientos existentes
    def ReadImportCB():
        actualPath = os.path.dirname(os.path.abspath(__file__)) + "/" + "bc"
        if os.path.isdir(actualPath):
            contenidos = os.listdir(actualPath)
            return contenidos
        else:
            messagebox.showwarning('ALERTA', 'La carpeta bc NO extiste')
            return False
        return False


# ======== [ Leer Regras ] ========
    # leer archivo usado en el sistema actualmente
    def FileReadActual():
        path       = METHODS_LOGIC.file_actual
        bc_file    = ""
        actualPath = os.path.dirname(os.path.abspath(__file__)) + "/" + "bc/"
        filee      = actualPath + path

        if os.path.isdir(actualPath):
            if os.path.isfile(filee):
                bc_file = open(filee)
                # --- caja de texto ---
                text = ""
                for line in bc_file:
                    text += line
                bc_file.close()
        else:
            messagebox.showwarning('ALERTA', 'La carpeta bc NO extiste')
        return text

       
        

    # Leé el Archivo de texto
    def FileRead(files,window_reads):
        bc_text    = str(files.get()) + ".txt"
        bc_file    = ""
        actualPath = os.path.dirname(os.path.abspath(__file__)) + "/" + "bc"
        filee      = actualPath + "/" + bc_text

        if os.path.isdir(actualPath):
            if os.path.isfile(filee):
                bc_file = open(filee)
                # --- caja de texto ---
                text = ""
                for line in bc_file:
                    text += line 

                bc_file.close()
                text_box = tk.Text(window_reads)
                text_box.insert("1.0",text)
                text_box.configure(state='disabled')
                text_box.grid(row=4, column=1,columnspan=3,rowspan=10,sticky=[tk.W,tk.E,tk.S,tk.N])
        else:
            messagebox.showwarning('ALERTA', 'La carpeta bc NO extiste')



# ======== [ Actualizar Regras ] ========
# Función para obtener y actualizar BC con la TextBox
    def GetTextBox(text_box,bc_text_update1):
        text_file  = text_box.get("1.0","end")
        pathActual = "bc/" + bc_text_update1 + ".txt"

        with open(pathActual, "w") as myfile:
            myfile.write(text_file)

        myfile.close()
        messagebox.showinfo('ENHORABUENA','Se actualizó '+bc_text_update1)

# Funcion Para Actualizar Reglas
    def FileUpdate(bc_update):
        bc_text_update1    = str(bc_update.get())
        #rules_text_update1 = str(rules_update.get())
        directory          = 'bc/'
        char               = ''
        text               = ""

        if bc_text_update1 != '':
            directory += bc_text_update1 + ".txt"
            with open(directory) as files:
                """if rules_text_update1 != '':
                    for lines in files:
                        for character in lines:
                            if character != '|' and character.isnumeric():
                                char += character
                            else:
                                break
                        if char == rules_text_update1:
                            print(lines)
                        char = ''"""
                #else:
                # --- caja de texto ---
                for line in files:
                    text += line 
        else:
            print('Campo vacio')
            messagebox.showwarning('ALERTA', 'Archivo NO encontrado')
            return ''
        return text
