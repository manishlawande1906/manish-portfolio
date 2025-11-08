import streamlit as st

# --- Main Page ---
st.set_page_config(page_title="Manish Lawande | Portfolio", layout="wide")

st.title("👋 Hi, I'm Manish Lawande")
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

# --- Projects --

st.subheader("📊 Mobile Sales Performance Dashboard")

st.markdown("""
#### 📝 Project Overview  
An interactive Power BI dashboard designed to analyze mobile sales across India.
It provides a complete view of sales performance using key KPIs such as Total Sales, Quantity, Average Price, and Transactions. The report includes:

Year-over-Year (YoY) and Month-to-Date (MTD) sales comparisons.
City-wise and Brand-wise performance visualization.
Insights on Payment Methods, Ratings, and customer feedback trends.
Dynamic filters for Model, Brand, Year, and Payment Method for flexible analysis.  
""")

# --- Display 3 dashboard screenshots ---
col1, col2, col3 = st.columns(3)

with col1:
    st.image("mobile_sales_dashboard.png", caption="Mobile sales Dashboard", use_container_width=True)

with col2:
    st.image("mobile_sales_mtd.png", caption="Sales MTD", use_container_width=True)

with col3:
    st.image("mobile_sales_sply.png", caption="Same period Last year", use_container_width=True)

# --- Add link to the live Power BI report ---
st.markdown("""
###### 🔗 View Mobile sales performace Dashboard  
👉 [Click here to view the live Power BI report](https://github.com/manishlawande1906/Mobile-Sales-performance-Analysis---Power-BI-Report/blob/main/Mobile%20sales%20data.pbix)  

**Tools Used:** Power BI, DAX, Data Modeling, and Power Query 
""")


st.subheader("📊 Road Accident Analysis Dashboard")

st.markdown("""
#### 📝 Project Overview  
This interactive Power BI dashboard provides a detailed analysis of road accident trends across the United Kingdom. It highlights critical KPIs such as total casualties, accident types, severity levels, and contributing factors like light conditions and road surfaces. The report includes:

📊 Key Insights:

Total 196K casualties reported, showing an 11.9% decline YoY.

Majority of accidents occurred on single carriageways and during daytime hours.

Urban areas (62%) account for most of the casualties.

Visual comparison between current and previous year (CY vs PY) trends to track safety improvements.

Dynamic filters allow users to explore data by road surface and weather conditions.

# --- Display 1 dashboard screenshots ---
col1 = st.columns(1)

with col1:
    st.image("road_accident_analysis.png", caption="Road Accident Analysis", use_container_width=True)

# --- Add link to the live Power BI report ---

st.markdown("""
###### 🔗 View Mobile Sales Performance Dashboard  
👉 [Click here to view the live Power BI report](https://github.com/manishlawande1906/Road-Accident-Data/blob/main/Road%20Accident%20Analysis.pbix)  
""")


**Tools Used:** Power BI, DAX, Data Modeling, and Power Query 
""")


st.write("### ⚙️ Data Engineering Pipeline")
st.write("Built an ETL pipeline using Azure Data Factory, Synapse, and Databricks.")

# --- Contact Section ---
st.header("Contact Me")
st.write("""
📧 Email: [manishlawande@gmail.com](mailto:your.email@example.com)  
🔗 LinkedIn: [linkedin.com/in/manishlavande](https://linkedin.com/in/manishlawande)  
💻 GitHub: [github.com/manishlawande1906](https://github.com/manishlawande1906)
""")
