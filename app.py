import streamlit as st

# --- Page Configuration (MUST BE THE FIRST STREAMLIT COMMAND) ---
st.set_page_config(
    page_title="AI Design Suite Portal",
    layout="wide",
    initial_sidebar_state="expanded"  # Keep sidebar open initially
)

# --- Configuration for Portal Links ---
# Replace with your actual deployed URLs
CHATBOT_APP_URL = "https://viab-interviewer.streamlit.app/"
RAG_UI_APP_URL = "https://viab-insights.streamlit.app/"

# --- Custom CSS for Dark Theme and Card Styling ---
st.markdown("""
<style>
    /* Import a nice font (optional) */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');

    /* General Page Styling - Dark Theme */
    body { /* Targeting body for overall background if .stApp doesn't cover fullscreen consistently */
        background-color: #1E1E1E; /* Dark background */
    }
    .stApp {
        background-color: #1E1E1E; /* Dark background for the app */
        color: #E0E0E0; /* Light gray text for readability */
        font-family: 'Roboto', sans-serif;
    }

    /* Title Styling */
    h1 { /* Main title of the portal */
        text-align: center;
        color: #00A9E0; /* A vibrant blue for contrast */
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 20px;
        letter-spacing: 1px;
    }
    
    /* Header for "System Modules" */
    h2 { 
        text-align: center;
        color: #CCCCCC; /* Lighter gray */
        font-weight: 500;
        margin-bottom: 10px;
    }
    
    /* Sub-description text */
    .stMarkdown p, .stText, .stAlert p { /* Targeting general text elements */
        color: #B0B0B0; /* Even lighter gray for descriptions */
    }


    /* Card Styling - Dark Theme */
    .card {
        background: linear-gradient(145deg, #2c3e50, #34495e); /* Dark gradient background */
        border-radius: 15px;
        padding: 30px; /* Increased padding */
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3), 0 6px 6px rgba(0, 0, 0, 0.25); /* More pronounced shadow */
        height: 400px; /* Fixed height for uniform cards */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out; /* For hover effect */
        border: 1px solid #4A5568; /* Subtle border */
    }
    .card:hover {
        transform: translateY(-10px) scale(1.02); /* Lift and slightly scale on hover */
        box-shadow: 0 12px 28px rgba(0, 0, 0, 0.4), 0 10px 10px rgba(0, 0, 0, 0.3);
    }
    .card h3 { /* Card Title */
        color: #5DADE2; /* Lighter, vibrant blue */
        margin-top: 0;
        font-size: 1.8em; /* Larger title */
        font-weight: 500;
        text-align: center;
        border-bottom: 1px solid #4A5568;
        padding-bottom: 10px;
        margin-bottom: 15px;
    }
    .card p.summary { /* Card Description Text - concise summary */
        color: #C0C0C0; 
        font-size: 0.9em;
        line-height: 1.7;
        flex-grow: 1;
        margin-bottom: 20px; /* Space before button */
        text-align: center;
    }
    .card .stButton>button { /* Card Button */
        background-color: #00A9E0; /* Vibrant blue */
        color: white;
        border: none;
        padding: 12px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 1.05em;
        font-weight: 500;
        border-radius: 8px;
        width: 100%;
        transition: background-color 0.3s ease;
    }
    .card .stButton>button:hover {
        background-color: #007B Vortex; /* Darker blue on hover */
    }

    /* Horizontal Rule Styling */
    hr {
        border: none;
        height: 1px;
        background-color: #4A5568; /* Darker gray for dark theme */
        margin-top: 30px;
        margin-bottom: 30px;
    }
    
    /* Styling for the detailed explanation section */
    .explanation-section h3 {
        color: #5DADE2;
        border-bottom: 1px solid #4A5568;
        padding-bottom: 8px;
    }
    .explanation-section p, .explanation-section li {
        color: #B0B0B0;
        line-height: 1.7;
    }
    .explanation-section strong {
        color: #E0E0E0; /* Slightly brighter for emphasis */
    }

</style>
""", unsafe_allow_html=True)


# --- Streamlit App UI Content Starts Here ---
st.title("AI Architectural Design Suite")
st.markdown("---")

