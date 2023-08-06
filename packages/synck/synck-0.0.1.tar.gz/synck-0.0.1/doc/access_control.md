
# Access Control

## Users and Groups (and Entities)

```python
# Entity (abstract base class - not instantiated on its own)

# Name for the entity - has character restrictions, e.g. the same restrictions as OS username and directory name
name: str

directory: str  # directory/folder name - for users default is "." and for groups default is the same as "name"
long_name: str  # human oriented long name for the entity (no character restrictions and is generally just used for display)
uuid: str  # unique identifier for the entity
active: bool  # True if still active

# cryptographic keys for the entity
public_key: str
private_key: str  # only stored locally - not stored in the cloud
```

For synchronization, one AWS bucket and DynamoDB table called `synck_fs` (for file system) is created per AWS account.

```python
# User (derived from Entity). The name is usually the OS username.

entity_type: str = "user"

# IAM cloud access
aws_profile: str
aws_access_key_id: str
aws_secret_access_key: str  # only stored locally - not in the cloud
```

```python
# Group (derived from Entity)

entity_type: str = "group"

members: list[str]  # list of member UUIDs
```

A `synck_entities` table contains all the users and groups for this AWS account (minus the fields that are only stored locally,
of course).

## Node

```python
# Node info (stored in the cloud)
uuid: str   # unique identifier for the node
computer_name: str  # computer name (from the OS)
computer_username: str  # username on the running computer (from the OS)
entities: list[str]  #  list of entities this node is servicing
```

When a new node is installed, synck requires the AWS IAM cloud access. From there the person installing synck can select
the user for this node. It then requires the cryptographic private key for the user, as well as any cryptographic
keys for the groups this user belongs to.

In the future, nodes will have an "enrollment request" where nodes on the same LAN will be able to accept a new node
(like what Wi-Fi routers can do). For now, the user is expected to be able to convey the AWS and private keys manually, e.g.
via flash drive or secure email.

## Local configuration data

```python
node_uuid: str  # UUID for the node running in this OS user instance (only one node allowed to run per OS user instance, i.e. is a singleton per OS login)
user_uuid: str  # UUID of user being serviced by the running node
parent_directory: str  # synck parent directory (default is $HOME/synck)
private_key: str  # cryptographic private key
aws_secret_access_key: str | None  # not needed if using aws_profile
```

## AWS Table

```python
# synck_fs table:

path: str  # file system path (from root)
miv: float  # MIV (see AWSimple MIV docs)
event: str  # create, update, move, delete
sha512: str  # sha512 of contents
source: str | None  # source path (e.g. for move), otherwise None
```
