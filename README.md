# 🏡 Real Estate AI Suite

## 🚀 Overview

This is a **Streamlit-powered AI dashboard** for real estate professionals, integrating multiple AI agents to assist with:

- Client Relations
- Market Analysis
- Transactions & Documents
- Marketing & Outreach
- Property Management
- Training & Support

It connects with OpenWebUI and external APIs (Zillow, DocuSign, HubSpot) for data-driven responses.

---

## 📌 Installation & Setup

### 1️⃣ **Clone the Repository**

```bash
git clone https://github.com/Crashicorn/RealEstateDashboard.git
cd Real_Estate_AI_Suite
```

### 2️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 3️⃣ **Run the Streamlit App**

```bash
streamlit run streamlit_dashboard.py
```

The app will be available at `localhost:8501`.

---

## 🔑 **API Setup**

To enable full functionality, users must **enter their API keys** in the **API Setup** section of the dashboard.

### Required API Keys:

- **Zillow API** → [Get API Key](https://www.zillow.com/howto/api/Overview.htm)
- **DocuSign API** → [Get API Key](https://developers.docusign.com/)
- **HubSpot API** → [Get API Key](https://developers.hubspot.com/docs/api/overview)

Without these, agents will still function but with limited capabilities.

---

## 🔗 **Pending Tasks for Full Deployment**

✔ **UI & Core Functionality Works** ✅  
✔ **Agent Communication with OpenWebUI is Integrated** ✅  
❌ **APIs Not Yet Tested on Live Server** (Needs Verification) ❗  
❌ **Error Handling for API Failures Needs Final Testing** ❗

---

## 📌 **Next Steps for Future Development**

1️⃣ **Verify API Calls on the Server** – Ensure Zillow, DocuSign, and HubSpot integrate correctly.  
2️⃣ **Optimize Response Formatting** – Improve AI output clarity for real estate professionals.  
3️⃣ **Deploy on Production Server** – Once stable, set up hosting for beta testers.  
4️⃣ **Expand Functionality** – Add logging, analytics, and scheduling tools.

---

## 👥 **Handoff Notes for Aaron**

- **Current Version is Fully Functional (Except API Testing)**
- **Streamlit Dashboard is Finalized** → No UI changes expected.
- **Only Remaining Step is API Verification** → Needs testing on live server.

**Once API connections are confirmed, this is ready for beta testing.** 🚀