st.header("System Modules")
st.markdown(
    "<p style='text-align: center; color: #B0B0B0; font-size: 1.1em; margin-bottom: 30px;'>"
    "Navigate through our intelligent tools to bring your architectural visions to life, "
    "from initial concept to standards-aware analysis."
    "</p>", unsafe_allow_html=True
)

# --- Card Layout for Modules ---
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="card">
        <h3>🎨 AI Design Interviewer</h3>
        <p class="summary">
            Start your design journey with a guided conversational interview. 
            This AI assistant helps articulate your vision, define project needs, 
            and analyze reference images.
            <br><br>
            <strong>Output:</strong> A structured <code>conversation.json</code> brief for detailed analysis.
        </p>
    </div>
    """, unsafe_allow_html=True)
    if CHATBOT_APP_URL and "YOUR_DEPLOYED_CHATBOT_APP_URL_HERE" not in CHATBOT_APP_URL:
        st.link_button("Launch Interviewer", CHATBOT_APP_URL,
                       use_container_width=True)
    else:
        st.warning("Chatbot Interviewer URL not configured.")


with col2:
    st.markdown("""
    <div class="card">
        <h3>🛠️ RAG Standards Analyzer</h3>
        <p class="summary">
            Upload your <code>conversation.json</code> brief here. This module leverages 
            Retrieval Augmented Generation (RAG) against a knowledge base of architectural standards.
            <br><br>
            <strong>Output:</strong> Detailed analysis, numerical standards, preliminary BOQs, and design considerations.
        </p>
    </div>
    """, unsafe_allow_html=True)
    if RAG_UI_APP_URL and "YOUR_DEPLOYED_RAG_UI_APP_URL_HERE" not in RAG_UI_APP_URL:
        st.link_button("Launch Analyzer", RAG_UI_APP_URL,
                       use_container_width=True)
    else:
        st.warning("RAG Analyzer URL not configured.")

st.markdown("---")

# --- Detailed Explanation of Module Interdependence ---
st.markdown("<div class='explanation-section'>",
            unsafe_allow_html=True)  # Apply class for styling
st.header("How These Modules Work Together")
st.markdown("""
The AI Architectural Design Suite streamlines your design process through a connected two-stage workflow:

1.  **Stage 1: Design Brief Creation (AI Design Interviewer)**
    *   **Purpose:** To meticulously capture your project's vision, functional requirements, and contextual details.
    *   **Process:** You engage in an interactive dialogue with the AI Interviewer. It guides you through defining your space, discussing rooms, styles, and specific needs. You can also upload images (like inspirational photos or existing floor plans) for the AI to analyze and incorporate into the brief.
    *   **Key Output:** The primary deliverable from this stage is a `conversation.json` file. This isn't just a chat log; it's a richly structured document that encapsulates all the gathered information, including any AI-driven image analysis results, ready for deep processing.

2.  **Stage 2: Standards-Based Analysis (RAG Standards Analyzer)**
    *   **Purpose:** To take your personalized design brief and elevate it by integrating relevant architectural standards, practical guidelines, and preliminary quantitative data.
    *   **Process:**
        *   You upload the `conversation.json` (from Stage 1) into the RAG Standards Analyzer.
        *   The Analyzer first uses AI to distill your conversation into core **structured requirements**.
        *   Based on these requirements, it formulates targeted **queries** to its specialized knowledge base. This knowledge base is pre-loaded with information from respected architectural texts (e.g., Time-Saver Standards, Neufert Architects' Data, Modern Construction Handbook).
        *   The system **retrieves** the most relevant text passages from these books.
        *   Finally, a sophisticated AI model **synthesizes** your original requirements with the retrieved standards. It extracts or deduces specific numerical values (dimensions, quantities), outlines preliminary Bill of Quantities (BOQ) items, and identifies potential design conflicts or important considerations.
    *   **Key Output:** A comprehensive JSON document detailing the standards-aware analysis, ready to inform the next steps in your design process.

**The `conversation.json` from the AI Design Interviewer is the essential bridge, transferring your articulated needs to the RAG Standards Analyzer for an expert, data-driven evaluation.**
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)


st.markdown("---")
st.caption("Select a module above to begin your design exploration or analysis.")
