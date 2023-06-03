import tkinter as tk
from tkinter import StringVar,filedialog
from tkinter import *
from tkinter import messagebox
from methods import METHODS_LOGIC as methods
import functools
import os


# ---- configuarcion de widget secundarios---
color_bg     = 'dark slate gray'
colorbg_pass = 'dim gray'
color_text   = 'alice blue'
font_text    = 'Arial 13'
longs        = '500x250'
widthtitle   = 70
heighttitle  = 3
# ---- configuarcion de widget primarios---
color_bg_secundario = 'black'
# cargars de widgets
widgets_carga     = []
widgets_modificar = []
widgets_preguntas = []
# guardar la respuesta de las preguntas
answer = ''
# obtenemos la lista de regras estructurada
list_file_actual  = methods.list_file_actual
list_file_actual2 = methods.list_file_actual2



# ======== [ Eliminar Widget ] ========
def DeleteWidget(widgets):
    for wid in widgets:
        wid.grid_remove()



# ======== [ Cargar Regras ] ========
def Load():
    fileOpen = filedialog.askopenfilename(initialdir='/',
    title='Seleccionar archivo',filetypes=(('txt files','*.txt'),
    ('all files','*.*')))

    methods.FileSave(fileOpen)
    print(fileOpen)



# ======== [ Leer Regras ] ========
# Retorna el contenido del archivo widgets_modificar.append()
def ReturnRead(windows,validator):
    global text_box1
    text = methods.FileReadActual()

    if text != '':
        if validator == True:
            text_box0 = tk.Text(windows)
            text_box0.insert("1.0",text)
            text_box0.configure(state='disabled')
            text_box0.grid(row=4, column=1,columnspan=3,rowspan=10,sticky=[tk.W,tk.E])
        else:
            text_box1 = tk.Text(windows)
            text_box1.insert("1.0",text)
            text_box1.configure(state='disabled')
            text_box1.grid(row=4, column=1,columnspan=3,rowspan=10,sticky=[tk.W,tk.E])
            widgets_modificar.append(text_box1)

# Ventana para leer archivo
def Read():
    #Una ventana es una instancia de la Tkclase de Tkinter. 
    global window_reads
    window_reads = tk.Tk()
    window_reads.configure(bg=color_bg)
    window_reads.title("File Read")
    window_reads.geometry(longs)
    window_reads.columnconfigure(0, weight=3)
    window_reads.columnconfigure(1, weight=3)
    window_reads.columnconfigure(2, weight=3)
    window_reads.columnconfigure(3, weight=3)
    window_reads.columnconfigure(4, weight=3)

    text_read2  = tk.Label(window_reads,text="Nombre del Archivo SIN .txt",font=font_text)
    actualfile  = tk.Button(window_reads,text='Archivo Actual',fg=color_text,bg=colorbg_pass,font='Arial 11',command=lambda:ReturnRead(window_reads,True))
    searchlabel = tk.Label(window_reads,text="Buscar: ",font=font_text)
    bc          = tk.Entry(window_reads,text="Placeholder text",width=60)
    button_read = tk.Button(window_reads,text='Aceptar',fg=color_text,bg=colorbg_pass,font='Arial 11',command=lambda:methods.FileRead(bc,window_reads))

    text_read2.grid(row=2,column=0,columnspan=10,sticky=[tk.W,tk.E])
    actualfile.grid(row=3,column=0,sticky=[tk.W,tk.E])
    searchlabel.grid(row=3,column=1,sticky=[tk.W,tk.E],ipady=5,ipadx=0.9,padx=1)
    bc.grid(row=3,column=2,columnspan=2,sticky=[tk.W,tk.E],ipady=5,ipadx=1,padx=1)
    button_read.grid(row=3,column=4,sticky=[tk.W,tk.E])
    


# ======== [ Actualizar Regras ] ========
def FileUpdate0(bc_update,window):
    global text_box, button_text_box
    bc_text_update1 = str(bc_update.get())
    text            = methods.FileUpdate(bc_update)

    if text != '':
        text_box = tk.Text(window)
        text_box.insert("1.0",text)
        text_box.grid(row=3, column=1,columnspan=3,rowspan=10,sticky=[tk.W,tk.E])

        button_text_box = tk.Button(window,text='Actualizar Archivo',fg=color_text,bg=colorbg_pass,font='Arial 11',command=lambda:methods.GetTextBox(text_box,bc_text_update1))
        button_text_box.grid(row=3,column=4,sticky=[tk.W,tk.E])
        widgets_modificar.append(text_box)
        widgets_modificar.append(button_text_box)

