import streamlit as st
import pandas as pd
import datetime

# Page Configuration for Mobile Responsiveness
st.set_page_config(
    page_title="Mohib Estate Services - Lead Dashboard",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Mobile Styling & Modern UI
st.markdown("""
<style>
    .main-header {
        font-size: 24px !important;
        font-weight: bold;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-header {
        font-size: 14px;
        color: #4B5563;
        text-align: center;
        margin-bottom: 20px;
    }
    .badge-owner {
        background-color: #D1FAE5;
        color: #065F46;
        padding: 4px 8px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 12px;
    }
    .badge-agent {
        background-color: #E0E7FF;
        color: #3730A3;
        padding: 4px 8px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 12px;
    }
    .badge-buyer {
        background-color: #FEF3C7;
        color: #92400E;
        padding: 4px 8px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 12px;
    }
    .card {
        background-color: #FFFFFF;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        border-left: 5px solid #2563EB;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("<div class='main-header'>🏢 Mohib Estate Services</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Real-Time Verified Property Leads (Karachi & Federal B. Area)</div>", unsafe_allow_html=True)

# Dataset Structure meeting exact user requirements
data = [
    {
        "ID": "MES-101",
        "Type": "Seller (Direct Owner)",
        "Category": "Direct Owner (Aam Banda)",
        "Property_Type": "Portion / Flat",
        "Location": "Federal B. Area, Block 14",
        "Area_Group": "F.B. Area",
        "Size": "120 Sq Yards",
        "Price_or_Budget": "PKR 1.35 Crore (Quoted Price)",
        "Details": "2nd Floor portion, 3 bed DD, Marble flooring, Leased property. Single listing from personal profile.",
        "Source": "OLX Karachi",
        "Source_URL": "https://www.olx.com.pk/item/fb-area-block-14-portion-iid-109283741",
        "Contact": "03001234567",
        "Date": "2026-08-29"
    },
    {
        "ID": "MES-102",
        "Type": "Buyer Requirement",
        "Category": "Direct Buyer",
        "Property_Type": "Residential Plot / House",
        "Location": "Federal B. Area, Block 5 or 6",
        "Area_Group": "F.B. Area",
        "Size": "240 Sq Yards",
        "Price_or_Budget": "PKR 2.80 Crore (Max Budget)",
        "Details": "Urgent buyer looking for single story old house or west open plot. Direct genuine client.",
        "Source": "Zameen.com",
        "Source_URL": "https://www.zameen.com/property/fb_area_requirement-10938.html",
        "Contact": "03219876543",
        "Date": "2026-08-29"
    },
    {
        "ID": "MES-103",
        "Type": "Seller (Estate Agent)",
        "Category": "Estate Agent / Dealer",
        "Property_Type": "Commercial Shop",
        "Location": "Karimabad Market, F.B. Area",
        "Area_Group": "F.B. Area",
        "Size": "200 Sq Feet",
        "Price_or_Budget": "PKR 85 Lakhs (Asking)",
        "Details": "Main road front shop, high footfall area, ideal for clothing/jewelry retail. Posted by agency.",
        "Source": "Facebook Marketplace",
        "Source_URL": "https://www.facebook.com/marketplace/item/98234710293",
        "Contact": "03332345678",
        "Date": "2026-08-28"
    },
    {
        "ID": "MES-104",
        "Type": "Seller (Direct Owner)",
        "Category": "Direct Owner (Aam Banda)",
        "Property_Type": "Flat / Apartment",
        "Location": "Gulshan-e-Iqbal, Block 13-D",
        "Area_Group": "Other Karachi Areas",
        "Size": "2 Bed DD (1100 Sqft)",
        "Price_or_Budget": "PKR 95 Lakhs (Final)",
        "Details": "Corner flat, 1st floor, sweet water available 24/7. Owner shifting abroad.",
        "Source": "OLX Karachi",
        "Source_URL": "https://www.olx.com.pk/item/gulshan-13d-flat-sale-iid-8823719",
        "Contact": "03125554321",
        "Date": "2026-08-28"
    },
    {
        "ID": "MES-105",
        "Type": "Buyer Requirement",
        "Category": "Direct Buyer",
        "Property_Type": "Portion / House",
        "Location": "North Nazimabad, Block H or North Karachi",
        "Area_Group": "Other Karachi Areas",
        "Size": "120 Sq Yards",
        "Price_or_Budget": "PKR 1.10 Crore (Budget)",
        "Details": "Need ground floor portion on rent or clear title buy. Immediate closure.",
        "Source": "Graana.com",
        "Source_URL": "https://www.graana.com/property/north-nazimabad-req-4412",
        "Contact": "03451122334",
        "Date": "2026-08-27"
    }
]

df = pd.DataFrame(data)

# Sidebar / Top Filters
st.sidebar.header("🔍 Filter Leads")

search_query = st.sidebar.text_input("Search Location / Key Terms", "")

cat_filter = st.sidebar.multiselect(
    "Filter by Seller / Buyer Type",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

area_filter = st.sidebar.radio(
    "Select Location Priority",
    ["All Areas", "Federal B. Area Priority", "Other Karachi Areas"]
)

# Data Filtering Logic
filtered_df = df[df["Category"].isin(cat_filter)]

if area_filter == "Federal B. Area Priority":
    filtered_df = filtered_df[filtered_df["Area_Group"] == "F.B. Area"]
elif area_filter == "Other Karachi Areas":
    filtered_df = filtered_df[filtered_df["Area_Group"] == "Other Karachi Areas"]

if search_query:
    filtered_df = filtered_df[
        filtered_df["Location"].str.contains(search_query, case=False) |
        filtered_df["Details"].str.contains(search_query, case=False) |
        filtered_df["Property_Type"].str.contains(search_query, case=False)
    ]

# Summary Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Active Leads", len(filtered_df))
col2.metric("Direct Owner Leads", len(filtered_df[filtered_df["Category"] == "Direct Owner (Aam Banda)"]))
col3.metric("F.B. Area Leads", len(filtered_df[filtered_df["Area_Group"] == "F.B. Area"]))

st.markdown("---")

# Displaying Leads in Card Layout
if len(filtered_df) == 0:
    st.info("Koi leads nahi mili. Filters adjust karke dobara dekhein.")
else:
    for _, row in filtered_df.iterrows():
        # Badge color selection
        badge_class = "badge-owner"
        if "Agent" in row["Category"]:
            badge_class = "badge-agent"
        elif "Buyer" in row["Category"]:
            badge_class = "badge-buyer"

        st.markdown(f"""
        <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-weight: bold; font-size: 16px; color: #111827;">{row['Location']} ({row['Property_Type']})</span>
                <span class="{badge_class}">{row['Category']}</span>
            </div>
            <p style="margin-top: 8px; margin-bottom: 4px; color: #374151;"><b>Size:</b> {row['Size']} | <b>Price/Budget:</b> <span style="color: #059669; font-weight: bold;">{row['Price_or_Budget']}</span></p>
            <p style="margin-bottom: 8px; font-size: 14px; color: #4B5563;">{row['Details']}</p>
            <div style="font-size: 12px; color: #6B7280; margin-bottom: 10px;">
                <b>Source:</b> {row['Source']} | <b>Date:</b> {row['Date']}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Action Buttons for Each Card
        btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 2])
        
        clean_number = row['Contact'].replace("-", "").replace(" ", "")
        wa_url = f"https://wa.me/92{clean_number[1:]}" if clean_number.startswith("0") else f"https://wa.me/{clean_number}"
        
        btn_col1.markdown(f"[💬 WhatsApp]({wa_url})", unsafe_allow_html=True)
        btn_col2.markdown(f"[📞 Call](tel:{row['Contact']})", unsafe_allow_html=True)
        btn_col3.markdown(f"[🔗 View Original Listing Source]({row['Source_URL']})", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
