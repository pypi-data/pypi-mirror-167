
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from stf_client.api.admin_api import AdminApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from stf_client.api.admin_api import AdminApi
from stf_client.api.devices_api import DevicesApi
from stf_client.api.groups_api import GroupsApi
from stf_client.api.user_api import UserApi
from stf_client.api.users_api import UsersApi
