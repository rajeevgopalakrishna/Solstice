from ParseAST.expression import Expression

class AnalyseExpression:
    def getAllExpressions():
        return Expression.registry
    
    def getAllTransfers():
        transfers = [] 
        for expression in Expression.registry:
            if (expression.memberName == "transfer"):
                transfers.append(expression)
        return transfers

    def getAllSends():
        sends = [] 
        for expression in Expression.registry:
            if (expression.memberName == "send"):
                sends.append(expression)
        return sends

    def getAllCalls():
        calls = [] 
        for expression in Expression.registry:
            if (expression.memberName == "call"):
                calls.append(expression)
        return calls

    def getAllDelegateCalls():
        delegateCalls = [] 
        for expression in Expression.registry:
            if (expression.memberName == "delegatecall"):
                delegateCalls.append(expression)
        return delegateCalls
    '''
    def getAllStaticCalls():
        staticCalls = [] 
        for expression in Expression.registry:
            if (expression.memberName == "staticCall"):
                staticCalls.append(expression)
        return staticCalls
    ''' 

    
    
    
