# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exchange/injective_campaign_rpc.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%exchange/injective_campaign_rpc.proto\x12\x16injective_campaign_rpc\"\xa1\x01\n\x0eRankingRequest\x12\x1f\n\x0b\x63\x61mpaign_id\x18\x01 \x01(\tR\ncampaignId\x12\x1b\n\tmarket_id\x18\x02 \x01(\tR\x08marketId\x12\'\n\x0f\x61\x63\x63ount_address\x18\x03 \x01(\tR\x0e\x61\x63\x63ountAddress\x12\x14\n\x05limit\x18\x04 \x01(\x11R\x05limit\x12\x12\n\x04skip\x18\x05 \x01(\x04R\x04skip\"\xc3\x01\n\x0fRankingResponse\x12<\n\x08\x63\x61mpaign\x18\x01 \x01(\x0b\x32 .injective_campaign_rpc.CampaignR\x08\x63\x61mpaign\x12:\n\x05users\x18\x02 \x03(\x0b\x32$.injective_campaign_rpc.CampaignUserR\x05users\x12\x36\n\x06paging\x18\x03 \x01(\x0b\x32\x1e.injective_campaign_rpc.PagingR\x06paging\"\xf7\x02\n\x08\x43\x61mpaign\x12\x1f\n\x0b\x63\x61mpaign_id\x18\x01 \x01(\tR\ncampaignId\x12\x1b\n\tmarket_id\x18\x02 \x01(\tR\x08marketId\x12\x1f\n\x0btotal_score\x18\x04 \x01(\tR\ntotalScore\x12!\n\x0clast_updated\x18\x05 \x01(\x12R\x0blastUpdated\x12\x1d\n\nstart_date\x18\x06 \x01(\x12R\tstartDate\x12\x19\n\x08\x65nd_date\x18\x07 \x01(\x12R\x07\x65ndDate\x12!\n\x0cis_claimable\x18\x08 \x01(\x08R\x0bisClaimable\x12\x19\n\x08round_id\x18\t \x01(\x11R\x07roundId\x12\x1a\n\x08\x63ontract\x18\n \x01(\tR\x08\x63ontract\x12\x36\n\x07rewards\x18\x0b \x03(\x0b\x32\x1c.injective_campaign_rpc.CoinR\x07rewards\x12\x1d\n\nuser_score\x18\x0c \x01(\tR\tuserScore\"4\n\x04\x43oin\x12\x14\n\x05\x64\x65nom\x18\x01 \x01(\tR\x05\x64\x65nom\x12\x16\n\x06\x61mount\x18\x02 \x01(\tR\x06\x61mount\"\xc8\x02\n\x0c\x43\x61mpaignUser\x12\x1f\n\x0b\x63\x61mpaign_id\x18\x01 \x01(\tR\ncampaignId\x12\x1b\n\tmarket_id\x18\x02 \x01(\tR\x08marketId\x12\'\n\x0f\x61\x63\x63ount_address\x18\x03 \x01(\tR\x0e\x61\x63\x63ountAddress\x12\x14\n\x05score\x18\x04 \x01(\tR\x05score\x12)\n\x10\x63ontract_updated\x18\x05 \x01(\x08R\x0f\x63ontractUpdated\x12!\n\x0c\x62lock_height\x18\x06 \x01(\x12R\x0b\x62lockHeight\x12\x1d\n\nblock_time\x18\x07 \x01(\x12R\tblockTime\x12)\n\x10purchased_amount\x18\x08 \x01(\tR\x0fpurchasedAmount\x12#\n\rgalxe_updated\x18\t \x01(\x08R\x0cgalxeUpdated\"\x86\x01\n\x06Paging\x12\x14\n\x05total\x18\x01 \x01(\x12R\x05total\x12\x12\n\x04\x66rom\x18\x02 \x01(\x11R\x04\x66rom\x12\x0e\n\x02to\x18\x03 \x01(\x11R\x02to\x12.\n\x13\x63ount_by_subaccount\x18\x04 \x01(\x12R\x11\x63ountBySubaccount\x12\x12\n\x04next\x18\x05 \x03(\tR\x04next\"v\n\x10\x43\x61mpaignsRequest\x12\x19\n\x08round_id\x18\x01 \x01(\x12R\x07roundId\x12\'\n\x0f\x61\x63\x63ount_address\x18\x02 \x01(\tR\x0e\x61\x63\x63ountAddress\x12\x1e\n\x0bto_round_id\x18\x03 \x01(\x11R\ttoRoundId\"\x9a\x01\n\x11\x43\x61mpaignsResponse\x12>\n\tcampaigns\x18\x01 \x03(\x0b\x32 .injective_campaign_rpc.CampaignR\tcampaigns\x12\x45\n\x0f\x61\x63\x63ount_rewards\x18\x02 \x03(\x0b\x32\x1c.injective_campaign_rpc.CoinR\x0e\x61\x63\x63ountRewards\"\x83\x01\n\x11ListGuildsRequest\x12+\n\x11\x63\x61mpaign_contract\x18\x01 \x01(\tR\x10\x63\x61mpaignContract\x12\x14\n\x05limit\x18\x02 \x01(\x11R\x05limit\x12\x12\n\x04skip\x18\x03 \x01(\x11R\x04skip\x12\x17\n\x07sort_by\x18\x04 \x01(\tR\x06sortBy\"\xf6\x01\n\x12ListGuildsResponse\x12\x35\n\x06guilds\x18\x01 \x03(\x0b\x32\x1d.injective_campaign_rpc.GuildR\x06guilds\x12\x36\n\x06paging\x18\x02 \x01(\x0b\x32\x1e.injective_campaign_rpc.PagingR\x06paging\x12\x1d\n\nupdated_at\x18\x03 \x01(\x12R\tupdatedAt\x12R\n\x10\x63\x61mpaign_summary\x18\x04 \x01(\x0b\x32\'.injective_campaign_rpc.CampaignSummaryR\x0f\x63\x61mpaignSummary\"\xe5\x03\n\x05Guild\x12+\n\x11\x63\x61mpaign_contract\x18\x01 \x01(\tR\x10\x63\x61mpaignContract\x12\x19\n\x08guild_id\x18\x02 \x01(\tR\x07guildId\x12%\n\x0emaster_address\x18\x03 \x01(\tR\rmasterAddress\x12\x1d\n\ncreated_at\x18\x04 \x01(\x12R\tcreatedAt\x12\x1b\n\ttvl_score\x18\x05 \x01(\tR\x08tvlScore\x12!\n\x0cvolume_score\x18\x06 \x01(\tR\x0bvolumeScore\x12$\n\x0erank_by_volume\x18\x07 \x01(\x11R\x0crankByVolume\x12\x1e\n\x0brank_by_tvl\x18\x08 \x01(\x11R\trankByTvl\x12\x12\n\x04logo\x18\t \x01(\tR\x04logo\x12\x1b\n\ttotal_tvl\x18\n \x01(\tR\x08totalTvl\x12\x1d\n\nupdated_at\x18\x0b \x01(\x12R\tupdatedAt\x12\x12\n\x04name\x18\x0e \x01(\tR\x04name\x12\x1b\n\tis_active\x18\r \x01(\x08R\x08isActive\x12%\n\x0emaster_balance\x18\x0f \x01(\tR\rmasterBalance\x12 \n\x0b\x64\x65scription\x18\x10 \x01(\tR\x0b\x64\x65scription\"\x82\x03\n\x0f\x43\x61mpaignSummary\x12\x1f\n\x0b\x63\x61mpaign_id\x18\x01 \x01(\tR\ncampaignId\x12+\n\x11\x63\x61mpaign_contract\x18\x02 \x01(\tR\x10\x63\x61mpaignContract\x12,\n\x12total_guilds_count\x18\x03 \x01(\x11R\x10totalGuildsCount\x12\x1b\n\ttotal_tvl\x18\x04 \x01(\tR\x08totalTvl\x12*\n\x11total_average_tvl\x18\x05 \x01(\tR\x0ftotalAverageTvl\x12!\n\x0ctotal_volume\x18\x06 \x01(\tR\x0btotalVolume\x12\x1d\n\nupdated_at\x18\x07 \x01(\x12R\tupdatedAt\x12.\n\x13total_members_count\x18\x08 \x01(\x11R\x11totalMembersCount\x12\x1d\n\nstart_time\x18\t \x01(\x12R\tstartTime\x12\x19\n\x08\x65nd_time\x18\n \x01(\x12R\x07\x65ndTime\"\xd2\x01\n\x17ListGuildMembersRequest\x12+\n\x11\x63\x61mpaign_contract\x18\x01 \x01(\tR\x10\x63\x61mpaignContract\x12\x19\n\x08guild_id\x18\x02 \x01(\tR\x07guildId\x12\x14\n\x05limit\x18\x03 \x01(\x11R\x05limit\x12\x12\n\x04skip\x18\x04 \x01(\x11R\x04skip\x12,\n\x12include_guild_info\x18\x05 \x01(\x08R\x10includeGuildInfo\x12\x17\n\x07sort_by\x18\x06 \x01(\tR\x06sortBy\"\xcf\x01\n\x18ListGuildMembersResponse\x12=\n\x07members\x18\x01 \x03(\x0b\x32#.injective_campaign_rpc.GuildMemberR\x07members\x12\x36\n\x06paging\x18\x02 \x01(\x0b\x32\x1e.injective_campaign_rpc.PagingR\x06paging\x12<\n\nguild_info\x18\x03 \x01(\x0b\x32\x1d.injective_campaign_rpc.GuildR\tguildInfo\"\xd3\x03\n\x0bGuildMember\x12+\n\x11\x63\x61mpaign_contract\x18\x01 \x01(\tR\x10\x63\x61mpaignContract\x12\x19\n\x08guild_id\x18\x02 \x01(\tR\x07guildId\x12\x18\n\x07\x61\x64\x64ress\x18\x03 \x01(\tR\x07\x61\x64\x64ress\x12\x1b\n\tjoined_at\x18\x04 \x01(\x12R\x08joinedAt\x12\x1b\n\ttvl_score\x18\x05 \x01(\tR\x08tvlScore\x12!\n\x0cvolume_score\x18\x06 \x01(\tR\x0bvolumeScore\x12\x1b\n\ttotal_tvl\x18\x07 \x01(\tR\x08totalTvl\x12\x36\n\x17volume_score_percentage\x18\x08 \x01(\x01R\x15volumeScorePercentage\x12\x30\n\x14tvl_score_percentage\x18\t \x01(\x01R\x12tvlScorePercentage\x12;\n\ntvl_reward\x18\n \x03(\x0b\x32\x1c.injective_campaign_rpc.CoinR\ttvlReward\x12\x41\n\rvolume_reward\x18\x0b \x03(\x0b\x32\x1c.injective_campaign_rpc.CoinR\x0cvolumeReward\"^\n\x15GetGuildMemberRequest\x12+\n\x11\x63\x61mpaign_contract\x18\x01 \x01(\tR\x10\x63\x61mpaignContract\x12\x18\n\x07\x61\x64\x64ress\x18\x02 \x01(\tR\x07\x61\x64\x64ress\"Q\n\x16GetGuildMemberResponse\x12\x37\n\x04info\x18\x01 \x01(\x0b\x32#.injective_campaign_rpc.GuildMemberR\x04info2\xa1\x04\n\x14InjectiveCampaignRPC\x12Z\n\x07Ranking\x12&.injective_campaign_rpc.RankingRequest\x1a\'.injective_campaign_rpc.RankingResponse\x12`\n\tCampaigns\x12(.injective_campaign_rpc.CampaignsRequest\x1a).injective_campaign_rpc.CampaignsResponse\x12\x63\n\nListGuilds\x12).injective_campaign_rpc.ListGuildsRequest\x1a*.injective_campaign_rpc.ListGuildsResponse\x12u\n\x10ListGuildMembers\x12/.injective_campaign_rpc.ListGuildMembersRequest\x1a\x30.injective_campaign_rpc.ListGuildMembersResponse\x12o\n\x0eGetGuildMember\x12-.injective_campaign_rpc.GetGuildMemberRequest\x1a..injective_campaign_rpc.GetGuildMemberResponseB\xc2\x01\n\x1a\x63om.injective_campaign_rpcB\x19InjectiveCampaignRpcProtoP\x01Z\x19/injective_campaign_rpcpb\xa2\x02\x03IXX\xaa\x02\x14InjectiveCampaignRpc\xca\x02\x14InjectiveCampaignRpc\xe2\x02 InjectiveCampaignRpc\\GPBMetadata\xea\x02\x14InjectiveCampaignRpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exchange.injective_campaign_rpc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.injective_campaign_rpcB\031InjectiveCampaignRpcProtoP\001Z\031/injective_campaign_rpcpb\242\002\003IXX\252\002\024InjectiveCampaignRpc\312\002\024InjectiveCampaignRpc\342\002 InjectiveCampaignRpc\\GPBMetadata\352\002\024InjectiveCampaignRpc'
  _globals['_RANKINGREQUEST']._serialized_start=66
  _globals['_RANKINGREQUEST']._serialized_end=227
  _globals['_RANKINGRESPONSE']._serialized_start=230
  _globals['_RANKINGRESPONSE']._serialized_end=425
  _globals['_CAMPAIGN']._serialized_start=428
  _globals['_CAMPAIGN']._serialized_end=803
  _globals['_COIN']._serialized_start=805
  _globals['_COIN']._serialized_end=857
  _globals['_CAMPAIGNUSER']._serialized_start=860
  _globals['_CAMPAIGNUSER']._serialized_end=1188
  _globals['_PAGING']._serialized_start=1191
  _globals['_PAGING']._serialized_end=1325
  _globals['_CAMPAIGNSREQUEST']._serialized_start=1327
  _globals['_CAMPAIGNSREQUEST']._serialized_end=1445
  _globals['_CAMPAIGNSRESPONSE']._serialized_start=1448
  _globals['_CAMPAIGNSRESPONSE']._serialized_end=1602
  _globals['_LISTGUILDSREQUEST']._serialized_start=1605
  _globals['_LISTGUILDSREQUEST']._serialized_end=1736
  _globals['_LISTGUILDSRESPONSE']._serialized_start=1739
  _globals['_LISTGUILDSRESPONSE']._serialized_end=1985
  _globals['_GUILD']._serialized_start=1988
  _globals['_GUILD']._serialized_end=2473
  _globals['_CAMPAIGNSUMMARY']._serialized_start=2476
  _globals['_CAMPAIGNSUMMARY']._serialized_end=2862
  _globals['_LISTGUILDMEMBERSREQUEST']._serialized_start=2865
  _globals['_LISTGUILDMEMBERSREQUEST']._serialized_end=3075
  _globals['_LISTGUILDMEMBERSRESPONSE']._serialized_start=3078
  _globals['_LISTGUILDMEMBERSRESPONSE']._serialized_end=3285
  _globals['_GUILDMEMBER']._serialized_start=3288
  _globals['_GUILDMEMBER']._serialized_end=3755
  _globals['_GETGUILDMEMBERREQUEST']._serialized_start=3757
  _globals['_GETGUILDMEMBERREQUEST']._serialized_end=3851
  _globals['_GETGUILDMEMBERRESPONSE']._serialized_start=3853
  _globals['_GETGUILDMEMBERRESPONSE']._serialized_end=3934
  _globals['_INJECTIVECAMPAIGNRPC']._serialized_start=3937
  _globals['_INJECTIVECAMPAIGNRPC']._serialized_end=4482
# @@protoc_insertion_point(module_scope)
