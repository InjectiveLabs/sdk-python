import asyncio
import time

from pyinjective.async_client import AsyncClient
from pyinjective.transaction import Transaction
from pyinjective.core.network import Network
from pyinjective.wallet import PrivateKey

def mint_amount_from_response(resp):
    for ev in resp.tx_response.events:
        if ev.type != "wasm-lp_balance_changed":
            continue
        for attr in ev.attributes:
            if attr.key == "mint_amount":
                return attr.value
    return ""
                    
            
async def main() -> None:
    # # select network: local, testnet, mainnet
    network = Network.testnet(node='sentry')

    # # initialize grpc client
    # # set custom cookie location (optional) - defaults to current dir
    client = AsyncClient(network)
    composer = await client.composer()
    await client.sync_timeout_height()

    # load account
    priv_key = PrivateKey.from_hex("f9db9bf330e23cb7839039e944adef6e9df447b90b503d5b4464c90bea9022f3")
    pub_key = priv_key.to_public_key()
    address = pub_key.to_address()
    await client.get_account(address.to_acc_bech32())
    subaccount_id = address.get_subaccount_id(0)

    contract_address = "inj1ckmdhdz7r8glfurckgtg0rt7x9uvner4ygqhlv"
    msg = composer.MsgPrivilegedExecuteContract(
        sender=address.to_acc_bech32(),
        contract=contract_address,
        msg="""
            {
				"origin":"%s",
				"name":"Subscribe",
				"args":{
					"Subscribe":{
						"args":{
							"subscriber_subaccount_id":"%s"
						}
					}
				}
			}
        """ % (address.to_acc_bech32(), subaccount_id),
        funds='10000000000000000000inj,80000000peggy0x87aB3B4C8661e07D6372361211B96ed4Dc36B1B5',
    )

    # build sim tx
    tx = (
        Transaction()
        .with_messages(msg)
        .with_sequence(client.get_sequence())
        .with_account_num(client.get_number())
        .with_chain_id(network.chain_id)
    )
    sim_sign_doc = tx.get_sign_doc(pub_key)
    sim_sig = priv_key.sign(sim_sign_doc.SerializeToString())
    sim_tx_raw_bytes = tx.get_tx_data(sim_sig, pub_key)

    # simulate tx
    (sim_res, success) = await client.simulate_tx(sim_tx_raw_bytes)
    if not success:
        print(sim_res)
        return

    # build tx
    gas_price = 500000000
    gas_limit = sim_res.gas_info.gas_used + 20000  # add 20k for gas, fee computation
    # gas_fee = '{:.18f}'.format((gas_price * gas_limit) / pow(10, 18)).rstrip('0')
    fee = [composer.Coin(
        amount=gas_price * gas_limit,
        denom=network.fee_denom,
    )]
    tx = tx.with_gas(gas_limit).with_fee(fee).with_memo('').with_timeout_height(client.timeout_height)
    sign_doc = tx.get_sign_doc(pub_key)
    sig = priv_key.sign(sign_doc.SerializeToString())
    tx_raw_bytes = tx.get_tx_data(sig, pub_key)

    # broadcast tx: send_tx_async_mode, send_tx_sync_mode, send_tx_block_mode
    res = await client.send_tx_sync_mode(tx_raw_bytes)
    hash = res.txhash
    print('instantiate tx hash:', hash)

    retry_count = 5
    resp = None
    for _ in range(retry_count):
        try:
            resp = await client.get_tx(hash)
            break
        except:
            pass
        time.sleep(0.2)

    if resp == None:
        print('tx is not succeeded')
        return
    print('spot vault LP mint amount:', mint_amount_from_response(resp) + 'factory/%s/lp' % contract_address)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())