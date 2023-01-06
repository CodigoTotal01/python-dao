

from loggin import logger_base as log

class Conexion:
    # varibles de clase
    _DATABASE = "test_db"
    _USERNAME = "postgres"
    _PASSWORD = "admin"
    _DB_PORT = "5432"
    _HOST = "127.0.0.1"

    # para la conexion en si -> singleton
    _conexion = None
    #permite realizar las acciones dao
    _cursor =None

    #! si ya tenenmos una conecion no lo cremos
    @classmethod
    def obtenerConexion(cls):
        try:
            cls._conexion = bd.connect
        except Exception as e:
            log.debug(f'Ocucrrio una exepcion')
