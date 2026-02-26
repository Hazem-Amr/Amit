import streamlit as st
import pandas as pd

from data_preprocessor.datatypes import DataTypeHandler
from data_preprocessor.missing import MissingValuesHandler
from data_preprocessor.duplicates import DuplicateHandler
from data_preprocessor.outliers import OutlierHandler
from data_preprocessor.multivariate import MultivariateHandler

# -------------------------------------------------
# Streamlit Page Setup
# -------------------------------------------------

st.set_page_config(page_title="Data Preprocessing App", layout="wide")
st.title("🧹 Data Preprocessing Pipeline")

# -------------------------------------------------
# Upload Data
# -------------------------------------------------

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is None:
    st.info("Please upload a CSV file to begin.")
    st.stop()

# -------------------------------------------------
# Load Data into Session State
# -------------------------------------------------

if "df" not in st.session_state:
    st.session_state.df = pd.read_csv(uploaded_file)

df = st.session_state.df

st.success("Dataset loaded successfully!")

st.subheader("Dataset Preview")
st.dataframe(df.head())
st.write("Shape:", df.shape)

# -------------------------------------------------
# Choose Preprocessing Step
# -------------------------------------------------

st.subheader("Choose Preprocessing Step")

step = st.selectbox(
    "Select a step",
    [
        "Check Data Types",
        "Convert Data Type",
        "Handle Missing Values",
        "Handle Duplicates",
        "Handle Outliers",
        "Multivariate Analysis",
    ],
)

# -------------------------------------------------
# 1️⃣ Check Data Types
# -------------------------------------------------

if step == "Check Data Types":
    handler = DataTypeHandler(df)
    st.dataframe(handler.check_dtypes())

# -------------------------------------------------
# 2️⃣ Convert Data Type
# -------------------------------------------------

if step == "Convert Data Type":
    handler = DataTypeHandler(df)

    column = st.selectbox("Select column", df.columns)
    dtype = st.selectbox("Select new dtype", ["int", "float", "category", "datetime"])

    if st.button("Convert Data Type"):
        handler.convert_dtype(column, dtype)
        st.session_state.df = handler.df
        st.success("Data type converted successfully!")
        st.write(handler.df.dtypes)

# -------------------------------------------------
# 3️⃣ Handle Missing Values
# -------------------------------------------------

if step == "Handle Missing Values":
    handler = MissingValuesHandler(df)

    st.write("Missing values summary:")
    st.dataframe(handler.check_nulls())

    column = st.selectbox("Select column", df.columns)
    strategy = st.selectbox("Strategy", ["drop", "mean", "median", "mode"])

    if st.button("Apply Missing Value Strategy"):
        handler.handle_nulls(column, strategy)
        st.session_state.df = handler.df
        st.success("Missing values handled successfully!")
        st.dataframe(handler.df.head())

# -------------------------------------------------
# 4️⃣ Handle Duplicates
# -------------------------------------------------

if step == "Handle Duplicates":
    handler = DuplicateHandler(df)

    duplicate_count = handler.check_duplicates()
    st.write(f"Duplicate rows: {duplicate_count}")

    if duplicate_count > 0 and st.button("Remove Duplicates"):
        handler.remove_duplicates()
        st.session_state.df = handler.df
        st.success("Duplicates removed successfully!")
        st.write("New shape:", handler.df.shape)

if step == "Handle Duplicates":
    handler = DuplicateHandler(df)

    dup_count = handler.check_duplicates()
    st.write(f"Duplicate rows: {dup_count}")

    if dup_count > 0:
        if st.checkbox("Show duplicated rows"):
            st.dataframe(handler.show_duplicates())

        column = st.selectbox("Column to edit (duplicates only)", df.columns)
        old_val = st.text_input("Old value")
        new_val = st.text_input("New value (empty = NaN)")

        if st.button("Replace in duplicated rows"):
            if new_val == "":
                new_val = None
            handler.replace_in_duplicates(column, old_val, new_val)
            st.session_state.df = handler.df
            st.success("Duplicated rows updated")

        if st.button("Remove duplicated rows"):
            handler.remove_duplicates()
            st.session_state.df = handler.df
            st.success("Duplicated rows removed")

# -------------------------------------------------
# 5️⃣ Handle Outliers
# -------------------------------------------------

if step == "Handle Outliers":
    handler = OutlierHandler(df)

    numeric_columns = df.select_dtypes(include="number").columns

    if len(numeric_columns) == 0:
        st.warning("No numeric columns available.")
    else:
        column = st.selectbox("Select numeric column", numeric_columns)

        if st.button("Cap Outliers (IQR Method)"):
            handler.cap_iqr(column)
            st.session_state.df = handler.df
            st.success(f"Outliers capped for column '{column}'")
            st.dataframe(handler.df[[column]].describe())

# -------------------------------------------------
# 6️⃣ Replace Values
# -------------------------------------------------
if step == "Replace Values":
    st.subheader("Replace Values in Column")

    column = st.selectbox("Select column", df.columns)

    old_value = st.text_input("Value to replace")
    new_value = st.text_input("New value (leave empty for NaN)")

    if st.button("Replace"):
        if new_value == "":
            new_value = None

        df[column] = df[column].replace(old_value, new_value)
        st.session_state.df = df

        st.success("Values replaced successfully")
        st.dataframe(df.head())

# -------------------------------------------------
# 7️⃣ Univariate Analysis
# -------------------------------------------------

# -------------------------------------------------
# 8️⃣ Bivariate Analysis
# -------------------------------------------------

# -------------------------------------------------
# 9️⃣ Multivariate Analysis
# -------------------------------------------------

if step == "Multivariate Analysis":
    st.subheader("📊 Multivariate Analysis")

    handler = MultivariateHandler(df)

    plot_choice = st.radio(
        "Choose a visualization:",
        [
            "Correlation Heatmap (All Variables)",
            "Correlation Between Selected Variables",
            "Correlation Between Statistics Variables",
        ],
    )

    if plot_choice == "Correlation Heatmap (All Variables)":
        handler.plot_correlation_heatmap()

    elif plot_choice == "Correlation Between Selected Variables":
        handler.plot_specific_correlation()

    elif plot_choice == "Correlation Between Statistics Variables":
        handler.plot_data_stat_correlation()

# -------------------------------------------------
# Download Cleaned Dataset
# -------------------------------------------------

st.subheader("Download Cleaned Dataset")

csv = st.session_state.df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download CSV", data=csv, file_name="cleaned_dataset.csv", mime="text/csv"
)
