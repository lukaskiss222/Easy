from antlr4.error.ErrorListener import ErrorListener
import sys


class MyErrorListener(ErrorListener):

    def __init__(self) -> None:
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(msg)
        print("Syntax error")
        sys.exit(0)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        print("Ambiguity error")
        sys.exit(0)

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        print("Attempting Full Context erro ")
        sys.exit(0)

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        print("ContextSensitivity error")
        sys.exit(0)


