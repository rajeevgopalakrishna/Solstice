from ParseAST.contractDefinition import ContractDefinition

class AnalyseContract:
    def getAllContractNames():
        contractNames = []
        for contract in ContractDefinition.registry:
            contractNames.append(contract.name)
        return contractNames

    def getAllContracts():
        return ContractDefinition.registry
