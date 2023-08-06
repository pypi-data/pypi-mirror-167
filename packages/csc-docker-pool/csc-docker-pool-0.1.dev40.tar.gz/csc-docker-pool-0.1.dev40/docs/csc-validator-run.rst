Run a Validator
===============================================================================

Hardware
-------------------------------------------------------------------------------

..code-block::bash
  
  CPU: 16Core
  RAM: 32GB
  HDD: SSD 1TB

Initialize
-------------------------------------------------------------------------------

You must run a relay node to deal with network. 

Refer to Run a Node.

Create Validator Address
-------------------------------------------------------------------------------

You need to create an account that represents a validator's consensus key for 
block signatures. Use the following command to create a new account and set a 
password for that account:

..code-block::bash
  
  genz-cetd validator init \
      --name GenZ \
      --relay ascc \
      --owner-wallet 0xeaff084e6da9afe8ecab4d85de940e7d3153296f \
      --reward-wallet 0x785f9c31920a827601f679ecee29a6fb47c31fc3 \
      --label GenZ \
      --description "GenZ CSC Full node" \
      --website "http://genz-bank.github.io" \
      --email "mostafa.barmshory@gmail.com" \
      --password xxx

Start Validator Node
-------------------------------------------------------------------------------

Save keyfile password of validator account in file


..code-block::bash
  
  genz-cetd validator start \
      --name GenZ \
      --password xxx






#--------------------------------------------------------------------------------
#----------------- GenZ Bank
#--------------------------------------------------------------------------------
validator: 0xeaff084e6da9afe8ecab4d85de940e7d3153296f
reward:   0x785f9c31920a827601f679ecee29a6fb47c31fc3

Init the validator

..code-block::bash
  
  genz-cetd --force validator init \
      --name GenZ \
      --relay ascc \
      --owner-wallet 0xeaff084e6da9afe8ecab4d85de940e7d3153296f \
      --reward-wallet 0x785f9c31920a827601f679ecee29a6fb47c31fc3 \
      --label GenZ \
      --description "GenZ CSC Full node" \
      --website "http://genz-bank.github.io" \
      --email "mostafa.barmshory@gmail.com" \
      --password 2625


Start mining

..code-block::bash
  
  genz-cetd validator start \
      --name GenZ \
      --password 2625

Stake from a wallet with in validator keystore file to the validator

..code-block::bash
  
  genz-cetd -vv validator stake \
      --name GenZ \
      --relay ascc \
      --from 0xeaff084e6da9afe8ecab4d85de940e7d3153296f \
      --value 1000000000000000000000 \
      --password 2625

Stake from a wallet in keystore to custom validator

..code-block::bash
  
  genz-cetd -vv wallet stake \
      --name GenZ \
      --relay ascc \
      --from 0xeaff084e6da9afe8ecab4d85de940e7d3153296f \
      --to 0xeaff084e6da9afe8ecab4d85de940e7d3153296f \
      --value 10000000000000000000000 \
      --password 2625



genz-cetd -vv wallet stake \
      --name CoinCodile \
      --relay ascc \
      --from 0x1b0cceee915abc0d2c22be9f4c47c16233212aff \
      --validator 0xEAfF084e6da9aFE8EcAB4d85de940e7d3153296F \
      --value 9000000000000000000000 \
      --password 2625


