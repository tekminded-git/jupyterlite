# Python for Finance Analysts: Tutorial Overview

This 30-lesson curriculum introduces Python through a series of corporate finance examples. All exercises draw on the synthetic dataset produced by `content/python4finance/generate_ecommerce_dataset.py`, which creates orders, order items, and product tables for an e‑commerce business. In each lesson, concepts are paired with code instructions that reference this dataset.

01 - Introduction to Python:
- Overview of Python's role in corporate finance and analytics.
- Demonstrate simple scripts that print text and calculate basic metrics from the ecommerce dataset.
- Concepts: syntax basics, the Python interpreter, using Jupyter notebooks.
- Exercises and examples:
  1. Run the generator script to create the dataset.
  2. Load the resulting CSVs into Python and print the number of orders and products.

02 - Installing Python and Setting Up Your Environment:
- Guide learners through installing Python, Jupyter, and packages required for working with corporate data.
- Provide configuration instructions for virtual environments.
- Concepts: package managers (pip), virtualenv, navigating the command line.
- Exercises and examples:
  1. Create a new virtual environment and install pandas, matplotlib, and faker.
  2. Generate the ecommerce dataset inside the environment and verify the files were written.

03 - Data Types and Variables:
- Explain numeric, string, and boolean types using transaction amounts and product information.
- Examples include storing total sales and flags for high-value customers.
- Concepts: variable assignment, type conversion, best practices for naming variables.
- Exercises and examples:
  1. Calculate the total value of all orders from the dataset.
  2. Create a boolean variable that marks orders above a chosen threshold.

04 - Basic Arithmetic and Logical Operations:
- Perform revenue growth calculations and percent changes across months.
- Use comparisons to flag unusual purchase amounts.
- Concepts: arithmetic operators, comparison operators, boolean logic.
- Exercises and examples:
  1. Compute month‑over‑month revenue differences.
  2. Use logical operators to identify orders over a certain dollar amount and placed on a weekend.

05 - Working with Lists and Tuples:
- Store sequences of customer IDs or locations for further analysis.
- Index and slice lists to retrieve subsets of transactions.
- Concepts: mutability, iterating over lists, using tuples for fixed data like payment methods.
- Exercises and examples:
  1. Build a list of all unique customer locations from the orders table.
  2. Iterate over a slice of the list to display the first five locations.

06 - Dictionaries and Sets in Finance:
- Map product IDs to categories and use sets to deduplicate customer IDs.
- Create a simple lookup for product prices.
- Concepts: key-value pairs, set operations, dictionary methods.
- Exercises and examples:
  1. Construct a dictionary keyed by ProductID with base prices as values.
  2. Use a set to find the number of unique customers who placed orders.

07 - String Manipulation:
- Parse invoice numbers and format descriptions for reports.
- Examples include cleaning whitespace and constructing formatted output.
- Concepts: f-strings, common string methods, joining and splitting text.
- Exercises and examples:
  1. Format a string showing a customer's total spend with two decimal places.
  2. Split the PaymentMethod column to separate words and count occurrences.

08 - Working with Dates and Times:
- Handle order dates, calculate durations between orders, and group by month.
- Demonstrate time zone handling for online sales across regions.
- Concepts: `datetime` module, formatting dates, timedelta arithmetic.
- Exercises and examples:
  1. Convert the OrderDate column to datetime and extract the month.
  2. Compute the number of days since each customer's previous order.

09 - Control Flow: if, else, and loops:
- Automate decisions such as flagging risky transactions or generating alerts.
- Use loops to iterate through orders and summarize totals by location.
- Concepts: `if` statements, `for` and `while` loops, nested conditions.
- Exercises and examples:
  1. Loop through orders and print a warning for purchases over a limit.
  2. Create a summary dictionary that accumulates sales by payment method.

10 - Functions and Scope:
- Modularize recurring calculations like computing order discounts.
- Provide examples of reusable helper functions on the ecommerce dataset.
- Concepts: function definitions, parameters, return values, local vs global scope.
- Exercises and examples:
  1. Write a function that calculates a volume discount based on the number of items in an order.
  2. Use the function to apply discounts to all order items and compute the new totals.

