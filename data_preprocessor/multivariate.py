import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class MultivariateHandler:
    """
    A class to handle multivariate analysis and visualizations.
    """

    def __init__(self, df: pd.DataFrame):
        """
        Initializes the handler with a pandas DataFrame.

        Args:
            df (pd.DataFrame): The data to analyze.
        """
        self.df = df

    # Question 1: Correlation between ALL variables
    def plot_correlation_heatmap(self):
        st.subheader("🔢 Correlation Heatmap (All Numerical Variables)")
        numeric_df = self.df.select_dtypes(include=["number"])

        # If number of columns is less than 2 => Raise a Warning
        if numeric_df.shape[1] < 2:
            st.warning("Not enough numerical columns to compute correlation.")
            return

        corr_matrix = numeric_df.corr()

        fig, ax = plt.subplots(figsize=(12, 10))
        sns.heatmap(
            corr_matrix,
            annot=True,
            fmt=".2f",
            cmap="coolwarm",
            square=True,
            linewidths=0.5,
            ax=ax,
            cbar_kws={"shrink": 0.8},
        )
        ax.set_title("Correlation Matrix of All Numeric Features")
        st.pyplot(fig)
        plt.close(fig)

        # Show strongest correlations
        st.markdown("**Top 5 Strongest Correlations:**")
        # Get upper triangle of correlation matrix (excluding diagonal)
        upper_tri = corr_matrix.where(
            np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
        )
        # Stack and sort
        stacked = upper_tri.stack().reset_index()
        stacked.columns = ["Variable 1", "Variable 2", "Correlation"]
        stacked["Abs Correlation"] = stacked["Correlation"].abs()
        top_corr = stacked.nlargest(5, "Abs Correlation")[
            ["Variable 1", "Variable 2", "Correlation"]
        ]
        st.dataframe(top_corr)

    # Question 2: Correlation between SPECIFIC numeric variables
    def plot_specific_correlation(self):
        st.subheader("🔢 Correlation Between Selected Variables")
        numeric_df = self.df.select_dtypes(include=["number"])

        # If number of columns is less than 2 => Raise a Warning
        if numeric_df.shape[1] < 2:
            st.warning("Not enough numerical columns to compute correlation.")
            return

        # Select specific variables
        cols_to_analyze = st.multiselect(
            "Select 2 or more variables to analyze:",
            options=numeric_df.columns.tolist(),
            default=(
                numeric_df.columns[:2].tolist() if len(numeric_df.columns) >= 2 else []
            ),
        )

        # If number of columns is less than 2 => Raise a Warning
        if len(cols_to_analyze) < 2:
            st.warning("Please select at least 2 variables.")
            return

        # Correlation for selected columns
        selected_df = numeric_df[cols_to_analyze]
        corr_matrix = selected_df.corr()

        # Display correlation matrix
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(
            corr_matrix,
            annot=True,
            fmt=".3f",
            cmap="RdBu_r",
            square=True,
            linewidths=0.5,
            ax=ax,
            vmin=-1,
            vmax=1,
            cbar_kws={"shrink": 0.8, "label": "Correlation Coefficient"},
        )
        ax.set_title(
            f"Correlation Matrix: {', '.join(cols_to_analyze[:3])}"
            + ("..." if len(cols_to_analyze) > 3 else "")
        )
        st.pyplot(fig)
        plt.close(fig)

        # Show scatter plot for the two main variables
        if len(cols_to_analyze) == 2:
            st.subheader("Scatter Plot with Regression Line")
            fig2, ax2 = plt.subplots(figsize=(8, 6))
            sns.regplot(
                data=selected_df,
                x=cols_to_analyze[0],
                y=cols_to_analyze[1],
                scatter_kws={"alpha": 0.5},
                line_kws={"color": "red"},
            )
            ax2.set_title(f"{cols_to_analyze[0]} vs {cols_to_analyze[1]}")
            st.pyplot(fig2)
            plt.close(fig2)

    # Question 3: Correlation between data_stat variables
    def plot_data_stat_correlation(self):
        """
        Assumes 'data_stat' variables are those with 'stat' in the name or a predefined list
        """
        st.subheader("🔢 Correlation Between Data Statistics Variables")
        numeric_df = self.df.select_dtypes(include=["number"])

        # Define what "data_stat" variables mean - adjust based on your dataset
        stat_keywords = [
            "stat",
            "count",
            "mean",
            "std",
            "min",
            "max",
            "percentile",
            "sum",
            "avg",
        ]

        # Find columns that might be statistics-related
        stat_columns = []
        for col in numeric_df.columns:
            col_lower = col.lower()
            if any(keyword in col_lower for keyword in stat_keywords):
                stat_columns.append(col)

        # Alternative: Let user define which are statistics variables
        if len(stat_columns) < 2:
            st.info(
                "No clear 'data_stat' variables detected. Please select them manually:"
            )
            stat_columns = st.multiselect(
                "Select the statistics-related variables:",
                options=numeric_df.columns.tolist(),
                default=[],
            )

        # If number of columns is less than 2 => Raise a Warning
        if len(stat_columns) < 2:
            st.warning("Need at least 2 statistics variables for correlation analysis.")
            return

        # Compute correlation for statistics variables
        stat_df = numeric_df[stat_columns]
        corr_matrix = stat_df.corr()

        fig, ax = plt.subplots(figsize=(10, 8))

        mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

        sns.heatmap(
            corr_matrix,
            mask=mask,
            annot=True,
            fmt=".3f",
            cmap="viridis",
            square=True,
            linewidths=0.5,
            ax=ax,
            vmin=-1,
            vmax=1,
            cbar_kws={"shrink": 0.8, "label": "Correlation Coefficient"},
        )
        ax.set_title("Correlation Between Data Statistics Variables")
        st.pyplot(fig)
        plt.close(fig)

        st.markdown("**Summary of Statistics Variable Correlations:**")
        # Get the correlation values (excluding diagonal)
        corr_values = corr_matrix.where(
            ~np.eye(corr_matrix.shape[0], dtype=bool)
        ).stack()
        st.markdown(f"- **Strongest positive correlation:** {corr_values.max():.3f}")
        st.markdown(f"- **Strongest negative correlation:** {corr_values.min():.3f}")
        st.markdown(
            f"- **Average absolute correlation:** {corr_values.abs().mean():.3f}"
        )
