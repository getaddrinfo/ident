# ident

A (WIP) identity provider built on top of FoundationDB.

## Applications

This project (will) consist of multiple applications:
- API: The backend for the project
- Gateway: A reverse proxy that handles managing authorization for an account
- Manage: A service that allows users to manage accounts, policies, etc from a visual UI instead of the API.

## Why?

This project was made to help me learn/apply a few different concepts:
- (learn) FoundationDB, and the implications it has on designing an application.
- (apply) Designing injection for middleware - Injecting values from middleware based on their type into route handlers.
- (apply) Codebase structuring in a manner in which (I hope) is understandable for others. Providing a consistent layout for routers and implementing features.

## Database

Models are stored as bytes in the `protocol buffer` format - The definitions for models are under `defs/*.proto`.

Each model is stored in subspaces within foundationdb, managed by the directory layer. Indexes, relations and other similar data is generally stored at a deeper subspace than the models.

## Principles

The application consists of different resources:
- Users: Members of your organisation
- Groups: Collections of users in your organisation, which could be:
    - Departments
    - Priviliged Access
- Applications: Apps (e.g., websites) that you want to restrict and manage access to.
- Network Groups: A set of `CIDR`s that can be referenced within ACLs
- ACLs: Reusable rules that consist of Groups, Networks or both.
- Webhooks: HTTP targets that filtered application events (e.g., sign in) are delivered to.  

ACLs are reusable rules that consist of Groups and Networks. They may allow or deny access based on the given conditions.
Groups and Network Groups can follow two behaviours:
- Allow: If the criteria is met (e.g., the user is on a corporate VPN), the ACL is permitted.
- Deny: If the criteria is met (e.g., the user is in a certain group), the ACL is rejected. 

Restrictions for Applications are applied based on these ACLs, which may be used for example:
- Only allowing access to an application from a corporate VPN.
- Only allowing access to an application if a user is in a certain group.
- Only allowing access to an application if a user is in a certain group, and on a corporate VPN.
- Denying access if the user is in a certain group.

Re-using ACLs allows for rules to easily be mass-updated, and applies the DRY (Don't Repeat Yourself) principle.

## TODO (API)

### Implementation Details

- [x] Database Connection
- [x] Data Validation
- [x] Responses
- [x] Injection
- [x] Authentication
- [ ] Authorization
- [ ] Webhook Validation (Disallow non globally-routable IPs)
- [ ] Webhook Delivery
- [ ] Webhook Targets (Filtering events)

### Future Possibilities
- Automatic Documentation

### Controller Completeness
- [ ] ACLs
- [ ] Action Logs
- [ ] Applications
- [ ] Groups
- [x] Meta
- [ ] Networks
- [ ] Sessions
- [ ] Users
- [ ] Webhooks