{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "422058f0-fd6f-4443-83c4-2bb4382217cc",
   "metadata": {},
   "source": [
    "#  <font color='blue'>Vendor Performance analysis - Retail Inventory and Sales</font>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3bf68061-e9c7-4e28-bddd-fd7e490b86d3",
   "metadata": {},
   "source": [
    "_Analyzing vendor efficiency and profitability to support strategic purchasing and inventory decisions\n",
    "using SQL, Python, and Power BI._"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9b88edcd-d571-4e81-bf8f-9785264f5f12",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d1a17624-0fb0-4403-b2bb-3ee6d53cb0a5",
   "metadata": {},
   "source": [
    "## Table Of Content\n",
    "- <a href=\"#overview\">Overview</a>\n",
    "- <a href=\"#business-problem\">Business Problem</a>\n",
    "- <a href=\"#dataset\">Dataset</a>\n",
    "- <a href=\"#tools -- technologies\">Tools & Technologies</a>\n",
    "- <a href=\"#project-structure\">Project Structure</a>\n",
    "<a href=\"#data-cleaning -- preparation\">Data Cleaning & Preparation</a>\n",
    "- <a href=\"#exploratory-data-analysis-eda\">Exploratory Data Analysis (EDA)</a>\n",
    "- <a href=\"#research-questions -- key-findings\">Research Questions & Key Findings</a>\n",
    "- <a href=\"#dashboard\">Dashboard</a>\n",
    "- <a href=\"#how-to-run-this-project\">How to Run This Project</a>\n",
    "- <a href=\"#final-recommendations\">Final Recommendations</a>\n",
    "- <a href=\"#author -- contact\">Author & Contact</a>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f17c8cf5-0d28-45b3-969d-cedae4aa6160",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "74227d7d-9996-472f-9f29-69d1980f8dc0",
   "metadata": {},
   "source": [
    "<h2><a class=\"anchor\" id=\"overview\"></a>Overview</h2>\n",
    "\n",
    "This project evaluates vendor performance and retail inventory dynamics to drive strategic insights for\n",
    "purchasing, pricing, and inventory optimization. A complete data pipeline was built using SQL for ETL,\n",
    "Python for analysis and hypothesis testing, and Power BI for visualization."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c6ce0f59-5564-4272-ab00-3ed34b4e1c39",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5836cddf-a705-40e5-bab0-e4924d39774a",
   "metadata": {},
   "source": [
    "<h2><a class=\"anchor\" id=\"business-problem\"></a>Business Problem</h2>\n",
    "\n",
    "Effective inventory and sales management are critical in the retail sector. This project aims to:\n",
    "- Identify underperforming brands needing pricing or promotional adjustments\n",
    "- Determine vendor contributions to sales and profits\n",
    "- Analyze the cost-benefit of bulk purchasing\n",
    "- Investigate inventory turnover inefficiencies\n",
    "- Statistically validate differences in vendor profitability"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6f114c0a-b102-413f-ac07-82421b49a484",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d3e5aeb0-90a0-4c01-94ae-36e5fbe5bd6c",
   "metadata": {},
   "source": [
    "<h2><a class=\"anchor\" id=\"dataset\"></a>Dataset</h2>\n",
    "\n",
    "- Multiple CSV files located in '/data/' folder (sales, vendors, inventory)\n",
    "- Summary table created from ingested data and used for analysis"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4992d03c-1539-443e-b63c-c63d833db91e",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "15ed3d6a-993c-46bc-935e-f4eb9ac23b3e",
   "metadata": {},
   "source": [
    "<h2><a class=\"anchor\" id=\"project-structure\"></a>Project Structure</h2>\n",
    "\n",
    "```\n",
    "vendor-performance-analysis/\n",
    "\n",
    "    -README. md\n",
    "    -.gitignore\n",
    "    -requirements.txt\n",
    "    -Vendor Performance Report.pdf\n",
    "\n",
    "    -notebooks/   # Jupyter notebooks\n",
    "        exploratory_data_analysis.ipynb\n",
    "        vendor_performance_analysis.ipynb\n",
    "\n",
    "\n",
    "\n",
    "    -scripts/    # Python scripts for ingestion and processing\n",
    "        ingestion_db.py\n",
    "        get_vendor_summary.py\n",
    "\n",
    "    -dashboard/   # Power BI dashboard file\n",
    "        vendor_performance_dashboard.pbix\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f73e6436-9da1-4d92-9b26-ed171a217579",
   "metadata": {},
   "source": [
    "|,\n",
    "|--"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e76f0044-ca90-489c-9414-92f8de11bc7f",
   "metadata": {},
   "source": [
    "----"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "32dca77c-c14c-4f21-b7b9-84809bd5131a",
   "metadata": {},
   "source": [
    "<h2><a class=\"anchor\" id=\"data-cleaning -- preparation\"></a>Data Cleaning & Preparation</h2>\n",
    "\n",
    "- Removed transactions with:\n",
    "- Gross Profit\n",
    "- Profit Margin 0\n",
    "- Sales Quantity = 0\n",
    "- Created summary tables with vendor-level metrics\n",
    "- Converted data types, handled outliers, merged lookup tables"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e4438bd9-d693-444b-b90c-403ca2f90680",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4641ea62-d8c9-42f5-b58e-b23f4d92067f",
   "metadata": {},
   "source": [
    "<h2><a class=\"anchor\" id=\"exploratory-data-analysis-eda\"></a>Exploratory Data Analysis (EDA)</h2>\n",
    "\n",
    "** Negative or Zero Values Detected :**\n",
    "- Gross Profit: Min -52,002.78 (loss-making sales)\n",
    "- Profit Margin: Min - (sales at zero or below cost)\n",
    "- Unsold Inventory: Indicating slow-moving stock\n",
    "\n",
    "** Outliers Identified :**\n",
    "- High Freight Costs (up to 257K)\n",
    "- Large Purchase/Actual Prices\n",
    "\n",
    "** Correlation Analysis :**\n",
    "- Weak between Purchase Price & Profit\n",
    "- Strong between Purchase Qty & Sales Qty (0.999)\n",
    "- Negative between Profit Margin & Sales Price (-0.179)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "52381c13-6037-4d04-838a-5f18fe57a4cd",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "15343766-5f25-4b58-8921-af3c96e717da",
   "metadata": {},
   "source": [
    "<h2><a class=\"anchor\" id=\"research-questions -- key-findings\"></a>Research Questions & Key Findings</h2>\n",
    "\n",
    "1. ** Brands for Promotions **: 198 brands with low sales but high profit margins\n",
    "2. ** Top Vendors **: Top 10 vendors = 65.69% of purchases risk of over-reliance\n",
    "3. ** Bulk Purchasing Impact **: 72% cost savings per unit in large orders\n",
    "4. ** Inventory Turnover **: $2.71M worth of unsold inventory\n",
    "5. ** Vendor Profitability **:\n",
    "- High Vendors: Mean Margin = 31.17%\n",
    "- Low Vendors: Mean Margin = 41.55%\n",
    "6. ** Hypothesis Testing **: Statistically significant difference in profit margins\n",
    "strategies"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "540be87c-4c3f-476e-9b31-fa482e3ff664",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b75cb437-b3a4-4c5c-87b2-99103b32fe3e",
   "metadata": {},
   "source": [
    "<h2><a class=\"anchor\" id=\"dashboard\"></a>Dashboard</h2>\n",
    "\n",
    "- Power BI Dashboard shows:\n",
    "- Vendor-wise Sales and Margins\n",
    "- Inventory Turnover\n",
    "- Bulk Purchase Savings\n",
    "- Performance Heatmaps\n",
    "\n",
    "! [Vendor Performance Dashboard] (images/dashboard.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e41f605e-27b7-494f-8b97-96e98d23a91f",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "75c90775-85e9-41fe-bcf5-15f26c0a2202",
   "metadata": {},
   "source": [
    "<h2><a class=\"anchor\" id=\"how-to-run-this-project\"></a>How to Run This Project</h2>\n",
    "\n",
    "1. Clone the repository:\n",
    "```bash\n",
    "git clone https://github.com/yourusername/vendor-performance-analysis.git\n",
    "```\n",
    "3. Load the CSVs and ingest into database:\n",
    "```bash\n",
    "python scripts/ingestion_db.py\n",
    "```\n",
    "4. Create vendor summary table:\n",
    "```bash\n",
    "python scripts/get_vendor_summary.py\n",
    "```\n",
    "\n",
    "5. Open and run notebooks:\n",
    "- 'notebooks/exploratory_data_analysis. ipynb'\n",
    "- 'notebooks/vendor_performance_analysis. ipynb\n",
    "6. Open Power BI Dashboard:\n",
    "- 'dashboard/vendor_performance_dashboard. pbix"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8d00ddf4-a6e2-4101-a660-936790f2e89b",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8066cd8b-ad99-483d-82f1-8ac9182862af",
   "metadata": {},
   "source": [
    "<h2><a class=\"anchor\" id=\"final-recommendations\"></a>Final Recommendations</h2>\n",
    "\n",
    "- Diversify vendor base to reduce risk\n",
    "- Optimize bulk order strategies\n",
    "- Reprice slow-maying, high-margin brands\n",
    "- Clear unsold inventory strategically\n",
    "- Improve marketing for underperforming vendors"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "704093d2-5e86-4356-8c20-a2e2d349c7b4",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f22f67f3-05e9-4604-909e-42c8e5b25286",
   "metadata": {},
   "source": [
    "<h2><a class=\"anchor\" id=\"author -- contact\"></a>Author & Contact</h2>\n",
    "\n",
    "** Lakshay Sharma **\n",
    "\n",
    "\n",
    "Data Analyst\n",
    "\n",
    "Email: Lakshaysharma406@gmail.com\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5bd87921-2e09-445d-98b1-01f368db5ef0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
