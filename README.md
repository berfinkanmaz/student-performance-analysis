# student-performance-analysis
Student performance data analysis and visualization dashboard built with Python and Streamlit

# Excel Student Performance Measurement Data Summarization Automation

## Overview
This project is a Streamlit-based web application designed to analyze and summarize student performance data from an Excel file (`StudentsPerformance.xlsx`). It provides insights into student performance across various dimensions such as gender, race/ethnicity, test preparation course, parental education, and socioeconomic status (via lunch program). The application generates detailed analyses, visualizes the results with charts, and allows users to download a comprehensive report in Excel format.

## Features
- **Interactive Dashboard:** Select different analyses via a dropdown menu.
- **Data Analysis:** Summarizes student performance metrics across multiple dimensions.
- **Visualizations:** Displays results with bar charts, line charts, stacked bar charts, and interactive Altair charts.
- **Downloadable Report:** Exports all analysis results into a single Excel file with separate sheets for each analysis.

## Installation
To run this project locally, follow these steps:

1. **Clone the repository or download the project files.**
   - If you have Git installed, you can clone the repository:
     ```
     git clone <repository-url>
     ```
   - Otherwise, download the project files and extract them to a folder (e.g., `excel-automation`).

2. **Set up a virtual environment (optional but recommended):**
   - Navigate to the project folder:
     ```
     cd excel-automation
     ```
   - Create a virtual environment:
     ```
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```
       source venv/bin/activate
       ```

3. **Install the required dependencies:**
   - Ensure you have `pip` installed. Then run:
     ```
     pip install -r requirements.txt
     ```
   - If `requirements.txt` is not available, install the following packages manually:
     ```
     pip install streamlit pandas matplotlib xlsxwriter altair
     ```

4. **Run the application:**
   - Start the Streamlit app:
     ```
     streamlit run app.py
     ```
   - Open your browser and go to `http://localhost:8501` to view the application.

## Usage
1. Open the application in your browser.
2. Use the dropdown menu to select an analysis (e.g., "Gender-Based Performance Analysis").
3. View the analysis results as tables and charts.
4. Click the "Download Analysis Report" button to download all results as an Excel file (`student_performance_report.xlsx`).

## Project Structure
- `app.py`: The main Streamlit application file that runs the dashboard.
- `main.py`: Contains the core logic for data analysis.
- `StudentsPerformance.xlsx`: The dataset used for analysis (ensure this file is in the project folder).
- `requirements.txt`: Lists the required Python packages.
- `README.md`: This file, containing project documentation.
- `screenshots/`: Folder containing screenshots of the application.

## Visuals
Below are some screenshots of the application:

### Dashboard Overview
![Dashboard Overview](screenshots/dashboard_overview.png)

### Gender-Based Performance Analysis with Interactive Altair Chart
![Gender-Based Performance](screenshots/gender_performance.png)

### Test Preparation Course Impact with Line Chart
![Test Preparation Course Impact](screenshots/test_prep_impact.png)

## Requirements
The following Python packages are available in the Requirements file to run the project

You can install them using the command mentioned in the Installation section.

## Future Improvements
- Add file upload functionality to allow users to upload their own Excel files.
- Enhance the report with more formatting (e.g., colored headers, bold text).
- Include charts in the downloadable report as images.

## License
This project is licensed under the MIT License.

## Contact
For any questions or suggestions, feel free to reach out at [your-email@example.com].
