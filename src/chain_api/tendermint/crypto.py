# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: tendermint/crypto/keys.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class PublicKey(betterproto.Message):
    """
    PublicKey defines the keys available for use with Tendermint Validators
    """

    ed25519: bytes = betterproto.bytes_field(1, group="sum")
    secp256k1: bytes = betterproto.bytes_field(2, group="sum")
