import os
import json


class CreateJava:
    def __init__(self):
        self.name = "create file JAVA"
        self.space = "     "
        self.close = " {"+"\n }"+"\n"
        self.keyclose ="\n"+" } "

    def saveFilebyDir(self, contenjava:dict,routeDir:str , nombre:str):
        #ruta = 'mydir1/mkdir2'
        try:
            ruta = os.makedirs(routeDir)
        except FileExistsError:
            print("ruta existente")
        
        print("guardadndo: "+routeDir)
        #f = open(os.path.join("mydir1/mkdir2", "myfile.txt"), "w")
        f = open(os.path.join(routeDir,nombre.capitalize()+'.java'), 'w')
        # f = open('myfile.txt', 'w')
        f.write(contenjava)
        f.close()
        print("fin proceso")

    def leerFormatoJava(self):
        try:
            with open('formtAuraBoot.json', 'r') as file:
                dict_valor_compuesto = json.load(file)          
            return dict_valor_compuesto
        except FileNotFoundError as e:
            print("Error leyendo el formato: "+ e)