# Ventana para Actualizar Regla
def Update(window):
    global bc_text_update,bc_update,button_update,actualfilebc

    # eliminando widget del botón usar 
    if widgets_carga != None:
        DeleteWidget(widgets_carga)
    
    bc_string         = StringVar()
    #rules_string      = StringVar()
    actualfilebc      = tk.Button(window,text='Actual',fg=color_text,bg=colorbg_pass,font='Arial 11',command=lambda:ReturnRead(window,False))
    bc_text_update    = tk.Label(window,text="Nombre del Archivo",font=font_text)
    bc_update         = tk.Entry(window,textvariable=bc_string,width=60)
    #rules_text_update = tk.Label(window,text="Numero de regla",font=font_text)
    #rules_update      = tk.Entry(window,textvariable=rules_string,width=60)
    button_update     = tk.Button(window,text='Aceptar',fg=color_text,bg=colorbg_pass,font='Arial 11',command=lambda:FileUpdate0(bc_update,window))

    #Se guardan los widget creados anteriormente en la lista "widgets_modificar"
    widgets_modificar.append(actualfilebc)
    widgets_modificar.append(bc_text_update)
    widgets_modificar.append(bc_update)
    #widgets_modificar.append(rules_text_update)
    #widgets_modificar.append(rules_update)
    widgets_modificar.append(button_update)

    actualfilebc.grid(row=2,column=0,sticky=[tk.W,tk.E])
    bc_text_update.grid(row=2,column=1,sticky=[tk.W,tk.E],ipady=5,ipadx=0.9,padx=1)
    bc_update.grid(row=2,column=2,columnspan=2,sticky=[tk.W,tk.E],ipady=5,ipadx=0.9,padx=1)
    #rules_text_update.grid(row=2,column=3,sticky=[tk.W,tk.E])
    #rules_update.grid(row=2,column=4,sticky=[tk.W,tk.E],ipady=5,ipadx=1,padx=1)
    button_update.grid(row=2,column=4,sticky=[tk.W,tk.E])


# Ventana para leer archivo
def Continius(result):
    mdirs = "bc2/"
    global window_reads2
    window_reads2 = tk.Tk()
    window_reads2.configure(bg=color_bg)
    window_reads2.title(result)
    window_reads2.geometry(longs)
    window_reads2.columnconfigure(0, weight=3)
    window_reads2.columnconfigure(1, weight=3)
    window_reads2.columnconfigure(2, weight=3)
    window_reads2.columnconfigure(3, weight=3)
    window_reads2.columnconfigure(4, weight=3)
    # eliminando widget del botón usar
    if widgets_preguntas != None:
        DeleteWidget(widgets_preguntas)
    #fileImportBC(window)
    FileEvent0(result,window_reads2,mdirs)