11 - Object-Oriented Programming Basics:
- Introduce classes and objects for organizing corporate finance logic.
- Demonstrate a `Customer` class that stores orders and methods for total spend.
- Concepts: defining classes, instance vs class variables, methods, simple inheritance.
- Exercises and examples:
  1. Implement a `Product` class with attributes for ID, category, and base price.
  2. Create instances of the class from the products table and compute the average price by calling a method.

12 - Comprehensions and Lambda Functions:
- Use list comprehensions to transform datasets succinctly.
- Show lambda expressions for quick calculations on order items.
- Concepts: list, dict, and set comprehensions; anonymous functions.
- Exercises and examples:
  1. Build a list of all purchase amounts using a list comprehension.
  2. Use a lambda with `apply` to categorize orders as small or large purchases.

13 - Error Handling and Debugging:
- Explain common pitfalls when processing financial data and how to catch them.
- Include try/except blocks around file loading and calculations.
- Concepts: exceptions, debugging with print statements or IDE tools.
- Exercises and examples:
  1. Attempt to load a missing file and handle the resulting exception gracefully.
  2. Use assertions to validate that no purchase amounts are negative.

14 - Introduction to NumPy:
- Store large numeric arrays of sales quantities and perform vectorized math.
- Examples include computing log growth rates across many months.
- Concepts: creating arrays, broadcasting, array methods.
- Exercises and examples:
  1. Convert the purchase amounts to a NumPy array and calculate descriptive statistics.
  2. Demonstrate broadcasting by applying a tax rate to all purchase amounts.

15 - Pandas Basics:
- Introduce DataFrames for handling the ecommerce orders, items, and products tables.
- Examples cover loading the generated dataset and exploring columns.
- Concepts: Series and DataFrame, indexing, merging tables, basic data wrangling.
- Exercises and examples:
  1. Merge orders with order items to create a single analysis DataFrame.
  2. Select orders from a specific location and compute the total revenue for that location.

16 - Data Cleaning:
- Handle missing values and inconsistent formats in the ecommerce data.
- Use techniques such as filling gaps and removing outliers.
- Concepts: detecting NaNs, filtering data, using `pandas` cleaning methods.
- Exercises and examples:
  1. Identify orders with missing customer locations and fill them with "Unknown".
  2. Remove outlier purchase amounts using the interquartile range method.

17 - Data Visualization with Matplotlib and Seaborn:
- Plot revenue trends, product category breakdowns, and customer distribution.
- Provide tips for customizing visuals for board presentations.
- Concepts: line and bar charts, histograms, style settings, legends, and labels.
- Exercises and examples:
  1. Create a monthly revenue line chart from the orders table.
  2. Plot a bar chart showing the number of orders by payment method using Seaborn.

18 - Working with External Data (CSV, Excel, Databases):
- Import supplemental corporate data such as budgets or HR costs.
- Demonstrate reading from and writing to CSV and Excel files alongside the ecommerce dataset.
- Concepts: `pandas.read_csv`, Excel helpers, and basic database connectors like SQLite.
- Exercises and examples:
  1. Save aggregated revenue by product category to an Excel file.
  2. Load a separate CSV of marketing spend and merge it with order totals.

19 - Time Series Analysis:
- Resample daily sales data to monthly and analyze seasonality.
- Calculate rolling averages to smooth revenue trends.
- Concepts: DateTime index, resample, rolling window operations.
- Exercises and examples:
  1. Resample the order data by month and compute average order value.
  2. Plot a 30‑day rolling mean of daily sales to visualize trends.

20 - Corporate Financial Metrics:
- Compute metrics such as gross margin, contribution margin, and cash conversion cycle.
- Use the ecommerce dataset to illustrate each calculation.
- Concepts: revenue, cost of goods sold, receivables and payables timing.
- Exercises and examples:
  1. Estimate gross margin by subtracting base price from purchase amounts.
  2. Derive days sales outstanding using simulated payment dates.

