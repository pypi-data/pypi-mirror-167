# stf_client.GroupsApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group_device**](GroupsApi.md#add_group_device) | **PUT** /groups/{id}/devices/{serial} | Adds a device into a transient group
[**add_group_devices**](GroupsApi.md#add_group_devices) | **PUT** /groups/{id}/devices | Adds devices into a transient group
[**add_group_user**](GroupsApi.md#add_group_user) | **PUT** /groups/{id}/users/{email} | Adds a user into a group
[**add_group_users**](GroupsApi.md#add_group_users) | **PUT** /groups/{id}/users | Adds users into a group
[**create_group**](GroupsApi.md#create_group) | **POST** /groups | Creates a group
[**delete_group**](GroupsApi.md#delete_group) | **DELETE** /groups/{id} | Removes a group
[**delete_groups**](GroupsApi.md#delete_groups) | **DELETE** /groups | Removes groups
[**get_group**](GroupsApi.md#get_group) | **GET** /groups/{id} | Gets a group
[**get_group_device**](GroupsApi.md#get_group_device) | **GET** /groups/{id}/devices/{serial} | Gets a device of a group
[**get_group_devices**](GroupsApi.md#get_group_devices) | **GET** /groups/{id}/devices | Gets the devices of a group
[**get_group_user**](GroupsApi.md#get_group_user) | **GET** /groups/{id}/users/{email} | Gets a user of a group
[**get_group_users**](GroupsApi.md#get_group_users) | **GET** /groups/{id}/users | Gets the users of a group
[**get_groups**](GroupsApi.md#get_groups) | **GET** /groups | Gets groups
[**remove_group_device**](GroupsApi.md#remove_group_device) | **DELETE** /groups/{id}/devices/{serial} | Removes a device from a transient group
[**remove_group_devices**](GroupsApi.md#remove_group_devices) | **DELETE** /groups/{id}/devices | Removes devices from a transient group
[**remove_group_user**](GroupsApi.md#remove_group_user) | **DELETE** /groups/{id}/users/{email} | Removes a user from a group
[**remove_group_users**](GroupsApi.md#remove_group_users) | **DELETE** /groups/{id}/users | Removes users from a group
[**update_group**](GroupsApi.md#update_group) | **PUT** /groups/{id} | Updates a group


# **add_group_device**
> GroupResponse add_group_device(id, serial)

Adds a device into a transient group

Adds a device into a transient group owned by you

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import groups_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.group_response import GroupResponse
from stf_client.model.conflicts_response import ConflictsResponse
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stf_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: accessTokenAuth
configuration.api_key['accessTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    id = "id_example" # str | Group identifier
    serial = "serial_example" # str | Device identifier (serial)

    # example passing only required values which don't have defaults set
    try:
        # Adds a device into a transient group
        api_response = api_instance.add_group_device(id, serial)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->add_group_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group identifier |
 **serial** | **str**| Device identifier (serial) |

### Return type

[**GroupResponse**](GroupResponse.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group information (an empty group is returned if no change is made) |  -  |
**409** | Conflicts information |  -  |
**0** | Unexpected Error:   * 400: Bad Request &#x3D;&gt; group is not transient   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Forbidden &#x3D;&gt; quota is reached   * 404: Not Found &#x3D;&gt; unknown group or device    * 500: Internal Server Error   * 503: Service Unavailable &#x3D;&gt; server too busy or a lock on a resource is pending  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_group_devices**
> GroupResponse add_group_devices(id)

Adds devices into a transient group

Adds devices into a transient group owned by you

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import groups_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.devices_payload import DevicesPayload
from stf_client.model.group_response import GroupResponse
from stf_client.model.conflicts_response import ConflictsResponse
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stf_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: accessTokenAuth
configuration.api_key['accessTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    id = "id_example" # str | Group identifier
    devices = DevicesPayload(
        serials="serials_example",
    ) # DevicesPayload | Devices to add as a comma-separated list of serials; note that by not providing this parameter it means all devices which could be potentially booked by that transient group are added into the latter (optional)

    # example passing only required values which don't have defaults set
    try:
        # Adds devices into a transient group
        api_response = api_instance.add_group_devices(id)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->add_group_devices: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds devices into a transient group
        api_response = api_instance.add_group_devices(id, devices=devices)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->add_group_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group identifier |
 **devices** | [**DevicesPayload**](DevicesPayload.md)| Devices to add as a comma-separated list of serials; note that by not providing this parameter it means all devices which could be potentially booked by that transient group are added into the latter | [optional]

### Return type

[**GroupResponse**](GroupResponse.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group information (an empty group is returned if no change is made) |  -  |
**409** | Conflicts information |  -  |
**0** | Unexpected Error:   * 400: Bad Request &#x3D;&gt; group is not transient   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Forbidden &#x3D;&gt; quota is reached   * 404: Not Found &#x3D;&gt; unknown group or devices   * 500: Internal Server Error   * 503: Service Unavailable &#x3D;&gt; server too busy or a lock on a resource is pending  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_group_user**
> GroupResponse add_group_user(id, email)

Adds a user into a group

Adds a user into a group owned by you

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import groups_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.group_response import GroupResponse
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stf_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: accessTokenAuth
configuration.api_key['accessTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    id = "id_example" # str | Group identifier
    email = "email_example" # str | User identifier (email)

    # example passing only required values which don't have defaults set
    try:
        # Adds a user into a group
        api_response = api_instance.add_group_user(id, email)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->add_group_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group identifier |
 **email** | **str**| User identifier (email) |

### Return type

[**GroupResponse**](GroupResponse.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group information (an empty group is returned if no change is made) |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 404: Not Found &#x3D;&gt; unknown group or device or user    * 500: Internal Server Error   * 503: Service Unavailable &#x3D;&gt; server too busy or a lock on a resource is pending  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_group_users**
> GroupResponse add_group_users(id)

Adds users into a group

Adds users into a group owned by you

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import groups_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.group_response import GroupResponse
from stf_client.model.users_payload import UsersPayload
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stf_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: accessTokenAuth
configuration.api_key['accessTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    id = "id_example" # str | Group identifier
    users = UsersPayload(
        emails="emails_example",
    ) # UsersPayload | Users to add as a comma-separated list of emails; note that by not providing this parameter it means all available users are added into the group (optional)

    # example passing only required values which don't have defaults set
    try:
        # Adds users into a group
        api_response = api_instance.add_group_users(id)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->add_group_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds users into a group
        api_response = api_instance.add_group_users(id, users=users)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->add_group_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group identifier |
 **users** | [**UsersPayload**](UsersPayload.md)| Users to add as a comma-separated list of emails; note that by not providing this parameter it means all available users are added into the group | [optional]

### Return type

[**GroupResponse**](GroupResponse.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group information (an empty group is returned if no change is made) |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 404: Not Found &#x3D;&gt; unknown group or device or users    * 500: Internal Server Error   * 503: Service Unavailable &#x3D;&gt; server too busy or a lock on a resource is pending  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group**
> GroupResponse create_group(group)

Creates a group

Creates a group with you as owner

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import groups_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.group_payload import GroupPayload
from stf_client.model.group_response import GroupResponse
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stf_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: accessTokenAuth
configuration.api_key['accessTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    group = GroupPayload(
        name="g",
        start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        stop_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        _class="once",
        repetitions=0,
        state="pending",
    ) # GroupPayload | Group properties; at least one property is required

    # example passing only required values which don't have defaults set
    try:
        # Creates a group
        api_response = api_instance.create_group(group)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->create_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | [**GroupPayload**](GroupPayload.md)| Group properties; at least one property is required |

### Return type

[**GroupResponse**](GroupResponse.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Group information |  -  |
**0** | Unexpected Error:   * 400: Bad Request &#x3D;&gt; invalid format or semantic of properties   * 401: Unauthorized &#x3D;&gt; bad credentials   * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> Response delete_group(id)

Removes a group

Removes a group owned by you

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import groups_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.response import Response
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stf_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: accessTokenAuth
configuration.api_key['accessTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    id = "id_example" # str | Group identifier

    # example passing only required values which don't have defaults set
    try:
        # Removes a group
        api_response = api_instance.delete_group(id)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->delete_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group identifier |

### Return type

[**Response**](Response.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group removing is OK |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Forbidden &#x3D;&gt; a device is currently booked or unremovable built-in group   * 404: Not Found &#x3D;&gt; unknown group    * 500: Internal Server Error   * 503: Service Unavailable &#x3D;&gt; server too busy or a lock on a resource is pending  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_groups**
> Response delete_groups()

Removes groups

Removes the groups owned by you

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import groups_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.groups_payload import GroupsPayload
from stf_client.model.response import Response
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stf_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: accessTokenAuth
configuration.api_key['accessTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    groups = GroupsPayload(
        ids="ids_example",
    ) # GroupsPayload | Groups to remove as a comma-separated list of group identifiers; note that by not providing this parameter it means all groups owned by you are removed (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Removes groups
        api_response = api_instance.delete_groups(groups=groups)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->delete_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groups** | [**GroupsPayload**](GroupsPayload.md)| Groups to remove as a comma-separated list of group identifiers; note that by not providing this parameter it means all groups owned by you are removed | [optional]

### Return type

[**Response**](Response.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Groups removing is OK (or no groups to remove) |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Forbidden &#x3D;&gt; a device is currently booked or unremovable built-in group   * 404: Not Found &#x3D;&gt; unknown groups   * 500: Internal Server Error   * 503: Service Unavailable &#x3D;&gt; server too busy or a lock on a resource is pending  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> GroupResponse get_group(id)

Gets a group

Returns a group to which you belong

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import groups_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.group_response import GroupResponse
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stf_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: accessTokenAuth
configuration.api_key['accessTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    id = "id_example" # str | Group identifier
    fields = "fields_example" # str | Comma-separated list of group fields; only listed fields will be returned in response (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets a group
        api_response = api_instance.get_group(id)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->get_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a group
        api_response = api_instance.get_group(id, fields=fields)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->get_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group identifier |
 **fields** | **str**| Comma-separated list of group fields; only listed fields will be returned in response | [optional]

### Return type

[**GroupResponse**](GroupResponse.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group information |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 404: Not Found &#x3D;&gt; unknown group   * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_device**
> DeviceResponse get_group_device(id, serial)

Gets a device of a group

Returns a device of a group to which you belong

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import groups_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.device_response import DeviceResponse
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stf_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: accessTokenAuth
configuration.api_key['accessTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    id = "id_example" # str | Group identifier
    serial = "serial_example" # str | Device identifier (serial)
    fields = "fields_example" # str | Comma-separated list of device fields; only listed fields will be returned in response (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets a device of a group
        api_response = api_instance.get_group_device(id, serial)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->get_group_device: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a device of a group
        api_response = api_instance.get_group_device(id, serial, fields=fields)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->get_group_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group identifier |
 **serial** | **str**| Device identifier (serial) |
 **fields** | **str**| Comma-separated list of device fields; only listed fields will be returned in response | [optional]

### Return type

[**DeviceResponse**](DeviceResponse.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group device information |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 404: Not Found &#x3D;&gt; unknown group or device   * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_devices**
> DeviceListResponse get_group_devices(id)

Gets the devices of a group

Returns the devices of the group to which you belong

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import groups_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.device_list_response import DeviceListResponse
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stf_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: accessTokenAuth
configuration.api_key['accessTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    id = "id_example" # str | Group identifier
    bookable = False # bool | Selects devices which could be potentially booked by that transient group (true => irrelevant for an origin group!), or selects all devices of the group (false); note that by not providing this parameter all devices of the group are selected (optional) if omitted the server will use the default value of False
    fields = "fields_example" # str | Comma-separated list of device fields; only listed fields will be returned in response (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the devices of a group
        api_response = api_instance.get_group_devices(id)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->get_group_devices: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the devices of a group
        api_response = api_instance.get_group_devices(id, bookable=bookable, fields=fields)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->get_group_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group identifier |
 **bookable** | **bool**| Selects devices which could be potentially booked by that transient group (true &#x3D;&gt; irrelevant for an origin group!), or selects all devices of the group (false); note that by not providing this parameter all devices of the group are selected | [optional] if omitted the server will use the default value of False
 **fields** | **str**| Comma-separated list of device fields; only listed fields will be returned in response | [optional]

### Return type

[**DeviceListResponse**](DeviceListResponse.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group devices information |  -  |
**0** | Unexpected Error:   * 400: Bad request &#x3D;&gt; group is not transient   * 401: Unauthorized &#x3D;&gt; bad credentials   * 404: Not Found &#x3D;&gt; unknown group    * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_user**
> UserResponse get_group_user(id, email)

Gets a user of a group

Gets a user of a group to which you belong; if you are the administrator user then all user fields are returned, otherwise only 'email', 'name' and 'privilege' user fields are returned

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import groups_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.user_response import UserResponse
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stf_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: accessTokenAuth
configuration.api_key['accessTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    id = "id_example" # str | Group identifier
    email = "email_example" # str | User identifier (email)
    fields = "fields_example" # str | Comma-separated list of user fields; only listed fields will be returned in response (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets a user of a group
        api_response = api_instance.get_group_user(id, email)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->get_group_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a user of a group
        api_response = api_instance.get_group_user(id, email, fields=fields)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->get_group_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group identifier |
 **email** | **str**| User identifier (email) |
 **fields** | **str**| Comma-separated list of user fields; only listed fields will be returned in response | [optional]

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group user information |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 404: Not Found &#x3D;&gt; unknown group or device or user   * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_users**
> UserListResponse get_group_users(id)

Gets the users of a group

Gets the users of a group to which you belong; if you are the administrator user then all user fields are returned, otherwise only 'email', 'name' and 'privilege' user fields are returned

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import groups_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.user_list_response import UserListResponse
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stf_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: accessTokenAuth
configuration.api_key['accessTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    id = "id_example" # str | Group identifier
    fields = "fields_example" # str | Comma-separated list of user fields; only listed fields will be returned in response (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the users of a group
        api_response = api_instance.get_group_users(id)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->get_group_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the users of a group
        api_response = api_instance.get_group_users(id, fields=fields)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->get_group_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group identifier |
 **fields** | **str**| Comma-separated list of user fields; only listed fields will be returned in response | [optional]

### Return type

[**UserListResponse**](UserListResponse.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group users information |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 404: Not Found &#x3D;&gt; unknown group    * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups**
> GroupListResponse get_groups()

Gets groups

Returns the groups to which you belong

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import groups_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.group_list_response import GroupListResponse
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stf_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: accessTokenAuth
configuration.api_key['accessTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    fields = "fields_example" # str | Comma-seperated list of fields; only listed fields will be returned in response (optional)
    owner = True # bool | Selects the groups for which you are the owner (true) or a simple member (false); note that by not providing this parameter, it means all groups to which you belong are selected (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets groups
        api_response = api_instance.get_groups(fields=fields, owner=owner)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->get_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-seperated list of fields; only listed fields will be returned in response | [optional]
 **owner** | **bool**| Selects the groups for which you are the owner (true) or a simple member (false); note that by not providing this parameter, it means all groups to which you belong are selected | [optional]

### Return type

[**GroupListResponse**](GroupListResponse.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Groups information |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_group_device**
> GroupResponse remove_group_device(id, serial)

Removes a device from a transient group

Removes a device from a transient group owned by you

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import groups_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.group_response import GroupResponse
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stf_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: accessTokenAuth
configuration.api_key['accessTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    id = "id_example" # str | Group identifier
    serial = "serial_example" # str | Device identifier (serial)

    # example passing only required values which don't have defaults set
    try:
        # Removes a device from a transient group
        api_response = api_instance.remove_group_device(id, serial)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->remove_group_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group identifier |
 **serial** | **str**| Device identifier (serial) |

### Return type

[**GroupResponse**](GroupResponse.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group information (an empty group is returned if no change is made) |  -  |
**0** | Unexpected Error:   * 400: Bad Request &#x3D;&gt; group is not transient   * 401: Unauthorized &#x3D;&gt; bad credentials   * 404: Not Found &#x3D;&gt; unknown group or device    * 500: Internal Server Error   * 503: Service Unavailable &#x3D;&gt; server too busy or a lock on a resource is pending  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_group_devices**
> GroupResponse remove_group_devices(id)

Removes devices from a transient group

Removes devices from a transient group owned by you

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import groups_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.devices_payload import DevicesPayload
from stf_client.model.group_response import GroupResponse
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stf_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: accessTokenAuth
configuration.api_key['accessTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    id = "id_example" # str | Group identifier
    devices = DevicesPayload(
        serials="serials_example",
    ) # DevicesPayload | Devices to remove as a comma-separated list of serials; note that by not providing this parameter it means all devices of the group are removed (optional)

    # example passing only required values which don't have defaults set
    try:
        # Removes devices from a transient group
        api_response = api_instance.remove_group_devices(id)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->remove_group_devices: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Removes devices from a transient group
        api_response = api_instance.remove_group_devices(id, devices=devices)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->remove_group_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group identifier |
 **devices** | [**DevicesPayload**](DevicesPayload.md)| Devices to remove as a comma-separated list of serials; note that by not providing this parameter it means all devices of the group are removed | [optional]

### Return type

[**GroupResponse**](GroupResponse.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group information (an empty group is returned if no change is made) |  -  |
**0** | Unexpected Error:   * 400: Bad Request &#x3D;&gt; group is not transient   * 401: Unauthorized &#x3D;&gt; bad credentials   * 404: Not Found &#x3D;&gt; unknown group or devices   * 500: Internal Server Error   * 503: Service Unavailable &#x3D;&gt; server too busy or a lock on a resource is pending  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_group_user**
> GroupResponse remove_group_user(id, email)

Removes a user from a group

Removes a user from a group owned by you

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import groups_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.group_response import GroupResponse
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stf_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: accessTokenAuth
configuration.api_key['accessTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    id = "id_example" # str | Group identifier
    email = "email_example" # str | User identifier (email)

    # example passing only required values which don't have defaults set
    try:
        # Removes a user from a group
        api_response = api_instance.remove_group_user(id, email)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->remove_group_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group identifier |
 **email** | **str**| User identifier (email) |

### Return type

[**GroupResponse**](GroupResponse.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group information (an empty group is returned if no change is made) |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Forbidden &#x3D;&gt; owner or administrator user can&#39;t be removed   * 404: Not Found &#x3D;&gt; unknown group or device or user   * 500: Internal Server Error   * 503: Service Unavailable &#x3D;&gt; server too busy or a lock on a resource is pending  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_group_users**
> GroupResponse remove_group_users(id)

Removes users from a group

Removes users from a group owned by you

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import groups_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.group_response import GroupResponse
from stf_client.model.users_payload import UsersPayload
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stf_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: accessTokenAuth
configuration.api_key['accessTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    id = "id_example" # str | Group identifier
    users = UsersPayload(
        emails="emails_example",
    ) # UsersPayload | Users to remove as a comma-separated list of emails; note that by not providing this parameter it means all users of the group are removed (optional)

    # example passing only required values which don't have defaults set
    try:
        # Removes users from a group
        api_response = api_instance.remove_group_users(id)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->remove_group_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Removes users from a group
        api_response = api_instance.remove_group_users(id, users=users)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->remove_group_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group identifier |
 **users** | [**UsersPayload**](UsersPayload.md)| Users to remove as a comma-separated list of emails; note that by not providing this parameter it means all users of the group are removed | [optional]

### Return type

[**GroupResponse**](GroupResponse.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group information (an empty group is returned if no change is made) |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Forbidden &#x3D;&gt; owner or administrator user can&#39;t be removed    * 404: Not Found &#x3D;&gt; unknown group or device or users    * 500: Internal Server Error   * 503: Service Unavailable &#x3D;&gt; server too busy or a lock on a resource is pending  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> GroupResponse update_group(id, group)

Updates a group

Updates a group owned by you

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import groups_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.group_payload import GroupPayload
from stf_client.model.group_response import GroupResponse
from stf_client.model.conflicts_response import ConflictsResponse
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stf_client.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: accessTokenAuth
configuration.api_key['accessTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accessTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    id = "id_example" # str | Group identifier
    group = GroupPayload(
        name="g",
        start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        stop_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        _class="once",
        repetitions=0,
        state="pending",
    ) # GroupPayload | Group properties; at least one property is required

    # example passing only required values which don't have defaults set
    try:
        # Updates a group
        api_response = api_instance.update_group(id, group)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling GroupsApi->update_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group identifier |
 **group** | [**GroupPayload**](GroupPayload.md)| Group properties; at least one property is required |

### Return type

[**GroupResponse**](GroupResponse.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group information (an empty group is returned if no change is made) |  -  |
**409** | Conflicts information |  -  |
**0** | Unexpected Error:   * 400: Bad Request &#x3D;&gt; invalid format or semantic of properties   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Forbidden &#x3D;&gt; quota is reached or unauthorized property   * 404: Not Found &#x3D;&gt; unknown group    * 500: Internal Server Error   * 503: Service Unavailable &#x3D;&gt; server too busy or a lock on a resource is pending  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

