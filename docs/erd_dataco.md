# ERD — DataCo Smart Supply Chain 


```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : "places (1:N)"
    ORDER ||--o{ ORDER_DETAILS : "contains (1:N)"
    PRODUCT ||--o{ ORDER_DETAILS : "appears_in (1:N)"
    DEPARTMENT ||--o{ CATEGORY : "has (1:N)"
    CATEGORY ||--o{ PRODUCT : "contains (1:N)"
    ORDER ||--|| SHIPMENT : "has (1:1)"

    CUSTOMER {
        int CustomerId PK
        string CustomerFname
        string CustomerLname
        string CustomerSegment
        string CustomerCity
        string CustomerState
        string CustomerCountry
        string CustomerZipcode
        string CustomerStreet
        double Latitude
        double Longitude
    }

    DEPARTMENT {
        int DepartmentId PK
        string DepartmentName
    }

    CATEGORY {
        int CategoryId PK
        string CategoryName
        int DepartmentId FK
    }

    PRODUCT {
        int ProductCardId PK
        string ProductName
        double ProductPrice
        string ProductImage
        int CategoryId FK
    }

    ORDER {
        int OrderId PK
        datetime OrderDate
        string OrderStatus
        string Market
        string OrderRegion
        string OrderCity
        string OrderState
        string OrderCountry
        int CustomerId FK
    }

    ORDER_DETAILS {
        int OrderItemId PK
        int OrderId FK
        int ProductCardId FK
        int OrderItemQuantity
        double OrderItemDiscount
        double OrderItemDiscountRate
        double OrderItemProductPrice
        double OrderItemProfitRatio
    }

    SHIPMENT {
        int OrderId PK
        string ShippingMode
        string DeliveryStatus
        int LateDeliveryRisk
        int DaysForShippingReal
        int DaysForShipmentScheduled
        datetime ShippingDate
    }