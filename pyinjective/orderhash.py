import sha3
import requests
from decimal import Decimal
from eip712_structs import make_domain, EIP712Struct, String

class OrderInfo(EIP712Struct):
    SubaccountId = String()
    FeeRecipient = String()
    Price = String()
    Quantity = String()

class SpotOrder(EIP712Struct):
    MarketId = String()
    OrderInfo = OrderInfo
    Salt = String()
    OrderType = String()
    TriggerPrice = String()

class DerivativeOrder(EIP712Struct):
    MarketId = String()
    OrderInfo = OrderInfo
    OrderType = String()
    Margin = String()
    TriggerPrice = String()
    Salt = String()

EIP712_domain = make_domain(
    name='Injective Protocol',
    version='2.0.0',
    chainId=888,
    verifyingContract='0xCcCCccccCCCCcCCCCCCcCcCccCcCCCcCcccccccC',
    salt='0x0000000000000000000000000000000000000000000000000000000000000000'
)

domain_separator = EIP712_domain.hash_struct()
order_type_dict = {0: '\x00', 1: '\x01', 2: '\x02', 3: '\x03', 4: '\x04', 5: '\x05', 6: '\x06', 7: '\x07', 8: '\x08'}

def param_to_backend_go(param) -> int:
    go_param = Decimal(param) / pow(10, 18)
    return format(go_param, '.18f')

def get_subaccount_nonce(network, subaccount_id) -> int:
    url = network.lcd_endpoint + '/injective/exchange/v1beta1/exchange/' + subaccount_id
    res = requests.get(url = url)
    return res.json()["nonce"]

def parse_order_type(order):
    return order_type_dict[order.order_type]

def build_eip712_msg(network, order, nonce):
    if order.__class__.__name__ == 'SpotOrder':
        go_price = param_to_backend_go(order.order_info.price)
        go_trigger_price = param_to_backend_go(order.trigger_price)
        go_quantity = param_to_backend_go(order.order_info.quantity)
        go_order_type = parse_order_type(order)
        return SpotOrder(
            MarketId=order.market_id,
            OrderInfo=OrderInfo(
                SubaccountId=order.order_info.subaccount_id,
                FeeRecipient=order.order_info.fee_recipient,
                Price=go_price,
                Quantity=go_quantity
            ),
            Salt=str(nonce),
            OrderType=go_order_type,
            TriggerPrice=go_trigger_price
        )
    if order.__class__.__name__ == 'DerivativeOrder':
        go_price = param_to_backend_go(order.order_info.price)
        go_trigger_price = param_to_backend_go(order.trigger_price)
        go_quantity = param_to_backend_go(order.order_info.quantity)
        go_margin = param_to_backend_go(order.margin)
        go_order_type = parse_order_type(order)
        return DerivativeOrder(
            MarketId=order.market_id,
            OrderInfo=OrderInfo(
                SubaccountId=order.order_info.subaccount_id,
                FeeRecipient=order.order_info.fee_recipient,
                Price=go_price,
                Quantity=go_quantity
            ),
            Salt=str(nonce),
            OrderType=go_order_type,
            TriggerPrice=go_trigger_price,
            Margin=go_margin
        )

# only support msgs from single subaccount
def compute_order_hashes(network, orders) -> [str]:
    # get starting nonce
    nonce = get_subaccount_nonce(network, orders[0].order_info.subaccount_id)
    print("starting subaccount nonce", nonce)
    # compute hashes
    order_hashes = []
    for o in orders:
        # increase nonce for next order
        nonce += 1
        # construct eip712 msg
        msg = build_eip712_msg(network, o, nonce)
        # compute order hash
        typed_data_hash = msg.hash_struct()
        typed_bytes = b'\x19\x01' + domain_separator + typed_data_hash
        keccak256 = sha3.keccak_256()
        keccak256.update(typed_bytes)
        order_hash = keccak256.hexdigest()
        order_hashes.append('0x' + order_hash)

    return order_hashes
