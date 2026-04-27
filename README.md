# 🛡️ PhishAudit Pro: Enterprise Security Console

An interactive, enterprise-grade platform designed to simulate phishing attacks, audit organizational vulnerabilities, and generate actionable security training reports. This project serves as a comprehensive dashboard for IT administrators to monitor real-time threat telemetry and manage employee risk statuses.

## ✨ Key Features

* **Real-Time Analytics Dashboard:** Interactive data visualizations (built with Plotly) tracking overall risk scores, department vulnerabilities, and open/click rates.
* **Status Management Logic:** A dynamic administrative backend that updates member statuses sequentially (e.g., from *Sent* -> *Clicked* -> *Compromised* -> *Secured*) as they interact with simulated security events.
* **Automated Report Generation:** Compiles and exports customized post-action training reports for all members respectively, streamlining the IT security audit workflow.
* **Premium UI/UX:** A responsive, dark-mode customized interface designed for high readability and professional deployment.

## 💻 Tech Stack

* **Frontend & Backend Logic:** Python, [Streamlit](https://streamlit.io/)
* **Data Manipulation:** Pandas
* **Data Visualization:** Plotly Express
* **Deployment:** Streamlit Community Cloud

## 🚀 Local Installation & Setup

To run this application locally on your machine for testing or development:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/PhishAudit-Pro.git](https://github.com/your-username/PhishAudit-Pro.git)
   cd PhishAudit-Pro
