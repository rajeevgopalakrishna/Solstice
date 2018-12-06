**SOLSTICE**: **SOL**idity **S**ecurity **T**ool for **I**nvestigative **C**ontract **E**xamination
===================================================================================================

The goal of Solstice is to provide a security analysis framework to software developers for investigative smart contract examination. The wish-list for such a framework typically includes the following features: offer a range of analyses relevant to highlighting and fixing security concerns in the source code, use heuristics to cover a broad range of properties, report results within seconds, allow users to annotate specific code or specify properties to be examined or ignored, allow users to configure the breadth and depth of analyses, allow users to filter out suspected false positives, provide an extensible language for user-defined analyses or queries and finally, be integrated with commonly used IDEs.

The first prototype of Solstice, code named W18 (see below for naming rationale), is a command-line tool which can be used to run 15 different static analyses on Solidity smart contracts. These cover a broad range of well-known security/software properties with Ethereum smart contracts today such as those dealing with reentrancy, exceptions, denial-of-service and uninitialised storage pointers.

Solstice infers syntactic and semantic properties from Solidity source code of smart contracts by analysing the abstract syntax tree (AST) generated by the Solidity compiler.

Analysers
=========

The 15 implemented analysers are briefly described below:

#### 1. Contract Features ####
This analyser discovers high-level summary features of the smart contract such as contract definitions, function definitions, modifiers, function visibility, constructors, fallback functions, variable declarations and type of variable: state/local/parameter.

#### 2. Control Flow Graph ####
This analyser discovers the control flow structure of the smart contract by identifying function calls and prints the names of caller, callee and line numbers. Control flow structure is a critical component of identifying program structure and helps developers understand interprocedural (procedure is another name for function and is frequently used in static analysis terminology) interactions within contracts.

#### 3. Default Visibility ####
Explicitly specifying visibility for functions in Solidity is a security best practise. This analyser detects missing visibility specifiers and warns the developer to check such assumptions. Relying on default visibility for functions has been a common/significant source of concern that 0.5.0 version of Solidity compiler has made it mandatory to explicitly specify function visibility.

#### 4. Deprecated Constructs ####
The use of *tx.origin* and block properties such as *number* and *timestamp* have been deprecated over time because developers used these features with incorrect assumptions about their semantics and security guarantees. So this analyser detects usage of such constructs and reminds developers that they have been deprecated.

