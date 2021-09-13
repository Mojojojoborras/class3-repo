### COMMANDS TO INITIATE BLOCKCHAIN

./geth account new --datadir node1<br>
./geth account new --datadir node2<br>
./geth --datadir node1 init networkname.json<br>
./geth --datadir node1 --unlock "SEALER_ONE_ADDRESS" --mine --rpc --allow-insecure-unlock<br>
./geth --datadir node2 --unlock "SEALER_TWO_ADDRESS" --mine --port 30304 --bootnodes "enode://SEALER_ONE_ENODE_ADDRESS@127.0.0.1:30303" --ipcdisable --allow-insecure-unlock<br>

<hr />

NOTE:  the following are paths and addresses created on my working dir and used only for this HW. Since deleted.

<hr />

$ /c/Users/rotar/Desktop/FinTech_Bootcamp/Blockhain-Tools/geth.exe account new --datadir node1

#### SEALER ONE

Public address of the key:   0xfDEF81117CA8f4CE218E7e69f0ac84F17caF3039
Path of the secret key file: node1\keystore\UTC--2021-09-13T15-14-48.571234100Z--fdef81117ca8f4ce218e7e69f0ac84f17caf3039

enode://435b6e06e099ae2310c438d590a3192a775c2f4e85bc0d82c3a8fe56f6ffdd5dfe2980f4e4185db229b3a0b6b395d9e9561b9c849a07b136470dbc8dfbb9a11c@127.0.0.1:30303

- You can share your public address with anyone. Others need it to interact with you.
- You must NEVER share the secret key with anyone! The key controls access to your funds!
- You must BACKUP your key file! Without the key, it's impossible to access account funds!
- You must REMEMBER your password! Without the password, it's impossible to decrypt the key!

$ /c/Users/rotar/Desktop/FinTech_Bootcamp/Blockhain-Tools/geth.exe account new --datadir node2

#### SEALER TWO

Public address of the key:   0x9fFb64Bca2331961B623E7843B150c203e893362
Path of the secret key file: node2\keystore\UTC--2021-09-13T15-15-56.539306800Z--9ffb64bca2331961b623e7843b150c203e893362

enode://e2f5b590b5cce5f1a71279a52580e53559d7fb43c75e73fbf20d36a1e235e8b5b5ef9b95ba569f981a2bf113109d83846cb3a4333ae25880bfe74d8d318e8a32@127.0.0.1:30304

- You can share your public address with anyone. Others need it to interact with you.
- You must NEVER share the secret key with anyone! The key controls access to your funds!
- You must BACKUP your key file! Without the key, it's impossible to access account funds!
- You must REMEMBER your password! Without the password, it's impossible to decrypt the key!

<hr />

Randomly Selected Chain ID 001