# ======== [ Usar Regras ] ========
def Asks(window,list_file_actual,finish,asks,answer,count_true,result):
    if len(list_file_actual) > 0:
        posicion       = 0
        number_ask     = 0
        si_dict        = []
        structure_dict = []
        si_dict        = []
        #result         = ''
        #finish         = ''

        if count_true != 0:# SI COUNTER_TRUE ES != 0 SE REALIZA EL ALGORITMO DE LAS REGLAS
            if answer == 'si':
            # se le asigna un check "1" cuando se seleciona que "SI" a la pregunta
            # 1 = SI, -1 = NO, 0 = No Contestado
                for i in range(len(list_file_actual)):
                    aux_list       = list_file_actual[i]['si']
                    list_validator = False

                    for j in range(len(aux_list)):
                        if asks == list_file_actual[i]['si'][j][0] and list_file_actual[i]['si'][j][1] == 0:
                            list_file_actual[i]['si'][j][1] = 1 # se guardan las regras hacertadas para realizar la probabilidad
                            list_file_actual[i]['bandera']  = True # se identifican las reglas que cumplan todas  las reglas
                            list_validator = True
                            break
                        #elif asks != list_file_actual[i]['si'][j][0] and list_file_actual[i]['si'][j][1] != 1:
                        #    list_file_actual[i]['si'][j][1] = -1
                        #    list_file_actual[i]['bandera']  = False
                        #asks = entonces_dict
                    if list_validator == False:
                        list_file_actual[i]['bandera']  = False
            
            if answer == 'no':
        # se le asigna un check "0" cuando se seleciona que "NO" a la pregunta
                for i in range(len(list_file_actual)):
                    aux = list_file_actual[i]['si']
                    for j in range(len(aux)):
                        if asks == list_file_actual[i]['si'][j][0]:
                            list_file_actual[i]['si'][j][1] = 0 # se guardan las regras hacertadas para realizar la probabilidad
                            list_file_actual[i]['bandera']  = False # se identifican las reglas que cumplan todas  las reglas
                            break
                    #asks = entonces_dict
            """
            for i in range(len(list_file_actual)):
                aux = list_file_actual[i]['si']
                contador = 0
                for j in range(len(aux)):
                    if list_file_actual[i]['si'][j][1] == 0:
                        contador +=1 # se guardan las regras hacertadas para realizar la probabilidad
                if contador == len(aux):
                    list_file_actual[i]['bandera']  = False"""
                        
        
        # se eliminan todos los registros que no tienen la bandera "True"
            while posicion < len(list_file_actual):
                if list_file_actual[posicion]['bandera'] == False:
                    list_file_actual.pop(posicion)
                else:
                    posicion=posicion+1

        # se realiza el calculo de los aciertos de cada regla para calcular el numero de porcentaje de probabilidad
            for i in range(len(list_file_actual)):
                aux_list = list_file_actual[i]['si']
                for j in range(len(aux_list)):
                    if list_file_actual[i]['si'][j][1] == 1:
                        number_ask += 1
                #if list_file_actual[i]['bandera'] == True:
                statitics = int((number_ask / len(aux_list)) * 100)
                list_file_actual[i]['estadistica'] = statitics
                number_ask = 0
        
        # filtra y selecciona la regla con mayor porcentaje 
            for i in range(len(list_file_actual)):
                for j in range(i,0,-1):
                    if(list_file_actual[j-1]['estadistica'] < list_file_actual[j]['estadistica']):
                        aux = list_file_actual[j]
                        list_file_actual[j] = list_file_actual[j-1]
                        list_file_actual[j-1] = aux
            
            for a in list_file_actual:
                print(a,"\n")
            
            print('\n')
                
            if len(list_file_actual) > 0:
                structure_dict = list_file_actual[0]
                si_dict        = structure_dict['si']

                if structure_dict['estadistica'] == 100.0 and structure_dict['asks_init'] != '1':
                    finish = structure_dict['entonces']
                    messagebox.showinfo('RESULTADO', finish)

                if structure_dict['asks_init'] == '1' and structure_dict['bandera'] == True:
                    list_file_actual[0]['bandera'] = False
                    asks = structure_dict['entonces']
                    finish = str(structure_dict['estadistica'])
                    if int(finish) != 0:
                        result = structure_dict['entonces']
                        finish = finish+ "% DE PADECER " + result
                    else:
                        finish = "SIN PADECIMIENTOS"
                else:
                    for i in range(len(si_dict)):
                        if si_dict[i][1] != 1:
                            asks = si_dict[i][0]
                            finish = str(structure_dict['estadistica'])
                            #result = structure_dict['entonces']
                            #finish = finish + result
                            if int(finish) != 0:
                                result = structure_dict['entonces']
                                finish = finish+ "% DE PADECER " + result
                            else:
                                finish = "SIN PADECIMIENTOS"
                            break
            else:
                messagebox.showinfo('EXISTE UN', finish)
                result = result.lower()+".txt"
                mdirs = "bc2/"
                actualPath = os.path.dirname(os.path.abspath(__file__)) + "/" + mdirs
                filee      = actualPath + result
                if os.path.isdir(actualPath): #Exixte la carpeta
                    if os.path.isfile(filee): #Existe el archivo
                        Continius(result)
                    else:
                        messagebox.showerror('ERROR', 'EL ARCHIVO ',result,' NO EXISTE')
                else:
                    messagebox.showinfo('ADVERTENCIA','LA CARPETA NO EXISTE PERO SE CREARA')
                    try:
                        os.mkdir(actualPath)
                    except OSError:
                        messagebox.showerror('ERROR', 'LA CARPETA "',mdirs,'" NO SE CREO CORRECTAMENTE')
            count_true = 1

        else:# SI COUNTER_TRUE ES 0 SE UTILIZA LA PREGUNTA INICIAL DE LA LISTA
            structure_dict = list_file_actual[0]
            si_dict        = structure_dict['si']
            asks           = si_dict[0][0]
            count_true     = 1

        print(asks,"\n\n\n")

        ask = Label(window,text=asks,font=font_text)
        no  = Button(window, text='SI',fg=color_text,bg=colorbg_pass,font='Arial 11',command=lambda:Asks(window,list_file_actual,finish,asks,'si',count_true,result))
        yes = Button(window, text='NO',fg=color_text,bg=colorbg_pass,font='Arial 11',command=lambda:Asks(window,list_file_actual,finish,asks,'no',count_true,result))
        
        ask.grid(row=2,column=0,columnspan=3,sticky=[tk.W,tk.E])
        yes.grid(row=3,column=0,sticky=[tk.W,tk.E])
        no.grid(row=3,column=2,sticky=[tk.W,tk.E])
        
        widgets_preguntas.append(ask)
        widgets_preguntas.append(no)
        widgets_preguntas.append(yes)


