from xmlrpc.client import boolean
from RupineHeroku.rupine_db import herokuDbAccess
from psycopg2 import sql
from datetime import datetime, timedelta
import pytz
from RupineHeroku.rupine_db.herokuDbDML import POST
import numpy

def getUniqueTokenAddrFromTransactions(connection, schema):
    
    query = sql.SQL("select distinct(amount_send_token_id) \
        FROM {}.evm_transaction \
        WHERE amount_send_token_id != '' AND amount_send_token_id != '0x'" ).format(sql.Identifier(schema))
    resultSend = herokuDbAccess.fetchDataInDatabase(query, [], connection)    

    query = sql.SQL("select distinct(amount_recv_token_id) \
        FROM {}.evm_transaction \
        WHERE amount_recv_token_id != '' AND amount_recv_token_id != '0x'").format(sql.Identifier(schema))
    resultRecv = herokuDbAccess.fetchDataInDatabase(query, [], connection)    

    allResults = [*resultSend, *resultRecv]

    return allResults