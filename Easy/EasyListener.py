# Generated from /home/lukas/Documents/kompilator/compiler/Easy.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .EasyParser import EasyParser
else:
    from EasyParser import EasyParser

# This class defines a complete listener for a parse tree produced by EasyParser.
class EasyListener(ParseTreeListener):

    # Enter a parse tree produced by EasyParser#compileUnit.
    def enterCompileUnit(self, ctx:EasyParser.CompileUnitContext):
        pass

    # Exit a parse tree produced by EasyParser#compileUnit.
    def exitCompileUnit(self, ctx:EasyParser.CompileUnitContext):
        pass


    # Enter a parse tree produced by EasyParser#d_type.
    def enterD_type(self, ctx:EasyParser.D_typeContext):
        pass

    # Exit a parse tree produced by EasyParser#d_type.
    def exitD_type(self, ctx:EasyParser.D_typeContext):
        pass


    # Enter a parse tree produced by EasyParser#a_type.
    def enterA_type(self, ctx:EasyParser.A_typeContext):
        pass

    # Exit a parse tree produced by EasyParser#a_type.
    def exitA_type(self, ctx:EasyParser.A_typeContext):
        pass


    # Enter a parse tree produced by EasyParser#block.
    def enterBlock(self, ctx:EasyParser.BlockContext):
        pass

    # Exit a parse tree produced by EasyParser#block.
    def exitBlock(self, ctx:EasyParser.BlockContext):
        pass


    # Enter a parse tree produced by EasyParser#test.
    def enterTest(self, ctx:EasyParser.TestContext):
        pass

    # Exit a parse tree produced by EasyParser#test.
    def exitTest(self, ctx:EasyParser.TestContext):
        pass


    # Enter a parse tree produced by EasyParser#or_test.
    def enterOr_test(self, ctx:EasyParser.Or_testContext):
        pass

    # Exit a parse tree produced by EasyParser#or_test.
    def exitOr_test(self, ctx:EasyParser.Or_testContext):
        pass


    # Enter a parse tree produced by EasyParser#and_test.
    def enterAnd_test(self, ctx:EasyParser.And_testContext):
        pass

    # Exit a parse tree produced by EasyParser#and_test.
    def exitAnd_test(self, ctx:EasyParser.And_testContext):
        pass


    # Enter a parse tree produced by EasyParser#not_test.
    def enterNot_test(self, ctx:EasyParser.Not_testContext):
        pass

    # Exit a parse tree produced by EasyParser#not_test.
    def exitNot_test(self, ctx:EasyParser.Not_testContext):
        pass


    # Enter a parse tree produced by EasyParser#comparison.
    def enterComparison(self, ctx:EasyParser.ComparisonContext):
        pass

    # Exit a parse tree produced by EasyParser#comparison.
    def exitComparison(self, ctx:EasyParser.ComparisonContext):
        pass


    # Enter a parse tree produced by EasyParser#comp_op.
    def enterComp_op(self, ctx:EasyParser.Comp_opContext):
        pass

    # Exit a parse tree produced by EasyParser#comp_op.
    def exitComp_op(self, ctx:EasyParser.Comp_opContext):
        pass


    # Enter a parse tree produced by EasyParser#expr.
    def enterExpr(self, ctx:EasyParser.ExprContext):
        pass

    # Exit a parse tree produced by EasyParser#expr.
    def exitExpr(self, ctx:EasyParser.ExprContext):
        pass


    # Enter a parse tree produced by EasyParser#arith_expr.
    def enterArith_expr(self, ctx:EasyParser.Arith_exprContext):
        pass

    # Exit a parse tree produced by EasyParser#arith_expr.
    def exitArith_expr(self, ctx:EasyParser.Arith_exprContext):
        pass


    # Enter a parse tree produced by EasyParser#term.
    def enterTerm(self, ctx:EasyParser.TermContext):
        pass

    # Exit a parse tree produced by EasyParser#term.
    def exitTerm(self, ctx:EasyParser.TermContext):
        pass


    # Enter a parse tree produced by EasyParser#factor.
    def enterFactor(self, ctx:EasyParser.FactorContext):
        pass

    # Exit a parse tree produced by EasyParser#factor.
    def exitFactor(self, ctx:EasyParser.FactorContext):
        pass


    # Enter a parse tree produced by EasyParser#access.
    def enterAccess(self, ctx:EasyParser.AccessContext):
        pass

    # Exit a parse tree produced by EasyParser#access.
    def exitAccess(self, ctx:EasyParser.AccessContext):
        pass


    # Enter a parse tree produced by EasyParser#default.
    def enterDefault(self, ctx:EasyParser.DefaultContext):
        pass

    # Exit a parse tree produced by EasyParser#default.
    def exitDefault(self, ctx:EasyParser.DefaultContext):
        pass


    # Enter a parse tree produced by EasyParser#creator.
    def enterCreator(self, ctx:EasyParser.CreatorContext):
        pass

    # Exit a parse tree produced by EasyParser#creator.
    def exitCreator(self, ctx:EasyParser.CreatorContext):
        pass


    # Enter a parse tree produced by EasyParser#trailer.
    def enterTrailer(self, ctx:EasyParser.TrailerContext):
        pass

    # Exit a parse tree produced by EasyParser#trailer.
    def exitTrailer(self, ctx:EasyParser.TrailerContext):
        pass


    # Enter a parse tree produced by EasyParser#atom.
    def enterAtom(self, ctx:EasyParser.AtomContext):
        pass

    # Exit a parse tree produced by EasyParser#atom.
    def exitAtom(self, ctx:EasyParser.AtomContext):
        pass


    # Enter a parse tree produced by EasyParser#stmt.
    def enterStmt(self, ctx:EasyParser.StmtContext):
        pass

    # Exit a parse tree produced by EasyParser#stmt.
    def exitStmt(self, ctx:EasyParser.StmtContext):
        pass


    # Enter a parse tree produced by EasyParser#s_stmt.
    def enterS_stmt(self, ctx:EasyParser.S_stmtContext):
        pass

    # Exit a parse tree produced by EasyParser#s_stmt.
    def exitS_stmt(self, ctx:EasyParser.S_stmtContext):
        pass


    # Enter a parse tree produced by EasyParser#expr_stmt.
    def enterExpr_stmt(self, ctx:EasyParser.Expr_stmtContext):
        pass

    # Exit a parse tree produced by EasyParser#expr_stmt.
    def exitExpr_stmt(self, ctx:EasyParser.Expr_stmtContext):
        pass


    # Enter a parse tree produced by EasyParser#c_stmt.
    def enterC_stmt(self, ctx:EasyParser.C_stmtContext):
        pass

    # Exit a parse tree produced by EasyParser#c_stmt.
    def exitC_stmt(self, ctx:EasyParser.C_stmtContext):
        pass


    # Enter a parse tree produced by EasyParser#for_stmt.
    def enterFor_stmt(self, ctx:EasyParser.For_stmtContext):
        pass

    # Exit a parse tree produced by EasyParser#for_stmt.
    def exitFor_stmt(self, ctx:EasyParser.For_stmtContext):
        pass


    # Enter a parse tree produced by EasyParser#while_stmt.
    def enterWhile_stmt(self, ctx:EasyParser.While_stmtContext):
        pass

    # Exit a parse tree produced by EasyParser#while_stmt.
    def exitWhile_stmt(self, ctx:EasyParser.While_stmtContext):
        pass


    # Enter a parse tree produced by EasyParser#if_stmt.
    def enterIf_stmt(self, ctx:EasyParser.If_stmtContext):
        pass

    # Exit a parse tree produced by EasyParser#if_stmt.
    def exitIf_stmt(self, ctx:EasyParser.If_stmtContext):
        pass


    # Enter a parse tree produced by EasyParser#flow_stmt.
    def enterFlow_stmt(self, ctx:EasyParser.Flow_stmtContext):
        pass

    # Exit a parse tree produced by EasyParser#flow_stmt.
    def exitFlow_stmt(self, ctx:EasyParser.Flow_stmtContext):
        pass


    # Enter a parse tree produced by EasyParser#break_stmt.
    def enterBreak_stmt(self, ctx:EasyParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by EasyParser#break_stmt.
    def exitBreak_stmt(self, ctx:EasyParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by EasyParser#continue_stmt.
    def enterContinue_stmt(self, ctx:EasyParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by EasyParser#continue_stmt.
    def exitContinue_stmt(self, ctx:EasyParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by EasyParser#return_stmt.
    def enterReturn_stmt(self, ctx:EasyParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by EasyParser#return_stmt.
    def exitReturn_stmt(self, ctx:EasyParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by EasyParser#varargslist.
    def enterVarargslist(self, ctx:EasyParser.VarargslistContext):
        pass

    # Exit a parse tree produced by EasyParser#varargslist.
    def exitVarargslist(self, ctx:EasyParser.VarargslistContext):
        pass


    # Enter a parse tree produced by EasyParser#argslist.
    def enterArgslist(self, ctx:EasyParser.ArgslistContext):
        pass

    # Exit a parse tree produced by EasyParser#argslist.
    def exitArgslist(self, ctx:EasyParser.ArgslistContext):
        pass


    # Enter a parse tree produced by EasyParser#parameters.
    def enterParameters(self, ctx:EasyParser.ParametersContext):
        pass

    # Exit a parse tree produced by EasyParser#parameters.
    def exitParameters(self, ctx:EasyParser.ParametersContext):
        pass


    # Enter a parse tree produced by EasyParser#varparameters.
    def enterVarparameters(self, ctx:EasyParser.VarparametersContext):
        pass

    # Exit a parse tree produced by EasyParser#varparameters.
    def exitVarparameters(self, ctx:EasyParser.VarparametersContext):
        pass


    # Enter a parse tree produced by EasyParser#listparameters.
    def enterListparameters(self, ctx:EasyParser.ListparametersContext):
        pass

    # Exit a parse tree produced by EasyParser#listparameters.
    def exitListparameters(self, ctx:EasyParser.ListparametersContext):
        pass


    # Enter a parse tree produced by EasyParser#funcdef.
    def enterFuncdef(self, ctx:EasyParser.FuncdefContext):
        pass

    # Exit a parse tree produced by EasyParser#funcdef.
    def exitFuncdef(self, ctx:EasyParser.FuncdefContext):
        pass


