import model.package_model.Database as Database
class Asunto:
    def __init__(self, idasunto='', descripcion=''):
        self.__idasunto=idasunto
        self.__descripcion=descripcion
        
    def update_asunto(self, obj_asp):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                query="update asunto set DESCRIPCION=%s where IDASUNTO=%s"
                vals=(obj_asp.__descripcion,obj_asp.__idasunto)
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
                
    def eliminar_asunto(self,id):
        affected=0
        conexion = Database.Database()
        with conexion.cursor as cursor:
            affected=cursor.execute("DELETE FROM asunto WHERE IDASUNTO = %s", (id))
        conexion.conn.commit()
        conexion.conn.close()
        return affected
    
    def insertar_asunto(self, obj_asp):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                query="INSERT INTO asunto(DESCRIPCION) VALUES (%s)"
                vals=(obj_asp.__descripcion)
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
                
    def obtener_asuntos(self):
        conexion = Database.Database()
        asunto = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT IDASUNTO, DESCRIPCION FROM asunto")
            asunto = cursor.fetchall()
        conexion.conn.close()
        return asunto
    
    def obtener_asunto_por_id(self,id):
        conexion = conexion = Database.Database()
        asunto = None
        with conexion.cursor as cursor:
            cursor.execute(
                "SELECT IDASUNTO,DESCRIPCION FROM asunto WHERE IDASUNTO = %s",(id))
            asuntos = cursor.fetchone()
        conexion.conn.close()
        return asuntos