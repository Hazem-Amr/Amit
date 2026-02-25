# 🧹 Data Preprocessing Pipeline (Python + Streamlit)

A reusable and interactive data preprocessing framework built with **Python**, **Pandas**, and **Streamlit**.

This project is designed to automate common preprocessing tasks for datasets that are updated regularly (e.g. monthly data).

---

## 🚀 Features

- ✅ Data type inspection & conversion
- ✅ Missing value analysis and handling
- ✅ Duplicate detection, visualization, and removal
- ✅ Outlier handling using IQR method
- ✅ Value replacement in any column
- ✅ Interactive Streamlit UI
- ✅ Download cleaned dataset

---

## 📂 Project Structure
AMIT/
│
├── data_preprocessor/
│   ├── __init__.py
│   ├── datatypes.py
│   ├── missing.py
│   ├── duplicates.py
│   ├── outliers.py
│   ├── pipeline.py
│
├── data/
├── main.py        # Streamlit app
├── README.md
├── .gitignore
└── .env/


---

## 🧠 Core Classes

### `DataTypeHandler`
- Check data types
- Filter columns by dtype
- Convert column data types

### `MissingValuesHandler`
- Null count & percentage
- Fill using mean / median / mode
- Drop missing values

### `DuplicateHandler`
- Count duplicates
- Show duplicated rows
- Edit duplicated values
- Remove duplicates

### `OutlierHandler`
- IQR-based outlier capping

### `PreprocessingPipeline`
- Central access to all handlers

---

## ▶️ Run the App

Activate environment:
```bash
.\.env\Scripts\activate

streamlit run main.py