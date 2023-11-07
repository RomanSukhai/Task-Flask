# DefaultApi

All URIs are relative to *http://localhost:5000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOrder**](DefaultApi.md#createOrder) | **POST** /orders | Створення замовлення
[**createProduct**](DefaultApi.md#createProduct) | **POST** /products | Створення товару
[**deleteProduct**](DefaultApi.md#deleteProduct) | **DELETE** /products/{productId} | Видалення товару
[**getProductById**](DefaultApi.md#getProductById) | **GET** /products/{productId} | Отримати товар за його ідентифікатором
[**listProducts**](DefaultApi.md#listProducts) | **GET** /products | Перелік усіх товарів
[**updateProduct**](DefaultApi.md#updateProduct) | **PUT** /products/{productId} | Оновлення товару


<a name="createOrder"></a>
# **createOrder**
> createOrder(order)

Створення замовлення

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:5000/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Order order = new Order(); // Order | 
    try {
      apiInstance.createOrder(order);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createOrder");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | [**Order**](Order.md)|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Замовлення створено |  -  |
**400** | Недійсне замовлення |  -  |

<a name="createProduct"></a>
# **createProduct**
> createProduct(product)

Створення товару

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:5000/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Product product = new Product(); // Product | 
    try {
      apiInstance.createProduct(product);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createProduct");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | [**Product**](Product.md)|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Товар створено |  -  |

<a name="deleteProduct"></a>
# **deleteProduct**
> deleteProduct(productId)

Видалення товару

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:5000/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String productId = "productId_example"; // String | 
    try {
      apiInstance.deleteProduct(productId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteProduct");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **productId** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Товар видалено |  -  |
**404** | Товар не знайдено |  -  |

<a name="getProductById"></a>
# **getProductById**
> Product getProductById(productId)

Отримати товар за його ідентифікатором

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:5000/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String productId = "productId_example"; // String | 
    try {
      Product result = apiInstance.getProductById(productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getProductById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **productId** | **String**|  |

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Об&#39;єкт товару |  -  |
**404** | Товар не знайдено |  -  |

<a name="listProducts"></a>
# **listProducts**
> List&lt;Product&gt; listProducts()

Перелік усіх товарів

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:5000/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      List<Product> result = apiInstance.listProducts();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listProducts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Product&gt;**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Масив товарів |  -  |

<a name="updateProduct"></a>
# **updateProduct**
> updateProduct(productId, product)

Оновлення товару

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:5000/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String productId = "productId_example"; // String | 
    Product product = new Product(); // Product | 
    try {
      apiInstance.updateProduct(productId, product);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateProduct");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **productId** | **String**|  |
 **product** | [**Product**](Product.md)|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Товар оновлено |  -  |
**404** | Товар не знайдено |  -  |

