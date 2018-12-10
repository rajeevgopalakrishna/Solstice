#	Copyright (c) 2018 Rajeev Gopalakrishna
#
#	This file is part of Solstice.
#
#	Solstice is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	Solstice is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with Solstice.  If not, see <http://www.gnu.org/licenses/>.

import logging, sys
from ParseAST.functionDefinition import FunctionDefinition
from ParseAST.expressionStatement import ExpressionStatement
from ParseAST.identifier import Identifier
from ParseAST.expression import Expression
from ParseAST.ifStatement import IfStatement
from AnalyseAST.defUse import DefUseAnalysis
from Libraries.myset import MySet

class TaintPropagate:
    def propagateTaintAtNode(node, taintFlow, _in):
        logging.debug("Node ID: " + str(node.id))
        if(_in is not None):
            logging.debug("_in: " + str(_in._set))
        _taint = MySet()                     
        _out = _in
        if (isinstance(node, FunctionDefinition) or
            isinstance(node, ExpressionStatement) or 
            (isinstance(node, Expression) and
            (node.type == "rightHandSide" or
             node.type == "subExpression" or
             node.type == "functionCallArgument" or
             node.type == "returnStatement" or
             node.type == "ifStatementCondition" or
             node.type == "doWhileCondition" or
             node.type == "forStatementCondition" or
             node.type == "forStatementLoopExpression"
            ))):
            defs = []
            if (isinstance(node, FunctionDefinition)):
                defs = DefUseAnalysis.getDefsAtFunctionDefinition(node, defs)
            else:
                defs = DefUseAnalysis.getAllDefsAtNode(node, defs)
            logging.debug("Defs: " + str(defs))
            uses = []
            uses = DefUseAnalysis.getAllUsesAtNode(node, uses)
            if (len(defs) == 0):
                taintFlow.append({"id":node.id, "src":node.src, "in":_in, "out":_out})
            else:
                for _def in defs:
                    if (_in is None):
                        logging.debug("_in is empty")
                        _in = MySet() 
                    if (isinstance(node, FunctionDefinition) and (node.visibility == "public" or node.visibility == "external")):
                        logging.debug("Adding function parameter to taint: " + _def["name"])
                        _taint.add(_def["referencedDeclaration"], node)
                    else:
                        useOfTaintedVariable = False
                        logging.debug("Uses: " + str(uses))
                        for _use in uses:
                            if (_use["referencedDeclaration"] in _in._set):
                                logging.debug("Use of tainted variable: " + _use["name"] + " in definition of: " + _def["name"])
                                useOfTaintedVariable = True
                                break
                        if (useOfTaintedVariable):
                            _taint.add(_def["referencedDeclaration"], node)
                    _out = _in.union(_taint)
                    if(_in is not None):
                        logging.debug("_in: " + str(_in._set))
                    if(_out is not None):
                        logging.debug("_out: " + str(_out._set))
                    taintFlow.append({"id":node.id, "src":node.src, "in":_in, "out":_out})
                return(_out)
        else:
            for child in node.children:
                logging.debug("Calling propagateTaintAtNode for node: " + str(child.id))
                if(_in is not None):
                    logging.debug("_in: " + str(_in._set))
                _out = TaintPropagate.propagateTaintAtNode(child, taintFlow, _in)
                if(_out is not None):
                    logging.debug("Returned _out: " + str(_out._set))
                _in = _out
            return(_out)
            
    def getTaintPropagationForFunction(functionDefinition):
        _in = MySet()
        _out = MySet()
        taintFlow = []

        _out = TaintPropagate.propagateTaintAtNode(functionDefinition, taintFlow, _in)
        _in = _out

        children = functionDefinition.children;
        for child in children:
            _out = TaintPropagate.propagateTaintAtNode(child, taintFlow, _in)
            _in = _out
        return taintFlow
