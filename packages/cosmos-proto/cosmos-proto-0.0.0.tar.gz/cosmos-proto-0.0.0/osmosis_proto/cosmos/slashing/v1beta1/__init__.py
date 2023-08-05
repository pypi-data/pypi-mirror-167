# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/slashing/v1beta1/genesis.proto, cosmos/slashing/v1beta1/query.proto, cosmos/slashing/v1beta1/slashing.proto, cosmos/slashing/v1beta1/tx.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict, List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


@dataclass(eq=False, repr=False)
class MsgUnjail(betterproto.Message):
    """MsgUnjail defines the Msg/Unjail request type"""

    validator_addr: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class MsgUnjailResponse(betterproto.Message):
    """MsgUnjailResponse defines the Msg/Unjail response type"""

    pass


@dataclass(eq=False, repr=False)
class ValidatorSigningInfo(betterproto.Message):
    """
    ValidatorSigningInfo defines a validator's signing info for monitoring
    their liveness activity.
    """

    address: str = betterproto.string_field(1)
    # Height at which validator was first a candidate OR was unjailed
    start_height: int = betterproto.int64_field(2)
    # Index which is incremented each time the validator was a bonded in a block
    # and may have signed a precommit or not. This in conjunction with the
    # `SignedBlocksWindow` param determines the index in the
    # `MissedBlocksBitArray`.
    index_offset: int = betterproto.int64_field(3)
    # Timestamp until which the validator is jailed due to liveness downtime.
    jailed_until: datetime = betterproto.message_field(4)
    # Whether or not a validator has been tombstoned (killed out of validator
    # set). It is set once the validator commits an equivocation or for any other
    # configured misbehiavor.
    tombstoned: bool = betterproto.bool_field(5)
    # A counter kept to avoid unnecessary array reads. Note that
    # `Sum(MissedBlocksBitArray)` always equals `MissedBlocksCounter`.
    missed_blocks_counter: int = betterproto.int64_field(6)


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params represents the parameters used for by the slashing module."""

    signed_blocks_window: int = betterproto.int64_field(1)
    min_signed_per_window: bytes = betterproto.bytes_field(2)
    downtime_jail_duration: timedelta = betterproto.message_field(3)
    slash_fraction_double_sign: bytes = betterproto.bytes_field(4)
    slash_fraction_downtime: bytes = betterproto.bytes_field(5)


@dataclass(eq=False, repr=False)
class QueryParamsRequest(betterproto.Message):
    """
    QueryParamsRequest is the request type for the Query/Params RPC method
    """

    pass


@dataclass(eq=False, repr=False)
class QueryParamsResponse(betterproto.Message):
    """
    QueryParamsResponse is the response type for the Query/Params RPC method
    """

    params: "Params" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QuerySigningInfoRequest(betterproto.Message):
    """
    QuerySigningInfoRequest is the request type for the Query/SigningInfo RPC
    method
    """

    # cons_address is the address to query signing info of
    cons_address: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QuerySigningInfoResponse(betterproto.Message):
    """
    QuerySigningInfoResponse is the response type for the Query/SigningInfo RPC
    method
    """

    # val_signing_info is the signing info of requested val cons address
    val_signing_info: "ValidatorSigningInfo" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QuerySigningInfosRequest(betterproto.Message):
    """
    QuerySigningInfosRequest is the request type for the Query/SigningInfos RPC
    method
    """

    pagination: "__base_query_v1_beta1__.PageRequest" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QuerySigningInfosResponse(betterproto.Message):
    """
    QuerySigningInfosResponse is the response type for the Query/SigningInfos
    RPC method
    """

    # info is the signing info of all validators
    info: List["ValidatorSigningInfo"] = betterproto.message_field(1)
    pagination: "__base_query_v1_beta1__.PageResponse" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the slashing module's genesis state."""

    # params defines all the paramaters of related to deposit.
    params: "Params" = betterproto.message_field(1)
    # signing_infos represents a map between validator addresses and their
    # signing infos.
    signing_infos: List["SigningInfo"] = betterproto.message_field(2)
    # missed_blocks represents a map between validator addresses and their missed
    # blocks.
    missed_blocks: List["ValidatorMissedBlocks"] = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class SigningInfo(betterproto.Message):
    """SigningInfo stores validator signing info of corresponding address."""

    # address is the validator address.
    address: str = betterproto.string_field(1)
    # validator_signing_info represents the signing info of this validator.
    validator_signing_info: "ValidatorSigningInfo" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class ValidatorMissedBlocks(betterproto.Message):
    """
    ValidatorMissedBlocks contains array of missed blocks of corresponding
    address.
    """

    # address is the validator address.
    address: str = betterproto.string_field(1)
    # missed_blocks is an array of missed blocks by the validator.
    missed_blocks: List["MissedBlock"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class MissedBlock(betterproto.Message):
    """MissedBlock contains height and missed status as boolean."""

    # index is the height at which the block was missed.
    index: int = betterproto.int64_field(1)
    # missed is the missed status.
    missed: bool = betterproto.bool_field(2)


class MsgStub(betterproto.ServiceStub):
    async def unjail(self, *, validator_addr: str = "") -> "MsgUnjailResponse":

        request = MsgUnjail()
        request.validator_addr = validator_addr

        return await self._unary_unary(
            "/cosmos.slashing.v1beta1.Msg/Unjail", request, MsgUnjailResponse
        )


class QueryStub(betterproto.ServiceStub):
    async def params(self) -> "QueryParamsResponse":

        request = QueryParamsRequest()

        return await self._unary_unary(
            "/cosmos.slashing.v1beta1.Query/Params", request, QueryParamsResponse
        )

    async def signing_info(
        self, *, cons_address: str = ""
    ) -> "QuerySigningInfoResponse":

        request = QuerySigningInfoRequest()
        request.cons_address = cons_address

        return await self._unary_unary(
            "/cosmos.slashing.v1beta1.Query/SigningInfo",
            request,
            QuerySigningInfoResponse,
        )

    async def signing_infos(
        self, *, pagination: "__base_query_v1_beta1__.PageRequest" = None
    ) -> "QuerySigningInfosResponse":

        request = QuerySigningInfosRequest()
        if pagination is not None:
            request.pagination = pagination

        return await self._unary_unary(
            "/cosmos.slashing.v1beta1.Query/SigningInfos",
            request,
            QuerySigningInfosResponse,
        )


class MsgBase(ServiceBase):
    async def unjail(self, validator_addr: str) -> "MsgUnjailResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_unjail(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "validator_addr": request.validator_addr,
        }

        response = await self.unjail(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.slashing.v1beta1.Msg/Unjail": grpclib.const.Handler(
                self.__rpc_unjail,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgUnjail,
                MsgUnjailResponse,
            ),
        }


class QueryBase(ServiceBase):
    async def params(self) -> "QueryParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def signing_info(self, cons_address: str) -> "QuerySigningInfoResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def signing_infos(
        self, pagination: "__base_query_v1_beta1__.PageRequest"
    ) -> "QuerySigningInfosResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_params(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.params(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_signing_info(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "cons_address": request.cons_address,
        }

        response = await self.signing_info(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_signing_infos(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "pagination": request.pagination,
        }

        response = await self.signing_infos(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.slashing.v1beta1.Query/Params": grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
            "/cosmos.slashing.v1beta1.Query/SigningInfo": grpclib.const.Handler(
                self.__rpc_signing_info,
                grpclib.const.Cardinality.UNARY_UNARY,
                QuerySigningInfoRequest,
                QuerySigningInfoResponse,
            ),
            "/cosmos.slashing.v1beta1.Query/SigningInfos": grpclib.const.Handler(
                self.__rpc_signing_infos,
                grpclib.const.Cardinality.UNARY_UNARY,
                QuerySigningInfosRequest,
                QuerySigningInfosResponse,
            ),
        }


from ...base.query import v1beta1 as __base_query_v1_beta1__
