import fdb

fdb.api_version(630)
conn = fdb.open()

ident = fdb.directory.create_or_open(conn, ('identity',))

# users
users = ident.create_or_open(conn, ('users',))
user_email_idx = ident.create_or_open(conn, ('users', 'idx', 'email'))

# access control list
acls = ident.create_or_open(conn, ('acls',)) # (acls, <id>) = proto(ACL)

# action logs
action_logs = ident.create_or_open(conn, ('action_logs',)) # (action_logs, <id>) = proto(Application)
action_logs_author_idx = ident.create_or_open(conn, ('action_logs', 'author')) # (action_logs, author, <user_id>, <action_id>) = b''
action_logs_involved_idx = ident.create_or_open(conn, ('action_logs', 'involved')) # (action_logs, involved, <user_id>, <action_id>) = b''

# applications
applications = ident.create_or_open(conn, ('applications',)) # (applications, <id>) = proto(Application)

## quick lookup indexes for applications:
## this means that when we are checking for access, we can actually just look at:
## - (applications, rules, group, <app_id>, <group_id>, [rule_id]) = <rule_id> for groups
## - (applications, rules, user, <app_id>, <user_id>, [rule_id]) = <rule_id> for users
## to provide much quicker lookups ([rule_id] is needed as rules for a group/user are a 1 (user/group) to many (rules) mapping)
## 
## user rules are greater priority than groups,
## meaning user rules are looked up first (and hence we *may* ignore group rules)
application_group_rules = ident.create_or_open(conn, ('applications', 'rules', 'group'))
application_user_rules = ident.create_or_open(conn, ('applications', 'rules', 'user'))

# network policies (acls)
network_policies = ident.create_or_open(conn, ('network_policies',)) # (network_policies, <id>) = proto(NetworkPolicy)

# sessions
sessions = ident.create_or_open(conn, ('sessions',)) # (sessions, <id>) = proto(Session)

session_idx_token_hash = ident.create_or_open(conn, ('sessions', 'idx', 'token_hash')) # (sessions, idx, token_hash, <token_hash>) = (<session_id>, <user_id>)
session_idx_user_id = ident.create_or_open(conn, ('sessions', 'idx', 'user_id')) # (sessions, idx, user_id, <user_id>) = <session_id>

# groups
groups = ident.create_or_open(conn, ('groups',)) # (groups, <id>) = proto(Group)
group_members = ident.create_or_open(conn, ('groups', 'membership')) # (groups, membership, <group_id>, <user_id>) = ''