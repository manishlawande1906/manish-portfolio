import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Manish Lawande | Portfolio", layout="wide")

# --- HEADER ---
st.title("👋 Hi, I'm Manish Lawande")
st.write("### Data Analyst | Data Engineer | Machine Learning Enthusiast")
st.write("Welcome to my portfolio! Explore my Power BI dashboards, data projects, and technical expertise.")

# --- ABOUT SECTION ---
st.header("💡 About Me")
st.write("""
I'm passionate about data — transforming raw information into meaningful insights.
With experience in **Excel, Power BI, SQL, and Python**, I’m now expanding my skills into **Data Engineering and Machine Learning**.
""")

# --- SKILLS ---
st.header("🧰 Skills")
st.write("""
- **Languages:** Python, SQL  
- **Tools:** Power BI, Excel, Git, Streamlit  
- **Platforms:** Azure, Snowflake, Databricks  
- **Areas:** Data Cleaning, Visualization, ETL, Machine Learning
""")

# ================================================================
# PROJECT 1 - MOBILE SALES PERFORMANCE DASHBOARD
# ================================================================
st.subheader("📊 Project 1: Mobile Sales Performance Dashboard")

st.markdown("""
#### 📝 Project Overview  
An interactive **Power BI Dashboard** designed to analyze mobile sales performance across India.  
It offers a clear view of KPIs such as Total Sales, Quantity Sold, Average Price, and Transactions.

**Key Highlights:**
- Year-over-Year (YoY) and Month-to-Date (MTD) comparisons  
- City-wise and Brand-wise performance visualization  
- Insights on Payment Methods, Ratings, and customer feedback  
- Dynamic filters for Model, Brand, Year, and Payment Method  
""")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("mobile_sales_dashboard.png", caption="Mobile Sales Dashboard", use_container_width=True)
with col2:
    st.image("mobile_sales_mtd.png", caption="Sales MTD", use_container_width=True)
with col3:
    st.image("mobile_sales_sply.png", caption="Same Period Last Year", use_container_width=True)

st.markdown("""
###### 🔗 View Mobile Sales Dashboard  
[Click here to view the Power BI report](https://github.com/manishlawande1906/Mobile-Sales-performance-Analysis---Power-BI-Report/blob/main/Mobile%20sales%20data.pbix)  

**Tools Used:** Power BI, DAX, Power Query, Data Modeling  
""")

# ================================================================
# PROJECT 2 - ROAD ACCIDENT ANALYSIS
# ================================================================
st.subheader("🚦 Project 2: Road Accident Analysis Dashboard")

st.markdown("""
#### 📝 Project Overview  
A detailed **Power BI dashboard** that visualizes road accident data across the United Kingdom.  
It highlights patterns, severity, and environmental factors influencing accidents.

**Key Insights:**
- **196K casualties**, showing an **11.9% YoY decline**  
- Most accidents occurred on **single carriageways** during **daytime**  
- **Urban areas (62%)** have the majority of accidents  
- Comparison between **Current Year vs Previous Year (CY vs PY)**  
- Filters for **road surface**, **weather**, and **light conditions**
""")

# Smaller image size (reduced width)
st.image("road_accident_analysis.png", caption="Road Accident Analysis Dashboard", width=900)

st.markdown("""
###### 🔗 View Road Accident Analysis Dashboard  
[Click here to view the Power BI report](https://github.com/manishlawande1906/Road-Accident-Data/raw/main/Road%20Accident%20Analysis.pbix)  

**Tools Used:** Power BI, DAX, Power Query, Data Modeling  
""")

# ================================================================
# PROJECT 3 - SPOTIFY LISTENING ANALYSIS
# ================================================================
st.subheader("🎧 Project 3: Spotify Listening Analysis Dashboard")

st.markdown("""
#### 📝 Project Overview  
An interactive **Power BI Dashboard** analyzing Spotify listening behavior and user engagement.  
It provides insights into listening patterns, top artists, and platform preferences.

**Key Insights:**
- Analyzed **7,905 albums**, **4,112 artists**, and **13,665 tracks**  
- Over **19 billion milliseconds of listening time**, averaging **2.14 minutes** per track  
- Identified top-performing artists, albums, and tracks  
- Heatmaps highlight **active listening hours** and days  
- Year-over-Year trends show consistent audience growth  
""")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("spotify_dashboard.png", caption="Spotify Overview Dashboard", use_container_width=True)
with col2:
    st.image("spotify_listening_pattern.png", caption="Listening Patterns", use_container_width=True)
with col3:
    st.image("spotify_details.png", caption="Artist & Album Insights", use_container_width=True)

