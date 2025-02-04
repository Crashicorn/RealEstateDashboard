import streamlit as st
import json
import os
import requests

# File to store API keys
API_KEYS_FILE = "api_keys.json"
OPENWEBUI_URL = "http://localhost:5001"  # Update if needed

# Load API keys if they exist
def load_api_keys():
    if os.path.exists(API_KEYS_FILE):
        with open(API_KEYS_FILE, "r") as file:
            return json.load(file)
    return {}

# Save API keys to file
def save_api_keys(api_keys):
    with open(API_KEYS_FILE, "w") as file:
        json.dump(api_keys, file)

# UI for API Setup Wizard
def api_setup():
    st.title("🔑 API Setup Wizard")
    st.write("Enter your API keys below. If you don't have them yet, click the links to get them.")
    
    api_keys = load_api_keys()
    
    api_keys["zillow"] = st.text_input("Zillow API Key", api_keys.get("zillow", ""))
    st.markdown("[Get Zillow API Key](https://www.zillow.com/howto/api/Overview.htm)")
    
    api_keys["docusign"] = st.text_input("DocuSign API Key", api_keys.get("docusign", ""))
    st.markdown("[Get DocuSign API Key](https://developers.docusign.com/)")
    
    api_keys["hubspot"] = st.text_input("HubSpot API Key", api_keys.get("hubspot", ""))
    st.markdown("[Get HubSpot API Key](https://developers.hubspot.com/docs/api/overview)")
    
    if st.button("Save API Keys"):
        save_api_keys(api_keys)
        st.success("API Keys Saved Successfully!")

# Function to send requests to OpenWebUI
def query_openwebui(agent_name, user_input):
    try:
        response = requests.post(f"{OPENWEBUI_URL}/query", json={"agent": agent_name, "input": user_input})
        if response.status_code == 200:
            return response.json().get("response", "No response received.")
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Request failed: {str(e)}"

# Main Dashboard
def main_dashboard():
    st.title("🏡 Real Estate AI Suite")
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Select an AI Agent", ["Client Relations", "Market Analysis", "Transactions", "Marketing", "Property Management", "Training & Support", "API Setup"])
    
    if choice == "API Setup":
        api_setup()
    else:
        st.write(f"### {choice} Agent")
        user_input = st.text_area("Enter your request:")
        if st.button("Submit Request"):
            response = query_openwebui(choice, user_input)
            st.write("### Response:")
            st.write(response)

# Run the app
if __name__ == "__main__":
    main_dashboard()
