# elevate-labs-internship
## 🧼 Data Cleaning: Marketing Campaign Dataset

### Objective:
To clean and prepare a raw marketing campaign dataset by removing inconsistencies and preparing it for analysis or modeling.

### Tools Used:
- Python 🐍
- Pandas 📊
- Excel (initial source)

### Cleaning Steps Performed:
1. **Removed Duplicates**  
   Ensured that no repeated rows existed.

2. **Handled Missing Values**  
   Dropped rows with missing income values (24 rows affected).

3. **Standardized Text Columns**  
   Cleaned and formatted the `Education` and `Marital_Status` columns for consistency.

4. **Converted Dates**  
   Converted `Dt_Customer` to a uniform `datetime` format (`YYYY-MM-DD`).

5. **Renamed Columns**  
   All column names were made lowercase and spaces replaced with underscores.

6. **Fixed Data Types**  
   `Income` was cast to `int` and all types were validated.

7. **Exported Cleaned Dataset**  
   Saved the cleaned dataset as `cleaned_marketing_campaign.xlsx`.

### Result:
The dataset is now clean, consistent, and ready for use in data analysis or machine learning projects.
