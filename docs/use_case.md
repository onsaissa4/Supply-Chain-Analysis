## Use Case Diagram

```mermaid
flowchart TD
    subgraph System [System]
        Auth(Authenticate)
        PlaceOrder(Place Order)
        CreateShipment(Create Shipment)
        ManageProducts(Manage Products)
        ManageOrders(Manage Orders)
    end

    Customer((Customer))
    Manager((Manager))
    Shipping((Shipping Service))

    Customer --> PlaceOrder
    PlaceOrder -.-> Auth
    PlaceOrder --> CreateShipment
    CreateShipment --> Shipping
    Manager --> ManageProducts
    ManageProducts -.-> Auth
    Manager --> ManageOrders
    ManageOrders -.-> Auth