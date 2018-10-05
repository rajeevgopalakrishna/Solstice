from ParseAST.expressionStatement import ExpressionStatement
from ParseAST.identifier import Identifier
from ParseAST.expression import Expression

class DefUseAnalysis:
    def getDefs(expression, defs):
        if (expression.nodeType == "Identifier"):
            print("Adding def: " + expression.name)
            defs.append(expression.name)
        for child in expression.children:
            DefUseAnalysis.getDefs(child, defs)
        return defs
        
    def getAllDefs():
        defs = []
        for expression in Expression.registry:
            if (expression.type == "leftHandSide" or expression.type == "subExpression"):
                print("Calling getDefs")
                defs = DefUseAnalysis.getDefs(expression, defs)
        return defs

    def getUses(expression, uses):
        if (expression.nodeType == "Identifier"):
            print("Adding use: " + expression.name)
            uses.append(expression.name)
        for child in expression.children:
            if (isinstance(child, Expression)):
                DefUseAnalysis.getUses(child, uses)
        return uses
        
    def getAllUses():
        uses = []
        for expression in Expression.registry:
            if (expression.type == "rightHandSide" or expression.type == "subExpression"):
                print("Calling getUses")
                defs = DefUseAnalysis.getUses(expression, uses)
        return uses
    '''
    def getAllDefs():
        defs = []
        for identifier in Identifier.registry:
            if (identifier.type == "leftHandSide" or identifier.type == "subExpression"):
                                defs.append(identifier.name)
        return defs

    def getAllDefs():
        defs = []
        for expressionStatement in ExpressionStatement.registry:
            for child in expressionStatement.children:
                if (child.type == "expressionStatement"):
                    for grandChild in child.children:
                        if (grandChild.nodeType == "Identifier" and (grandChild.type == "leftHandSide" or grandChild.type == "subExpression")):
                            defs.append(grandChild.name)
                        for gGrandChild in grandChild.children:
                            if (gGrandChild.nodeType == "Identifier" and (gGrandChild.type == "leftHandSide" or gGrandChild.type == "subExpression")):
                                defs.append(gGrandChild.name)
        return defs

    def getAllUses():
        uses = []
        for expressionStatement in ExpressionStatement.registry:
            for child in expressionStatement.children:
                if (child.type == "expressionStatement"):
                    for grandChild in child.children:
                        if (grandChild.nodeType == "Identifier" and (grandChild.type == "rightHandSide" or grandChild.type == "subExpression")):
                            uses.append(grandChild.name)
                        for gGrandChild in grandChild.children:
                            if (gGrandChild.nodeType == "Identifier"):
                                uses.append(gGrandChild.name)
        return uses
    '''

    
    
    
