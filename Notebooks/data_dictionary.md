# Data Dictionary  
**Vendor Sales & Inventory Dataset**

## Overview
This data dictionary documents the structure, meaning, data types, and business relevance of each variable across the five raw source tables used in the *Data Immersion & Wrangling* task. The dataset represents a real-world vendor sales, purchasing, invoicing, and inventory management scenario.

---

## Table: Begin Inventory (`begin_inventory.csv`)

| Column Name | Data Type | Description | Business Relevance |
|------------|----------|-------------|--------------------|
| InventoryId | Integer | Unique identifier for inventory record | Record-level tracking |
| Store | Integer | Store identifier | Store-level inventory analysis |
| City | String | City where the store is located | Regional inventory analysis |
| Brand | Integer | Brand identifier | Product grouping and comparison |
| Description | String | Product description | Product identification |
| Size | String | Package size (e.g., 750mL) | Inventory comparison |
| onHand | Integer | Quantity available at the beginning of the period | Opening stock position |
| Price | Float | Retail price per unit | Inventory valuation |
| startDate | Date | Inventory start date | Period alignment |

---

## Table: End Inventory (`end_inventory.csv`)

| Column Name | Data Type | Description | Business Relevance |
|------------|----------|-------------|--------------------|
| InventoryId | Integer | Unique inventory record identifier | Record tracking |
| Store | Integer | Store identifier | Store-level inventory analysis |
| City | String | Store city | Regional inventory trends |
| Brand | Integer | Brand identifier | Product grouping |
| Description | String | Product description | Product tracking |
| Size | String | Package size | Inventory consistency |
| onHand | Integer | Quantity at the end of the period | Unsold inventory measurement |
| Price | Float | Retail price per unit | Inventory valuation |
| endDate | Date | Inventory end date | Closing stock tracking |

---

## Table: Sales (`sales.csv`)

| Column Name | Data Type | Description | Business Relevance |
|------------|----------|-------------|--------------------|
| InvoiceNo | String | Sales invoice number | Transaction tracking |
| Store | Integer | Store identifier | Sales by store |
| City | String | City of store | Regional sales analysis |
| Brand | Integer | Brand identifier | Product-level sales |
| Description | String | Product description | Item identification |
| Size | String | Package size | Sales comparison |
| SalesQuantity | Integer | Units sold | Demand measurement |
| SalesAmount | Float | Total sales value | Revenue calculation |
| SalesDate | Date | Date of sale | Time-based sales analysis |

---

## Table: Purchase Prices (`purchase_prices.csv`)

| Column Name | Data Type | Description | Business Relevance |
|------------|----------|-------------|--------------------|
| Brand | Integer | Brand identifier | Product linkage |
| Description | String | Product description | Product reference |
| Price | Float | Retail price | Margin analysis |
| Size | String | Product size | Product comparison |
| Volume | String | Volume measurement | Packaging insights |
| Classification | Integer | Product classification code | Category analysis |
| PurchasePrice | Float | Vendor purchase price | Cost and profitability analysis |
| VendorNumber | Integer | Vendor identifier | Supplier tracking |
| VendorName | String | Vendor name | Vendor performance evaluation |

---

## Table: Vendor Invoice (`vendor_invoice.csv`)

| Column Name | Data Type | Description | Business Relevance |
|------------|----------|-------------|--------------------|
| VendorNumber | Integer | Vendor identifier | Vendor-level analysis |
| VendorName | String | Vendor name | Supplier identification |
| InvoiceDate | Date | Date of vendor invoice | Financial period tracking |
| PONumber | String | Purchase order number | Procurement tracking |
| InvoiceNumber | String | Vendor invoice identifier | Financial reconciliation |
| Freight | Float | Freight or shipping cost | Logistics cost analysis |
| Approval | String | Invoice approval status | Process and control validation |
| InvoiceAmount | Float | Total invoice amount | Expense and cost tracking |

---

