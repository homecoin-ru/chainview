# Common config for chainview
import os
from dotenv import load_dotenv

load_dotenv()

VERSION = '1.1'
#Original repo GITHUB = 'https://github.com/bitcoinedu-io/chainview'
GITHUB = 'https://github.com/homecoin-ru/chainview'

DBFILE = 'homecoin-db.sqlite3'

CHECK_NEW_BLOCK_TIMEOUT_SEC = 100 # delay between checking for new blocks in seconds
rpc_user = os.environ.get("RPC_USER", "user")
rpc_pass = os.environ.get("RPC_PASS", "pass")
rpc_port = os.environ.get("RPC_PORT", "8332")

NODEURL = 'http://%s:%s@localhost:%s' % (rpc_user, rpc_pass, rpc_port)

chaininfo = {
    'name': 'Homecoin',
    'unit': 'HOME'
    }

params = {
    'SubsidyHalvingInterval': 210000,     # blocks, miner reward halving
    'PowTargetTimespan': 1*24*60*60,      # sec, retarget time: one day
    'PowTargetSpacing': 10*60,            # sec, block time 10 min
    'DifficultyAdjustmentInterval': 144   # blocks, PowTargetTimespan / PowTargetSpacing
    }
