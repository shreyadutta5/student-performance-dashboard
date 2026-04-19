# Student Performance Data Analytics Dashboard

## 📌 Project Description
This project is an end-to-end data analytics pipeline that processes student performance data and visualizes insights through an interactive dashboard.

## 🚀 Features
- Data ingestion from CSV files
- Data cleaning and transformation using Python
- Database storage using SQLite
- SQL-based analysis
- Flask-based web application
- Interactive dashboard with charts and summary cards

## 🛠️ Technologies Used
- Python (Pandas, SQLite)
- SQL
- Flask
- HTML, CSS
- Chart.js

## 📊 Dashboard Insights
- Average Marks
- Highest Marks
- Total Students
- Average Marks per Student (Bar Chart)

## 📁 Project Structure
student-data-pipeline/
│
├── data/
├── scripts/
├── app/
├── sql/
└── README.md


## ▶️ How to Run
1. Run data processing:
   python scripts/clean_data.py

2. Load database:
   python scripts/load_db.py

3. Run web app:
   cd app
   python app.py

4. Open browser:
   http://127.0.0.1:5000/