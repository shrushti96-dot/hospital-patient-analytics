# Healthcare Data Analytics – Mini Project (Data Engineering)

This repository contains my mini project for **Assignment 1.1 (Unit 1: Experiential Learning & Case Study)** of the **Data Engineering** course.  
It demonstrates the **data lifecycle** (Capture → Store → Clean → Analyze → Visualize) using a healthcare admissions dataset.  

---

## Repository Contents
- **Documentation (PDF)** → Assignment report (Q1: Research, Q2: Case Study, Conclusion).  
- **Dataset (CSV)** → `healthcare_dataset_1000.csv` (raw data) and `cleaned_healthcare_dataset.csv`.  
- **Python Scripts** → Data cleaning and analysis (`src/analyze.py`).  
- **Outputs** → Visualizations, cleaned dataset, and summary CSVs (`outputs/`).  

---
## Student Information
- **Name**: Shrushti Sambhaji Shinde
- **Enrollment No**: ADT23SOCB1090
- **Roll No**: 48
- **Division**: AIEC-1
- **Course**: Data Engineering
  
----

## Dataset Information
- **File:** `healthcare_dataset_1000.csv`  
- **Records:** 1000+ patients  
- **Fields:**  
  - PatientID  
  - Age  
  - Gender  
  - Disease  
  - AdmissionDate  
  - DischargeDate  
  - TreatmentCost  
  - Outcome  

---

## Data Lifecycle (Steps Followed)
1. **Capture** → Patient admission data collected in CSV format.  
2. **Store** → Dataset stored as CSV, similar to how hospitals use databases/EHR systems.  
3. **Clean** → Missing values filled (Age → median, Gender → Unknown, Disease → Not Specified, TreatmentCost → average), duplicates removed.  
4. **Analyze** → Identified most common diseases, treatment cost distribution, age groups, and gender ratio.  
5. **Visualize** → Imported into **Power BI** and created interactive charts:  
   - Bar Chart → Disease frequency  
   - Column Chart → Average treatment cost by disease  
   - Pie Chart → Gender distribution  
   - Histogram → Age distribution  
   - Line Chart → Monthly admissions trend  

---

## 🛠 Tools & Technologies
- **Python** → Pandas, Matplotlib, Seaborn (for preprocessing and basic charts)  
- **Power BI** → Final visualization dashboards  
- **GitHub** → Version control and project sharing  

---

## Key Insights
- Flu and Diabetes were the most common diseases.  
- Cardiac cases had the highest treatment costs.  
- Majority of patients were between 40–60 years.  
- Slightly more male patients than female.  
- Admissions peaked in February and June (seasonal trend).  

---

## Conclusion
This project highlights how raw hospital admission data can be converted into **actionable insights** using data engineering techniques. Hospitals can use such analysis for better **resource planning, budgeting, and improving patient care**.  

---

## Project Link
*(https://github.com/shrushti96-dot/hospital-patient-analytics)*  
