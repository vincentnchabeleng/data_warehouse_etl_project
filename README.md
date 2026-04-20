# Data Warehouse ETL Project

## 📌 Project Overview

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline built using Python and SQLite.
The system reads raw data from a CSV file, transforms it, loads it into a database, and displays metadata such as tables and columns.

This project was created to practice data warehousing concepts such as ETL processes, database structures, and metadata tracking.

---

## ⚙️ Technologies Used

* Python
* Pandas
* SQLite
* SQL

---

## 🔄 ETL Process Explained

### 1. Extract

* Data is read from a CSV file (`sales.csv`)

### 2. Transform

* A new column (`total`) is created using calculations
* Data is cleaned and structured

### 3. Load

* Data is saved into a SQLite database (`warehouse.db`)
* Stored in a table called `sales_table`

---

## 📊 Metadata Tracking

The project also retrieves metadata from the database, including:

* Table names
* Column names and data types
* Indexes created for performance

---

## ▶️ How to Run the Project ##

### Step 1: Install requirements 

Run this command:
pip install pandas

### Step 2: Run the script

python main.py

---

## 📁 Project Structure

* `sales.csv` → Raw data
* `main.py` → Main ETL script
* `warehouse.db` → Database file

---

## 💡 Key Features

* Simple ETL pipeline
* Data transformation with Python
* Database storage using SQLite
* Metadata extraction
* Index creation for performance

---

## 🚀 Future Improvements

* Use SQL Server instead of SQLite
* Add SSIS integration
* Build a dashboard for data visualization
* Automate ETL scheduling

---

## 👤 Author

Vincent Nchabeleng
BSc Mathematical Sciences | Aspiring Data Engineer / Software Engineer
