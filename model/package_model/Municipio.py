import model.package_model.Database as Database
class Municipio:
    def __init__(self, idmunicipio='', nombre=''):
        self.__idmunicipio=idmunicipio
        self.__nombre=nombre
        
    def update_municipio(self, obj_asp):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                query="update municipio set NOMBRE=%s where IDMUNICIPIO=%s"
                vals=(obj_asp.__NOMBRE,obj_asp.__idmunicipio)
                #return (query % vals) 
                affected=cursor.execute(query,vals)
                conexion.conn.commit()
                return str(cursor.rowcount)
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
            finally:
                conexion.conn.close()
                
    def eliminar_municipio(self,id):
        affected=0
        conexion = Database.Database()
        with conexion.cursor as cursor:
            affected=cursor.execute("DELETE FROM municipio WHERE IDMUNICIPIO = %s", (id))
        conexion.conn.commit()
        conexion.conn.close()
        return affected
    
    def insertar_municipio(self, obj_asp):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                query="INSERT INTO municipio(NOMBRE) VALUES (%s)"
                vals=(obj_asp.__nombre)
                #return (query % vals) 
                affected=cursor.execute(query,vals)
                conexion.conn.commit()
                return str(cursor.rowcount)
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
            finally:
                conexion.conn.close() 
        
    def obtener_municipios(self):
        conexion = Database.Database()
        municipio = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT IDMUNICIPIO, NOMBRE FROM municipio")
            municipio = cursor.fetchall()
        conexion.conn.close()
        return municipio
    
    def obtener_municipio_por_id(self, id):
        conexion = conexion = Database.Database()
        municipio = None
        with conexion.cursor as cursor:
            cursor.execute(
                "SELECT IDMUNICIPIO,NOMBRE FROM municipio WHERE IDMUNICIPIO = %s",(id))
            municipio = cursor.fetchone()
        conexion.conn.close()
        return municipio