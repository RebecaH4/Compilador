from GrammarVisitor import GrammarVisitor
from GrammarParser import GrammarParser

class MyVisitor(GrammarVisitor):
    # Define la memoria o el entorno
    def __init__(self):
        self.memory = {}
        
    #Define la assing
    def visitAssign(self, ctx):
        # Se obtiene el id o nombre de la variable
        name = ctx.ID().getText()
        # Se obtiene el valor de la variable (Numerico o una expresion)
        value = self.visit(ctx.expr())
        # Se almacena en memoria a partir del nombre y el valor
        self.memory[name] = value
        
    # Define print
    def visitPrin(self, ctx):
        # Se define la expresion a mostrar
        value = self.visit(ctx.expr())
        # Se imprime el valor
        print(value)
        
    # Definir las expresiones
    def visitExpr(self, ctx):
        # Busta si existen IDs
        if ctx.ID():
            # Obtiene el contexto del nombre de la variable 
            name = ctx.ID().getText()
            # Si el nombre de la variable no esta, lanza un error
            if name not in self.memory:
                raise NameError(f"Variable {name} no definida")
            # Si existe el nombre retorna la variable
            return self.memory[name]
        # Busca el operador 
        elif ctx.op:
            # Visita y obtiene lado derecho e izquierdo
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            # Evalua la operacion
            if ctx.op.text == '+':
                return left + right
            elif ctx.op.text == '-':
                return left - right
            elif ctx.op.text == '*':
                return left * right
            elif ctx.op.text == '/':
                # Verifica la division por cero
                if right == 0:
                    raise ValueError("Division por cero")
                return left / right
        