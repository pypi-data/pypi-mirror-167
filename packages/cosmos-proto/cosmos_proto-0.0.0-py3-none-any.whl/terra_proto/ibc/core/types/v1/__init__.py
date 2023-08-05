# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ibc/core/types/v1/genesis.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the ibc module's genesis state."""

    # ICS002 - Clients genesis state
    client_genesis: "__client_v1__.GenesisState" = betterproto.message_field(1)
    # ICS003 - Connections genesis state
    connection_genesis: "__connection_v1__.GenesisState" = betterproto.message_field(2)
    # ICS004 - Channel genesis state
    channel_genesis: "__channel_v1__.GenesisState" = betterproto.message_field(3)


from ...channel import v1 as __channel_v1__
from ...client import v1 as __client_v1__
from ...connection import v1 as __connection_v1__
