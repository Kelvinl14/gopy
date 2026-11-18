# Generated from Gopy.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GopyParser import GopyParser
else:
    from GopyParser import GopyParser

# This class defines a complete listener for a parse tree produced by GopyParser.
class GopyListener(ParseTreeListener):

    # Enter a parse tree produced by GopyParser#program.
    def enterProgram(self, ctx:GopyParser.ProgramContext):
        pass

    # Exit a parse tree produced by GopyParser#program.
    def exitProgram(self, ctx:GopyParser.ProgramContext):
        pass


    # Enter a parse tree produced by GopyParser#statement.
    def enterStatement(self, ctx:GopyParser.StatementContext):
        pass

    # Exit a parse tree produced by GopyParser#statement.
    def exitStatement(self, ctx:GopyParser.StatementContext):
        pass


    # Enter a parse tree produced by GopyParser#varDecl.
    def enterVarDecl(self, ctx:GopyParser.VarDeclContext):
        pass

    # Exit a parse tree produced by GopyParser#varDecl.
    def exitVarDecl(self, ctx:GopyParser.VarDeclContext):
        pass


    # Enter a parse tree produced by GopyParser#type.
    def enterType(self, ctx:GopyParser.TypeContext):
        pass

    # Exit a parse tree produced by GopyParser#type.
    def exitType(self, ctx:GopyParser.TypeContext):
        pass


    # Enter a parse tree produced by GopyParser#ifStmt.
    def enterIfStmt(self, ctx:GopyParser.IfStmtContext):
        pass

    # Exit a parse tree produced by GopyParser#ifStmt.
    def exitIfStmt(self, ctx:GopyParser.IfStmtContext):
        pass


    # Enter a parse tree produced by GopyParser#whileStmt.
    def enterWhileStmt(self, ctx:GopyParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by GopyParser#whileStmt.
    def exitWhileStmt(self, ctx:GopyParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by GopyParser#functionDecl.
    def enterFunctionDecl(self, ctx:GopyParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by GopyParser#functionDecl.
    def exitFunctionDecl(self, ctx:GopyParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by GopyParser#block.
    def enterBlock(self, ctx:GopyParser.BlockContext):
        pass

    # Exit a parse tree produced by GopyParser#block.
    def exitBlock(self, ctx:GopyParser.BlockContext):
        pass


    # Enter a parse tree produced by GopyParser#params.
    def enterParams(self, ctx:GopyParser.ParamsContext):
        pass

    # Exit a parse tree produced by GopyParser#params.
    def exitParams(self, ctx:GopyParser.ParamsContext):
        pass


    # Enter a parse tree produced by GopyParser#param.
    def enterParam(self, ctx:GopyParser.ParamContext):
        pass

    # Exit a parse tree produced by GopyParser#param.
    def exitParam(self, ctx:GopyParser.ParamContext):
        pass


    # Enter a parse tree produced by GopyParser#returnStmt.
    def enterReturnStmt(self, ctx:GopyParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by GopyParser#returnStmt.
    def exitReturnStmt(self, ctx:GopyParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by GopyParser#assignment.
    def enterAssignment(self, ctx:GopyParser.AssignmentContext):
        pass

    # Exit a parse tree produced by GopyParser#assignment.
    def exitAssignment(self, ctx:GopyParser.AssignmentContext):
        pass


    # Enter a parse tree produced by GopyParser#expr.
    def enterExpr(self, ctx:GopyParser.ExprContext):
        pass

    # Exit a parse tree produced by GopyParser#expr.
    def exitExpr(self, ctx:GopyParser.ExprContext):
        pass


    # Enter a parse tree produced by GopyParser#args.
    def enterArgs(self, ctx:GopyParser.ArgsContext):
        pass

    # Exit a parse tree produced by GopyParser#args.
    def exitArgs(self, ctx:GopyParser.ArgsContext):
        pass



del GopyParser