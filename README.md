Odoo Sales Report -
This project analyzes sales and invoice data from Odoo ERP using Python, SQLite, and Jupyter Notebooks.
Data is extracted directly from Google BigQuery and explored to generate insights for business reporting and analysis.

It helps answer key business questions like:
- Which products are generating the most revenue?
- Which partners (customers) contribute the most to sales?
- What are the payment trends and outstanding balances?
- How does sales performance vary over time?

📁 Files Included
- odoo.db → SQLite database created from the raw CSV file
- ingestion.py → Python script to load data into SQLite
- log.log → Log file to track the ingestion/debugging process
- crmanalysis.ipynb → Notebook for data exploration and cleaning
- report.qmd → Final report in notebook format
- report.html → HTML version of final report (rendered using Quarto)

🛠 Tools Used
- Python (Pandas, SQLite3, Matplotlib)
- Google BigQuery (for extracting raw Odoo data)
- Jupyter Notebook (for EDA and reporting)
- Quarto (for generating shareable reports)
- Git (version control)
- VS Code (development environment)
