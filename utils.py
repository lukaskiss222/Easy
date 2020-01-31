import llvmlite.ir as ir
from Easy.EasyParser import EasyParser
import sys

def getDtype(ctx):
    """
    Get type from terminal
    :param ctx:
    :return:
    """
    if ctx.T_INT() is not None:
        return ir.IntType(32)
    if ctx.T_CHAR() is not None:
        return ir.IntType(8)
    if ctx.T_BOOL() is not None:
        return ir.IntType(1)
    if ctx.T_STR() is not None:
        return ir.IntType(8).as_pointer()
    if ctx.T_VOID() is not None:
        return ir.VoidType()
    raise ValueError("Doesn't know the type")


def getAtype(ctx: EasyParser.A_typeContext):
    """
    Return advaced type => pointer to normal type
    :param ctx:
    :return:
    """
    ret = getDtype(ctx.d_type())
    for _ in range(len(ctx.children) - 1):
        ret = ret.as_pointer()
    return ret


def getVarArgList(ctx: EasyParser.VarargslistContext):
    """
    Return list with names and for each name its advanced type
    :param ctx:
    :return:
    """
    ret = []
    i = 0
    if ctx is None:
        return ret
    while True:
        if ctx.NAME(i) is None:
            break
        typ = getAtype(ctx.a_type(i))
        ret.append((str(ctx.NAME(i)),
                    typ))
        i += 1
    return ret


def printError(ctx, string=None):
    """
    Print error message
    :param ctx:
    :param string:
    :return:
    """
    if string is None:
        print("[-] Error occured at:")
    else:
        print("[-] Error: ", string)
    print("On text: {}".format(ctx.start.text))
    print("On line: {}".format(ctx.start.line))
    print("On column: {}".format(ctx.start.column))


class FuncSymb(object):
    """
    Takes care of symbolic table
    """
    def __init__(self) -> None:
        self._func_symb = {}

    def set(self, ctx, name, addr):
        ret = self._func_symb.get(name)
        if ret is not None:
            printError(ctx, "Variable {} already declared!".format(
                name
            ))
            sys.exit(0)
        self._func_symb[name] = addr

    def get(self, ctx,  name):
        ret = self._func_symb.get(name)
        if ret is None:
            printError(ctx, "Variable {} is not declared!!!!".format(
                name
            ))
            sys.exit(0)
        return ret

    def reset(self):
        self._func_symb = {}

    def pop(self, name):
        self._func_symb.pop(name)
