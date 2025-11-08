import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Manish Lawande | Portfolio", layout="wide")

# --- Header ---
st.title("👋 Hi, I'm Manish Lawande")
st.write("### Data Analyst | Data Engineer | Machine Learning Enthusiast")
st.write("Welcome to my portfolio! Explore my Power BI dashboards, data projects, and technical expertise.")

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

# --- PROJECT 1: Mobile Sales Performance Dashboard ---
st.subheader("📊 Project 1: Mobile Sales Performance Dashboard")

st.markdown("""
#### 📝 Project Overview  
An interactive Power BI dashboard designed to analyze mobile sales across India.  
It provides a complete view of sales performance using key KPIs such as Total Sales, Quantity, Average Price, and Transactions.  

**Key Highlights:**
- Year-over-Year (YoY) and Month-to-Date (MTD) comparisons  
- City-wise and Brand-wise performance visualization  
- Insights on Payment Methods, Ratings, and customer feedback  
- Dynamic filters for Model, Brand, Year, and Payment Method for flexible analysis  
""")

# --- Display 3 dashboard screenshots ---
col1, col2, col3 = st.columns(3)

with col1:
    st.image("mobile_sales_dashboard.png", caption="Mobile Sales Dashboard", use_container_width=True)

with col2:
    st.image("mobile_sales_mtd.png", caption="Sales MTD", use_container_width=True)

with col3:
    st.image("mobile_sales_sply.png", caption="Same Period Last Year", use_container_width=True)

# --- Add link to the live Power BI report ---
st.markdown("""
###### 🔗 View Mobile Sales Performance Dashboard  
[Click here to view the live Power BI report](https://github.com/manishlawande1906/Mobile-Sales-performance-Analysis---Power-BI-Report/blob/main/Mobile%20sales%20data.pbix)  

**Tools Used:** Power BI, DAX, Data Modeling, Power Query  
""")

# --- PROJECT 2: Road Accident Analysis Dashboard ---
st.subheader("📊 Project 2: Road Accident Analysis Dashboard")

st.markdown("""
#### 📝 Project Overview  
This Power BI dashboard provides a detailed analysis of road accident trends across the United Kingdom.  
It highlights key KPIs such as total casualties, accident types, severity levels, and contributing factors like light conditions and road surfaces.

**Key Insights:**
- Total **196K casualties** reported, showing an **11.9% decline YoY**  
- Majority of accidents occurred on **single carriageways** during **daytime**  
- **Urban areas (62%)** account for most of the casualties  
- Visual comparison between **current and previous year (CY vs PY)**  
- Dynamic filters allow exploration by **road surface and weather conditions**  
""")

# --- Display 1 dashboard screenshot ---
st.image("road_accident_analysis.png", caption="Road Accident Analysis", use_container_width=True)

# --- Add link to the live Power BI report ---
st.markdown("""
###### 🔗 View Road Accident Analysis Dashboard  
[Click here to view the live Power BI report](https://github.com/manishlawande1906/Road-Accident-Data/raw/main/Road%20Accident%20Analysis.pbix)  

**Tools Used:** Power BI, DAX, Data Modeling, Power Query  
""")

# --- PROJECT 2: Road Accident Analysis Dashboard ---
st.subheader("🎧 Spotify Listening Analysis Dashboard")

st.markdown("""
#### 📝 Project Overview  
This interactive Power BI dashboard explores Spotify listening patterns using streaming data.  
It provides insights into **user engagement, platform usage, and listening behavior** across multiple years.

📊 **Key Insights:**
- Total of **7,905 albums**, **4,112 artists**, and **13,665 tracks** analyzed.  
- Users spent **over 19 billion milliseconds** listening — with an **average listening time of 2.14 minutes** per track.  
- The dashboard identifies **top artists, albums, and tracks** across different platforms like Android, iOS, and Desktop.  
- Heatmaps highlight the **most active listening hours** (evenings and weekends).  
- Scatter plots analyze **track frequency vs. average listening time** to find user preferences.  
- Year-over-Year trends show **steady growth** in album and artist engagement.

""")

# --- Display 3 dashboard screenshots ---
col1, col2, col3 = st.columns(3)

with col1:
    st.image("spotify_dashboard.png", caption="Spotify Overview Dashboard", use_container_width=True)

with col2:
    st.image("spotify_listening_pattern.png", caption="Listening Patterns Analysis", use_container_width=True)

with col3:
    st.image("spotify_details.png", caption="Detailed Artist and Album Insights", use_container_width=True)

# --- Add link to Power BI report ---
st.markdown("""
###### 🔗 View Spotify Listening Analysis Dashboard  
[Click here to view the live Power BI report](https://github.com/manishlawande1906/Spotify-Listening-Analysis---Power-Bi-dashboard/blob/main/Spotify%20Dashboard_Manish.pbix)

**Tools Used:** Power BI, DAX, Power Query, Data Modeling, and Data Visualization
""")


# --- Data Engineering Pipeline Section ---
st.header("⚙️ Data Engineering Pipeline")
st.write("""
Built an end-to-end ETL pipeline using **Azure Data Factory**, **Azure Synapse**, and **Databricks** for data integration and transformation.
""")

# --- Contact Section ---
st.header("📬 Contact Me")
st.write("""
📧 Email: [manishlawande@gmail.com](mailto:manishlawande@gmail.com)  
🔗 LinkedIn: [linkedin.com/in/manishlawande](https://linkedin.com/in/manishlawande)  
💻 GitHub: [github.com/manishlawande1906](https://github.com/manishlawande1906)
""")
