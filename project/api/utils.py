from antlr4 import *
from lenguaje.GrammarLexer import GrammarLexer
from lenguaje.GrammarParser import GrammarParser
import io
import sys
from lenguaje.MyVisitor import MyVisitor

def run_code(code:str):
    input_stream = InputStream(code)
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.program()

    # Capturan la salida
    old_stdout = sys.stdout()
    buf = io.StringIO()
    sys.stdout = buf
    run_code
    
    # Crear un objeto de Visitor
    visitor = MyVisitor()
    # Visitar el árbol
    visitor.visit(tree)
    # Capturamos la salida
    output = buf.getvalue()
    
    return output


