import Easy.EasyVisitor as visitor
import llvmlite.ir as ir
from Easy.EasyParser import EasyParser
import utils as utils
from ctypes import pointer, c_int, c_bool, c_char, sizeof
import sys
import copy


class LLVMCodeGenerator(visitor.EasyVisitor):


    def __init__(self, module = None, mode32 = False):

        self.int1 = ir.IntType(1)
        self.int8 = ir.IntType(8)
        self.int32 = ir.IntType(32)

        self.mode32 = mode32
        if module is None:
            self.module = ir.Module(__file__)
        else:
            self.module = module
        self.builder: ir.IRBuilder = None

        #declaring types of useful functions
        calloct = ir.FunctionType(self.int8.as_pointer(), [self.int32, self.int32])
        printft = ir.FunctionType(self.int32, [self.int8.as_pointer()], var_arg=True)
        freet = ir.FunctionType(ir.VoidType(), [self.int8.as_pointer()])
        scanft = ir.FunctionType(self.int32, [self.int8.as_pointer()], var_arg=True)
        atoit = ir.FunctionType(self.int32,[self.int8.as_pointer()])
        strcmpt = ir.FunctionType(self.int32, [self.int8.as_pointer(),
                                               self.int8.as_pointer()])
        #Loading the useful functions to our code
        self.module.declare_intrinsic("calloc", fnty=calloct)
        self.module.declare_intrinsic("printf", fnty=printft)
        self.module.declare_intrinsic("free", fnty=freet)
        self.module.declare_intrinsic("scanf", fnty=scanft)
        self.module.declare_intrinsic("atoi", fnty=atoit)
        self.module.declare_intrinsic("strcmp", fnty=strcmpt)

        # table of all declared variables
        self.funcs_symtab = utils.FuncSymb()


        #Create readint function, whichan be used by our programmer to read integers
        readintt = ir.FunctionType(self.int32,[])
        readint = ir.Function(self.module, readintt, name="readint")
        block = readint.append_basic_block("entry")
        builder = ir.IRBuilder(block)
        i = builder.alloca(self.int32, name="i")

        new_name = self.module.get_unique_name()
        string = b"%d\x00"
        my_type = ir.ArrayType(self.int8, len(string))
        glo = ir.GlobalVariable(self.module, my_type, new_name)
        glo.initializer = ir.Constant(my_type, bytearray(string))
        string = glo.gep([self.int32(0), self.int32(0)])

        scanf = self.module.get_global("scanf")
        builder.call(scanf, [string, i])
        i = builder.load(i)
        builder.ret(i)


    # Allocates a new variable on the stack
    def alloc(self, name, typ):
        with self.builder.goto_entry_block():
            return self.builder.alloca(typ, size=None, name=name)



    def generateCode(self, ctx):
        """
        Python doesn;t support directly visitor pattern,
        so this function get type of argument and call appropiate function

        :param ctx:
        :return:
        """
        method = 'visit' + ctx.__class__.__name__.replace("Context", "")
        return getattr(self, method)(ctx)

    def visitExpr_stmt(self, ctx: EasyParser.Expr_stmtContext):
        """
        Main function, which takes care of calculating or calling statemants
        :param ctx:
        :return:
        """
        name = str(ctx.NAME())

        # This part checks if we want to dealocate ofcreated array
        if ctx.DEL() is not None:
            addr = self.funcs_symtab.get(ctx, name)
            addr = self.builder.load(addr)
            if ctx.listparameters() is not None:
                param = self.generateCode(ctx.listparameters())
                for par in param:
                    addr = self.builder.gep(addr, [par])
                    addr = self.builder.load(addr)
            addr = self.builder.bitcast(addr, self.int8.as_pointer())
            free = self.module.get_global("free")
            self.builder.call(free, [addr])
            return

        #This parts checks for array of default type declaration
        if (ctx.DOUBE_DOT() is not None) and (ctx.test() is None):
            my_type = utils.getAtype(ctx.a_type())

            if ctx.default() is None:
                addr = self.alloc(name, my_type)
                self.funcs_symtab.set(ctx, name, addr)
                return
            else:
                if my_type.is_pointer:
                    if self.mode32:
                        block_size = 4
                    else:
                        block_size = 8
                else:
                    block_size = my_type.width//8
                block_size = ir.Constant(self.int32, block_size)
                number = self.generateCode(ctx.default())
                calloc = self.module.get_global("calloc")
                allo = self.builder.call(calloc, [number, block_size])
                allo = self.builder.bitcast(allo, my_type.as_pointer())
                addr = self.alloc(name, my_type.as_pointer())
                self.builder.store(allo, addr)
                self.funcs_symtab.set(ctx, name, addr)
                return

        #This part is reposible for basic aritmetic statetes traslations and
        #declaring and setting variables
        if ctx.test() is not None:
            to_store = None
            if ctx.a_type() is not None:
                my_type = utils.getAtype(ctx.a_type())
                addr2 = self.alloc(name, my_type)
                self.funcs_symtab.set(ctx, name, addr2)
                to_store = addr2
            elif ctx.listparameters() is not None:
                to_store = self.funcs_symtab.get(ctx, name)
                param = self.generateCode(ctx.listparameters())
                for par in param:
                    to_store = self.builder.load(to_store)
                    to_store = self.builder.gep(to_store, [par])
            else:
                to_store = self.funcs_symtab.get(ctx, name)

            addr = self.generateCode(ctx.test())

            self.builder.store(addr, to_store)
            return

        # This part traslates basic one line call functions
        if ctx.parameters() is not None:
            func = self.module.get_global(name)
            param = self.generateCode(ctx.parameters())
            self.builder.call(func, param)
            return
        raise ValueError("Can not parser expression")


    def visitFuncdef(self, ctx: EasyParser.FuncdefContext):
        """
        This function handles function traslation
        :param ctx:
        :return:
        """
        #It resets symbolic table -> so no global variables are allowed
        self.funcs_symtab.reset()
        funcname = str(ctx.NAME())
        param = utils.getVarArgList(ctx.varparameters().varargslist())
        arg_types = list(map(lambda x: x[1], param))

        functype = ir.FunctionType(
            utils.getDtype(ctx.d_type()),
            arg_types
        )

        if funcname in self.module.globals:
            utils.printError(ctx, "Function already declared")
            sys.exit(0)

        else:
            func = ir.Function(self.module, functype, funcname)

        entry = func.append_basic_block('entry')
        self.builder = ir.IRBuilder(entry)

        for i, arg in enumerate(func.args):
            alloca = self.alloc(*param[i])
            self.builder.store(arg, alloca)
            self.funcs_symtab.set(ctx, param[i][0], alloca)

        self.generateCode(ctx.block()) # Build the inner body of function

        if not self.builder.block.is_terminated:
            if functype.return_type == ir.VoidType():
                # if the function is void type, we automatcaly
                # add return void
                self.builder.ret_void()
            else:
                utils.printError(ctx, "Function :{} is not terminated!!! "
                                      "by  return statement".format(
                    funcname
                ))
                sys.exit(0)



    def visitBlock(self, ctx: EasyParser.BlockContext):
        """
        Generate code for each statement in each block
        :param ctx:
        :return:
        """
        i = 0
        while True:
            if ctx.stmt(i) is None:
                break
            self.generateCode(ctx.stmt(i))
            i += 1

    #Next three functions just passed code generation to lower parts
    #because they don't have any useful info for code generation
    def visitStmt(self, ctx: EasyParser.StmtContext):
        self.generateCode(ctx.children[0])

    def visitS_stmt(self, ctx: EasyParser.S_stmtContext):
        self.generateCode(ctx.children[0])

    def visitC_stmt(self, ctx: EasyParser.C_stmtContext):
        self.generateCode(ctx.children[0])

    def visitIf_stmt(self, ctx: EasyParser.If_stmtContext):
        """
        generate if statement code
        :param ctx:
        :return:
        """
        cond_val = self.generateCode(ctx.test())
        is_else = ctx.block(1) is not None
        cmp = self.builder.icmp_signed('!=',
                                       cond_val,
                                       ir.Constant(self.int1, 0), 'notnull')
        thenb = ir.Block(self.builder.function, 'then')
        #Do we have else statement?
        if is_else:
            elseb = ir.Block(self.builder.function, 'else')

        mergeb = ir.Block(self.builder.function, 'merge')

        if is_else:
            self.builder.cbranch(cmp, thenb, elseb)
        else:
            self.builder.cbranch(cmp, thenb, mergeb)


        #Generate then block
        self.builder.function.basic_blocks.append(thenb)
        self.builder.position_at_start(thenb)
        self.generateCode(ctx.block(0))
        # Maybe we add return statement in this block
        if not self.builder.block.is_terminated:
            self.builder.branch(mergeb)

        #Generate else block
        if is_else:
            self.builder.function.basic_blocks.append(elseb)
            self.builder.position_at_start(elseb)
            self.generateCode(ctx.block(1))
            # Maybe we add return statement in this block
            if not self.builder.block.is_terminated:
                self.builder.branch(mergeb)

        # End of if
        self.builder.function.basic_blocks.append(mergeb)
        self.builder.position_at_start(mergeb)

        return

    def visitWhile_stmt(self, ctx: EasyParser.While_stmtContext):
        """
        We generate while cycle code
        :param ctx:
        :return:
        """
        testb = ir.Block(self.builder.function, 'test')
        cycleb = ir.Block(self.builder.function, 'cycle')
        endb = ir.Block(self.builder.function, 'end')
        self.builder.branch(testb)
        # Test while
        self.builder.function.basic_blocks.append(testb)
        self.builder.position_at_start(testb)
        test_val = self.generateCode(ctx.test())
        cmp = self.builder.icmp_signed('==', test_val,
                                       ir.Constant(self.int1, 0))
        self.builder.cbranch(cmp, endb, cycleb)

        # While block
        self.builder.function.basic_blocks.append(cycleb)
        self.builder.position_at_start(cycleb)
        self.generateCode(ctx.block())
        if not self.builder.block.is_terminated:
            self.builder.branch(testb)

        # end of cycle
        self.builder.function.basic_blocks.append(endb)
        self.builder.position_at_start(endb)

        return

    def visitFor_stmt(self, ctx: EasyParser.For_stmtContext):
        """
        We generate code for fo cycle, now it just support integer
        ineration
        :param ctx:
        :return:
        """
        name = str(ctx.NAME())
        init = self.generateCode(ctx.expr(0))
        end = self.generateCode(ctx.expr(1))
        step = self.generateCode(ctx.expr(2))

        i_ptr = self.alloc(name, self.int32)
        self.builder.store(init, i_ptr)


        checkb = ir.Block(self.builder.function, 'check')
        cycleb = ir.Block(self.builder.function, 'cycle')
        endb = ir.Block(self.builder.function, 'end')

        #Jump tp loop
        self.builder.branch(checkb)
        self.funcs_symtab.set(ctx, name, i_ptr)

        #Check condition
        self.builder.function.basic_blocks.append(checkb)
        self.builder.position_at_start(checkb)
        i_value = self.builder.load(i_ptr)
        cmp = self.builder.icmp_signed('==', i_value, end, "comp")
        self.builder.cbranch(cmp, endb, cycleb)

        #Generate inner block code
        self.builder.function.basic_blocks.append(cycleb)
        self.builder.position_at_start(cycleb)
        self.generateCode(ctx.block())

        #step
        added = self.builder.add(i_value, step)
        self.builder.store(added, i_ptr)

        #Jump to loop
        self.builder.branch(checkb)

        #endblock
        self.builder.function.basic_blocks.append(endb)
        self.builder.position_at_start(endb)
        self.funcs_symtab.pop(name)

    def visitFlow_stmt(self, ctx: EasyParser.Flow_stmtContext):
        return self.generateCode(ctx.children[0])

    def visitReturn_stmt(self, ctx: EasyParser.Return_stmtContext):
        """
        Just generate ret op with the value
        :param ctx:
        :return:
        """
        if ctx.test() is not None:
            ret = self.generateCode(ctx.test())
            self.builder.ret(ret)
        else:
            self.builder.ret_void()

    def visitTest(self, ctx: EasyParser.TestContext):
        return self.generateCode(ctx.or_test())

    def visitOr_test(self, ctx: EasyParser.Or_testContext):
        ret = self.generateCode(ctx.and_test(0))
        i = 1
        while True:
            if ctx.and_test(i) is None:
                break
            ret = self.builder.or_(ret,
                                   self.generateCode(ctx.and_test(i)))

            i += 1
        return ret

    def visitAnd_test(self, ctx: EasyParser.And_testContext):
        ret = self.generateCode(ctx.not_test(0))
        i = 1
        while True:
            if ctx.not_test(i) is None:
                break
            ret = self.builder.and_(ret,
                                    self.generateCode(ctx.not_test(i)))
            i += 1
        return ret

    def visitNot_test(self, ctx: EasyParser.Not_testContext):
        if ctx.not_test() is not None:
            ret = self.generateCode(ctx.not_test())
            return self.builder.not_(ret)
        else:
            return self.generateCode(ctx.comparison())

    def visitComparison(self, ctx: EasyParser.ComparisonContext):
        """
        Generate comparision code for statement.
        Using strcmp function, we support also string comparision
        by default
        :param ctx:
        :return:
        """
        expr = self.generateCode(ctx.expr(0))
        if ctx.comp_op() is not None:
            expr2 = self.generateCode(ctx.expr(1))
            comp = ctx.comp_op().getText()
            # String Comparision
            if expr.type.is_pointer:
                strcmp = self.module.get_global("strcmp")
                expr = self.builder.call(strcmp, [expr, expr2])
                expr2 = ir.Constant(self.int32, 0)

            expr = self.builder.icmp_signed(comp, expr, expr2)

        return expr

    def visitExpr(self, ctx: EasyParser.ExprContext):
        return self.generateCode(ctx.arith_expr())

    def visitArith_expr(self, ctx: EasyParser.Arith_exprContext):
        """
        Generate code for + and -
        We iterate through each child
        Generate code for each child and then use add or sub
        to join the childs together
        :param ctx:
        :return:
        """
        ret = self.generateCode(ctx.term(0))
        i = 1
        while True:
            if ctx.term(i) is None:
                break
            ret2 = self.generateCode(ctx.term(i))
            if ctx.children[2*i-1].getText() == "+":
                ret = self.builder.add(ret,
                                       ret2)
            else:
                ret = self.builder.sub(ret, ret2)
            i += 1

        return ret

    def visitTerm(self, ctx: EasyParser.TermContext):
        """
        We do the same here as for aritmetic + and -, but with sdiv
        and mul op code
        :param ctx:
        :return:
        """
        ret = self.generateCode(ctx.factor(0))
        i = 1
        while True:
            if ctx.factor(i) is None:
                break
            ret2 = self.generateCode(ctx.factor(i))
            if ctx.children[2*i - 1].getText() == "*":
                ret = self.builder.mul(ret,ret2)
            else:
                ret = self.builder.sdiv(ret,ret2)
            i += 1

        return ret

    def visitFactor(self, ctx: EasyParser.FactorContext):
        """
        If we have - before our variable, we
        generate neg op code
        :param ctx:
        :return:
        """
        ret = self.generateCode(ctx.creator())
        if len(ctx.children) > 1:
            return self.builder.neg(ret)
        return ret

    def visitCreator(self, ctx: EasyParser.CreatorContext):
        return self.generateCode(ctx.children[0])

    def visitAtom(self, ctx: EasyParser.AtomContext):
        """
        Continue the cycle with brackets :D
        :param ctx:
        :return:
        """
        return self.generateCode(ctx.test())

    def visitAccess(self, ctx: EasyParser.AccessContext):
        """
        This function take care list acess by listparameters ot
        function call
        :param ctx:
        :return:
        """
        if ctx.default() is not None:
            return self.generateCode(ctx.default())
        elif ctx.trailer().parameters() is not None:
            param = self.generateCode(ctx.trailer())
            name = str(ctx.NAME())
            # print(self.module.globals)
            func = self.module.get_global(name)
            return self.builder.call(func, param)

        elif ctx.trailer().listparameters() is not None:
            name = str(ctx.NAME())
            addr = self.funcs_symtab.get(ctx, name)
            addr = self.builder.load(addr)
            param = self.generateCode(ctx.trailer().listparameters())
            for par in param:
                addr = self.builder.gep(addr, [par])
                addr = self.builder.load(addr)
            return addr #ziskavam uz danu hodnotu :D
        else:
            raise ValueError("Incorect calling convetion!!!!!")


    def visitParameters(self, ctx: EasyParser.ParametersContext):
        """
        This function generate list of parameters for function call
        :param ctx:
        :return:
        """
        if ctx.argslist() is not None:
            return self.generateCode(ctx.argslist())
        else:
            return []

    def visitListparameters(self, ctx: EasyParser.ListparametersContext):
        """
        This function generate list of parameter for array acess
        :param ctx:
        :return:
        """
        if ctx.argslist() is not None:
            return self.generateCode(ctx.argslist())
        else:
            return []

    def visitArgslist(self, ctx: EasyParser.ArgslistContext):
        """
        Generate list of parameters for function call or list accss
        :param ctx:
        :return:
        """
        ret = [self.generateCode(ctx.test(0))]
        i = 1
        while ctx.test(i) is not None:
            ret.append(
                self.generateCode(ctx.test(i))
            )
            i += 1
        return ret

    def visitDefault(self, ctx: EasyParser.DefaultContext):
        """
        Function, which generate variable declaration code
        or just return a constant
        :param ctx:
        :return:
        """
        # accesing a variable or statement true or False
        if ctx.NAME() is not None:
            name = str(ctx.NAME())
            if name == "True":
                return ir.Constant(self.int1, 1)
            if name == "False":
                return ir.Constant(self.int1, 0)
            tmp = self.funcs_symtab.get(ctx, name)
            return self.builder.load(tmp)

        # Generating code for number
        elif ctx.NUMBER() is not None:
            return ir.Constant(self.int32, int(str(ctx.NUMBER())))
        #generating code for char
        elif ctx.CHAR() is not None:
            ch = str(ctx.CHAR())[1:][:-1]
            return ir.Constant(self.int8, ord(ch))
        # Creating a global string variable and return pointer
        # to that string
        elif ctx.STRING() is not None:
            string = str(ctx.STRING())
            string = string.replace('\\n', '\n')
            string = string.replace('\\r', '\r')
            string = string[1:][:-1].encode() + b'\x00'
            new_name = self.module.get_unique_name()
            my_type = ir.ArrayType(self.int8, len(string))
            glo = ir.GlobalVariable(self.module, my_type, new_name)
            glo.initializer = ir.Constant(my_type, bytearray(string))
            return glo.gep([self.int32(0), self.int32(0)])
        else:
            utils.printError(ctx, "Parsing basic type")
            sys.exit(0)



























































