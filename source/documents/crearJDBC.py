import os
import json
from utils import CreateJava
from variables import Variables 

class CrearJavaJdbc:

    def __init__(self):
        self.variables = Variables()
        self.name = "Archivos JAVA"
        self.espacio = "     "
        self.cierre = " {"+"\n }"+"\n"
        self.llaveCerrada ="\n"+" } "
        self.llaveCerrada ="\n"+" } "
        self.nombreClassConfiguration = "JdbcTemplateConfig"


    def crearConfiguracion(self, head:dict,ruta:str):

        pacake:str = "package {package}.{dir} ;".format(package=head["package"],dir=ruta)+"\n \n \n"
        data:str ="""
        import org.springframework.beans.factory.annotation.Autowired;
        import org.springframework.context.annotation.Bean;
        import org.springframework.context.annotation.Configuration;
        import org.springframework.jdbc.core.JdbcTemplate;

        @Configuration
        public class JdbcTemplateConfig {
            @Autowired
            private DataSource dataSource;

            @Bean
            public JdbcTemplate jdbcTemplate() {
                return new JdbcTemplate(dataSource);
            }
        }"""

        return str(pacake + data)
    

    def organizarAtributosRowMapper(self,data:dict):
        atributos :str = ""
        for(key, value )in data["atributos"].items():
            atributos=atributos +"\n"+  str(self.variables.atributeRowMapper).format(
                nameClass=data["head"]["entity"],
                atributoUp =str(key).capitalize(),
                type = str(value["type"]).capitalize(),
                atributo= str(key)
            )
            
        return atributos
        
        
    
    def crearConsultaSelect(self,data:dict):
        consulta:str = str(self.variables.selectQuery).format(
            nameClassUp=str( data["head"]["entity"]).capitalize(),
            schema = data["head"]["schema"],
            nameClass= str(data["head"]["entity"])
        )

        atributos:str= self.organizarAtributosRowMapper(data)
        rowMapper:str = str(self.variables.rowMapper).format(
            nameClass =data["head"]["entity"],
            nameClassUp = str(data["head"]["entity"]).capitalize(),
            Atributos = atributos
        )
        
        return str(consulta +rowMapper)


    def crearConsultaCreate(self):
        pass
    def crearConsultaUpdatePorID(self):
        pass
    def crearConsultaDeletePorId(self):
        pass


    def createFileConfiguration(self,data:dict,ruta:str="JDBC"):
        archivoConfiguracion:str = self.crearConfiguracion(head=data["head"],ruta=ruta)

        CreateJava.saveFilebyDir(self,contenjava=archivoConfiguracion,routeDir=ruta,nombre="JdbcTemplateConfig")

        self.crearConsultaSelect(data)
    ## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def startCreacionJdbc(self):
        ruta:str = "JDBC"
        data:dict = CreateJava.leerFormatoJava(self)
        # Crear el archivo de 
        self.createFileConfiguration(data=data)

        claseCompleta:str = self.crearConsultaSelect(data)
        nombre:str= str(data["head"]["entity"])+"DAO"
        CreateJava.saveFilebyDir(self,contenjava=claseCompleta,routeDir=ruta,nombre=nombre )

       



clase = CrearJavaJdbc()
clase.startCreacionJdbc()