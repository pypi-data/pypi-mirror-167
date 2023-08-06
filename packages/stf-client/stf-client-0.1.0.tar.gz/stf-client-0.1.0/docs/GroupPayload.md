# GroupPayload

Payload object for creating/updating a group

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Group Name; default value &#x3D;&gt; generated at runtime | [optional] 
**start_time** | **datetime** | Group starting time (in UTC, conforming to RFC 3339 section 5.6); default value &#x3D;&gt; group creation time | [optional] 
**stop_time** | **datetime** | Group expiration time (in UTC, conforming to RFC 3339 section 5.6); default value &#x3D;&gt; startTime + 1 hour | [optional] 
**_class** | **str** | Group class; privileged value &#x3D;&gt; debug, bookable, standard | [optional]  if omitted the server will use the default value of "once"
**repetitions** | **int** | Group repetitions; default value &#x3D;&gt; 0 | [optional] 
**state** | **str** | Group state; default value &#x3D;&gt; pending or ready for bookable/standard classes | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