def Asks2(windows2,list_file_actual2,finish,asks,answer,count_true,contador):
    if len(list_file_actual2) > 0:
        number_ask     = 0
        si_dict        = []
        structure_dict = []
        si_dict        = []

        if count_true != 0:# SI COUNTER_TRUE ES != 0 SE REALIZA EL ALGORITMO DE LAS REGLAS
            if answer == 'si':
            # se le asigna un check "1" cuando se seleciona que "SI" a la pregunta
            # 1 = SI, -1 = NO, 0 = No Contestado
                for i in range(len(list_file_actual2)):
                    aux_list       = list_file_actual2[i]['si']
                    list_validator = False

                    for j in range(len(aux_list)):
                        if asks == list_file_actual2[i]['si'][j][0] and list_file_actual2[i]['si'][j][1] == 0:
                            list_file_actual2[i]['si'][j][1] = 1 # se guardan las regras hacertadas para realizar la probabilidad
                            list_file_actual2[i]['bandera']  = True # se identifican las reglas que cumplan todas  las reglas
                            list_validator = True
                            break

                    if list_validator == False:
                        list_file_actual2[i]['bandera']  = False
            
            if answer == 'no':
        # se le asigna un check "0" cuando se seleciona que "NO" a la pregunta
                for i in range(len(list_file_actual2)):
                    aux = list_file_actual2[i]['si']
                    for j in range(len(aux)):
                        if asks == list_file_actual2[i]['si'][j][0]:
                            list_file_actual2[i]['si'][j][1] = 0 # se guardan las regras hacertadas para realizar la probabilidad
                            list_file_actual2[i]['bandera']  = False # se identifican las reglas que cumplan todas  las reglas
                            break
                            
            if len(list_file_actual2) > contador:
                structure_dict = list_file_actual2[contador]
                si_dict        = structure_dict['si']

                asks     = structure_dict['si'][0][0]
                finish   = structure_dict['entonces']
                contador += 1
            else:
                for i in range(len(list_file_actual2)):
                    aux_list = list_file_actual2[i]['si'][0][1]
                    if aux_list == 1:
                        number_ask += 1

                statitics  = int((number_ask / len(list_file_actual2)) * 100)
                if statitics != 0:
                    finish     = str(statitics) +"% "+ finish
                else:
                    finish = "SIN PADECIMIENTOS"
                number_ask = 0
                contador   = 0
                messagebox.showinfo('EXISTE UN', finish)
                windows2.destroy()
            
            count_true = 1

        else:# SI COUNTER_TRUE ES 0 SE UTILIZA LA PREGUNTA INICIAL DE LA LISTA
            structure_dict = list_file_actual2[0]
            si_dict        = structure_dict['si']
            asks           = si_dict[0][0]
            count_true     = 1
            contador      += 1

        ask = Label(windows2,text=asks,font=font_text)
        no  = Button(windows2, text='SI',fg=color_text,bg=colorbg_pass,font='Arial 11',command=lambda:Asks2(windows2,list_file_actual2,finish,asks,'si',count_true,contador))
        yes = Button(windows2, text='NO',fg=color_text,bg=colorbg_pass,font='Arial 11',command=lambda:Asks2(windows2,list_file_actual2,finish,asks,'no',count_true,contador))
        
        ask.grid(row=2,column=0,columnspan=3,sticky=[tk.W,tk.E])
        yes.grid(row=3,column=0,sticky=[tk.W,tk.E])
        no.grid(row=3,column=2,sticky=[tk.W,tk.E])
        
        widgets_preguntas.append(ask)
        widgets_preguntas.append(no)
        widgets_preguntas.append(yes)


