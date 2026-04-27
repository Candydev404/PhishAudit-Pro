import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import random

# Configure the page layout to utilize the full screen
st.set_page_config(page_title="Enterprise Audit Platform", layout="wide", initial_sidebar_state="expanded")

# --- DATABASE SIMULATION ---
# We simulate a database of company members and their interaction with the phishing campaign
if 'audit_data' not in st.session_state:
    # Generating dummy data to make the dashboard look populated and premium immediately
    statuses = ["Sent", "Clicked", "Compromised"]
    departments = ["Finance", "Engineering", "HR", "Marketing", "Operations"]
    
    dummy_data = []
    base_time = datetime.now() - timedelta(hours=48)
    
    for i in range(1, 51):
        status = random.choices(statuses, weights=[0.4, 0.3, 0.3])[0]
        dummy_data.append({
            "Member ID": f"EMP-{1000+i}",
            "Department": random.choice(departments),
            "Status": status,
            "Time Logged": (base_time + timedelta(minutes=random.randint(10, 2800))).strftime("%Y-%m-%d %H:%M") if status != "Sent" else "--"
        })
    st.session_state.audit_data = dummy_data

df = pd.DataFrame(st.session_state.audit_data)

# --- SIDEBAR NAVIGATION ---
st.sidebar.markdown("### 🛡️ PhishAudit Pro")
st.sidebar.markdown("Enterprise Security Console")
page = st.sidebar.radio("Navigation:", ["Campaign Analytics", "Process Audit Status", "Member Reports"])

# --- PAGE 1: CAMPAIGN ANALYTICS (The "Breathtaking" Dashboard) ---
if page == "Campaign Analytics":
    st.title("Phishing Campaign Analytics")
    st.markdown("Real-time telemetry of internal security awareness audit.")
    
    # Top-level metrics
    total_targets = len(df)
    compromised = len(df[df["Status"] == "Compromised"])
    clicked = len(df[df["Status"] == "Clicked"])
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Members Targeted", total_targets)
    col2.metric("Emails Opened/Clicked", clicked + compromised)
    col3.metric("Accounts Compromised", compromised, delta_color="inverse")
    col4.metric("Overall Risk Score", f"{(compromised/total_targets)*100:.1f}%")
    
    st.markdown("---")
    
    # Data Visualizations
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.subheader("Audit Status Distribution")
        # Interactive Donut Chart
        fig_donut = px.pie(df, names="Status", hole=0.6, 
                           color="Status",
                           color_discrete_map={"Sent":"#555555", "Clicked":"#F4D03F", "Compromised":"#E74C3C"})
        fig_donut.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font_color="white")
        st.plotly_chart(fig_donut, use_container_width=True)
        
    with chart_col2:
        st.subheader("Vulnerability by Department")
        # Interactive Bar Chart
        dept_counts = df[df["Status"] == "Compromised"]["Department"].value_counts().reset_index()
        dept_counts.columns = ["Department", "Compromised Count"]
        fig_bar = px.bar(dept_counts, x="Department", y="Compromised Count", color="Department",
                         color_discrete_sequence=px.colors.qualitative.Pastel)
        fig_bar.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font_color="white")
        st.plotly_chart(fig_bar, use_container_width=True)

# --- PAGE 2: PROCESS AUDIT STATUS ---
elif page == "Process Audit Status":
    st.title("Audit Status Management")
    st.markdown("Monitor and manually update member risk status based on real-time triggers.")
    
    st.dataframe(df, use_container_width=True)
    
    st.markdown("### Update Member Record")
    col1, col2 = st.columns(2)
    with col1:
        # Logical flow update: User login -> browse items -> admin updates status
        member_to_update = st.selectbox("Select Member ID:", df["Member ID"].tolist())
    with col2:
        new_status = st.selectbox("Assign New Status:", ["Sent", "Clicked", "Compromised", "Secured"])
        
    if st.button("Update System Status"):
        # Find the index of the member and update the session state dictionary
        for i, record in enumerate(st.session_state.audit_data):
            if record["Member ID"] == member_to_update:
                st.session_state.audit_data[i]["Status"] = new_status
                st.session_state.audit_data[i]["Time Logged"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                break
        st.success(f"Status for {member_to_update} successfully updated to '{new_status}'.")
        st.rerun()

# --- PAGE 3: MEMBER REPORTS ---
elif page == "Member Reports":
    st.title("Generate Security Reports")
    st.markdown("Compile automated post-action training reports for all members respectively.")
    
    report_target = st.selectbox("Select target group for report generation:", 
                                 ["All Compromised Members", "Finance Department", "Engineering Department", "Company-Wide Executive Summary"])
    
    if st.button("Generate Report"):
        with st.spinner("Compiling data..."):
            # Simulate processing time
            import time
            time.sleep(1.5)
            
            st.success("Report generated successfully.")
            st.markdown(f"### 📄 {report_target} - Q2 Phishing Audit")
            st.markdown("""
            **Summary of Findings:**
            * Members failed to identify the spoofed `gtbank-alerts-ng.com` domain.
            * The malicious link masked via IP tunneling successfully bypassed visual checks.
            
            **Required Action:**
            Mandatory retraining modules on URL verification and zero-trust authentication have been queued for the affected personnel.
            """)
            st.download_button("Download Report (PDF)", data="Dummy PDF Data", file_name="audit_report.pdf", mime="application/pdf")
