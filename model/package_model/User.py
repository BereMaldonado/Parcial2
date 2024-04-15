import model.package_model.Database as Database
class User:
    def __init__(self, iduser='', user='', password='', rol=''):
        self.__iduser=iduser
        self.__user=user
        self.__password=password
        self.__rol=rol
      
    def update_user(self, obj_asp):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                query="update user set USER=%s where IDUSER=%s"
                vals=(obj_asp.__user,obj_asp.__iduser)
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
                
    def eliminar_user(self,id):
        affected=0
        conexion = Database.Database()
        with conexion.cursor as cursor:
            affected=cursor.execute("DELETE FROM user WHERE IDUSER = %s", (id))
        conexion.conn.commit()
        conexion.conn.close()
        return affected
    
    def insertar_user(self, obj_asp):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                query="INSERT INTO user(USER) VALUES (%s)"
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
    
        
    def obtener_users(self):
        conexion = Database.Database()
        user = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT IDUSER, USER, PASSWORD, ROL FROM user")
            users = cursor.fetchall()
        conexion.conn.close()
        return users
    
    def obtener_user_por_id(self,id):
        conexion = conexion = Database.Database()
        user = None
        with conexion.cursor as cursor:
            cursor.execute(
                "SELECT IDUSER, USER, PASSWORD, ROL FROM user WHERE IDUSER = %s",(id))
            user = cursor.fetchone()
        conexion.conn.close()
        return user