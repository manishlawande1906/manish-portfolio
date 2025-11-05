import streamlit as st

# --- Main Page ---
st.set_page_config(page_title="Manish Lavande | Portfolio", layout="wide")

st.title("👋 Hi, I'm Manish Lavande")
st.write("### Data Analyst | Data Engineer | Machine Learning Enthusiast")
st.write("Welcome to my portfolio! Here you can explore my projects, dashboards, and technical skills.")

# --- About Section ---
st.header("About Me")
st.write("""
I'm passionate about data — turning raw information into meaningful insights.
With experience in Excel, Power BI, SQL, and Python, I'm now expanding my skills in data engineering and machine learning.
""")

# --- Skills ---
st.header("Skills")
st.write("""
- **Languages:** Python, SQL  
- **Tools:** Power BI, Excel, Git, Streamlit  
- **Platforms:** Azure, Snowflake, Databricks  
- **Areas:** Data Cleaning, Visualization, ETL, Machine Learning
""")

# --- Projects ---
st.header("Projects")
st.write("### 🧮 Loan Approval Prediction App")
st.write("A machine learning model built using Streamlit and deployed on Streamlit Cloud.")

st.write("### 📊 Power BI Sales Dashboard")
st.write("Interactive visualization showing regional performance and KPIs.")

st.write("### ⚙️ Data Engineering Pipeline")
st.write("Built an ETL pipeline using Azure Data Factory, Synapse, and Databricks.")

# --- Contact Section ---
st.header("Contact Me")
st.write("""
📧 Email: [your.email@example.com](mailto:your.email@example.com)  
🔗 LinkedIn: [linkedin.com/in/manishlavande](https://linkedin.com/in/manishlavande)  
💻 GitHub: [github.com/manishlawande1906](https://github.com/manishlawande1906)
""")
