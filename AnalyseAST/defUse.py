import logging, sys
from ParseAST.expressionStatement import ExpressionStatement
from ParseAST.identifier import Identifier
from ParseAST.expression import Expression

class DefUseAnalysis:
    def getDefs(expression, defs, src):
        if (isinstance(expression, Identifier)):
            logging.debug("getDefs expression: " + expression.name)
            defs.append({"name":expression.name, "referencedDeclaration":expression.referencedDeclaration, "src":src})
        for child in expression.children:
            DefUseAnalysis.getDefs(child, defs, src)
        return defs

    def getAllDefs():
        defs = []
        for expression in Expression.registry:
            if (expression.type == "leftHandSide" or expression.type == "subExpression"):
                logging.debug("Calling getDefs")
                defs = DefUseAnalysis.getDefs(expression, defs, expression.src)
        return defs


    def getAllDefsAtNode(node, defs):
        if (isinstance(node, Expression) and (node.type == "leftHandSide" or node.type == "subExpression")):
            defs = DefUseAnalysis.getDefs(node, defs, node.src)
        for child in node.children:
            DefUseAnalysis.getAllDefsAtNode(child, defs)
        return defs
        

    def getUses(expression, uses, src):
        if (isinstance(expression, Identifier)):
            uses.append({"name":expression.name, "referencedDeclaration":expression.referencedDeclaration, "src":src})
        for child in expression.children:
            DefUseAnalysis.getUses(child, uses, src)
        return uses
        
    def getAllUses():
        uses = []
        for expression in Expression.registry:
            if (expression.type == "rightHandSide" or expression.type == "subExpression"):
                logging.debug("Calling getUses")
                defs = DefUseAnalysis.getUses(expression, uses, expression.src)
        return uses

    def getAllUsesAtNode(node, uses):
        if (isinstance(node, Expression) and
            (node.type == "rightHandSide" or
             node.type == "subExpression" or
             node.type == "functionCallArgument" or
             node.type == "returnStatement" or
             node.type == "ifStatementCondition" or
             node.type == "doWhileCondition" or
             node.type == "forStatementCondition" or
             node.type == "forStatementLoopExpression"
            )):
            uses = DefUseAnalysis.getUses(node, uses, node.src)
        for child in node.children:
            DefUseAnalysis.getAllUsesAtNode(child, uses)
        return uses
        

    def getAllSuccessorSiblingsOfNode(node):
        successorSiblings = []
        parent = node.parent
        seen = False
        for child in parent.children:
            if (seen):
                successorSiblings.append(child)
            elif (child.id == node.id):
                seen = True
            else:
                continue
        return successorSiblings

    def getAllDefintionsAfterStatement(node):
        successorSiblings = DefUseAnalysis.getAllSuccessorSiblingsOfNode(node)
        defs = []
        for sibling in successorSiblings:
            defs = DefUseAnalysis.getAllDefsAtNode(sibling, defs)
        return defs


    def getDataflowForNode(node, dataflow, _in):
        logging.debug("Node ID: " + str(node.id))
        logging.debug("_in: " + str(_in))
        _gen = set()
        _kill = set()
        _out = _in
        if (isinstance(node, ExpressionStatement)):
            defs = []
            defs = DefUseAnalysis.getAllDefsAtNode(node, defs)
            for _def in defs:
                _gen.add(_def["referencedDeclaration"])
                logging.debug("Adding " + str(_def["referencedDeclaration"]) + " to _gen for node ID: " + str(node.id))
                if(_in and _def["referencedDeclaration"] in _in):
                    _kill.add(_def["referencedDeclaration"])
                if (not _in):
                    logging.debug("_in is empty")
                    _in = set()
                _out = _in.union(_gen.difference(_kill))
                logging.debug("_in: " + str(_in))
                logging.debug("_gen: " + str(_gen))
                logging.debug("_kill: " + str(_kill))
                logging.debug("_out: " + str(_out))
                dataflow.append({"id":node.id, "src":node.src, "in":_in, "gen":_gen, "kill":_kill, "out":_out})
            return(_out)
        else:
            for child in node.children:
                logging.debug("Calling getDataflowForNode for node: " + str(child.id))
                logging.debug("_in: " + str(_in))
                _out = DefUseAnalysis.getDataflowForNode(child, dataflow, _in)
                logging.debug("Returned _out: " + str(_out))
                _in = _out
            return(_out)
            
    def getDataflowForFunction(functionDefinition):
        _in = set()
        _out = set()
        dataflow = []
        children = functionDefinition.children;
        for child in children:
            _gen = set()
            _kill = set()
            _out = DefUseAnalysis.getDataflowForNode(child, dataflow, _in)
            _in = _out
        return dataflow

    def getDataflowForFunctionNaive(functionDefinition):
        _in = set()
        _out = set()
        dataflow = []
        children = functionDefinition.children;
        for child in children:
            _gen = set()
            _kill = set()
            _in = _out
            if (isinstance(child, ExpressionStatement)):
                defs = []
                defs = DefUseAnalysis.getAllDefsAtNode(child, defs)
                for _def in defs:
                    _gen.add(_def["referencedDeclaration"])
                    logging.debug("Adding " + str(_def["referencedDeclaration"]) + " to _gen for child ID: " + str(child.id))
                    if(_def["referencedDeclaration"] in _in):
                        _kill.add(_def["referencedDeclaration"])
                    _out = _in.union(_gen.difference(_kill))
                logging.debug("_in: " + str(_in))
                logging.debug("_gen: " + str(_gen))
                logging.debug("_kill: " + str(_kill))
                logging.debug("_out: " + str(_out))
                dataflow.append({"id":child.id, "src":child.src, "in":_in, "gen":_gen, "kill":_kill, "out":_out})
        logging.debug("Returning dataflow: " + str(dataflow))
        return dataflow
