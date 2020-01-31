# Generated from /home/lukas/Documents/kompilator/compiler/Easy.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .EasyParser import EasyParser
else:
    from EasyParser import EasyParser

# This class defines a complete generic visitor for a parse tree produced by EasyParser.

class EasyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EasyParser#compileUnit.
    def visitCompileUnit(self, ctx:EasyParser.CompileUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#d_type.
    def visitD_type(self, ctx:EasyParser.D_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#a_type.
    def visitA_type(self, ctx:EasyParser.A_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#block.
    def visitBlock(self, ctx:EasyParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#test.
    def visitTest(self, ctx:EasyParser.TestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#or_test.
    def visitOr_test(self, ctx:EasyParser.Or_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#and_test.
    def visitAnd_test(self, ctx:EasyParser.And_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#not_test.
    def visitNot_test(self, ctx:EasyParser.Not_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#comparison.
    def visitComparison(self, ctx:EasyParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#comp_op.
    def visitComp_op(self, ctx:EasyParser.Comp_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#expr.
    def visitExpr(self, ctx:EasyParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#arith_expr.
    def visitArith_expr(self, ctx:EasyParser.Arith_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#term.
    def visitTerm(self, ctx:EasyParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#factor.
    def visitFactor(self, ctx:EasyParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#access.
    def visitAccess(self, ctx:EasyParser.AccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#default.
    def visitDefault(self, ctx:EasyParser.DefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#creator.
    def visitCreator(self, ctx:EasyParser.CreatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#trailer.
    def visitTrailer(self, ctx:EasyParser.TrailerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#atom.
    def visitAtom(self, ctx:EasyParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#stmt.
    def visitStmt(self, ctx:EasyParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#s_stmt.
    def visitS_stmt(self, ctx:EasyParser.S_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#expr_stmt.
    def visitExpr_stmt(self, ctx:EasyParser.Expr_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#c_stmt.
    def visitC_stmt(self, ctx:EasyParser.C_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#for_stmt.
    def visitFor_stmt(self, ctx:EasyParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#while_stmt.
    def visitWhile_stmt(self, ctx:EasyParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#if_stmt.
    def visitIf_stmt(self, ctx:EasyParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#flow_stmt.
    def visitFlow_stmt(self, ctx:EasyParser.Flow_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#break_stmt.
    def visitBreak_stmt(self, ctx:EasyParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#continue_stmt.
    def visitContinue_stmt(self, ctx:EasyParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#return_stmt.
    def visitReturn_stmt(self, ctx:EasyParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#varargslist.
    def visitVarargslist(self, ctx:EasyParser.VarargslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#argslist.
    def visitArgslist(self, ctx:EasyParser.ArgslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#parameters.
    def visitParameters(self, ctx:EasyParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#varparameters.
    def visitVarparameters(self, ctx:EasyParser.VarparametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#listparameters.
    def visitListparameters(self, ctx:EasyParser.ListparametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyParser#funcdef.
    def visitFuncdef(self, ctx:EasyParser.FuncdefContext):
        return self.visitChildren(ctx)



del EasyParser