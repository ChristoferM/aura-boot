import os
import json
from utils import CreateJava



class CrearJavaClass:
    def __init__(self):
        self.name = "Archivos JAVA"
        self.espacio = "     "
        self.cierre = " {"+"\n }"+"\n"
        self.llaveCerrada ="\n"+" } "
        self.llaveCerrada ="\n"+" } "
        

    def say_hello(self):
        print("Hello, my name is {}.".format(self.name))


    def crearArchiv(self,contenjava:str,mkdir:str):

        print(contenjava)
        print(mkdir)
        print(mkdir)
        #ruta = 'mydir1/mkdir2'
        try:
            ruta = os.makedirs(mkdir)
        except FileExistsError:
            print("ruta existente")
        
        print(mkdir)
        #f = open(os.path.join("mydir1/mkdir2", "myfile.txt"), "w")
        f = open(os.path.join(mkdir,'Usuario.java'), 'w')
        # f = open('myfile.txt', 'w')
        f.write(contenjava)
        f.close()
        print("fin proceso")

    
    def javaFile(self,nombre:str, atributos:dict, ):
        f = open(nombre+".java", 'w')
        pass

    def leerFormatoJava(self):
        try:
            with open('formtAuraBoot.json', 'r') as file:
                dict_valor_compuesto = json.load(file)          
            return dict_valor_compuesto
        except FileNotFoundError as e:
            print("Error leyendo el formato: "+ e)

    def extrarJavaAtributos(self,dict_valor_compuesto:dict):
        head:str = "public class {entity} "
        base:str= self.espacio+"private {tipo} {nombre} ;"
        atributos:str = head.format(entity=dict_valor_compuesto["head"]["entity"]+" {")
        # primera Capa Atributos 
        # TODO: hacer un format para las claves de extracción de estructura
        for(key, value) in dict_valor_compuesto["atributos"].items():
            #print(key +": "+ value["type"] )
            tmp = base.format(tipo=value["type"],nombre=key )
            atributos= atributos+"\n"+tmp
        return atributos

    #############################!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def startCreacionJava(self):
        ruta = "domine"

        claseCompleta:str = ""
        jsonFormat = CreateJava.leerFormatoJava(self)
        #self.extrarJavaAtributos(jsonFormat)
        imports: str = self.agregarImports(jsonFormat["head"],ruta)
        clase: str = self.extrarJavaAtributos(jsonFormat)
        constructor:str = self.agregaCosntructor(jsonFormat["head"])
        getters:str=  self.agregaGet(jsonFormat["atributos"])
        setters:str=  self. agregaSet(jsonFormat["atributos"])

        claseCompleta = imports+clase+constructor+getters+setters+self.llaveCerrada

        CreateJava.saveFilebyDir(self,contenjava=claseCompleta,routeDir=ruta,nombre=jsonFormat["head"]["entity"] )
        print(claseCompleta)
        

    def agregaCosntructor(self,atributos:dict):
        baseConstructo:str ="\n"+ self.espacio+"public {entity} ()"
        constructor:str = baseConstructo.format( entity=atributos["entity"].capitalize())+self.cierre
        return constructor

    def agregaGet(self,atributos:dict):
        baseGet:str = self.espacio+" public {tipo} get{atributo}() "
        getters: str = ""
        for(key,value) in atributos.items():
            #print(key + " "+ value["type"])
            getters = getters + baseGet.format(tipo=  value["type"],atributo=key.capitalize()) + self.cierre
        return getters

    def agregaSet(self,atributos:dict):
        baseGet:str = self.espacio+" public {tipo} set{atributo}() "
        setters: str = ""
        for(key,value) in atributos.items():
            #print(key + " "+ value["type"])
            setters = setters + baseGet.format(tipo=  value["type"],atributo=key.capitalize()) + self.cierre
        return setters
    
    def agregarImports(self,head:dict,ruta:str):
        print(head)
        pacake = "package {package}.{dir} ;".format(package=head["package"],dir=ruta)+"\n \n \n"

        imports:str = pacake
        return imports
        

my_class = CrearJavaClass()
#my_class.say_hello()
#my_class.crearArchiv( "java", "asldmas", "sadasd")
my_class.startCreacionJava()