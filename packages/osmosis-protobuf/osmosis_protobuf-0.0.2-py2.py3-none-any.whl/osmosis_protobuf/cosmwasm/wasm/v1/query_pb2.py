"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmwasm.wasm.v1 import types_pb2 as cosmwasm_dot_wasm_dot_v1_dot_types__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ccosmwasm/wasm/v1/query.proto\x12\x10cosmwasm.wasm.v1\x1a\x14gogoproto/gogo.proto\x1a\x1ccosmwasm/wasm/v1/types.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto"+\n\x18QueryContractInfoRequest\x12\x0f\n\x07address\x18\x01 \x01(\t"w\n\x19QueryContractInfoResponse\x12\x0f\n\x07address\x18\x01 \x01(\t\x12C\n\rcontract_info\x18\x02 \x01(\x0b2\x1e.cosmwasm.wasm.v1.ContractInfoB\x0c\xd0\xde\x1f\x01\xc8\xde\x1f\x00\xea\xde\x1f\x00:\x04\xe8\xa0\x1f\x01"j\n\x1bQueryContractHistoryRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x9e\x01\n\x1cQueryContractHistoryResponse\x12A\n\x07entries\x18\x01 \x03(\x0b2*.cosmwasm.wasm.v1.ContractCodeHistoryEntryB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"j\n\x1bQueryContractsByCodeRequest\x12\x0f\n\x07code_id\x18\x01 \x01(\x04\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"n\n\x1cQueryContractsByCodeResponse\x12\x11\n\tcontracts\x18\x01 \x03(\t\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"k\n\x1cQueryAllContractStateRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x8b\x01\n\x1dQueryAllContractStateResponse\x12-\n\x06models\x18\x01 \x03(\x0b2\x17.cosmwasm.wasm.v1.ModelB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"C\n\x1cQueryRawContractStateRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12\x12\n\nquery_data\x18\x02 \x01(\x0c"-\n\x1dQueryRawContractStateResponse\x12\x0c\n\x04data\x18\x01 \x01(\x0c"]\n\x1eQuerySmartContractStateRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12*\n\nquery_data\x18\x02 \x01(\x0cB\x16\xfa\xde\x1f\x12RawContractMessage"G\n\x1fQuerySmartContractStateResponse\x12$\n\x04data\x18\x01 \x01(\x0cB\x16\xfa\xde\x1f\x12RawContractMessage"#\n\x10QueryCodeRequest\x12\x0f\n\x07code_id\x18\x01 \x01(\x04"\xeb\x01\n\x10CodeInfoResponse\x12!\n\x07code_id\x18\x01 \x01(\x04B\x10\xe2\xde\x1f\x06CodeID\xea\xde\x1f\x02id\x12\x0f\n\x07creator\x18\x02 \x01(\t\x12K\n\tdata_hash\x18\x03 \x01(\x0cB8\xfa\xde\x1f4github.com/tendermint/tendermint/libs/bytes.HexBytes\x12D\n\x16instantiate_permission\x18\x06 \x01(\x0b2\x1e.cosmwasm.wasm.v1.AccessConfigB\x04\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x01J\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06"r\n\x11QueryCodeResponse\x12?\n\tcode_info\x18\x01 \x01(\x0b2".cosmwasm.wasm.v1.CodeInfoResponseB\x08\xd0\xde\x1f\x01\xea\xde\x1f\x00\x12\x16\n\x04data\x18\x02 \x01(\x0cB\x08\xea\xde\x1f\x04data:\x04\xe8\xa0\x1f\x01"O\n\x11QueryCodesRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x8f\x01\n\x12QueryCodesResponse\x12<\n\ncode_infos\x18\x01 \x03(\x0b2".cosmwasm.wasm.v1.CodeInfoResponseB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"U\n\x17QueryPinnedCodesRequest\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"z\n\x18QueryPinnedCodesResponse\x12!\n\x08code_ids\x18\x01 \x03(\x04B\x0f\xc8\xde\x1f\x00\xe2\xde\x1f\x07CodeIDs\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse2\x89\x0b\n\x05Query\x12\x95\x01\n\x0cContractInfo\x12*.cosmwasm.wasm.v1.QueryContractInfoRequest\x1a+.cosmwasm.wasm.v1.QueryContractInfoResponse",\x82\xd3\xe4\x93\x02&\x12$/cosmwasm/wasm/v1/contract/{address}\x12\xa6\x01\n\x0fContractHistory\x12-.cosmwasm.wasm.v1.QueryContractHistoryRequest\x1a..cosmwasm.wasm.v1.QueryContractHistoryResponse"4\x82\xd3\xe4\x93\x02.\x12,/cosmwasm/wasm/v1/contract/{address}/history\x12\xa4\x01\n\x0fContractsByCode\x12-.cosmwasm.wasm.v1.QueryContractsByCodeRequest\x1a..cosmwasm.wasm.v1.QueryContractsByCodeResponse"2\x82\xd3\xe4\x93\x02,\x12*/cosmwasm/wasm/v1/code/{code_id}/contracts\x12\xa7\x01\n\x10AllContractState\x12..cosmwasm.wasm.v1.QueryAllContractStateRequest\x1a/.cosmwasm.wasm.v1.QueryAllContractStateResponse"2\x82\xd3\xe4\x93\x02,\x12*/cosmwasm/wasm/v1/contract/{address}/state\x12\xb2\x01\n\x10RawContractState\x12..cosmwasm.wasm.v1.QueryRawContractStateRequest\x1a/.cosmwasm.wasm.v1.QueryRawContractStateResponse"=\x82\xd3\xe4\x93\x027\x125/cosmwasm/wasm/v1/contract/{address}/raw/{query_data}\x12\xba\x01\n\x12SmartContractState\x120.cosmwasm.wasm.v1.QuerySmartContractStateRequest\x1a1.cosmwasm.wasm.v1.QuerySmartContractStateResponse"?\x82\xd3\xe4\x93\x029\x127/cosmwasm/wasm/v1/contract/{address}/smart/{query_data}\x12y\n\x04Code\x12".cosmwasm.wasm.v1.QueryCodeRequest\x1a#.cosmwasm.wasm.v1.QueryCodeResponse"(\x82\xd3\xe4\x93\x02"\x12 /cosmwasm/wasm/v1/code/{code_id}\x12r\n\x05Codes\x12#.cosmwasm.wasm.v1.QueryCodesRequest\x1a$.cosmwasm.wasm.v1.QueryCodesResponse"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/cosmwasm/wasm/v1/code\x12\x8c\x01\n\x0bPinnedCodes\x12).cosmwasm.wasm.v1.QueryPinnedCodesRequest\x1a*.cosmwasm.wasm.v1.QueryPinnedCodesResponse"&\x82\xd3\xe4\x93\x02 \x12\x1e/cosmwasm/wasm/v1/codes/pinnedB0Z&github.com/CosmWasm/wasmd/x/wasm/types\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_QUERYCONTRACTINFOREQUEST = DESCRIPTOR.message_types_by_name['QueryContractInfoRequest']
_QUERYCONTRACTINFORESPONSE = DESCRIPTOR.message_types_by_name['QueryContractInfoResponse']
_QUERYCONTRACTHISTORYREQUEST = DESCRIPTOR.message_types_by_name['QueryContractHistoryRequest']
_QUERYCONTRACTHISTORYRESPONSE = DESCRIPTOR.message_types_by_name['QueryContractHistoryResponse']
_QUERYCONTRACTSBYCODEREQUEST = DESCRIPTOR.message_types_by_name['QueryContractsByCodeRequest']
_QUERYCONTRACTSBYCODERESPONSE = DESCRIPTOR.message_types_by_name['QueryContractsByCodeResponse']
_QUERYALLCONTRACTSTATEREQUEST = DESCRIPTOR.message_types_by_name['QueryAllContractStateRequest']
_QUERYALLCONTRACTSTATERESPONSE = DESCRIPTOR.message_types_by_name['QueryAllContractStateResponse']
_QUERYRAWCONTRACTSTATEREQUEST = DESCRIPTOR.message_types_by_name['QueryRawContractStateRequest']
_QUERYRAWCONTRACTSTATERESPONSE = DESCRIPTOR.message_types_by_name['QueryRawContractStateResponse']
_QUERYSMARTCONTRACTSTATEREQUEST = DESCRIPTOR.message_types_by_name['QuerySmartContractStateRequest']
_QUERYSMARTCONTRACTSTATERESPONSE = DESCRIPTOR.message_types_by_name['QuerySmartContractStateResponse']
_QUERYCODEREQUEST = DESCRIPTOR.message_types_by_name['QueryCodeRequest']
_CODEINFORESPONSE = DESCRIPTOR.message_types_by_name['CodeInfoResponse']
_QUERYCODERESPONSE = DESCRIPTOR.message_types_by_name['QueryCodeResponse']
_QUERYCODESREQUEST = DESCRIPTOR.message_types_by_name['QueryCodesRequest']
_QUERYCODESRESPONSE = DESCRIPTOR.message_types_by_name['QueryCodesResponse']
_QUERYPINNEDCODESREQUEST = DESCRIPTOR.message_types_by_name['QueryPinnedCodesRequest']
_QUERYPINNEDCODESRESPONSE = DESCRIPTOR.message_types_by_name['QueryPinnedCodesResponse']
QueryContractInfoRequest = _reflection.GeneratedProtocolMessageType('QueryContractInfoRequest', (_message.Message,), {'DESCRIPTOR': _QUERYCONTRACTINFOREQUEST, '__module__': 'cosmwasm.wasm.v1.query_pb2'})
_sym_db.RegisterMessage(QueryContractInfoRequest)
QueryContractInfoResponse = _reflection.GeneratedProtocolMessageType('QueryContractInfoResponse', (_message.Message,), {'DESCRIPTOR': _QUERYCONTRACTINFORESPONSE, '__module__': 'cosmwasm.wasm.v1.query_pb2'})
_sym_db.RegisterMessage(QueryContractInfoResponse)
QueryContractHistoryRequest = _reflection.GeneratedProtocolMessageType('QueryContractHistoryRequest', (_message.Message,), {'DESCRIPTOR': _QUERYCONTRACTHISTORYREQUEST, '__module__': 'cosmwasm.wasm.v1.query_pb2'})
_sym_db.RegisterMessage(QueryContractHistoryRequest)
QueryContractHistoryResponse = _reflection.GeneratedProtocolMessageType('QueryContractHistoryResponse', (_message.Message,), {'DESCRIPTOR': _QUERYCONTRACTHISTORYRESPONSE, '__module__': 'cosmwasm.wasm.v1.query_pb2'})
_sym_db.RegisterMessage(QueryContractHistoryResponse)
QueryContractsByCodeRequest = _reflection.GeneratedProtocolMessageType('QueryContractsByCodeRequest', (_message.Message,), {'DESCRIPTOR': _QUERYCONTRACTSBYCODEREQUEST, '__module__': 'cosmwasm.wasm.v1.query_pb2'})
_sym_db.RegisterMessage(QueryContractsByCodeRequest)
QueryContractsByCodeResponse = _reflection.GeneratedProtocolMessageType('QueryContractsByCodeResponse', (_message.Message,), {'DESCRIPTOR': _QUERYCONTRACTSBYCODERESPONSE, '__module__': 'cosmwasm.wasm.v1.query_pb2'})
_sym_db.RegisterMessage(QueryContractsByCodeResponse)
QueryAllContractStateRequest = _reflection.GeneratedProtocolMessageType('QueryAllContractStateRequest', (_message.Message,), {'DESCRIPTOR': _QUERYALLCONTRACTSTATEREQUEST, '__module__': 'cosmwasm.wasm.v1.query_pb2'})
_sym_db.RegisterMessage(QueryAllContractStateRequest)
QueryAllContractStateResponse = _reflection.GeneratedProtocolMessageType('QueryAllContractStateResponse', (_message.Message,), {'DESCRIPTOR': _QUERYALLCONTRACTSTATERESPONSE, '__module__': 'cosmwasm.wasm.v1.query_pb2'})
_sym_db.RegisterMessage(QueryAllContractStateResponse)
QueryRawContractStateRequest = _reflection.GeneratedProtocolMessageType('QueryRawContractStateRequest', (_message.Message,), {'DESCRIPTOR': _QUERYRAWCONTRACTSTATEREQUEST, '__module__': 'cosmwasm.wasm.v1.query_pb2'})
_sym_db.RegisterMessage(QueryRawContractStateRequest)
QueryRawContractStateResponse = _reflection.GeneratedProtocolMessageType('QueryRawContractStateResponse', (_message.Message,), {'DESCRIPTOR': _QUERYRAWCONTRACTSTATERESPONSE, '__module__': 'cosmwasm.wasm.v1.query_pb2'})
_sym_db.RegisterMessage(QueryRawContractStateResponse)
QuerySmartContractStateRequest = _reflection.GeneratedProtocolMessageType('QuerySmartContractStateRequest', (_message.Message,), {'DESCRIPTOR': _QUERYSMARTCONTRACTSTATEREQUEST, '__module__': 'cosmwasm.wasm.v1.query_pb2'})
_sym_db.RegisterMessage(QuerySmartContractStateRequest)
QuerySmartContractStateResponse = _reflection.GeneratedProtocolMessageType('QuerySmartContractStateResponse', (_message.Message,), {'DESCRIPTOR': _QUERYSMARTCONTRACTSTATERESPONSE, '__module__': 'cosmwasm.wasm.v1.query_pb2'})
_sym_db.RegisterMessage(QuerySmartContractStateResponse)
QueryCodeRequest = _reflection.GeneratedProtocolMessageType('QueryCodeRequest', (_message.Message,), {'DESCRIPTOR': _QUERYCODEREQUEST, '__module__': 'cosmwasm.wasm.v1.query_pb2'})
_sym_db.RegisterMessage(QueryCodeRequest)
CodeInfoResponse = _reflection.GeneratedProtocolMessageType('CodeInfoResponse', (_message.Message,), {'DESCRIPTOR': _CODEINFORESPONSE, '__module__': 'cosmwasm.wasm.v1.query_pb2'})
_sym_db.RegisterMessage(CodeInfoResponse)
QueryCodeResponse = _reflection.GeneratedProtocolMessageType('QueryCodeResponse', (_message.Message,), {'DESCRIPTOR': _QUERYCODERESPONSE, '__module__': 'cosmwasm.wasm.v1.query_pb2'})
_sym_db.RegisterMessage(QueryCodeResponse)
QueryCodesRequest = _reflection.GeneratedProtocolMessageType('QueryCodesRequest', (_message.Message,), {'DESCRIPTOR': _QUERYCODESREQUEST, '__module__': 'cosmwasm.wasm.v1.query_pb2'})
_sym_db.RegisterMessage(QueryCodesRequest)
QueryCodesResponse = _reflection.GeneratedProtocolMessageType('QueryCodesResponse', (_message.Message,), {'DESCRIPTOR': _QUERYCODESRESPONSE, '__module__': 'cosmwasm.wasm.v1.query_pb2'})
_sym_db.RegisterMessage(QueryCodesResponse)
QueryPinnedCodesRequest = _reflection.GeneratedProtocolMessageType('QueryPinnedCodesRequest', (_message.Message,), {'DESCRIPTOR': _QUERYPINNEDCODESREQUEST, '__module__': 'cosmwasm.wasm.v1.query_pb2'})
_sym_db.RegisterMessage(QueryPinnedCodesRequest)
QueryPinnedCodesResponse = _reflection.GeneratedProtocolMessageType('QueryPinnedCodesResponse', (_message.Message,), {'DESCRIPTOR': _QUERYPINNEDCODESRESPONSE, '__module__': 'cosmwasm.wasm.v1.query_pb2'})
_sym_db.RegisterMessage(QueryPinnedCodesResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z&github.com/CosmWasm/wasmd/x/wasm/types\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _QUERYCONTRACTINFORESPONSE.fields_by_name['contract_info']._options = None
    _QUERYCONTRACTINFORESPONSE.fields_by_name['contract_info']._serialized_options = b'\xd0\xde\x1f\x01\xc8\xde\x1f\x00\xea\xde\x1f\x00'
    _QUERYCONTRACTINFORESPONSE._options = None
    _QUERYCONTRACTINFORESPONSE._serialized_options = b'\xe8\xa0\x1f\x01'
    _QUERYCONTRACTHISTORYRESPONSE.fields_by_name['entries']._options = None
    _QUERYCONTRACTHISTORYRESPONSE.fields_by_name['entries']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYALLCONTRACTSTATERESPONSE.fields_by_name['models']._options = None
    _QUERYALLCONTRACTSTATERESPONSE.fields_by_name['models']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYSMARTCONTRACTSTATEREQUEST.fields_by_name['query_data']._options = None
    _QUERYSMARTCONTRACTSTATEREQUEST.fields_by_name['query_data']._serialized_options = b'\xfa\xde\x1f\x12RawContractMessage'
    _QUERYSMARTCONTRACTSTATERESPONSE.fields_by_name['data']._options = None
    _QUERYSMARTCONTRACTSTATERESPONSE.fields_by_name['data']._serialized_options = b'\xfa\xde\x1f\x12RawContractMessage'
    _CODEINFORESPONSE.fields_by_name['code_id']._options = None
    _CODEINFORESPONSE.fields_by_name['code_id']._serialized_options = b'\xe2\xde\x1f\x06CodeID\xea\xde\x1f\x02id'
    _CODEINFORESPONSE.fields_by_name['data_hash']._options = None
    _CODEINFORESPONSE.fields_by_name['data_hash']._serialized_options = b'\xfa\xde\x1f4github.com/tendermint/tendermint/libs/bytes.HexBytes'
    _CODEINFORESPONSE.fields_by_name['instantiate_permission']._options = None
    _CODEINFORESPONSE.fields_by_name['instantiate_permission']._serialized_options = b'\xc8\xde\x1f\x00'
    _CODEINFORESPONSE._options = None
    _CODEINFORESPONSE._serialized_options = b'\xe8\xa0\x1f\x01'
    _QUERYCODERESPONSE.fields_by_name['code_info']._options = None
    _QUERYCODERESPONSE.fields_by_name['code_info']._serialized_options = b'\xd0\xde\x1f\x01\xea\xde\x1f\x00'
    _QUERYCODERESPONSE.fields_by_name['data']._options = None
    _QUERYCODERESPONSE.fields_by_name['data']._serialized_options = b'\xea\xde\x1f\x04data'
    _QUERYCODERESPONSE._options = None
    _QUERYCODERESPONSE._serialized_options = b'\xe8\xa0\x1f\x01'
    _QUERYCODESRESPONSE.fields_by_name['code_infos']._options = None
    _QUERYCODESRESPONSE.fields_by_name['code_infos']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYPINNEDCODESRESPONSE.fields_by_name['code_ids']._options = None
    _QUERYPINNEDCODESRESPONSE.fields_by_name['code_ids']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x07CodeIDs'
    _QUERY.methods_by_name['ContractInfo']._options = None
    _QUERY.methods_by_name['ContractInfo']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x12$/cosmwasm/wasm/v1/contract/{address}'
    _QUERY.methods_by_name['ContractHistory']._options = None
    _QUERY.methods_by_name['ContractHistory']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/cosmwasm/wasm/v1/contract/{address}/history'
    _QUERY.methods_by_name['ContractsByCode']._options = None
    _QUERY.methods_by_name['ContractsByCode']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/cosmwasm/wasm/v1/code/{code_id}/contracts'
    _QUERY.methods_by_name['AllContractState']._options = None
    _QUERY.methods_by_name['AllContractState']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/cosmwasm/wasm/v1/contract/{address}/state'
    _QUERY.methods_by_name['RawContractState']._options = None
    _QUERY.methods_by_name['RawContractState']._serialized_options = b'\x82\xd3\xe4\x93\x027\x125/cosmwasm/wasm/v1/contract/{address}/raw/{query_data}'
    _QUERY.methods_by_name['SmartContractState']._options = None
    _QUERY.methods_by_name['SmartContractState']._serialized_options = b'\x82\xd3\xe4\x93\x029\x127/cosmwasm/wasm/v1/contract/{address}/smart/{query_data}'
    _QUERY.methods_by_name['Code']._options = None
    _QUERY.methods_by_name['Code']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /cosmwasm/wasm/v1/code/{code_id}'
    _QUERY.methods_by_name['Codes']._options = None
    _QUERY.methods_by_name['Codes']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18\x12\x16/cosmwasm/wasm/v1/code'
    _QUERY.methods_by_name['PinnedCodes']._options = None
    _QUERY.methods_by_name['PinnedCodes']._serialized_options = b'\x82\xd3\xe4\x93\x02 \x12\x1e/cosmwasm/wasm/v1/codes/pinned'
    _QUERYCONTRACTINFOREQUEST._serialized_start = 176
    _QUERYCONTRACTINFOREQUEST._serialized_end = 219
    _QUERYCONTRACTINFORESPONSE._serialized_start = 221
    _QUERYCONTRACTINFORESPONSE._serialized_end = 340
    _QUERYCONTRACTHISTORYREQUEST._serialized_start = 342
    _QUERYCONTRACTHISTORYREQUEST._serialized_end = 448
    _QUERYCONTRACTHISTORYRESPONSE._serialized_start = 451
    _QUERYCONTRACTHISTORYRESPONSE._serialized_end = 609
    _QUERYCONTRACTSBYCODEREQUEST._serialized_start = 611
    _QUERYCONTRACTSBYCODEREQUEST._serialized_end = 717
    _QUERYCONTRACTSBYCODERESPONSE._serialized_start = 719
    _QUERYCONTRACTSBYCODERESPONSE._serialized_end = 829
    _QUERYALLCONTRACTSTATEREQUEST._serialized_start = 831
    _QUERYALLCONTRACTSTATEREQUEST._serialized_end = 938
    _QUERYALLCONTRACTSTATERESPONSE._serialized_start = 941
    _QUERYALLCONTRACTSTATERESPONSE._serialized_end = 1080
    _QUERYRAWCONTRACTSTATEREQUEST._serialized_start = 1082
    _QUERYRAWCONTRACTSTATEREQUEST._serialized_end = 1149
    _QUERYRAWCONTRACTSTATERESPONSE._serialized_start = 1151
    _QUERYRAWCONTRACTSTATERESPONSE._serialized_end = 1196
    _QUERYSMARTCONTRACTSTATEREQUEST._serialized_start = 1198
    _QUERYSMARTCONTRACTSTATEREQUEST._serialized_end = 1291
    _QUERYSMARTCONTRACTSTATERESPONSE._serialized_start = 1293
    _QUERYSMARTCONTRACTSTATERESPONSE._serialized_end = 1364
    _QUERYCODEREQUEST._serialized_start = 1366
    _QUERYCODEREQUEST._serialized_end = 1401
    _CODEINFORESPONSE._serialized_start = 1404
    _CODEINFORESPONSE._serialized_end = 1639
    _QUERYCODERESPONSE._serialized_start = 1641
    _QUERYCODERESPONSE._serialized_end = 1755
    _QUERYCODESREQUEST._serialized_start = 1757
    _QUERYCODESREQUEST._serialized_end = 1836
    _QUERYCODESRESPONSE._serialized_start = 1839
    _QUERYCODESRESPONSE._serialized_end = 1982
    _QUERYPINNEDCODESREQUEST._serialized_start = 1984
    _QUERYPINNEDCODESREQUEST._serialized_end = 2069
    _QUERYPINNEDCODESRESPONSE._serialized_start = 2071
    _QUERYPINNEDCODESRESPONSE._serialized_end = 2193
    _QUERY._serialized_start = 2196
    _QUERY._serialized_end = 3613