#### 5. Denial-of-Service with Block Gas Limit ####
When *send* or *transfer* is used within a loop, there is a possibility of a denial-of-service attack if the attacker can control the number of addresses being processed. The vulnerability related to this scenario and the block gas limit is best explained [here](https://consensys.github.io/smart-contract-best-practices/known_attacks/#dos-with-block-gas-limit). This analyser uses semantic heuristics to detect the use of *send* or *transfer* within *while* or *for* loops to warn the developer.

#### 6. Denial-of-Service with Unexpected *revert* ####
An attacker who controls the destination address of a payment can force the transaction to fail. Depending on the use of *transfer*, or *send* along with *require*, this will cause a revert. The vulnerability related to this scenario resulting in a denial-of-service is described [here](https://consensys.github.io/smart-contract-best-practices/known_attacks/#dos-with-unexpected-revert). If the contract logic is not programmed defensively (i.e. pull over push payments) to consider this scenario then it will result in a denial-of-service attack. This analyser uses semantic heuristics to detect and warn about the use of *send* with *require* or *transfer*.

#### 7. Denial-of-Service with Unexpected *revert* in Loop ####
This vulnerability is similar to the previous one but the presence of a loop indicates a greater likelihood of a denial-of-service attack because the revert will force the loop to terminate prematurely. The analyser detects loop semantics to warn the developer.

#### 8. External Contract Interactions #####
Interacting with other contracts using *call*, *send*, *transfer* and *delegatecall* has to be done with care and knowledge of the underlying semantics of gas usage, return values and access to contract state. This analyser detects these calls to warn developers about using the appropriate assumptions and checks at such interactions.

#### 9. Exceptions ####
Error-handling in Solidity using *require*, *assert* and *revert* have some nuances as described [here](https://solidity.readthedocs.io/en/latest/control-structures.html#error-handling-assert-require-revert-and-exceptions) and have to be used appropriately. For example, *require* is to be used for input validation whereas *assert* is to be used for invariant validation as part of internal error checking. Also exceptions from *require* do not consume any gas but those from *assert* consume all the available gas. This analyser highlights the use of these constructs so that developers can validate these nuances.

#### 10. Reentrancy ####
Reentrancy as an attack vector has been well [documented](https://consensys.github.io/smart-contract-best-practices/known_attacks/#reentrancy) and exploited. This analyser uses heuristics to infer potential changes to contract state after detecting a *call* construct.

#### 11. Unchecked *call* ####
A *call* is a low-level interface used to interact with other contracts and returns a boolean value which should be checked by the caller. This analyser uses heuristics to detect the presence of *call* whose return value is not checked by an *assert*, *require* or an *if* condition.

#### 12. Unchecked *selfdestruct* ####
*selfdestruct* is a very powerful functionality which is used to clean up the calling contract by removing all the bytecode from its address and send all the ether stored in that contract address to the parameter-specified address. This analyser detects calls to *selfdestruct* which are not access restricted within *if* conditionals and probably executable by anyone.

#### 13. Uninitialised Storage Pointers ####
Local variables of reference type (structs, arrays and mappings) default to storage pointers in Solidity. If these are not initialised, they point to other storage variables in the contract such as the state variables, which is a source for vulnerabilities as described [here](https://medium.com/cryptronics/storage-allocation-exploits-in-ethereum-smart-contracts-16c2aa312743). This analyser uses heuristics to detect and warn about such uninitialised storage pointers.

#### 14. DefUse ####
The flow of data within programs is achieved by assigning variables to other variables. In static analysis terminology, a variable is "defined" when its value changes in an assignment and a variable is "used" when its value is read to change the value of a variable or influence a control flow decision. The DefUse analyser uses heuristics to determine where variables are defined and used in the smart contract. While it does not illustrate any vulnerabilities by itself, this capability can be used to build powerful analysers which leverage this dataflow analysis instead of relying on imprecise textual comparison for tracking values.
    
#### 15. Tainted Variables ####
Taint analysis is the process of discovering attacker-controlled variables (termed "sources") along program paths which can influence sensitive functions (termed "sinks") without being programmatically sanitised. For example, in the case of Solidity smart contracts, a commonly used access control mechanism is to set the contract creator address as the "owner" within the constructor and then check future transaction origin addresses against this owner address to perform any critical operations. If a malicious user figures out a way to change this owner address somehow (e.g. misnamed constructor) then the sensitive operations guarded by owner address are exposed. The implemented taint analyser uses the previously described DefUse analyser to track data flow for parameters of public and external functions, which will serve as a building block for future analysers with configurable sinks and sources.

Usage
=====

#### Installation and Configuration ####

     $ git clone https://github.com/rajeevgopalakrishna/Solstice.git && cd Solstice

Solstice requires Python 3.6+ and Solidity compiler solc version < 0.5.0. It has been tested with Python 3.6.5 and solc 0.4.24. The available options are:

  `-i <Input Solidity File>` :Specify the input Solidity file.
  `-o <Output Report File>` :Specify the output report file. Default is stdout.
  `-d` :Print debug statements. Helpful in debugging during development.
  `-h` :Print help message.
  `--<AnalyserID to be run>` :Specify the analyser to be run by IDs 1,2..15. Default is to run all 15 analysers.

### Run Solstice ###

    $ python3 Solstice.py -i ./Tests/Analysers/Contracts/Real-World/GnosisSafe.sol


Current Status and Next Steps
=============================

While the coverage, correctness and precision of implemented analysers and underlying framework is admittedly limited in this initial release, the goal was to experiment with Solidity compiler's AST parsing and evaluate feasibility of simple static analysis (vis-a-vis other approaches, e.g. symbolic execution). This initial release of a work-in-progress prototype is mainly to get feedback from smart contract developers for improving the depth, breadth and usability of this tool in future releases.

For example, there are many Solidity-related aspects which need a lot more work such as complete parsing of the AST, handling modifiers/inheritance/interfaces/libraries, better handling of different value/reference data types and the scoping rules (from JavaScript earlier to C99 in Solidity compiler v0.5.0 onwards).

There are also significant algorithmic improvements desired for the analysers such as making them interprocedural (i.e. track control/data flow across function calls), making them context-sensitive (i.e. accounting for different call sites for a particular function and hence the different data flows) and increasing path-sensitivity (i.e. accounting for different data flows along different paths e.g. if-then-else and loops). The analysers are currently intraprocedural and somewhat flow-sensitive. The DefUse and Taint analysers especially are still very basic and minimally functional at this point. So a lot more work is required to make this prototype useful in the real-world.

There are many open-source security tools being developed for analysing smart contracts such as Mythril, Manticore, Oyente, Securify and Slither. Of these, Solstice is similar to Slither in its approach. These are early days for smart contract security tools and it will be interesting to see how their capabilities evolve along with the ecosystem.

Why "Solstice"?
===============

From Wikipedia: "a solstice is an event occurring when the Sun appears to reach its most northerly or southerly excursion relative to the celestial equator on the celestial sphere. Two solstices occur annually, around June 21 and December 21. The day of a solstice in either hemisphere has either the most sunlight of the year (summer solstice) or the least sunlight of the year (winter solstice) for any place other than the Equator."

Security vulnerabilities, figuratively speaking, exist in software where the least light is shone, i.e. untested code with programmer errors, and security tools are expected to shine the most light on such parts/aspects of software. Hence the name "Solstice" :-). The code name for the initial release W18 stands for Winter Solstice 2018 (in the northern hemisphere).











