import fdb

from ident.lib.id import generate

from ident.db.models import ActionLog
from ident.db.connection import action_logs, action_logs_author_idx

@fdb.transactional
def insert_entry(tr, entry: ActionLog):
    entry.id = 1 # TODO: replace with generate()
    tr[action_logs.pack((entry.id,))] = entry.SerializeToString()
    tr[action_logs_author_idx.pack((entry.actor.id,entry.id))] = b''