from xmlrpc.client import boolean
from RupineHeroku.rupine_db import herokuDbAccess
from psycopg2 import sql
from datetime import datetime, timedelta
import pytz
from RupineHeroku.rupine_db.herokuDbDML import POST

def getUniqueRriFromTransactions(connection, schema):
    
    query = sql.SQL("select distinct(amount_token_id) \
        FROM {}.rdx_transaction \
        ORDER BY amount_token_id").format(sql.Identifier(schema))
    result = herokuDbAccess.fetchDataInDatabase(query, [], connection)    
    
    return result