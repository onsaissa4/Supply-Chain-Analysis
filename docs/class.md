# Class Diagram 

```mermaid
classDiagram
    class Customer {
        - int CustomerId
        - string CustomerFname
        - string CustomerLname
        - string CustomerSegment
        - string CustomerCity
        - string CustomerState
        - string CustomerCountry
        - string CustomerZipcode
        - string CustomerStreet
        - double Latitude
        - double Longitude
        + TotalCustomers() int
        + AvgOrdersPerCustomer() float
    }

    class Department {
        - int DepartmentId
        - string DepartmentName
    }

    class Category {
        - int CategoryId
        - string CategoryName
        - int DepartmentId
    }

    class Product {
        - int ProductCardId
        - string ProductName
        - double ProductPrice
        - string ProductImage
        - int CategoryId
        + NegativeProfitProducts() int
    }

    class Order {
        - int OrderId
        - datetime OrderDate
        - string OrderStatus
        - string Market
        - string OrderRegion
        - string OrderCity
        - string OrderState
        - string OrderCountry
        - int CustomerId
        + TotalOrders() int
        + CancellationRate() float
    }

    class OrderDetails {
        - int OrderItemId
        - int OrderId
        - int ProductCardId
        - int OrderItemQuantity
        - double OrderItemDiscount
        - double OrderItemDiscountRate
        - double OrderItemProductPrice
        - double OrderItemProfitRatio
        + TotalSales() float
        + TotalProfit() float
        + ProfitMargin() float
    }

    class Shipment {
        - int OrderId
        - string ShippingMode
        - string DeliveryStatus
        - int LateDeliveryRisk
        - int DaysForShippingReal
        - int DaysForShipmentScheduled
        - datetime ShippingDate
        + LateDeliveryRate() float
        + AvgShippingDaysReal() float
        + AvgShippingDaysScheduled() float
    }

    Customer "1" -- "0..*" Order
    Order "1" -- "1..*" OrderDetails
    Product "1" -- "0..*" OrderDetails
    Department "1" -- "0..*" Category
    Category "1" -- "0..*" Product
    Order "1" -- "1" Shipment