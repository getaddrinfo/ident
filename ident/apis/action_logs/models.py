from ident.lib.validation import Lax 

class ListActionLogsQueryParams(Lax):
    user_id: int

class GetActionLogEntryPathParams(Lax):
    entry_id: int