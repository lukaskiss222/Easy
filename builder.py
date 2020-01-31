import antlr4 as at
from Easy.EasyParser import EasyParser
from Easy.EasyLexer import EasyLexer
from LLVMCodeGenerator import LLVMCodeGenerator
from ctypes import CFUNCTYPE
import llvmlite.binding as llvm
from errorlistener import MyErrorListener

class builder(object):

    def __init__(self):
        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()

        self.target = llvm.Target.from_default_triple()
        backing_mod = llvm.parse_assembly("")
        self.engine = llvm.create_mcjit_compiler(backing_mod,
                                                 self.target.create_target_machine())

    def compile(self, string, name, ret_type, args_types, verbose = True, mode32=False):

        input_stream = at.InputStream(string)
        lexer = EasyLexer(input_stream)
        stream = at.CommonTokenStream(lexer)
        parser = EasyParser(stream)
        tree = parser.compileUnit()

        generator = LLVMCodeGenerator()
        tree.accept(generator)
        if verbose:
            print(generator.module)



        mod = llvm.parse_assembly(str(generator.module))
        mod.verify()
        if mode32:
            mod.triple = "i386-pc-linux-gnu"
        else:
            mod.triple = self.target.create_target_machine().triple

        #print(target_machine.emit_assembly(mod))

        self.engine.add_module(mod)
        self.engine.finalize_object()
        self.engine.run_static_constructors()

        func_ptr = self.engine.get_function_address(name)

        func = CFUNCTYPE(ret_type, *args_types)(func_ptr)
        return func


    def traslate(self, string, verbose = False, optimize = False, mode32 = False):
        input_stream = at.InputStream(string)
        lexer = EasyLexer(input_stream)
        stream = at.CommonTokenStream(lexer)
        parser = EasyParser(stream)
        parser.addErrorListener(MyErrorListener())
        tree = parser.compileUnit()


        generator = LLVMCodeGenerator(mode32=mode32)
        tree.accept(generator)

        target_machine = self.target.create_target_machine()




        mod = llvm.parse_assembly(str(generator.module))
        mod.verify()
        if mode32:
            mod.triple = "i386-pc-linux-gnu"
        else:
            mod.triple = self.target.create_target_machine().triple

        if optimize:
            pmb = llvm.create_pass_manager_builder()
            pmb.opt_level = 3
            pm = llvm.create_module_pass_manager()
            pmb.populate(pm)
            pm.run(mod)

        if verbose:
            print(mod)

        return str(mod)
