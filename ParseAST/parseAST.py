import os
import json
import logging, sys
from collections import Counter
from .ast import AST
from .contractDefinition import ContractDefinition
from .functionDefinition import FunctionDefinition
from .modifierDefinition import ModifierDefinition
from .eventDefinition import EventDefinition
from .variableDeclaration import VariableDeclaration
from .functionCall import FunctionCall
from .expression import Expression
from .variableDeclarationStatement import VariableDeclarationStatement
from .ifStatement import IfStatement
from .whileStatement import WhileStatement
from .doWhileStatement import DoWhileStatement
from .forStatement import ForStatement
from .expressionStatement import ExpressionStatement
from .identifier import Identifier

class ParseAST:

    parseResults = {}
    parseResults['Counts'] = Counter()
    parseResults['AST'] = ""
    
    def visitVariableDeclaration(self, variable, parent):
       logging.debug("Variable: " + variable['name'])
       variableDeclaration = VariableDeclaration(variable)
       variableDeclaration.parent = parent
       parent.children.append(variableDeclaration)
       self.parseResults['Counts']['VariableDeclarationCount'] += 1

    def visitVariableDeclarationStatement(self, statement, parent):
       logging.debug("VariableDeclarationStatement")
       variableDeclarationStatement = VariableDeclarationStatement(statement)
       variableDeclarationStatement.parent = parent
       parent.children.append(variableDeclarationStatement)
       self.parseResults['Counts']['VariableDeclarationStatementCount'] += 1
       for declaration in statement['declarations']:
                self.visitVariableDeclaration(declaration, variableDeclarationStatement)
        
    def visitIfStatement(self, ifStatement, parent):
        logging.debug("IfStatement")
        ifStatementInstance = IfStatement(ifStatement)
        ifStatementInstance.parent = parent
        parent.children.append(ifStatementInstance)
        if (ifStatement.get("condition")):
            logging.debug("If condition")
            self.parseResults['Counts']['ifCondition'] += 1
            self.visitExpression(ifStatement['condition'], ifStatementInstance,"ifStatementCondition")            
        if (ifStatement.get("trueBody")):
            logging.debug("If trueBody")
            self.parseResults['Counts']['ifTrueBody'] += 1
            if (ifStatement['trueBody'].get('statements')):
                for statement in ifStatement['trueBody']['statements']:
                    self.visitStatement(statement, ifStatementInstance)
            if (ifStatement['trueBody'].get('expression')): # Body with only a single expression without {}
                    self.visitExpression(ifStatement['trueBody']['expression'], ifStatementInstance,"ifStatementTruebody")
        if (ifStatement.get("falseBody")):
            logging.debug("If falseBody")
            self.parseResults['Counts']['ifFalseBody'] += 1
            if (ifStatement['falseBody'].get("statements")):
                for statement in ifStatement['falseBody']['statements']:
                    self.visitStatement(statement, ifStatementInstance)
            if (ifStatement['falseBody'].get('expression')): # Body with only a single expression without {}
                self.visitExpression(ifStatement['falseBody']['expression'], ifStatementInstance,"ifStatementFalsebody")

    def visitWhileStatement(self, whileStatement, parent):
        logging.debug("WhileStatement")
        whileStatementInstance = WhileStatement(whileStatement)
        whileStatementInstance.parent = parent
        parent.children.append(whileStatementInstance)
        self.parseResults['Counts']['WhileCount'] += 1
        if (whileStatement.get("condition")):
            logging.debug("While Condition")
            self.parseResults['Counts']['whileCondition'] += 1
            self.visitExpression(whileStatement['condition'], whileStatementInstance, "whileStatementCondition")
        if (whileStatement['body'].get("statements")):
            logging.debug("While Statements")
            for statement in whileStatement['body']['statements']:
                self.visitStatement(statement, whileStatementInstance)
        if (whileStatement['body'].get("expression")): # Body with only a single expression without {}
            logging.debug("While Expression")
            self.visitExpression(whileStatement['body']['expression'], whileStatementInstance, "whileStatementBody")

    def visitForStatement(self, forStatement, parent):
        logging.debug("ForStatement")
        forStatementInstance = ForStatement(forStatement)
        forStatementInstance.parent = parent
        parent.children.append(forStatementInstance)
        self.parseResults['Counts']['ForCount'] += 1
        if (forStatement.get("condition")):
            logging.debug("For condition")
            self.parseResults['Counts']['forCondition'] += 1
            self.visitExpression(forStatement['condition'], forStatementInstance, "forStatementCondition")
        if (forStatement.get("loopExpression")):
            logging.debug("For loopExpression")
            self.parseResults['Counts']['ForLoopExpression'] += 1
            self.visitExpression(forStatement['loopExpression'], forStatementInstance, "forStatementLoopExpression")
        #TODO: Evaluate initializationExpression
        if (forStatement['body'].get("statements")):
            logging.debug("For Statements")
            for statement in forStatement['body']['statements']:
                self.visitStatement(statement, forStatementInstance)
        if (forStatement['body'].get("expression")): # Body with only a single expression without {}
            logging.debug("For Expression")
            for statement in forStatement['body']['expression']:
                self.visitExpression(expression, forStatementInstance, "forStatementBody")

            
    def visitDoWhileStatement(self, doWhileStatement, parent):
        logging.debug("DoWhileStatement")
        doWhileStatementInstance = DoWhileStatement(doWhileStatement)
        doWhileStatementInstance.parent = parent
        parent.children.append(doWhileStatementInstance)
        self.parseResults['Counts']['DoWhileCount'] += 1
        if (doWhileStatement.get("condition")):
            logging.debug("condition")
            self.parseResults['Counts']['doWhileCondition'] += 1
            self.visitExpression(doWhileStatement['condition'], doWhileStatementInstance, "doWhileCondition")
        if (doWhileStatement['body'].get("statements")):
            for statement in doWhileStatement['body']['statements']:
                self.visitStatement(statement, doWhileStatementInstance)
        if (doWhileStatement['body'].get("expression")): # Body with only a single expression without {}  
            self.visitExpression(doWhileStatement['body']['expression'], doWhileStatementInstance, "doWhileExpression")


    def visitExpressionStatement(self, expressionStatement, parent):
        logging.debug("ExpressionStatement")
        expressionStatementInstance = ExpressionStatement(expressionStatement)
        expressionStatementInstance.parent = parent
        parent.children.append(expressionStatementInstance)
        self.parseResults['Counts']['ExpressionStatementCount'] += 1
        self.visitExpression(expressionStatement['expression'],expressionStatementInstance,"expressionStatement")
        
    def visitContinueStatement(self, continueStatement, parent):
        logging.debug("Continue")

    def visitBreakStatement(self, breakStatement, parent):
        logging.debug("Break")

    def visitReturnStatement(self, returnStatement, parent):
        logging.debug("Return")
        self.visitExpression(returnStatement['expression'], parent, "returnStatement")

    def visitExpression(self, expression, parent, typeOfExpression):
        logging.debug("Expression")
        logging.debug("Expression nodeType: " + expression['nodeType'])
        logging.debug("Expression Type: " + typeOfExpression)
        self.parseResults['Counts']['ExpressionCount'] += 1

        expressionInstance = Expression(expression,typeOfExpression)
        expressionInstance.parent = parent
        parent.children.append(expressionInstance)
        
        if ('expression' in expression):
            self.visitExpression(expression['expression'], expressionInstance, "expression")
        if ('leftHandSide' in expression):
            self.visitExpression(expression['leftHandSide'], expressionInstance, "leftHandSide")
        if ('rightHandSide' in expression):
            self.visitExpression(expression['rightHandSide'], expressionInstance, "rightHandSide")
        if ('leftExpression' in expression):
            self.visitExpression(expression['leftExpression'], expressionInstance,"leftExpression")
        if ('rightExpression' in expression):
            self.visitExpression(expression['rightExpression'], expressionInstance,"rightExpression")
        if ('subExpression' in expression):
            self.visitExpression(expression['subExpression'], expressionInstance,"subExpression")
        if ('baseExpression' in expression):
            self.visitExpression(expression['baseExpression'], expressionInstance,"baseExpression")
        if ('indexExpression' in expression):
            self.visitExpression(expression['indexExpression'], expressionInstance,"indexExpression")
        if ('components' in expression):
            for component in expression['components']:
                self.visitExpression(component, expressionInstance,"component")        

        if (expression['nodeType'] == "FunctionCall"):
            logging.debug("FunctionCall")
            self.parseResults['Counts']['FunctionCallCount'] += 1
            functionCall = FunctionCall(expression)
            functionCall.parent = expressionInstance
            expressionInstance.children.append(functionCall)
            if (expression.get("arguments")):
                for argument in expression['arguments']:
                    logging.debug("FunctionCall Argument")
                    self.visitExpression(argument, functionCall,"functionCallArgument")
            return
        
        if (expression['nodeType'] == "Identifier"):
            logging.debug("Identifier")
            self.parseResults['Counts']['IdentifierCount'] += 1
            identifier = Identifier(expression, typeOfExpression)
            identifier.parent = expressionInstance
            expressionInstance.children.append(identifier)
            return
        

    def visitStatement(self, statement, parent):
        logging.debug("Statement Type: " + statement['nodeType'])
        if (statement['nodeType'] == "VariableDeclarationStatement"):
            self.visitVariableDeclarationStatement(statement, parent)
        if (statement['nodeType'] == "IfStatement"):
            self.visitIfStatement(statement, parent)
        if (statement['nodeType'] == "WhileStatement"):
            self.visitWhileStatement(statement, parent)
        if (statement['nodeType'] == "ForStatement"):
            self.visitForStatement(statement, parent)
        if (statement['nodeType'] == "DoWhileStatement"):
            self.visitDoWhileStatement(statement, parent)
        if (statement['nodeType'] == "Continue"):
            self.visitContinueStatement(statement, parent)
        if (statement['nodeType'] == "Break"):
            self.visitBreakStatement(statement, parent)
        if (statement['nodeType'] == "Return"):
            self.visitReturnStatement(statement, parent) 
        elif (statement['nodeType'] == "ExpressionStatement"):
            self.visitExpressionStatement(statement, parent)

    def visitStructDefinition(self, node, parent):
        logging.debug("Struct Name: " + node['name'])

    def visitPragmaDirective(self, pragma, parent):
        logging.debug("Pragma: " + "".join(str(x) for x in pragma['literals']))

    def visitImportDirective(self, _import, parent):
        logging.debug("Import Directive")

    def visitContractDefinition(self, node, parent):
        logging.debug("Contract Name: " + node['name'])
        contractDefinition = ContractDefinition(node)
        contractDefinition.parent = parent
        parent.children.append(contractDefinition)
        nodes = node['nodes']
        for node in nodes:
            self.visit(node, contractDefinition)

    def visitEventDefinition(self, node, parent):
        logging.debug("Event Name: " + node['name'])
        eventDefinition = EventDefinition(node)
        eventDefinition.parent = parent
        parent.children.append(eventDefinition)
        self.parseResults['Counts']['EventCount'] += 1
            
    def visitFunctionDefinition(self, node, parent):
        logging.debug("Function Name: " + node['name'])
        functionDefinition = FunctionDefinition(node)
        functionDefinition.parent = parent
        parent.children.append(functionDefinition)
        body = node['body']
        for statement in body['statements']:
            self.visitStatement(statement, functionDefinition)
        parameters = node['parameters']['parameters']
        logging.debug("Parameters: " + str(parameters))
        for parameter in parameters:
            self.visitVariableDeclaration(parameter, functionDefinition)
            
    def visitModifierDefinition(self, node, parent):
        logging.debug("Modifier Name: " + node['name'])
        modifierDefinition = ModifierDefinition(node)
        modifierDefinition.parent = parent
        parent.children.append(modifierDefinition)
        self.parseResults['Counts']['ModifierCount'] += 1
        body = node['body']
        for statement in body['statements']:
            self.visitStatement(statement, modifierDefinition)

    def visit(self, node, parent):
        logging.debug(node['nodeType'])
        if (node['nodeType'] == "PragmaDirective"):
            self.visitPragmaDirective(node, parent)
        if (node['nodeType'] == "ImportDirective"):
            self.visitImportDirective(node, parent)
        if (node['nodeType'] == "ContractDefinition"):
            self.visitContractDefinition(node, parent)
        if (node['nodeType'] == "EventDefinition"):
            self.visitEventDefinition(node, parent)
        if (node['nodeType'] == "FunctionDefinition"):
            self.visitFunctionDefinition(node, parent)
        if (node['nodeType'] == "ModifierDefinition"):
            self.visitModifierDefinition(node, parent)
        if (node['nodeType'] == "StructDefinition"):
            self.visitStructDefinition(node, parent)
        if (node['nodeType'] == "VariableDeclaration"):
            self.visitVariableDeclaration(node, parent)

    def parse(self, astFD):
        astFile = astFD.readlines()
        astFile[0:4]=[]
        astJson = json.loads(''.join(astFile))
        astFD.close()

        ast = AST()
        self.parseResults['AST'] = ast
        nodes = astJson["nodes"]
        for node in nodes:
            self.visit(node, ast)
        return self.parseResults    
            
