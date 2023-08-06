# stf_client.AdminApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_origin_group_device**](AdminApi.md#add_origin_group_device) | **PUT** /devices/{serial}/groups/{id} | Adds a device into an origin group
[**add_origin_group_devices**](AdminApi.md#add_origin_group_devices) | **PUT** /devices/groups/{id} | Adds devices into an origin group
[**add_user_device_v3**](AdminApi.md#add_user_device_v3) | **POST** /users/{email}/devices/{serial} | Places a device under user control
[**create_user**](AdminApi.md#create_user) | **POST** /users/{email} | Creates a user
[**create_user_access_token**](AdminApi.md#create_user_access_token) | **POST** /users/{email}/accessTokens | Create an access token for a user
[**delete_device**](AdminApi.md#delete_device) | **DELETE** /devices/{serial} | Removes a device
[**delete_devices**](AdminApi.md#delete_devices) | **DELETE** /devices | Removes devices
[**delete_user**](AdminApi.md#delete_user) | **DELETE** /users/{email} | Removes a user
[**delete_user_access_token**](AdminApi.md#delete_user_access_token) | **DELETE** /users/{email}/accessTokens/{id} | Removes an access token of a user
[**delete_user_access_tokens**](AdminApi.md#delete_user_access_tokens) | **DELETE** /users/{email}/accessTokens | Remove the access tokens of a user
[**delete_user_device**](AdminApi.md#delete_user_device) | **DELETE** /users/{email}/devices/{serial} | Remove a device from the user control
[**delete_users**](AdminApi.md#delete_users) | **DELETE** /users | Removes users
[**get_device_groups**](AdminApi.md#get_device_groups) | **GET** /devices/{serial}/groups | Gets the groups to which the device belongs
[**get_user_access_token**](AdminApi.md#get_user_access_token) | **GET** /users/{email}/accessTokens/{id} | Gets an access token of a user
[**get_user_access_tokens_v2**](AdminApi.md#get_user_access_tokens_v2) | **GET** /users/{email}/accessTokens | Gets the access tokens of a user
[**get_user_device**](AdminApi.md#get_user_device) | **GET** /users/{email}/devices/{serial} | Gets a device controlled by a user
[**get_user_devices_v2**](AdminApi.md#get_user_devices_v2) | **GET** /users/{email}/devices | Gets the devices controlled by a user
[**put_device_by_serial**](AdminApi.md#put_device_by_serial) | **PUT** /devices/{serial} | Adds device informatin
[**remote_connect_user_device**](AdminApi.md#remote_connect_user_device) | **POST** /users/{email}/devices/{serial}/remoteConnect | Allows to remotely connect to a device controlled by a user
[**remote_disconnect_user_device**](AdminApi.md#remote_disconnect_user_device) | **DELETE** /users/{email}/devices/{serial}/remoteConnect | Forbids to remotely connect to a device controlled by a user
[**remove_origin_group_device**](AdminApi.md#remove_origin_group_device) | **DELETE** /devices/{serial}/groups/{id} | Removes a device from an origin group
[**remove_origin_group_devices**](AdminApi.md#remove_origin_group_devices) | **DELETE** /devices/groups/{id} | Removes devices from an origin group
[**update_default_user_groups_quotas**](AdminApi.md#update_default_user_groups_quotas) | **PUT** /users/groupsQuotas | Updates the default groups quotas of users
[**update_user_groups_quotas**](AdminApi.md#update_user_groups_quotas) | **PUT** /users/{email}/groupsQuotas | Updates the groups quotas of a user


# **add_origin_group_device**
> DeviceResponse add_origin_group_device(serial, id)

Adds a device into an origin group

Adds a device into an origin group along with updating the added device; returns the updated device

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import admin_api
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
    api_instance = admin_api.AdminApi(api_client)
    serial = "serial_example" # str | Device identifier (serial)
    id = "id_example" # str | Group identifier

    # example passing only required values which don't have defaults set
    try:
        # Adds a device into an origin group
        api_response = api_instance.add_origin_group_device(serial, id)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->add_origin_group_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **str**| Device identifier (serial) |
 **id** | **str**| Group identifier |

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
**200** | Device information |  -  |
**0** | Unexpected Error:   * 400: Bad Request &#x3D;&gt; group is not an origin one   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Fobidden &#x3D;&gt; the device is currently booked   * 404: Not Found &#x3D;&gt; unknown group or device   * 500: Internal Server Error   * 503: Service Unavailable &#x3D;&gt; server too busy or a lock on a resource is pending   * 504: Gateway Time-out &#x3D;&gt; server is not responding  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_origin_group_devices**
> DeviceListResponse add_origin_group_devices(id)

Adds devices into an origin group

Adds devices into an origin group along with updating each added device; returns the updated devices

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import admin_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.devices_payload import DevicesPayload
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
    api_instance = admin_api.AdminApi(api_client)
    id = "id_example" # str | Group identifier
    fields = "fields_example" # str | Comma-seperated list of fields; only listed fields will be returned in response (optional)
    devices = DevicesPayload(
        serials="serials_example",
    ) # DevicesPayload | Devices to add as a comma-separated list of serials; note that by not providing this parameter it means all 'available devices' are selected for adding:  * 'availables devices' means all devices in case of a bookable group  * 'availables devices' means all not yet booked devices in case of a standard group  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Adds devices into an origin group
        api_response = api_instance.add_origin_group_devices(id)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->add_origin_group_devices: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds devices into an origin group
        api_response = api_instance.add_origin_group_devices(id, fields=fields, devices=devices)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->add_origin_group_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group identifier |
 **fields** | **str**| Comma-seperated list of fields; only listed fields will be returned in response | [optional]
 **devices** | [**DevicesPayload**](DevicesPayload.md)| Devices to add as a comma-separated list of serials; note that by not providing this parameter it means all &#39;available devices&#39; are selected for adding:  * &#39;availables devices&#39; means all devices in case of a bookable group  * &#39;availables devices&#39; means all not yet booked devices in case of a standard group  | [optional]

### Return type

[**DeviceListResponse**](DeviceListResponse.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Devices information (an empty device list is returned if no change is made) |  -  |
**0** | Unexpected Error:   * 400: Bad Request &#x3D;&gt; group is not an origin one   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Fobidden &#x3D;&gt; a device is currently booked    * 404: Not Found &#x3D;&gt; unknown group or devices    * 500: Internal Server Error   * 503: Service Unavailable &#x3D;&gt; server too busy or a lock on a resource is pending   * 504: Gateway Time-out &#x3D;&gt; server is not responding  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_device_v3**
> Response add_user_device_v3(email, serial)

Places a device under user control

Places a device under user control; note this is not completely analogous to press the 'Use' button in the UI because that does not authorize remote connection through ADB

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import admin_api
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
    api_instance = admin_api.AdminApi(api_client)
    email = "email_example" # str | User identifier (email)
    serial = "serial_example" # str | Device identifier (serial)
    timeout = 0 # int | Means the device will be automatically removed from the user control if it is kept idle for this period (in milliseconds); default value is provided by the provider 'group timeout' (optional)

    # example passing only required values which don't have defaults set
    try:
        # Places a device under user control
        api_response = api_instance.add_user_device_v3(email, serial)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->add_user_device_v3: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Places a device under user control
        api_response = api_instance.add_user_device_v3(email, serial, timeout=timeout)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->add_user_device_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| User identifier (email) |
 **serial** | **str**| Device identifier (serial) |
 **timeout** | **int**| Means the device will be automatically removed from the user control if it is kept idle for this period (in milliseconds); default value is provided by the provider &#39;group timeout&#39; | [optional]

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
**200** | Device controlling is OK |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Forbidden &#x3D;&gt; Device is already controlled or is not available   * 404: Not Found &#x3D;&gt; unknown user or device   * 500: Internal Server Error   * 504: Gateway Time-out &#x3D;&gt; device is not responding  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> UserResponse create_user(email, name)

Creates a user

Creates a user in the database

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import admin_api
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
    api_instance = admin_api.AdminApi(api_client)
    email = "email_example" # str | User identifier (email)
    name = "name_example" # str | User name

    # example passing only required values which don't have defaults set
    try:
        # Creates a user
        api_response = api_instance.create_user(email, name)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->create_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| User identifier (email) |
 **name** | **str**| User name |

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
**201** | User information |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Forbidden &#x3D;&gt; user already exists   * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_access_token**
> UserAccessTokenResponse create_user_access_token(email, title)

Create an access token for a user

Creates an access token for a user.

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import admin_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.user_access_token_response import UserAccessTokenResponse
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
    api_instance = admin_api.AdminApi(api_client)
    email = "email_example" # str | User identifier (email)
    title = "title_example" # str | Access token title

    # example passing only required values which don't have defaults set
    try:
        # Create an access token for a user
        api_response = api_instance.create_user_access_token(email, title)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->create_user_access_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| User identifier (email) |
 **title** | **str**| Access token title |

### Return type

[**UserAccessTokenResponse**](UserAccessTokenResponse.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Access token information |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 404: Not Found &#x3D;&gt; unknown user    * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device**
> Response delete_device(serial)

Removes a device

Removes a device from the database

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import admin_api
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
    api_instance = admin_api.AdminApi(api_client)
    serial = "serial_example" # str | Device identifier (serial)
    present = True # bool | Allows or not the removing of the device depending respectively if the device is present (true) or not (false); note that by not providing this parameter it means an unconditional removing (optional)
    booked = True # bool | Allows or not the removing of the device depending respectively if the device is booked (true) or not (false); note that by not providing this parameter it means an unconditional removing (optional)
    annotated = True # bool | Allows or not the removing of the device depending respectively if the device is annotated (true) or not (false); note that by not providing this parameter it means an unconditional removing (optional)
    controlled = True # bool | Allows or not the removing of the device depending respectively if the device is controlled (true) or not (false); note that by not providing this parameter it means an unconditional removing (optional)

    # example passing only required values which don't have defaults set
    try:
        # Removes a device
        api_response = api_instance.delete_device(serial)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->delete_device: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Removes a device
        api_response = api_instance.delete_device(serial, present=present, booked=booked, annotated=annotated, controlled=controlled)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->delete_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **str**| Device identifier (serial) |
 **present** | **bool**| Allows or not the removing of the device depending respectively if the device is present (true) or not (false); note that by not providing this parameter it means an unconditional removing | [optional]
 **booked** | **bool**| Allows or not the removing of the device depending respectively if the device is booked (true) or not (false); note that by not providing this parameter it means an unconditional removing | [optional]
 **annotated** | **bool**| Allows or not the removing of the device depending respectively if the device is annotated (true) or not (false); note that by not providing this parameter it means an unconditional removing | [optional]
 **controlled** | **bool**| Allows or not the removing of the device depending respectively if the device is controlled (true) or not (false); note that by not providing this parameter it means an unconditional removing | [optional]

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
**200** | Device removing is OK |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 404: Not Found &#x3D;&gt; unknown device   * 500: Internal Server Error   * 503: Service Unavailable &#x3D;&gt; server too busy or a lock on a resource is pending  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_devices**
> Response delete_devices()

Removes devices

Removes devices from the database

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import admin_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.devices_payload import DevicesPayload
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
    api_instance = admin_api.AdminApi(api_client)
    present = True # bool | Allows or not the removing of each device depending respectively if the device is present (true) or not (false); note that by not providing this parameter it means an unconditional removing (optional)
    booked = True # bool | Allows or not the removing of each device depending respectively if the device is booked (true) or not (false); note that by not providing this parameter it means an unconditional removing (optional)
    annotated = True # bool | Allows or not the removing of each device depending respectively if the device is annotated (true) or not (false); note that by not providing this parameter it means an unconditional removing (optional)
    controlled = True # bool | Allows or not the removing of each device depending respectively if the device is controlled (true) or not (false); note that by not providing this parameter it means an unconditional removing (optional)
    devices = DevicesPayload(
        serials="serials_example",
    ) # DevicesPayload | Devices to remove as a comma-separated list of serials; note that by not providing this parameter it means all devices are selected for removing (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Removes devices
        api_response = api_instance.delete_devices(present=present, booked=booked, annotated=annotated, controlled=controlled, devices=devices)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->delete_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **present** | **bool**| Allows or not the removing of each device depending respectively if the device is present (true) or not (false); note that by not providing this parameter it means an unconditional removing | [optional]
 **booked** | **bool**| Allows or not the removing of each device depending respectively if the device is booked (true) or not (false); note that by not providing this parameter it means an unconditional removing | [optional]
 **annotated** | **bool**| Allows or not the removing of each device depending respectively if the device is annotated (true) or not (false); note that by not providing this parameter it means an unconditional removing | [optional]
 **controlled** | **bool**| Allows or not the removing of each device depending respectively if the device is controlled (true) or not (false); note that by not providing this parameter it means an unconditional removing | [optional]
 **devices** | [**DevicesPayload**](DevicesPayload.md)| Devices to remove as a comma-separated list of serials; note that by not providing this parameter it means all devices are selected for removing | [optional]

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
**200** | Devices removing is OK (or no devices to remove) |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 404: Not Found &#x3D;&gt; unknown devices    * 500: Internal Server Error   * 503: Service Unavailable &#x3D;&gt; server too busy or a lock on a resource is pending  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> Response delete_user(email)

Removes a user

Removes a user from the database

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import admin_api
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
    api_instance = admin_api.AdminApi(api_client)
    email = "email_example" # str | User identifier (email)
    group_owner = True # bool | Allows or not the removing of the user depending respectively if the user is a group owner (true) or not (false); note that by not providing this parameter it means an unconditionally removing (optional)

    # example passing only required values which don't have defaults set
    try:
        # Removes a user
        api_response = api_instance.delete_user(email)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->delete_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Removes a user
        api_response = api_instance.delete_user(email, group_owner=group_owner)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->delete_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| User identifier (email) |
 **group_owner** | **bool**| Allows or not the removing of the user depending respectively if the user is a group owner (true) or not (false); note that by not providing this parameter it means an unconditionally removing | [optional]

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
**200** | User removing is OK |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Forbidden &#x3D;&gt; administrator user can&#39;t be removed   * 404: Not Found &#x3D;&gt; unknown user   * 500: Internal Server Error   * 503: Service Unavailable &#x3D;&gt; server too busy or a lock on a resource is pending  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_access_token**
> Response delete_user_access_token(email, id)

Removes an access token of a user

Removes an access token of a user

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import admin_api
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
    api_instance = admin_api.AdminApi(api_client)
    email = "email_example" # str | User identifier (email)
    id = "id_example" # str | Access token identifier

    # example passing only required values which don't have defaults set
    try:
        # Removes an access token of a user
        api_response = api_instance.delete_user_access_token(email, id)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->delete_user_access_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| User identifier (email) |
 **id** | **str**| Access token identifier |

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
**200** | Access token removing is OK |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 404: Not Found &#x3D;&gt; unknown user or token    * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_access_tokens**
> Response delete_user_access_tokens(email)

Remove the access tokens of a user

Remove the access tokens of a user

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import admin_api
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
    api_instance = admin_api.AdminApi(api_client)
    email = "email_example" # str | User identifier (email)

    # example passing only required values which don't have defaults set
    try:
        # Remove the access tokens of a user
        api_response = api_instance.delete_user_access_tokens(email)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->delete_user_access_tokens: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| User identifier (email) |

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
**200** | Access tokens removing is OK |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 404: Not Found &#x3D;&gt; unknown user    * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_device**
> Response delete_user_device(email, serial)

Remove a device from the user control

Remove a device from the user control; note this is analogous to press the 'Stop Using' button in the UI because that forbids also remote connection through ADB

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import admin_api
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
    api_instance = admin_api.AdminApi(api_client)
    email = "email_example" # str | User identifier (email)
    serial = "serial_example" # str | Device identifier (serial)

    # example passing only required values which don't have defaults set
    try:
        # Remove a device from the user control
        api_response = api_instance.delete_user_device(email, serial)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->delete_user_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| User identifier (email) |
 **serial** | **str**| Device identifier (serial) |

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
**200** | Device releasing is OK |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Forbidden &#x3D;&gt; device is not controlled by the user   * 404: Not Found &#x3D;&gt; unknown user or device    * 500: Internal Server Error   * 504: Gateway Time-out &#x3D;&gt; device is not responding  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_users**
> Response delete_users()

Removes users

Removes users from the database

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import admin_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.users_payload import UsersPayload
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
    api_instance = admin_api.AdminApi(api_client)
    group_owner = True # bool | Allows or not the removing of each user depending respectively if the user is a group owner (true) or not (false); note that by not providing the groupOwner parameter it means an unconditionally removing (optional)
    users = UsersPayload(
        emails="emails_example",
    ) # UsersPayload | Users to remove as a comma-separated list of emails; note that by not providing this parameter it means all users are selected for removing (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Removes users
        api_response = api_instance.delete_users(group_owner=group_owner, users=users)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->delete_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_owner** | **bool**| Allows or not the removing of each user depending respectively if the user is a group owner (true) or not (false); note that by not providing the groupOwner parameter it means an unconditionally removing | [optional]
 **users** | [**UsersPayload**](UsersPayload.md)| Users to remove as a comma-separated list of emails; note that by not providing this parameter it means all users are selected for removing | [optional]

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
**200** | Users removing is OK (or no users to remove) |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Forbidden &#x3D;&gt; administrator user can&#39;t be removed   * 404: Not Found &#x3D;&gt; unknown users    * 500: Internal Server Error   * 503: Service Unavailable &#x3D;&gt; server too busy or a lock on a resource is pending  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_groups**
> GroupListResponse get_device_groups(serial)

Gets the groups to which the device belongs

Gets the groups to which the device belongs

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import admin_api
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
    api_instance = admin_api.AdminApi(api_client)
    serial = "serial_example" # str | Device identifier (serial)
    fields = "fields_example" # str | Comma-seperated list of fields; only listed fields will be returned in response (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the groups to which the device belongs
        api_response = api_instance.get_device_groups(serial)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->get_device_groups: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the groups to which the device belongs
        api_response = api_instance.get_device_groups(serial, fields=fields)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->get_device_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **str**| Device identifier (serial) |
 **fields** | **str**| Comma-seperated list of fields; only listed fields will be returned in response | [optional]

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
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 404: Not Found &#x3D;&gt; unknown device    * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_access_token**
> UserAccessTokenResponse get_user_access_token(email, id)

Gets an access token of a user

Gets an access token of a user

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import admin_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.user_access_token_response import UserAccessTokenResponse
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
    api_instance = admin_api.AdminApi(api_client)
    email = "email_example" # str | User identifier (email)
    id = "id_example" # str | Access token identifier

    # example passing only required values which don't have defaults set
    try:
        # Gets an access token of a user
        api_response = api_instance.get_user_access_token(email, id)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->get_user_access_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| User identifier (email) |
 **id** | **str**| Access token identifier |

### Return type

[**UserAccessTokenResponse**](UserAccessTokenResponse.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Access token information |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 404: Not Found &#x3D;&gt; unknown user or token    * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_access_tokens_v2**
> UserAccessTokensResponse get_user_access_tokens_v2(email)

Gets the access tokens of a user

Gets the access tokens of a user

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import admin_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.user_access_tokens_response import UserAccessTokensResponse
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
    api_instance = admin_api.AdminApi(api_client)
    email = "email_example" # str | User identifier (email)

    # example passing only required values which don't have defaults set
    try:
        # Gets the access tokens of a user
        api_response = api_instance.get_user_access_tokens_v2(email)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->get_user_access_tokens_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| User identifier (email) |

### Return type

[**UserAccessTokensResponse**](UserAccessTokensResponse.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Access tokens information |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 404: Not Found &#x3D;&gt; unknown user    * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_device**
> DeviceResponse get_user_device(email, serial)

Gets a device controlled by a user

Gets a device controlled by a user

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import admin_api
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
    api_instance = admin_api.AdminApi(api_client)
    email = "email_example" # str | User identifier (email)
    serial = "serial_example" # str | Device identifier (Serial)
    fields = "fields_example" # str | Comma-separated list of device fields; only listed fields will be returned in response (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets a device controlled by a user
        api_response = api_instance.get_user_device(email, serial)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->get_user_device: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a device controlled by a user
        api_response = api_instance.get_user_device(email, serial, fields=fields)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->get_user_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| User identifier (email) |
 **serial** | **str**| Device identifier (Serial) |
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
**200** | Controlled device information |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Forbidden &#x3D;&gt; device is not controlled by the user   * 404: Not Found &#x3D;&gt; unknown user or device    * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_devices_v2**
> DeviceListResponse get_user_devices_v2(email)

Gets the devices controlled by a user

Gets the devices controlled by a user

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import admin_api
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
    api_instance = admin_api.AdminApi(api_client)
    email = "email_example" # str | User identifier (email)
    fields = "fields_example" # str | Comma-separated list of device fields; only listed fields will be returned in response (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the devices controlled by a user
        api_response = api_instance.get_user_devices_v2(email)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->get_user_devices_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the devices controlled by a user
        api_response = api_instance.get_user_devices_v2(email, fields=fields)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->get_user_devices_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| User identifier (email) |
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
**200** | Controlled devices information |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 404: Not Found &#x3D;&gt; unknown user   * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_device_by_serial**
> Response put_device_by_serial(serial, device)

Adds device informatin

Adds device information

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import admin_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.device_payload import DevicePayload
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
    api_instance = admin_api.AdminApi(api_client)
    serial = "serial_example" # str | Device identifier (serial)
    device = DevicePayload(
        note="note_example",
    ) # DevicePayload | Information to add for device. Supports only notes -field. 

    # example passing only required values which don't have defaults set
    try:
        # Adds device informatin
        api_response = api_instance.put_device_by_serial(serial, device)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->put_device_by_serial: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **str**| Device identifier (serial) |
 **device** | [**DevicePayload**](DevicePayload.md)| Information to add for device. Supports only notes -field.  |

### Return type

[**Response**](Response.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Storing success |  -  |
**0** | Unexpected Error:   * 400: Bad Request &#x3D;&gt; invalid request   * 401: Unauthorized &#x3D;&gt; bad credentials   * 404: Not Found &#x3D;&gt; unknown device   * 500: Internal Server Error   * 503: Service Unavailable &#x3D;&gt; server too busy or a lock on a resource is pending   * 504: Gateway Time-out &#x3D;&gt; server is not responding  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_connect_user_device**
> RemoteConnectUserDeviceResponse remote_connect_user_device(email, serial)

Allows to remotely connect to a device controlled by a user

Allows to remotely connect to a device controlled by a user; returns the remote debug URL in response for use with ADB

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import admin_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.remote_connect_user_device_response import RemoteConnectUserDeviceResponse
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
    api_instance = admin_api.AdminApi(api_client)
    email = "email_example" # str | User identifier (email)
    serial = "serial_example" # str | Device identifier (serial)

    # example passing only required values which don't have defaults set
    try:
        # Allows to remotely connect to a device controlled by a user
        api_response = api_instance.remote_connect_user_device(email, serial)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->remote_connect_user_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| User identifier (email) |
 **serial** | **str**| Device identifier (serial) |

### Return type

[**RemoteConnectUserDeviceResponse**](RemoteConnectUserDeviceResponse.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Remote debug URL |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Forbidden &#x3D;&gt; device is not controlled by the user   * 404: Not Found &#x3D;&gt; unknown user or device    * 500: Internal Server Error   * 504: Gateway Time-out &#x3D;&gt; device is not responding  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_disconnect_user_device**
> Response remote_disconnect_user_device(email, serial)

Forbids to remotely connect to a device controlled by a user

Forbids using ADB to remotely connect to a device controlled by a user

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import admin_api
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
    api_instance = admin_api.AdminApi(api_client)
    email = "email_example" # str | User identifier (email)
    serial = "serial_example" # str | Device identifier (serial)

    # example passing only required values which don't have defaults set
    try:
        # Forbids to remotely connect to a device controlled by a user
        api_response = api_instance.remote_disconnect_user_device(email, serial)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->remote_disconnect_user_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| User identifier (email) |
 **serial** | **str**| Device identifier (serial) |

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
**200** | Remote debug URL disabling is OK |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Forbidden &#x3D;&gt; device is not controlled by the user   * 404: Not Found &#x3D;&gt; unknown user or device    * 500: Internal Server Error   * 504: Gateway Time-out &#x3D;&gt; device is not responding  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_origin_group_device**
> DeviceResponse remove_origin_group_device(serial, id)

Removes a device from an origin group

Removes a device from an origin group along with updating the removed device; returns the updated device

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import admin_api
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
    api_instance = admin_api.AdminApi(api_client)
    serial = "serial_example" # str | Device identifier (serial)
    id = "id_example" # str | Group identifier

    # example passing only required values which don't have defaults set
    try:
        # Removes a device from an origin group
        api_response = api_instance.remove_origin_group_device(serial, id)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->remove_origin_group_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **str**| Device identifier (serial) |
 **id** | **str**| Group identifier |

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
**200** | Device information |  -  |
**0** | Unexpected Error:   * 400: Bad Request &#x3D;&gt; group is not an origin one   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Fobidden &#x3D;&gt; the device is currently booked   * 404: Not Found &#x3D;&gt; unknown group or device   * 500: Internal Server Error   * 503: Service Unavailable &#x3D;&gt; server too busy or a lock on a resource is pending   * 504: Gateway Time-out &#x3D;&gt; server is not responding  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_origin_group_devices**
> DeviceListResponse remove_origin_group_devices(id)

Removes devices from an origin group

Removes devices from an origin group along with updating each removed device; returns the updated devices

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import admin_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.devices_payload import DevicesPayload
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
    api_instance = admin_api.AdminApi(api_client)
    id = "id_example" # str | Group identifier
    fields = "fields_example" # str | Comma-seperated list of fields; only listed fields will be returned in response (optional)
    devices = DevicesPayload(
        serials="serials_example",
    ) # DevicesPayload | Devices to remove as a comma-separated list of serials; note that by not providing this parameter it means all devices of the group are selected for removing (optional)

    # example passing only required values which don't have defaults set
    try:
        # Removes devices from an origin group
        api_response = api_instance.remove_origin_group_devices(id)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->remove_origin_group_devices: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Removes devices from an origin group
        api_response = api_instance.remove_origin_group_devices(id, fields=fields, devices=devices)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->remove_origin_group_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group identifier |
 **fields** | **str**| Comma-seperated list of fields; only listed fields will be returned in response | [optional]
 **devices** | [**DevicesPayload**](DevicesPayload.md)| Devices to remove as a comma-separated list of serials; note that by not providing this parameter it means all devices of the group are selected for removing | [optional]

### Return type

[**DeviceListResponse**](DeviceListResponse.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Devices information (an empty device list is returned if no change is made) |  -  |
**0** | Unexpected Error:   * 400: Bad Request &#x3D;&gt; group is not an origin one   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Fobidden &#x3D;&gt; a device is currently booked   * 404: Not Found &#x3D;&gt; unknown group or devices    * 500: Internal Server Error   * 503: Service Unavailable &#x3D;&gt; server too busy or a lock on a resource is pending   * 504: Gateway Time-out &#x3D;&gt; server is not responding  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_default_user_groups_quotas**
> UserResponse update_default_user_groups_quotas()

Updates the default groups quotas of users

Updates the default groups quotas allocated to each new user

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import admin_api
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
    api_instance = admin_api.AdminApi(api_client)
    number = 0 # int | Number of groups (optional)
    duration = 0 # int | Total duration of groups (milliseconds) (optional)
    repetitions = 0 # int | Number of repetitions per Group (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates the default groups quotas of users
        api_response = api_instance.update_default_user_groups_quotas(number=number, duration=duration, repetitions=repetitions)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->update_default_user_groups_quotas: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **int**| Number of groups | [optional]
 **duration** | **int**| Total duration of groups (milliseconds) | [optional]
 **repetitions** | **int**| Number of repetitions per Group | [optional]

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
**200** | Administrator user information (an empty user is returned if no change is made) |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 500: Internal Server Error   * 503: Service Unavailable &#x3D;&gt; server too busy or a lock on a resource is pending  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_groups_quotas**
> UserResponse update_user_groups_quotas(email)

Updates the groups quotas of a user

Updates the groups quotas of a user

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import admin_api
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
    api_instance = admin_api.AdminApi(api_client)
    email = "email_example" # str | User identifier (email)
    number = 0 # int | Number of groups (optional)
    duration = 0 # int | Total duration of groups (milliseconds) (optional)
    repetitions = 0 # int | Number of repetitions per Group (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates the groups quotas of a user
        api_response = api_instance.update_user_groups_quotas(email)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->update_user_groups_quotas: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates the groups quotas of a user
        api_response = api_instance.update_user_groups_quotas(email, number=number, duration=duration, repetitions=repetitions)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling AdminApi->update_user_groups_quotas: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| User identifier (email) |
 **number** | **int**| Number of groups | [optional]
 **duration** | **int**| Total duration of groups (milliseconds) | [optional]
 **repetitions** | **int**| Number of repetitions per Group | [optional]

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
**200** | User information (an empty user is returned if no change is made) |  -  |
**0** | Unexpected Error:   * 400: Bad Request &#x3D;&gt; quotas must be &gt;&#x3D; actual consumed resources   * 401: Unauthorized &#x3D;&gt; bad credentials   * 404: Not Found &#x3D;&gt; unknown user   * 500: Internal Server Error   * 503: Service Unavailable &#x3D;&gt; server too busy or a lock on a resource is pending  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

