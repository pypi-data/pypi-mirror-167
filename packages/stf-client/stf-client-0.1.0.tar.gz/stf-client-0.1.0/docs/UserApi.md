# stf_client.UserApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_adb_public_key**](UserApi.md#add_adb_public_key) | **POST** /user/adbPublicKeys | Adb public keys
[**add_user_device**](UserApi.md#add_user_device) | **POST** /user/devices | Add a device to a user
[**add_user_device_v2**](UserApi.md#add_user_device_v2) | **POST** /user/devices/{serial} | Places a device under user control
[**create_access_token**](UserApi.md#create_access_token) | **POST** /user/accessTokens | Create an access token
[**delete_access_token**](UserApi.md#delete_access_token) | **DELETE** /user/accessTokens/{id} | Removes an access token
[**delete_access_tokens**](UserApi.md#delete_access_tokens) | **DELETE** /user/accessTokens | Removes your access tokens
[**delete_user_device_by_serial**](UserApi.md#delete_user_device_by_serial) | **DELETE** /user/devices/{serial} | Delete User Device
[**get_access_token**](UserApi.md#get_access_token) | **GET** /user/accessTokens/{id} | Gets an access token
[**get_access_tokens**](UserApi.md#get_access_tokens) | **GET** /user/fullAccessTokens | Gets your access tokens
[**get_user**](UserApi.md#get_user) | **GET** /user | User Profile
[**get_user_access_tokens**](UserApi.md#get_user_access_tokens) | **GET** /user/accessTokens | Access Tokens
[**get_user_device_by_serial**](UserApi.md#get_user_device_by_serial) | **GET** /user/devices/{serial} | User Device
[**get_user_devices**](UserApi.md#get_user_devices) | **GET** /user/devices | User Devices
[**remote_connect_user_device_by_serial**](UserApi.md#remote_connect_user_device_by_serial) | **POST** /user/devices/{serial}/remoteConnect | Remote Connect
[**remote_disconnect_user_device_by_serial**](UserApi.md#remote_disconnect_user_device_by_serial) | **DELETE** /user/devices/{serial}/remoteConnect | Remote Disconnect


# **add_adb_public_key**
> add_adb_public_key()

Adb public keys

Add adb public key for current user

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import user_api
from stf_client.model.error_response import ErrorResponse
from stf_client.model.add_adb_public_key_request import AddAdbPublicKeyRequest
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
    api_instance = user_api.UserApi(api_client)
    adb = AddAdbPublicKeyRequest(
        publickey="publickey_example",
        title="title_example",
    ) # AddAdbPublicKeyRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adb public keys
        api_instance.add_adb_public_key(adb=adb)
    except stf_client.ApiException as e:
        print("Exception when calling UserApi->add_adb_public_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adb** | [**AddAdbPublicKeyRequest**](AddAdbPublicKeyRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add adb key response |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_device**
> add_user_device(device)

Add a device to a user

The User Devices endpoint will request stf server for a new device.

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import user_api
from stf_client.model.unexpected_error_response import UnexpectedErrorResponse
from stf_client.model.add_user_device_payload import AddUserDevicePayload
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
    api_instance = user_api.UserApi(api_client)
    device = AddUserDevicePayload(
        serial="serial_example",
        timeout=1,
    ) # AddUserDevicePayload | Device to add

    # example passing only required values which don't have defaults set
    try:
        # Add a device to a user
        api_instance.add_user_device(device)
    except stf_client.ApiException as e:
        print("Exception when calling UserApi->add_user_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | [**AddUserDevicePayload**](AddUserDevicePayload.md)| Device to add |

### Return type

void (empty response body)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add User Device Status |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Forbidden &#x3D;&gt; device is already controlled or is not available   * 404: Not Found &#x3D;&gt; unknown device    * 500: Internal Server Error   * 504: Gateway Time-out &#x3D;&gt; device is not responding  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_device_v2**
> Response add_user_device_v2(serial)

Places a device under user control

Places a device under user control; note this is not completely analogous to press the 'Use' button in the UI because that does not authorize remote connection through ADB

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    serial = "serial_example" # str | Device identifier (serial)
    timeout = 0 # int | Means the device will be automatically removed from the user control if it is kept idle for this period (in milliseconds); default value is provided by the provider 'group timeout' (optional)

    # example passing only required values which don't have defaults set
    try:
        # Places a device under user control
        api_response = api_instance.add_user_device_v2(serial)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling UserApi->add_user_device_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Places a device under user control
        api_response = api_instance.add_user_device_v2(serial, timeout=timeout)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling UserApi->add_user_device_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Forbidden &#x3D;&gt; device is already controlled or is not available   * 404: Not Found &#x3D;&gt; unknown device    * 500: Internal Server Error   * 504: Gateway Time-out &#x3D;&gt; device is not responding  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_access_token**
> UserAccessTokenResponse create_access_token(title)

Create an access token

Create an access token for you

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    title = "title_example" # str | Access token title

    # example passing only required values which don't have defaults set
    try:
        # Create an access token
        api_response = api_instance.create_access_token(title)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling UserApi->create_access_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**201** | Access token information |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_token**
> Response delete_access_token(id)

Removes an access token

Removes one of your access tokens

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    id = "id_example" # str | Access token identifier

    # example passing only required values which don't have defaults set
    try:
        # Removes an access token
        api_response = api_instance.delete_access_token(id)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling UserApi->delete_access_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 404: Not Found &#x3D;&gt; unknown token    * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_tokens**
> Response delete_access_tokens()

Removes your access tokens

Removes your access tokens

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import user_api
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Removes your access tokens
        api_response = api_instance.delete_access_tokens()
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling UserApi->delete_access_tokens: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_device_by_serial**
> Response delete_user_device_by_serial(serial)

Delete User Device

The User Devices endpoint will request for device release from stf server. It will return request accepted if device is being used by current user

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    serial = "serial_example" # str | Device Serial

    # example passing only required values which don't have defaults set
    try:
        # Delete User Device
        api_response = api_instance.delete_user_device_by_serial(serial)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling UserApi->delete_user_device_by_serial: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **str**| Device Serial |

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
**200** | Delete User Device Status |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Forbidden &#x3D;&gt; device is not controlled by the user   * 404: Not Found &#x3D;&gt; unknown device    * 500: Internal Server Error   * 504: Gateway Time-out &#x3D;&gt; device is not responding  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_token**
> UserAccessTokenResponse get_access_token(id)

Gets an access token

Gets one of your access tokens

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    id = "id_example" # str | Access token identifier

    # example passing only required values which don't have defaults set
    try:
        # Gets an access token
        api_response = api_instance.get_access_token(id)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling UserApi->get_access_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 404: Not Found &#x3D;&gt; unknown token    * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_tokens**
> UserAccessTokensResponse get_access_tokens()

Gets your access tokens

Gets your access tokens; note that all fields are returned in reponse including the 'id' one

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import user_api
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Gets your access tokens
        api_response = api_instance.get_access_tokens()
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling UserApi->get_access_tokens: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserResponse get_user()

User Profile

The User Profile endpoint returns information about current authorized user

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import user_api
from stf_client.model.user_response import UserResponse
from stf_client.model.error_response import ErrorResponse
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # User Profile
        api_response = api_instance.get_user()
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling UserApi->get_user: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**200** | Current User Profile information |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_access_tokens**
> AccessTokensResponse get_user_access_tokens()

Access Tokens

The Access Tokens endpoints returns titles of all the valid access tokens

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import user_api
from stf_client.model.error_response import ErrorResponse
from stf_client.model.access_tokens_response import AccessTokensResponse
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Access Tokens
        api_response = api_instance.get_user_access_tokens()
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling UserApi->get_user_access_tokens: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessTokensResponse**](AccessTokensResponse.md)

### Authorization

[accessTokenAuth](../README.md#accessTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Access Tokens titles |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_device_by_serial**
> DeviceResponse get_user_device_by_serial(serial)

User Device

The devices enpoint return information about device owned by user

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    serial = "serial_example" # str | Device Serial
    fields = "fields_example" # str | Fields query parameter takes a comma seperated list of fields. Only listed field will be return in response (optional)

    # example passing only required values which don't have defaults set
    try:
        # User Device
        api_response = api_instance.get_user_device_by_serial(serial)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling UserApi->get_user_device_by_serial: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # User Device
        api_response = api_instance.get_user_device_by_serial(serial, fields=fields)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling UserApi->get_user_device_by_serial: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **str**| Device Serial |
 **fields** | **str**| Fields query parameter takes a comma seperated list of fields. Only listed field will be return in response | [optional]

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
**200** | Device Information owned by user |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Forbidden &#x3D;&gt; device is not controlled by the user   * 404: Not Found &#x3D;&gt; unknown device    * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_devices**
> DeviceListResponse get_user_devices()

User Devices

The User Devices endpoint returns device list owner by current authorized user

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    fields = "fields_example" # str | Fields query parameter takes a comma seperated list of fields. Only listed field will be return in response (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # User Devices
        api_response = api_instance.get_user_devices(fields=fields)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling UserApi->get_user_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields query parameter takes a comma seperated list of fields. Only listed field will be return in response | [optional]

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
**200** | Current User Devices List |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_connect_user_device_by_serial**
> RemoteConnectUserDeviceResponse remote_connect_user_device_by_serial(serial)

Remote Connect

The device connect endpoint will request stf server to connect remotely

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    serial = "serial_example" # str | Device Serial

    # example passing only required values which don't have defaults set
    try:
        # Remote Connect
        api_response = api_instance.remote_connect_user_device_by_serial(serial)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling UserApi->remote_connect_user_device_by_serial: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **str**| Device Serial |

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
**200** | Remote Connect User Device Request Status |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Forbidden &#x3D;&gt; device is not controlled by the user   * 404: Not Found &#x3D;&gt; unknown device    * 500: Internal Server Error   * 504: Gateway Time-out &#x3D;&gt; device is not responding  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_disconnect_user_device_by_serial**
> Response remote_disconnect_user_device_by_serial(serial)

Remote Disconnect

The device connect endpoint will request stf server to disconnect remotely

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    serial = "serial_example" # str | Device Serial

    # example passing only required values which don't have defaults set
    try:
        # Remote Disconnect
        api_response = api_instance.remote_disconnect_user_device_by_serial(serial)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling UserApi->remote_disconnect_user_device_by_serial: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **str**| Device Serial |

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
**200** | Remote Disonnect User Device Request Status |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 403: Forbidden &#x3D;&gt; device is not controlled by the user   * 404: Not Found &#x3D;&gt; unknown device    * 500: Internal Server Error   * 504: Gateway Time-out &#x3D;&gt; device is not responding  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