21 - Capital Allocation Optimization:
- Introduce optimization methods for budgeting and resource allocation.
- Provide a small example using `scipy.optimize` to allocate marketing spend across channels.
- Concepts: objective functions, constraints, interpreting optimization results.
- Exercises and examples:
  1. Define a cost function that maximizes projected revenue for different budget allocations.
  2. Use `scipy.optimize.minimize` to find the best allocation under a fixed budget.

22 - Scenario Analysis and Forecasting:
- Walk through creating scenarios for revenue forecasts based on varying assumptions.
- Show how to evaluate outcomes using simple loops and data transformations.
- Concepts: scenario generation, sensitivity testing, summary statistics.
- Exercises and examples:
  1. Create optimistic, base, and pessimistic growth scenarios for monthly revenue.
  2. Compute the effect on annual revenue under each scenario.

23 - Monte Carlo Simulation:
- Demonstrate simulating sales outcomes to model uncertainty.
- Include examples for cash-flow forecasting and risk analysis.
- Concepts: random number generation, repeated simulations, analyzing distributions.
- Exercises and examples:
  1. Simulate thousands of revenue paths assuming random monthly growth rates.
  2. Plot the distribution of simulated yearly revenue totals.

24 - Regression Analysis with Statsmodels and Scikit-Learn:
- Apply linear regression to model relationships like advertising spend versus sales.
- Provide examples predicting revenue from marketing and seasonal variables.
- Concepts: fitting models, interpreting coefficients, train/test split.
- Exercises and examples:
  1. Fit a linear model using product category dummy variables to predict purchase amounts.
  2. Evaluate the model using out-of-sample test data.

25 - Web Scraping and Data APIs:
- Pull supplemental economic data or competitor pricing information.
- Show basic HTML parsing and API requests.
- Concepts: requests library, BeautifulSoup, ethical scraping considerations.
- Exercises and examples:
  1. Retrieve currency exchange rates from a public API and merge them with the orders data.
  2. Scrape product prices from a sample website and compare them to internal pricing.

26 - Automating Reports with Python:
- Generate PDF or HTML reports summarizing revenue and key metrics.
- Examples include scheduling weekly report generation.
- Concepts: templating with Jinja2, report generation libraries, cron basics.
- Exercises and examples:
  1. Create an HTML report that includes charts generated in earlier lessons.
  2. Schedule the report script to run automatically using a cron job.

27 - Using Python for Excel:
- Automate Excel tasks common in corporate workflows.
- Examples use openpyxl or xlsxwriter to update management spreadsheets.
- Concepts: cell manipulation, formulas, formatting spreadsheets.
- Exercises and examples:
  1. Write the monthly revenue summary to an Excel workbook with formatting.
  2. Insert a chart object showing product category sales into a worksheet.

28 - Risk Management and Sensitivity Testing:
- Teach methods to quantify financial risk and potential losses in a corporate context.
- Provide examples calculating value at risk on projected sales.
- Concepts: distribution assumptions, confidence intervals, stress testing.
- Exercises and examples:
  1. Use historical revenue volatility to estimate value at risk.
  2. Stress test a sharp drop in demand and quantify the revenue impact.

29 - Building a Corporate Dashboard with Plotly or Dash:
- Show how interactive dashboards visualize KPIs in real time.
- Include examples deploying locally for stakeholders.
- Concepts: Plotly basics, Dash layouts, callbacks for interactivity.
- Exercises and examples:
  1. Create an interactive dashboard showing revenue by region and payment method.
  2. Add filters that allow users to view metrics for selected product categories.

30 - Machine Learning Applications in Corporate Finance:
- Explore classification and clustering for customer segmentation or anomaly detection.
- Provide examples using scikit-learn pipelines on the ecommerce dataset.
- Concepts: feature engineering, model evaluation, considerations for overfitting.
- Exercises and examples:
  1. Cluster customers based on order history to identify high-value segments.
  2. Train a classification model to flag potentially fraudulent orders.
