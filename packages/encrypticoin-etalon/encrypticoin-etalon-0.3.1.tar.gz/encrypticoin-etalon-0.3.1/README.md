# encrypticoin-etalon

Implementation of the Etalon Token by Encrypticoin UAB.

Etalon is a BEP20 token implemented in Solidity, heavily utilizing the framework provided by the OpenZeppelin project.

## Etalon contract

The contract is found at `encrypticoin_etalon/contract/BEP20EtalonToken.sol`. Its pre-compiled ABI and binary-code is also committed that were compiled by the specified Solidity compiler version.

## Python packaging

The contract is wrapped in a Python package for easy development and distribution in the relevant server systems.

Testing of the contract is performed in other environments, this repository is purely for the contract itself. 

A source distribution package is available from PyPI named `encrypticoin-etalon`:

```
pip install encrypticoin-etalon
```
