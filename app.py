import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import main as m
import io

st.title("Excel Student Performance Measurement Data Summarization Automation")
st.write("""
### Student Performance Analytics Dashboard

This interactive dashboard provides comprehensive analysis of student performance metrics across multiple dimensions. The system automatically processes and visualizes key educational indicators to help educators and administrators identify patterns, disparities, and opportunities for improvement.

**Key Features:**
- Demographic performance analysis by gender, race/ethnicity, and socioeconomic factors
- Comparative assessment of test preparation course effectiveness
- Parental education level impact evaluation
- Identification of high and low performing students
- Multi-dimensional score aggregation and ranking

All analyses are generated automatically from the source dataset, ensuring consistent, data-driven insights. The dashboard presents both granular data points and summary statistics to support evidence-based decision making in educational programs.
"""
)

data = m.df

def plot_bar_chart(df, title, xlabel, ylabel):
    df.plot(kind="bar", figsize=(8, 6))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()

def plot_stacked_bar_chart(df, title, xlabel, ylabel):
    df.plot(kind="bar", stacked=True, figsize=(8, 6))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()

def plot_line_chart(df, title, xlabel, ylabel):
    df.plot(kind="line", marker="o", figsize=(8, 6))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()

def clean_sheet_name(name):
    # remove special characters
    invalid_chars = '[]:*?/\\'
    for char in invalid_chars:
        name = name.replace(char, '')
    # max 31 character
    return name[:31]


def create_report(data_dict):
    output = io.BytesIO()
    try:
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            for key, value in data_dict.items():
                sheet_name = clean_sheet_name(key)  # clear tab name
                if isinstance(value, dict):
                    for sub_key, sub_value in value.items():
                        sub_sheet_name = clean_sheet_name(f"{sheet_name}_{sub_key}")  # Clear alt tab name too
                        if isinstance(sub_value, pd.Series):
                            sub_value = sub_value.to_frame()
                        sub_value.to_excel(writer, sheet_name=sub_sheet_name)
                else:
                    value.to_excel(writer, sheet_name=sheet_name)
        excel_data = output.getvalue()
        return excel_data
    except Exception as e:
        st.error(f"Rapor oluştururken hata oluştu: {str(e)}")
        return None

# options
option = st.selectbox(
    "What analysis do you see?",
    [
        "Raw Performance Data", 
        "Summary Statistics", 
        "Gender-Based Performance Analysis", 
        "Test Preparation Course Impact Analysis", 
        "Parental Education Correlation Study", 
        "Top and Bottom Performing Students",
        "Overall Performance Ranking",
        "Racial/Ethnic Group Performance Metrics",
        "Socioeconomic Status Analysis (Lunch Program)"
    ]
)

# A dictionary that links each option to data
data_dict = {
    "Raw Performance Data": data,
    "Summary Statistics": data.describe(),
    "Gender-Based Performance Analysis": m.gender_average,
    "Test Preparation Course Impact Analysis": m.prep_course_effect,
    "Parental Education Correlation Study": m.performance_by_parent_education_level,
    "Top and Bottom Performing Students": {
        "Highest Scoring Students": m.max_average,
        "Lowest Scoring Students": m.min_average,
    },
    "Overall Performance Ranking": m.overall_sorted,
    "Racial/Ethnic Group Performance Metrics": m.race_ethnicity_average,
    "Socioeconomic Status Analysis (Lunch Program)": m.lunch_average
}

# Generate report and add download button
excel_data = create_report(data_dict)
if excel_data:
    st.download_button(
        label="Download Analysis Report",
        data=excel_data,
        file_name="student_performance_report.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
else:
    st.warning("Rapor oluşturulamadı, lütfen hata mesajını kontrol edin.")

# Show selected data
st.write(f"### {option}")

#If the selected item contains two sets of data (e.g. 'Top and Bottom Performing Students') treat it specially.
if isinstance(data_dict[option], dict):
    for title, df in data_dict[option].items():
        st.write(f"#### {title}")
        st.write(df)
else:
    st.write(data_dict[option])
    if option == "Gender-Based Performance Analysis":
        plot_bar_chart(data_dict[option], "Gender-Based Performance", "Gender", "Scores")
    elif option == "Socioeconomic Status Analysis (Lunch Program)":
        plot_bar_chart(data_dict[option], "Socioeconomic Status (Lunch Program)", "Lunch Type", "Scores")
    elif option == "Test Preparation Course Impact Analysis":
        plot_line_chart(data_dict[option], "Test Preparation Course Impact", "Course Status", "Scores")
    elif option == "Racial/Ethnic Group Performance Metrics":
        plot_stacked_bar_chart(data_dict[option], "Racial/Ethnic Group Performance", "Race/Ethnicity", "Scores")