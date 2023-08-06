# stf_client.UsersApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_by_email**](UsersApi.md#get_user_by_email) | **GET** /users/{email} | Gets a user
[**get_users**](UsersApi.md#get_users) | **GET** /users | Gets users


# **get_user_by_email**
> UserResponse get_user_by_email(email)

Gets a user

Gets a user; if you are the administrator user then all user fields are returned, otherwise only 'email', 'name' and 'privilege' user fields are returned

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    email = "email_example" # str | User identifier (email)
    fields = "fields_example" # str | Comma-separated list of user fields; only listed fields will be returned in response (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets a user
        api_response = api_instance.get_user_by_email(email)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling UsersApi->get_user_by_email: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a user
        api_response = api_instance.get_user_by_email(email, fields=fields)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling UsersApi->get_user_by_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | User information |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 404: Not Found &#x3D;&gt; unknown user   * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> UserListResponse get_users()

Gets users

gets users; if you are the administrator user then all user fields are returned, otherwise only 'email', 'name' and 'privilege' user fields are returned

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    fields = "fields_example" # str | Comma-separated list of user fields; only listed fields will be returned in response (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets users
        api_response = api_instance.get_users(fields=fields)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling UsersApi->get_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | Users information |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

