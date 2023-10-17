import sys
import ident.db.buf.action_log_pb2

"""
We have to shim this in since protobuf compiler is not 
aware of the directory that we are storing files in. This
is a bit dodgy but it works.
"""

sys.modules['action_log_pb2'] = ident.db.buf.action_log_pb2