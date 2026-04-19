# Class Diagram – DataCo Supply Chain Project



```mermaid
classDiagram
    class Customer {
        int CustomerId
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

    class Department {
        int DepartmentId
        string DepartmentName
    }

    class Category {
        int CategoryId
        string CategoryName
        int DepartmentId
    }

    class Product {
        int ProductCardId
        string ProductName
        double ProductPrice
        string ProductImage
        int CategoryId
    }

    class Order {
        int OrderId
        datetime OrderDate
        string OrderStatus
        string Market
        string OrderRegion
        string OrderCity
        string OrderState
        string OrderCountry
        int CustomerId
    }

    class OrderDetails {
        int OrderItemId
        int OrderId
        int ProductCardId
        int OrderItemQuantity
        double OrderItemDiscount
        double OrderItemDiscountRate
        double OrderItemProductPrice
        double OrderItemProfitRatio
    }

    class Shipment {
        int OrderId
        string ShippingMode
        string DeliveryStatus
        int LateDeliveryRisk
        int DaysForShippingReal
        int DaysForShipmentScheduled
        datetime ShippingDate
    }

    Customer "1" -- "0..*" Order
    Order "1" -- "1..*" OrderDetails
    Product "1" -- "0..*" OrderDetails
    Department "1" -- "0..*" Category
    Category "1" -- "0..*" Product
    Order "1" -- "1" Shipment