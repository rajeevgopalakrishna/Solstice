**SOLSTICE**: **SOL**idity **S**ecurity **T**ool for **I**nvestigative **C**ontract **E**xamination

The goal of Solstice is to provide a security analysis framework to software developers for investigative smart contract examination. The typical wishlist for such a framework includes the following features: offer a range of analyses relevant to highlighting and fixing security concerns in the source code, use heuristics to cover a broad range of properties, report results within seconds, allow users to annotate specific code or specify properties to be examined or ignored, allow users to configure the breadth and depth of analyses, allow users to filter out suspected false positives, provide an extensible language for user-defined analyses or queries and finally, be integrated with commonly used IDEs.

The first prototype of Solstice, code named W18 (see below for the naming rationale/convention), is a command-line tool which can be used to run 15 different static analyses on Solidity smart contracts. These cover a broad range of well-known security/software properties with Ethereum smart contracts today such as those dealing with reentrancy, exceptions, denial-of-service and uninitialised storage pointers. The 15 implemented analysers are described below:

1. Contract Features
2. Control Flow Graph
3. Default Visibility
4. Deprecated Constructs
5. Denial-of-Service with Block Gas Limit
6. Denial-of-Service with Unexpected *revert*
7. Denial-of-Service with Unexpected *revert* in Loop
8. External Contract Interactions
9. Exceptions
10. Reentrancy
11. Unchecked *call*
12. Unchecked *selfdestruct*
13. Uninitialised Storage Pointers
14. DefUse
15. Tainted Variables

While the precision and coverage of these analyses is admittedly limited in this initial release, the goal was to demonstrate the basic capabilities of static analysis (vis-a-vis other approaches, e.g. symbolic execution) and keep improving it iteratively in future releases.

(A brief fun note on the naming rationale/convention - from Wikipedia: "a solstice is an event occurring when the Sun appears to reach its most northerly or southerly excursion relative to the celestial equator on the celestial sphere. Two solstices occur annually, around June 21 and December 21. The day of a solstice in either hemisphere has either the most sunlight of the year (summer solstice) or the least sunlight of the year (winter solstice) for any place other than the Equator." Metaphorically speaking, security vulnerabilities exist in software where the least light is shone, i.e. untested code with programmer errors, and security tools are expected to shine the most light on such parts/aspects of software. Hence the name "Solstice" :-). W18 stands for Winter Solstice 2018 in the northern hemisphere. The major releases are anticipated to be scheduled twice a year on the days of winter and summer solstices.)









