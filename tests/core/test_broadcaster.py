import json
import os
import unittest
from unittest.mock import Mock

import pytest

import pyinjective.ofac as ofac
from pyinjective import PrivateKey
from pyinjective.async_client import AsyncClient
from pyinjective.composer import Composer
from pyinjective.core.broadcaster import MsgBroadcasterWithPk, StandardAccountBroadcasterConfig
from pyinjective.core.network import Network


class TestBroadcastAddressInOfacList(unittest.TestCase):
    def setUp(self):
        ofac.OFAC_LIST_FILENAME = "ofac_test.json"
        self.private_key_banned = PrivateKey.from_mnemonic("test mnemonic never use other places")
        public_key_banned = self.private_key_banned.to_public_key()
        address_banned = public_key_banned.to_address()

        ofac_list = [address_banned.to_acc_bech32()]

        with open(ofac.OfacChecker.get_ofac_list_path(), "w") as ofac_file:
            json.dump(ofac_list, ofac_file)

    def tearDown(self):
        os.remove(ofac.OfacChecker.get_ofac_list_path())
        ofac.OFAC_LIST_FILENAME = ofac.OFAC_LIST_FILENAME_DEFAULT

    def test_broadcast_address_in_ofac_list(self):
        network = Network.local()
        client = AsyncClient(
            network=Network.local(),
        )
        composer = Mock(spec=Composer)

        account_config = StandardAccountBroadcasterConfig(private_key=self.private_key_banned.to_hex())

        with pytest.raises(Exception):
            _ = MsgBroadcasterWithPk(
                network=network,
                account_config=account_config,
                client=client,
                composer=composer,
                fee_calculator=Mock(),
            )
