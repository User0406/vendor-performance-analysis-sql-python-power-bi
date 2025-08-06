import pandas
import sqlite3
import logging
from ingestion_db import ingest_db
import pandas as pd
import sqlite3
import logging

# Setup logging
logging.basicConfig(
    filename='logs/get_vendor_sales_summary.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)

def create_vendor_summary(conn):
    '''This function merges different tables to get the overall vendor summary and adds new columns.'''
    query = '''
    WITH FreightSummary AS (
        SELECT VendorNumber, SUM(Freight) AS FreightCost 
        FROM Vendor_invoice 
        GROUP BY VendorNumber
    ),
    PurchaseSummary AS (
        SELECT 
            p.VendorNumber, 
            p.VendorName,
            p.Brand,
            p.Description,
            p.PurchasePrice,
            pp.Price AS ActualPrice,
            pp.Volume,
            SUM(p.Quantity) AS TotalPurchaseQuantity,
            SUM(p.Dollars) AS TotalPurchaseDollars 
        FROM Purchases p
        JOIN purchase_prices pp ON p.Brand = pp.Brand
        WHERE p.PurchasePrice > 0
        GROUP BY p.VendorName, p.VendorNumber, p.Brand, p.Description, p.PurchasePrice, pp.Price, pp.Volume
    ),
    SalesSummary AS (
        SELECT  
            vendorNo,
            Brand,
            SUM(SalesDollars) AS TotalSalesDollars,
            SUM(SalesPrice) AS TotalSalesPrice,
            SUM(SalesQuantity) AS TotalSalesQuantity,
            SUM(ExciseTax) AS TotalExciseTax
        FROM sales
        GROUP BY vendorNo, Brand
    )

    SELECT
        ps.VendorNumber, 
        ps.VendorName,
        ps.Brand,
        ps.Description,
        ps.PurchasePrice,
        ps.ActualPrice,
        ps.Volume,
        ps.TotalPurchaseQuantity,
        ps.TotalPurchaseDollars,
        ss.TotalSalesDollars,
        ss.TotalSalesPrice,
        ss.TotalSalesQuantity,
        ss.TotalExciseTax,
        fs.FreightCost
    FROM PurchaseSummary ps
    LEFT JOIN SalesSummary ss ON ps.VendorNumber = ss.vendorNo AND ps.Brand = ss.Brand
    LEFT JOIN FreightSummary fs ON ps.VendorNumber = fs.VendorNumber
    ORDER BY ps.TotalPurchaseDollars DESC
    '''

    df = pd.read_sql_query(query, conn)
    return df

def clean_data(df):
    '''This function cleans and enriches the data.'''
    # Fix typo: 'Volumn' → 'Volume' and fix syntax
    df['Volume'] = df['Volume'].astype('float64')

    # Fill missing values
    df.fillna(0, inplace=True)

    # Clean categorical strings
    df['VendorName'] = df['VendorName'].str.strip()
    df['Description'] = df['Description'].str.strip()

    # Add computed columns
    df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']
    df['ProfitMargin'] = (df['GrossProfit'] / df['TotalSalesDollars'].replace(0, pd.NA)) * 100
    df['StockTurnover'] = df['TotalSalesQuantity'] - df['TotalPurchaseQuantity']
    df['SalestoPurchaseRatio'] = df['TotalSalesDollars'] / df['TotalPurchaseDollars'].replace(0, pd.NA)

    return df

# Dummy ingest function
def ingest_db(df, table_name, conn):
    '''This function ingests the dataframe into a given table in the SQLite DB.'''
    df.to_sql(table_name, conn, if_exists='replace', index=False)

if __name__ == '__main__':
    conn = sqlite3.connect('inventory.db')

    logging.info('Creating Vendor Summary Table...')
    summary_df = create_vendor_summary(conn)
    logging.info(f'Vendor Summary Head:\n{summary_df.head()}')

    logging.info('Cleaning Data...')
    clean_df = clean_data(summary_df)
    logging.info(f'Cleaned Data Head:\n{clean_df.head()}')

    logging.info('Ingesting data...')
    ingest_db(clean_df, 'vendor_sales_summary', conn)
    logging.info('Data ingestion completed.')
