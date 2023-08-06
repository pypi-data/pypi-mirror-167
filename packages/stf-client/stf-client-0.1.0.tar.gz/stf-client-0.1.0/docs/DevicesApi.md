# stf_client.DevicesApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_bookings**](DevicesApi.md#get_device_bookings) | **GET** /devices/{serial}/bookings | Gets the bookings to which the device belongs
[**get_device_by_serial**](DevicesApi.md#get_device_by_serial) | **GET** /devices/{serial} | Device Information
[**get_devices**](DevicesApi.md#get_devices) | **GET** /devices | Device List


# **get_device_bookings**
> GroupListResponse get_device_bookings(serial)

Gets the bookings to which the device belongs

Gets the bookings (i.e. transient groups) to which the device belongs

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import devices_api
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
    api_instance = devices_api.DevicesApi(api_client)
    serial = "serial_example" # str | Device identifier (serial)
    fields = "fields_example" # str | Fields query parameter takes a comma seperated list of fields. Only listed field will be return in response (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the bookings to which the device belongs
        api_response = api_instance.get_device_bookings(serial)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling DevicesApi->get_device_bookings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the bookings to which the device belongs
        api_response = api_instance.get_device_bookings(serial, fields=fields)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling DevicesApi->get_device_bookings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial** | **str**| Device identifier (serial) |
 **fields** | **str**| Fields query parameter takes a comma seperated list of fields. Only listed field will be return in response | [optional]

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
**200** | Bookings information |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 404: Not Found &#x3D;&gt; unknown device    * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_by_serial**
> DeviceResponse get_device_by_serial(serial)

Device Information

The devices serial enpoint return information about a single device

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import devices_api
from stf_client.model.error_response import ErrorResponse
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
    api_instance = devices_api.DevicesApi(api_client)
    serial = "serial_example" # str | Device Serial
    fields = "fields_example" # str | Fields query parameter takes a comma seperated list of fields. Only listed field will be return in response (optional)

    # example passing only required values which don't have defaults set
    try:
        # Device Information
        api_response = api_instance.get_device_by_serial(serial)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling DevicesApi->get_device_by_serial: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Device Information
        api_response = api_instance.get_device_by_serial(serial, fields=fields)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling DevicesApi->get_device_by_serial: %s\n" % e)
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
**200** | Device Information |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices**
> DeviceListResponse get_devices()

Device List

The devices endpoint return list of all the STF devices including Disconnected and Offline

### Example

* Api Key Authentication (accessTokenAuth):

```python
import time
import stf_client
from stf_client.api import devices_api
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
    api_instance = devices_api.DevicesApi(api_client)
    target = "user" # str | Targets devices of your universe:  * bookable - devices belonging to a bookable group  * standard - devices belonging to a standard group  * origin - all devices  * standardizable - devices which are not yet booked including those belonging to a standard group  * user (default value) - devices which are accessible by you at a given time  (optional) if omitted the server will use the default value of "user"
    fields = "fields_example" # str | Fields query parameter takes a comma seperated list of fields. Only listed field will be return in response (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Device List
        api_response = api_instance.get_devices(target=target, fields=fields)
        pprint(api_response)
    except stf_client.ApiException as e:
        print("Exception when calling DevicesApi->get_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | **str**| Targets devices of your universe:  * bookable - devices belonging to a bookable group  * standard - devices belonging to a standard group  * origin - all devices  * standardizable - devices which are not yet booked including those belonging to a standard group  * user (default value) - devices which are accessible by you at a given time  | [optional] if omitted the server will use the default value of "user"
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
**200** | Devices information |  -  |
**0** | Unexpected Error:   * 401: Unauthorized &#x3D;&gt; bad credentials   * 500: Internal Server Error  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

