from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos

class var_asignacion(NodoArbol):

    def __init__(self, identificador, exp, line, coliumn):
        super().__init__(line, coliumn)
        self.exp = exp
        self.identificador = identificador

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        tmp = entorno.obtener_temporal_deVar(str(self.identificador))
        val:Valor = self.exp.getValueAbstract(entorno, arbol)
        if str(val.tipo) == '2':
            arbol.addC3D(tmp + ' = ' + '\'' + str(val.data) + '\'')
        else:
            arbol.addC3D(tmp + ' = ' + str(val.data))
        return

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass
