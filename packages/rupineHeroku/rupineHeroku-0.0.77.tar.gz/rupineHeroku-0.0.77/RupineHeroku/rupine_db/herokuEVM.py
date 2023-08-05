from xmlrpc.client import boolean
from RupineHeroku.rupine_db import herokuDbAccess
from psycopg2 import sql
from datetime import datetime, timedelta
import pytz
from RupineHeroku.rupine_db.herokuDbDML import POST
import numpy

def getUniqueTokenAddrFromTransactions(connection, schema, public_address=None, join_abi=False):
    
    queryStrSend = "select distinct(amount_send_token_id) \
        FROM {}.evm_transaction \
        WHERE amount_recv_token_id != '' AND amount_recv_token_id != '0x'"

    queryStrRecv = "select distinct(amount_recv_token_id) \
        FROM {}.evm_transaction \
        WHERE amount_recv_token_id != '' AND amount_recv_token_id != '0x'"

    if join_abi:
        queryStrSend = "SELECT distinct(amount_send_token_id), basis.abi \
                        FROM {}.evm_transaction \
                        LEFT JOIN (SELECT t.token_address , t.abi FROM dbdev.evm_token t ) basis \
                        ON basis.token_address = amount_send_token_id \
                        WHERE amount_send_token_id != '' AND amount_send_token_id != '0x'"
        queryStrRecv = "SELECT distinct(amount_recv_token_id), basis.abi \
                        FROM {}.evm_transaction \
                        LEFT JOIN (SELECT t.token_address , t.abi FROM dbdev.evm_token t ) basis \
                        ON basis.token_address = amount_recv_token_id \
                        WHERE amount_recv_token_id != '' AND amount_recv_token_id != '0x'"

    if public_address:
        queryStrSend = queryStrSend + " AND public_address=%s"
        queryStrRecv = queryStrRecv + " AND public_address=%s"


    querySend = sql.SQL(queryStrSend).format(sql.Identifier(schema))
    queryRecv = sql.SQL(queryStrRecv).format(sql.Identifier(schema))

    resultSend = herokuDbAccess.fetchDataInDatabase(querySend, [public_address], connection)    
    resultRecv = herokuDbAccess.fetchDataInDatabase(queryRecv, [public_address], connection)    


    allResults = [*resultSend, *resultRecv]

    return allResults