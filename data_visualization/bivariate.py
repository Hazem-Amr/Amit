import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class BivariateHandler:
    """Helper for bivariate visualizations."""

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def avg_duration_by_user_type(self):
        self.df['duration_min'] = (self.df['duration_sec'] / 60).round(2)
        st.subheader("⏳ Average Trip Duration by User Type")
        avg_duration = self.df.groupby('user_type')['duration_min'].mean().reset_index()
        avg_duration.columns = ['user_type', 'avg_duration_min']
        avg_duration = avg_duration.sort_values('avg_duration_min', ascending=False)

        fig, ax = plt.subplots(figsize=(8, 4))
        sns.barplot(x='user_type', y='avg_duration_min', data=avg_duration,
                    palette=['#2aaaa4', '#C5B048'], ax=ax)
        ax.set_title('Average Trip Duration (min) by User Type', fontweight='black')
        ax.set_xlabel('User Type')
        ax.set_ylabel('Avg Duration (min)')
        for i, row in avg_duration.reset_index(drop=True).iterrows():
            ax.text(i, row['avg_duration_min'] + 0.3,
                    f"{row['avg_duration_min']:.2f}", ha='center')
        st.pyplot(fig)
        plt.close(fig)

        grouped = self.df.groupby('user_type')['duration_min'].agg(['mean', 'median', 'std']).round(2)
        st.markdown("**Duration statistics:**")
        st.dataframe(grouped)

    def duration_by_gender(self):
        st.subheader("🚻 Trip Duration by Gender")
        p99 = self.df['duration_min'].quantile(0.99)
        df_capped = self.df[self.df['duration_min'] <= p99].copy()

        fig, axs = plt.subplots(1, 2, figsize=(17, 6))
        sns.violinplot(x='member_gender', y='duration_min', data=df_capped,
                       palette=['#2aaaa4', '#C5B048'], inner='quartile', order=['Male','Female'], ax=axs[0])
        axs[0].set_title('Trip Duration (min) Distribution by Gender')
        sns.boxplot(x='member_gender', y='duration_min', data=df_capped,
                    palette=['#2aaaa4', '#C5B048'], order=['Male','Female'], ax=axs[1])
        axs[1].set_title('Trip Duration (min) Box Plot by Gender')
        st.pyplot(fig)
        plt.close(fig)

        st.markdown("**Summary stats:**")
        st.write(self.df.groupby('member_gender')['duration_min'].agg(['mean','median','std']).round(2))

    def duration_by_user_type(self):
        self.df['duration_min'] = (self.df['duration_sec'] / 60).round(2)
        st.subheader("🚻 Trip Duration by User Type")
        p99 = self.df['duration_min'].quantile(0.99)
        df_capped = self.df[self.df['duration_min'] <= p99].copy()

        fig, axs = plt.subplots(1, 2, figsize=(17, 6))
        sns.violinplot(x='user_type', y='duration_min', data=df_capped,
                       palette=['#2aaaa4', '#C5B048'], inner='quartile', order=['Subscriber','Customer'], ax=axs[0])
        axs[0].set_title('Trip Duration (min) Distribution by User Type')
        sns.boxplot(x='user_type', y='duration_min', data=df_capped,
                    palette=['#2aaaa4', '#C5B048'], order=['Subscriber','Customer'], ax=axs[1])
        axs[1].set_title('Trip Duration (min) Box Plot by User Type')
        st.pyplot(fig)
        plt.close(fig)

        st.markdown("**Summary stats:**")
        st.write(self.df.groupby('user_type')['duration_min'].agg(['mean','median','std']).round(2))

    def age_by_user_type(self):
        CURRENT_YEAR = 2019
        self.df['member_age'] = CURRENT_YEAR - self.df['member_birth_year']
        st.subheader("👥 Age Distribution by User Type")
        fig, axs = plt.subplots(1, 2, figsize=(17, 6))
        for utype, color in zip(['Subscriber','Customer'], ['#2aaaa4','#C5B048']):
            subset = self.df[self.df['user_type']==utype]['member_age'].dropna()
            sns.histplot(subset, kde=True, color=color, label=utype, alpha=0.6, binwidth=2, ax=axs[0])
        axs[0].legend()
        axs[0].set_title('Age Distribution by User Type')
        axs[0].set_xlabel('Age')
        axs[0].set_ylabel('Count')

        sns.boxplot(x='user_type', y='member_age', data=self.df,
                    palette=['#2aaaa4','#C5B048'], order=['Subscriber','Customer'], ax=axs[1])
        axs[1].set_title('Age Box Plot by User Type')
        axs[1].set_xlabel('User Type')
        axs[1].set_ylabel('Age')

        st.pyplot(fig)
        plt.close(fig)

        st.markdown("**Summary stats:**")
        st.write(self.df.groupby('user_type')['member_age'].agg(['mean','median','std']).round(2))

    def age_by_gender(self):
        CURRENT_YEAR = 2019
        self.df['member_age'] = CURRENT_YEAR - self.df['member_birth_year']
        st.subheader("👥 Age Distribution by Gender")
        fig, axs = plt.subplots(1, 2, figsize=(17, 6))
        for gender, color in zip(['Male','Female'], ['#2aaaa4','#C5B048']):
            subset = self.df[self.df['member_gender']==gender]['member_age'].dropna()
            sns.histplot(subset, kde=True, color=color, label=gender, alpha=0.6, binwidth=2, ax=axs[0])
        axs[0].legend()
        axs[0].set_title('Age Distribution by Gender')
        axs[0].set_xlabel('Age')
        axs[0].set_ylabel('Count')

        sns.boxplot(x='member_gender', y='member_age', data=self.df,
                    palette=['#2aaaa4','#C5B048'], order=['Male','Female'], ax=axs[1])
        axs[1].set_title('Age Box Plot by Gender')
        axs[1].set_xlabel('Gender')
        axs[1].set_ylabel('Age')

        st.pyplot(fig)
        plt.close(fig)

        st.markdown("**Summary stats:**")
        st.write(self.df.groupby('member_gender')['member_age'].agg(['mean','median','std']).round(2))
