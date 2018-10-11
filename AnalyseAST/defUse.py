from ParseAST.expressionStatement import ExpressionStatement
from ParseAST.identifier import Identifier
from ParseAST.expression import Expression

class DefUseAnalysis:
    def getDefs(expression, defs, src):
        if (isinstance(expression, Identifier)):
            defs.append({"name":expression.name, "referencedDeclaration":expression.referencedDeclaration, "src":src})
        for child in expression.children:
            DefUseAnalysis.getDefs(child, defs, src)
        return defs

    def getAllDefs():
        defs = []
        for expression in Expression.registry:
            if (expression.type == "leftHandSide" or expression.type == "subExpression"):
                print("Calling getDefs")
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
#            print("Adding use: " + expression.name)
            uses.append({"name":expression.name, "referencedDeclaration":expression.referencedDeclaration, "src":src})
        for child in expression.children:
            DefUseAnalysis.getUses(child, uses, src)
        return uses
        
    def getAllUses():
        uses = []
        for expression in Expression.registry:
            if (expression.type == "rightHandSide" or expression.type == "subExpression"):
                print("Calling getUses")
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
#            print("Uses at node: " + str(node))
            uses = DefUseAnalysis.getUses(node, uses, node.src)
        for child in node.children:
            DefUseAnalysis.getAllUsesAtNode(child, uses)
        return uses
        

    def getAllSuccessorSiblingsOfNode(node):
        successorSiblings = []
#        print("Node ID: " + str(node.id))
        parent = node.parent
#        print("Parent of node ID: " + str(node.id) + " is:" + str(parent.id))
        seen = False
        for child in parent.children:
            if (seen):
#                print("Adding sibling: " + str(child.id))
                successorSiblings.append(child)
            elif (child.id == node.id):
#                print("Setting seen to True")
                seen = True
            else:
                continue
        return successorSiblings

    def getAllDefintionsAfterStatement(node):
        successorSiblings = DefUseAnalysis.getAllSuccessorSiblingsOfNode(node)
        defs = []
        for sibling in successorSiblings:
#            print("Sibling: " + str(sibling.id))
            defs = DefUseAnalysis.getAllDefsAtNode(sibling, defs)
        return defs


    
    
    
