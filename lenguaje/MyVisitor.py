from GrammarVisitor import GrammarVisitor
from GrammarParser import GrammarParser

class MyVisitor(GrammarVisitor):
    def __init__(self):
        self.memory = {}
        
    #Definimos la assing
    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value
        
    # Definimos print
    def visitPrin(self, ctx):
        value = self.visit(ctx.expr())
        print(value)