import io
from typing import Union, List

import sys

from antlr4 import InputStream, CommonTokenStream

from drb import DrbNode

from .XQueryLexer import XQueryLexer
from .XQueryParser import XQueryParser
from .drb_xquery_context import DynamicContext
from .drb_xquery_visitor import DrbQueryVisitor, \
    DrbXqueryParserErrorListener


class DrbXQuery:

    def __init__(self, xquery):
        self.static_context = None

        if isinstance(xquery, DrbNode):
            xquery = xquery.get_impl(io.BufferedIOBase)

        if isinstance(xquery, io.BufferedIOBase):
            xquery = xquery.read().decode()

        # init Lexer with query
        lexer = XQueryLexer(InputStream(xquery))

        self.stream = CommonTokenStream(lexer)
        self.parser = XQueryParser(self.stream)

        self.parser.addErrorListener(DrbXqueryParserErrorListener())
        # parse query and reject it if error
        self.tree = self.parser.module()

    def execute(self, *args, **kwargs):

        old_limit = sys.getrecursionlimit()
        sys.setrecursionlimit(10000)

        list_nodes = args

        output_list = []
        for node_item in list_nodes:
            visitor = DrbQueryVisitor(DynamicContext(node_item),
                                      tokens=self.stream)

            visitor.external_var_map = kwargs
            self.static_context = visitor.static_context

            output = visitor.visitModule(self.tree)
            if not isinstance(output, list):
                output_list.append(output)
            else:
                output_list.extend(output)

        sys.setrecursionlimit(old_limit)

        return output_list
