# Data Preprocessing Pipeline (Python)

A reusable and modular **data preprocessing framework** built with **Python**, **Pandas**, and **Streamlit**.

This project is designed to automate common data cleaning tasks for datasets that are updated regularly (e.g. monthly data), while keeping preprocessing logic reusable and independent from the user interface.

---

## Features

- Inspect and filter column data types
- Convert column data types dynamically
- Analyze and handle missing values
- Detect, display, edit, and remove duplicate rows
- Handle outliers using the IQR method
- Centralized preprocessing pipeline
- Interactive Streamlit interface
- Download cleaned datasets

---

## Project Structure

```text
AMIT/
├── data_preprocessor/
│   ├── __init__.py
│   ├── datatypes.py        # DataTypeHandler
│   ├── missing.py          # MissingValuesHandler
│   ├── duplicates.py       # DuplicateHandler
│   ├── outliers.py         # OutlierHandler
│   └── pipeline.py         # PreprocessingPipeline
│
├── data/                   # Raw datasets
├── main.py                 # Streamlit application
├── README.md
├── .gitignore
└── .env/                   # Virtual environment
```
---

## Core Classes

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

## Setup and Run the App

1. **Create a virtual environment:**
```bash
python -m venv .env
```

2. **Activate the environment:**
- On Windows:
```bash
.\.env\Scripts\activate
```
- On macOS/Linux:
```bash
source .env/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the Streamlit app:**
```bash
streamlit run main.py