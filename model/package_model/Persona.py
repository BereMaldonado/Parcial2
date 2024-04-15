import model.package_model.Database as Database
class Persona:
    def __init__(self, idpersona='', curp='', nombre='', paterno='', materno='', telefono='', celular='', correo=''):
        self.__idpersona=idpersona
        self.__curp=curp
        self.__nombre=nombre
        self.__paterno=paterno
        self.__materno=materno
        self.__telefono=telefono
        self.__celular=celular
        self.__correo=correo
        
    def obtener_personas(self):
        conexion = Database.Database()
        persona = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT IDPERSONA, CURP, NOMBRE, PATERNO, MATERNO, TELEFONO, CELULAR, CORREO FROM persona")
            persona = cursor.fetchall()
        conexion.conn.close()
        return persona
    
    def obtener_persona_por_id(self, id):
        conexion = conexion = Database.Database()
        persona = None
        with conexion.cursor as cursor:
            cursor.execute(
                "SELECT IDPERSONA, CURP, NOMBRE, PATERNO, MATERNO, TELEFONO, CELULAR, CORREO FROM persona WHERE IDPERSONA= %s",(id))
            persona = cursor.fetchone()
        conexion.conn.close()
        return persona