# obtener el archivo a usar
def FileEvent0(event,window,mdirs):
    actual              = methods.FileEvent(event,mdirs)
    print(actual,"hhhhhh")
    # se pasa el nombre de la bc a la variable global de la instancia
    methods.file_actual = actual
    finish     = ''  # OBTIENE LA PRIMERA POSICIÓN DE LA LISTA
    asks       = '' # GUARDA LA PREGUNTA
    answer     = '' # GUARDA LA RESPUESTA
    count_true = 0 # VERIFICA SI YA SE PREGUNTO ANTES
    result     = ''
    contador   = 0
    if mdirs == "bc/":
        Asks(window,list_file_actual,finish,asks,answer,count_true,result)
    if mdirs == "bc2/":
        Asks2(window,list_file_actual2,finish,asks,answer,count_true,contador)


def fileImportBC(window):
    global et,b
    
    # eliminando widget del botón usar
    if widgets_modificar != None:
        DeleteWidget(widgets_modificar)
    
    contenidos = methods.ReadImportCB()

    if contenidos != False:
        count = 2
        for i in range(len(contenidos)):
            et = Label(window,text=contenidos[i],font=font_text)
            b  = Button(window, text=contenidos[i],fg=color_text,bg=colorbg_pass,font='Arial 11',command=functools.partial(FileEvent0,et["text"],window,"bc/"))
            
            #et.grid(row=count,column=2,columnspan=2,sticky=[tk.W,tk.E])
            b.grid(row=count,column=3,columnspan=2,sticky=[tk.W,tk.E])
            count = count + 1
            #Se guardan los widget creados en el ciclo en la lista "widgets_modificar"
            widgets_carga.append(et)
            widgets_carga.append(b)
    else:
        messagebox.showinfo('ALERTA','El directorio no contiene BC')



# ======== [ Venta de Inicio ] ========
def init():
    #Una ventana es una instancia de la Tkclase de Tkinter. 
    global window
    window = tk.Tk()
    window.configure(bg=color_bg)
    window.title("Expert System")
    window.geometry(longs)
    window.columnconfigure(0, weight=3)
    window.columnconfigure(1, weight=3)
    window.columnconfigure(2, weight=3)
    window.columnconfigure(3, weight=3)
    window.columnconfigure(4, weight=3)

    text   = tk.Label(window,text="SISTEMA EXPERTO",fg="whitesmoke",bg=colorbg_pass,font=font_text)
    # se crea los botónes a usar
    load   = tk.Button(window, text='Importar',fg=color_text,bg=color_bg_secundario,font='Arial 11' ,command=Load)
    read   = tk.Button(window, text='Ver',fg=color_text,bg=color_bg_secundario,font='Arial 11' ,command=Read)
    use    = tk.Button(window, text='Cargar',fg=color_text,bg=color_bg_secundario,font='Arial 11' ,command=lambda:fileImportBC(window))
    update = tk.Button(window, text='Modificar',fg=color_text,bg=color_bg_secundario,font='Arial 11' ,command=lambda:Update(window))
    closes = tk.Button(window, text='Cerrar',fg=color_text,bg=color_bg_secundario,font='Arial 11' ,command=window.quit)
    
    text.grid(row=0,column=0,columnspan=10,sticky=[tk.W,tk.E])
    load.grid(row=1,column=0,sticky=[tk.W,tk.E])
    read.grid(row=1,column=1,sticky=[tk.W,tk.E])
    update.grid(row=1,column=2,sticky=[tk.W,tk.E])
    use.grid(row=1,column=3,sticky=[tk.W,tk.E])
    closes.grid(row=1,column=4,columnspan=2,sticky=[tk.W,tk.E])
    window.mainloop()



if __name__ == "__main__":
    init()