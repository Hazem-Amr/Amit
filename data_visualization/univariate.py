import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class UnivariateHandler:
    """Helper for univariate visualizations."""

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def plot_user_type_distribution(self):
        st.subheader("🧍 User Type Distribution")
        user_type = self.df['user_type'].value_counts().reindex(["Subscriber", "Customer"])

        fig, ax = plt.subplots(figsize=(8, 4))
        sns.barplot(x=user_type.index, y=user_type.values, palette=["#2aaaa4", "#C5B048"], ax=ax)
        ax.set_title("User Type Counts", fontweight='black')
        for i, v in enumerate(user_type.values):
            ax.text(i, v, v, ha='center', va='bottom')
        st.pyplot(fig)
        plt.close(fig)

        st.markdown("**Percentages**")
        st.write((user_type / user_type.sum() * 100).round(2))

    def plot_bike_share_distribution(self):
        st.subheader("🚲 Bike Share for All Trip Distribution")
        bs = self.df['bike_share_for_all_trip'].value_counts()

        fig, ax = plt.subplots(figsize=(8, 4))
        sns.barplot(x=bs.index, y=bs.values, palette=["#2aaaa4", "#C5B048"], ax=ax)
        ax.set_title("Bike share for all trip Counts", fontweight='black')
        st.pyplot(fig)
        plt.close(fig)

        st.markdown("**Percentages**")
        st.write((bs / bs.sum() * 100).round(2))

    def plot_age_distribution(self):
        CURRENT_YEAR = 2019
        self.df['member_age'] = CURRENT_YEAR - self.df['member_birth_year']
        st.subheader("🎂 User Age Distribution")
        fig, axs = plt.subplots(1, 2, figsize=(17, 6))
        sns.histplot(x='member_age', data=self.df, kde=True, ax=axs[0], color="#2aaaa4", binwidth=2)
        axs[0].set_title("users' distribution by age")
        sns.boxplot(x='member_age', data=self.df, ax=axs[1], color="#C5B048")
        axs[1].set_title("Age boxplot")
        st.pyplot(fig)
        plt.close(fig)

        outliers = self.df[self.df['member_age'] > 100].shape[0]
        st.write(f"Number of age outliers (>100): {outliers}")

    def plot_duration_min_distribution(self):
        self.df['duration_min'] = (self.df['duration_sec'] / 60).round(2)
        st.subheader("⏱ Trip Duration (minutes) Distribution")
        fig, axs = plt.subplots(1, 2, figsize=(17, 6))
        sns.histplot(x='duration_min', data=self.df, kde=True, ax=axs[0], color="#2aaaa4")
        axs[0].set_title("distribution for the trip duration in minutes")
        sns.boxplot(x='duration_min', data=self.df, ax=axs[1], color="#C5B048")
        axs[1].set_title("distribution for the trip duration in minutes")
        st.pyplot(fig)
        plt.close(fig)

    def plot_gender_distribution(self):
        st.subheader("👥 Member Gender Distribution")
        gender = self.df['member_gender'].value_counts().reindex(["Male", "Female"])

        fig, axs = plt.subplots(1, 2, figsize=(17, 6))
        sns.barplot(x=gender.index, y=gender.values, palette=["#2aaaa4", "#C5B048"], ax=axs[0])
        axs[0].set_title("Member Gender Counts", fontweight='black')
        for i, v in enumerate(gender.values):
            axs[0].text(i, v, v, ha='center', va='bottom')

        axs[1].pie(gender, labels=gender.index, autopct="%.2f%%", colors=["#2aaaa4", "#C5B048"], explode=[0, 0.1], startangle=90)
        center = plt.Circle((0, 0), 0.3, fc='white')
        axs[1].add_artist(center)
        axs[1].set_title("Member Gender Rate", fontweight='black')

        st.pyplot(fig)
        plt.close(fig)

    def plot_duration_hr_distribution(self):
        self.df['duration_hr'] = (self.df['duration_sec'] / 3600).round(2)
        st.subheader("⏱ Trip Duration (hours) Distribution")
        fig, axs = plt.subplots(1, 2, figsize=(17, 6))
        sns.histplot(x='duration_hr', data=self.df, kde=True, ax=axs[0], color="#2aaaa4")
        axs[0].set_title("distribution for the trip duration in hours")
        sns.boxplot(x='duration_hr', data=self.df, ax=axs[1], color="#C5B048")
        axs[1].set_title("distribution for the trip duration in hours")
        st.pyplot(fig)
        plt.close(fig)
