import model.package_model.Database as Database
class Tramitante:
    def __init__(self, idtramitante='', nombreCompleto=''):
        self.__idtramitante=idtramitante
        self.__nombreCompleto=nombreCompleto
        
    def obtener_tramitantes(self):
        conexion = Database.Database()
        tramitante = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT IDTRAMITANTE, NOMBRECOMPLETO FROM tramitante")
            tramitantes = cursor.fetchall()
        conexion.conn.close()
        return tramitantes
    
    def obtener_tramitante_por_id(self,id):
        conexion = conexion = Database.Database()
        tramitante = None
        with conexion.cursor as cursor:
            cursor.execute(
                "SELECT IDTRAMITANTE,NOMBRECOMPLETO FROM tramitante WHERE IDTRAMITANTE = %s",(id))
            tramitante = cursor.fetchone()
        conexion.conn.close()
        return tramitante