st.markdown("""
###### 🔗 View Spotify Listening Analysis Dashboard  
[Click here to view the Power BI report](https://github.com/manishlawande1906/Spotify-Listening-Analysis---Power-Bi-dashboard/blob/main/Spotify%20Dashboard_Manish.pbix)  

**Tools Used:** Power BI, DAX, Power Query, Data Modeling  
""")

# ================================================================
# PROJECT 4 - UBER TRIP ANALYSIS
# ================================================================
st.subheader("🚖 Project 4: Uber Trip Analysis Dashboard")

st.markdown("""
#### 📝 Project Overview  
A data-driven **Uber Trip Analysis Dashboard** that reveals ride behavior, booking trends, and payment patterns for June 2024.

**Key Insights:**
- **103.7K total bookings** with a total value of **$1.6M**  
- **Average fare:** $15 per trip, **total distance:** 349K miles  
- **UberX & UberXL** dominate by bookings and revenue  
- **Uber Pay (67%)** is the most preferred payment type  
- Peak activity during **6–9 AM** and **5–9 PM**  
- Longest recorded trip: *144 miles (Lower East Side → Crown Heights North)*  
""")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("uber_analysis_overview.png", caption="Uber Trip Overview Dashboard", use_container_width=True)
with col2:
    st.image("uber_time_analysis.png", caption="Trip Time Analysis", use_container_width=True)
with col3:
    st.image("uber_details.png", caption="Detailed Trip Data", use_container_width=True)

st.markdown("""
###### 🔗 View Uber Trip Analysis Dashboard  
[Click here to view the Power BI report](https://github.com/manishlawande1906/Uber-Trip-Analysis---Power-BI-Dashboard/blob/main/Uber%20Trip%20Analysis.pbix)  

**Tools Used:** Power BI, DAX, Power Query, Data Modeling  
""")

# ================================================================
# PROJECT 4 - Zomato Analysis Dashboard
# ================================================================
st.subheader("🍽️ Project 5: Zomato Analysis Dashboard")

st.markdown("""
#### 📝 Project Overview  
An interactive **Power BI dashboard** designed to analyze Zomato’s business performance across multiple cities.  
It provides insights into **customer behavior, city-wise orders, user activity, and food category trends**.

**Key Insights:**
- Over **987M total sales** and **150K+ orders** analyzed across major cities  
- **Bikaner, Noida, and Indirapuram** are top-performing cities by users and ratings  
- Tracks **gain and loss of customers** with demographic and age analysis  
- Identifies **most popular food categories** (Veg, Non-Veg, and Others)  
- Year-over-Year sales trend shows major growth in **2018 and 2019**  
""")

# --- Display 4 dashboard screenshots (2x2 layout) ---
col1, col2 = st.columns(2)
with col1:
    st.image("zomato_dashboard.png", caption="Zomato Dashboard Overview", use_container_width=True)
with col2:
    st.image("zomato_city_performace.png", caption="City Performance Analysis", use_container_width=True)

col3, col4 = st.columns(2)
with col3:
    st.image("zomato_user_performance.png", caption="User Performance Analysis", use_container_width=True)
with col4:
    st.image("zomato_overview.png", caption="Sales & Category Overview", use_container_width=True)

# --- Stylish Google Drive link section ---
st.markdown(
    """
    <div style="text-align: center; padding: 15px; border-radius: 10px; background-color: #f7f9fc; border: 1px solid #dfe3e6; margin-top: 20px;">
        <h5 style="color:#000000;">🔗 View All Power BI Dashboards</h5>
        <a href="https://drive.google.com/drive/folders/1bCooRfSH-S38AqIh3e0ONRuWkrJavqJY" target="_blank" style="text-decoration:none;">
            <button style="background-color:#FF4B4B; color:white; padding:10px 20px; border:none; border-radius:8px; font-weight:bold; cursor:pointer;">
                📊 Open Power BI Projects Folder
            </button>
        </a>
        <p style="color:#5a5a5a; margin-top:10px;">Tools Used: Power BI, DAX, Power Query, Data Modeling, and Visualization</p>
    </div>
    """,
    unsafe_allow_html=True
)




# ================================================================
# DATA ENGINEERING PIPELINE
# ================================================================
st.header("⚙️ Data Engineering Pipeline")
st.write("""
Built an end-to-end **ETL pipeline** using **Azure Data Factory**, **Azure Synapse**, and **Databricks** for automated data integration, transformation, and reporting.
""")

# ================================================================
# CONTACT SECTION
# ================================================================
st.header("📬 Contact Me")
st.write("""
📧 Email: [manishlawande@gmail.com](mailto:manishlawande@gmail.com)  
🔗 LinkedIn: [linkedin.com/in/manishlawande](https://linkedin.com/in/manishlawande)  
💻 GitHub: [github.com/manishlawande1906](https://github.com/manishlawande1906)
""")
