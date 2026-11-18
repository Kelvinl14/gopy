# Generated from Gopy.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GopyParser import GopyParser
else:
    from GopyParser import GopyParser

# This class defines a complete generic visitor for a parse tree produced by GopyParser.

class GopyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GopyParser#program.
    def visitProgram(self, ctx:GopyParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopyParser#statement.
    def visitStatement(self, ctx:GopyParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopyParser#varDecl.
    def visitVarDecl(self, ctx:GopyParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopyParser#type.
    def visitType(self, ctx:GopyParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopyParser#ifStmt.
    def visitIfStmt(self, ctx:GopyParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopyParser#whileStmt.
    def visitWhileStmt(self, ctx:GopyParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopyParser#functionDecl.
    def visitFunctionDecl(self, ctx:GopyParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopyParser#block.
    def visitBlock(self, ctx:GopyParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopyParser#params.
    def visitParams(self, ctx:GopyParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopyParser#param.
    def visitParam(self, ctx:GopyParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopyParser#returnStmt.
    def visitReturnStmt(self, ctx:GopyParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopyParser#assignment.
    def visitAssignment(self, ctx:GopyParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopyParser#expr.
    def visitExpr(self, ctx:GopyParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GopyParser#args.
    def visitArgs(self, ctx:GopyParser.ArgsContext):
        return self.visitChildren(ctx)



del GopyParser