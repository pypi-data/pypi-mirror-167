import time
from web3 import Web3
from web3.middleware import geth_poa_middleware
import argparse
import requests
from datetime import datetime

relayCache = []

def listSort(val):
    return val["times_shown"]


def relay(key, RelayerAddress, gas, rpc, apiURL, timeout):
    api = apiURL+'?rewardRecipient='+RelayerAddress
    req = requests.get(api, timeout=timeout)
    #print(req.text);

    # print(req.json()[0]["id"])

    try:
        docList = req.json()
    except Exception as e:
        print("Bad Fetch from the API")
        return

    if len(docList) < 1:
        print('No get request returned')
        return

    CXORelayABI = '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"uint256","name":"nonce","type":"uint256"},{"indexed":true,"internalType":"bytes32","name":"encodedFunctionHash","type":"bytes32"}],"name":"TransactionRelayed","type":"event"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"bytes","name":"encodedFunction","type":"bytes"},{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"bytes","name":"signature","type":"bytes"},{"internalType":"uint256","name":"reward","type":"uint256"},{"internalType":"address","name":"rewardRecipient","type":"address"},{"internalType":"bytes","name":"rewardSignature","type":"bytes"}],"name":"relayCall","outputs":[],"stateMutability":"nonpayable","type":"function"}]'

    w3 = Web3(Web3.HTTPProvider(rpc))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    addy = w3.eth.account.from_key(key).address
    nonce = 0   # w3.eth.getTransactionCount(addy) Init as a 0 to stop infura consumption unless we actually have a txn

    docList.sort(key=listSort)
    for doc in docList:
        if doc["id"] in relayCache:     # How we check if we've already processed the doc
            print('skipping: ', doc["id"])
        else:
            if nonce == 0:
                nonce = w3.eth.getTransactionCount(addy)
            print("Times shown: ", doc["times_shown"], " ID: ", doc["id"])
            relayCache.append(doc["id"])    # Add this doc's ID to the cache
            RelayerContract = w3.eth.contract(address=doc["relay_address"], abi=CXORelayABI)    # Make a Contract Object
            # Build our unsigned TXN
            txn = RelayerContract.functions.relayCall(Web3.toChecksumAddress(doc["from"]),
                                                      doc["recipient"],
                                                      doc["encoded_function"],
                                                      doc["nonce"],
                                                      doc["signature"],
                                                      Web3.toInt(text=doc["reward"]),
                                                      doc["reward_recipient"],
                                                      doc["reward_signature"]).buildTransaction(
                {
                    'chainId': 137,
                    'gas': 2100000,
                    'gasPrice': w3.toWei(gas, 'gwei'),
                    'nonce': nonce
                }
            )
            # Building a txn doesn't fill out the from field on the txn, we need this to estimate gas
            txn["from"] = addy

            try:
                w3.eth.estimateGas(txn)     # Check if this txn will fail.  This throws an error if it can't estimate gas
                signedTxn = w3.eth.account.sign_transaction(txn, key)
                w3.eth.sendRawTransaction(signedTxn.rawTransaction)
                print(w3.toHex(w3.keccak(signedTxn.rawTransaction)))
                nonce = nonce + 1
            except Exception as e:
                print("Gas Estimation failed.  Already Relayed.")


def main():
    # Set up the command line arguments
    parser = argparse.ArgumentParser(
        description='Python Based CXO CLI Relayer'
    )
    parser.add_argument(
        "-gas", "--gas", help="Gas amount you want to process with in gwei.", type=str, default='100'
    )
    parser.add_argument(
        "-key", "--key", help="Private Key for the matic account.", type=str, required=True
    )
    parser.add_argument(
        "-vault", "--vault", help="Address for storing the CXO.", type=str, required=True
    )
    parser.add_argument(
        "-fetchDelay", "--fetchDelay", help="Time between API requests [seconds].", type=int, default=25
    )
    parser.add_argument(
        "-cacheDelay", "--cacheDelay", help="Time between cache clears [seconds].", type=int, default=43200
    )
    parser.add_argument(
        "-rpcURL", "--rpcURL", help="Full RPC URL", type=str, default="https://polygon-rpc.com/"
    )
    parser.add_argument(
        "-apiURL", "--apiURL", help="API URL ends with /relay", type=str, default="https://cargox.digital/api/v3/relay/"
    )
    parser.add_argument(
        "-timeout", "--timeout", help="Timeout for the api requests", type=int, default=10
    )
    args = parser.parse_args()
    # print(args)
    # End of command line arguments set up

    # get time at the start of the program and store in the fetch and cache starts
    startTime = time.time()
    fetchStartTime = startTime
    cacheStartTime = startTime

    # Pull the command line args for the fetch and cache delay
    fetchDelay = args.fetchDelay
    cacheClearDelay = args.cacheDelay
    # Initial Relay at start up so that we don't wait a full delay before relaying
    relay(args.key, args.vault, args.gas, args.rpcURL, args.apiURL, args.timeout)

    while 1:
        # Get current Time
        currentTime = time.time()
        # Get the individual delta times to know when to attempt to relay and when to clear cache
        fetchDelta = currentTime - fetchStartTime
        cacheClearDelta = currentTime - cacheStartTime
        if fetchDelta >= fetchDelay:
            # Attempt to Relay
            fetchDelta = 0
            try:
                relay(args.key, args.vault, args.gas, args.rpcURL, args.apiURL, args.timeout)
            except Exception as e:
                print('Strange Error, ignoring probably an api issue.')
            fetchStartTime = time.time()
            timestamp = datetime.now()
            print("Resetting Timer: ", timestamp)
        if cacheClearDelta >= cacheClearDelay:
            # Clear our cache
            cacheClearDelta = 0
            relayCache = []
            print("Clearing Cache")
            cacheStartTime = time.time()
        time.sleep(args.fetchDelay / 5)


if __name__ == '__main__':
    main()

