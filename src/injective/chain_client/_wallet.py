import bech32
import ecdsa
import hdwallets
import mnemonic
import sha3

from hdwallets import BIP32DerivationError as BIP32DerivationError
from ._typings import Wallet


DEFAULT_DERIVATION_PATH = "m/44'/60'/0'/0/0"
DEFAULT_BECH32_HRP = "inj"


def generate_wallet(
    *, path: str = DEFAULT_DERIVATION_PATH, hrp: str = DEFAULT_BECH32_HRP
) -> Wallet:
    while True:
        phrase = mnemonic.Mnemonic(language="english").generate(strength=256)
        try:
            privkey = seed_to_privkey(phrase, path=path)
            break
        except BIP32DerivationError:
            pass
    pubkey = privkey_to_uncompressed_pubkey(privkey)
    address = pubkey_to_address(pubkey, hrp=hrp)
    return {
        "seed": phrase,
        "derivation_path": path,
        "private_key": privkey,
        "public_key": pubkey,
        "address": address,
    }


def seed_to_privkey(seed: str, path: str = DEFAULT_DERIVATION_PATH) -> bytes:
    """Get a private key from a mnemonic seed and a derivation path.

    Assumes a BIP39 mnemonic seed with no passphrase. Raises
    `BIP32DerivationError` if the resulting private key is
    invalid.
    """
    seed_bytes = mnemonic.Mnemonic.to_seed(seed, passphrase="")
    hd_wallet = hdwallets.BIP32.from_seed(seed_bytes)
    # This can raise a `hdwallets.BIP32DerivationError` (which we alias so
    # that the same exception type is also in the `chainclient` namespace).
    derived_privkey = hd_wallet.get_privkey_from_path(path)

    return derived_privkey


def privkey_to_uncompressed_pubkey(privkey: bytes) -> bytes:
    privkey_obj = ecdsa.SigningKey.from_string(privkey, curve=ecdsa.SECP256k1)
    pubkey_obj = privkey_obj.get_verifying_key()
    return pubkey_obj.to_string("uncompressed")


def privkey_to_pubkey(privkey: bytes) -> bytes:
    privkey_obj = ecdsa.SigningKey.from_string(privkey, curve=ecdsa.SECP256k1)
    pubkey_obj = privkey_obj.get_verifying_key()
    return pubkey_obj.to_string("compressed")


def pubkey_to_address(pubkey: bytes, *, hrp: str = DEFAULT_BECH32_HRP) -> str:
    if len(pubkey) != 65:
        raise ValueError("wrong pubkey length (must be uncompressed, len = 65)")

    # This is for vanilla Cosmos SDK folks
    #   s = hashlib.new("sha256", pubkey).digest()
    #   r = hashlib.new("ripemd160", s).digest()

    # --
    # This is for EVM compatible chads
    k = sha3.keccak_256()
    k.update(pubkey[1:])
    addr = k.digest()[12:]

    five_bit_r = bech32.convertbits(addr, 8, 5)
    assert five_bit_r is not None, "Unsuccessful bech32.convertbits call"
    return bech32.bech32_encode(hrp, five_bit_r)


def privkey_to_address(privkey: bytes, *, hrp: str = DEFAULT_BECH32_HRP) -> str:
    pubkey = privkey_to_uncompressed_pubkey(privkey)
    return pubkey_to_address(pubkey, hrp=hrp)
