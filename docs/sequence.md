# Sequence Diagram 


```mermaid
sequenceDiagram
    actor Customer
    participant UI as User Interface
    participant System as System Platform
    participant DB as Database
    participant ShippingService as Shipping Service

    Customer->>UI: Place Order
    UI->>System: Send Order Request
    System->>DB: Check product availability
    DB-->>System: Available / OK
    System->>DB: Create Order
    System->>ShippingService: Create Shipment Request
    ShippingService-->>System: Shipment Confirmed
    System-->>UI: Order Success + Tracking Info
    UI-->>Customer: Display Confirmation