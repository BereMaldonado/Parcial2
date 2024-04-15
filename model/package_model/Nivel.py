import model.package_model.Database as Database
class Nivel:
    def __init__(self, idnivel='', nivel=''):
        self.__idnivel=idnivel
        self.__nivel=nivel
        
    def update_nivel(self, obj_asp):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                query="update nivel set NIVEL=%s where IDNIVEL=%s"
                vals=(obj_asp.__nivel,obj_asp.__idnivel)
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
                
    def eliminar_nivel(self,id):
        affected=0
        conexion = Database.Database()
        with conexion.cursor as cursor:
            affected=cursor.execute("DELETE FROM nivel WHERE IDNIVEL = %s", (id))
        conexion.conn.commit()
        conexion.conn.close()
        return affected
    
    def insertar_nivel(self, obj_asp):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                query="INSERT INTO nivel(NIVEL) VALUES (%s)"
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
    
        
    def obtener_niveles(self):
        conexion = Database.Database()
        nivel = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT IDNIVEL, NIVEL FROM nivel")
            niveles = cursor.fetchall()
        conexion.conn.close()
        return niveles
    
    def obtener_nivel_por_id(self,id):
        conexion = conexion = Database.Database()
        nivel = None
        with conexion.cursor as cursor:
            cursor.execute(
                "SELECT IDNIVEL,NIVEL FROM nivel WHERE IDNIVEL = %s",(id))
            nivel = cursor.fetchone()
        conexion.conn.close()
        return nivel