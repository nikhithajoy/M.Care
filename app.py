import os
import streamlit as st
import google.generativeai as genai
from PIL import Image
from api_key import api_key  # Ensure this imports the correct key

# Streamlit app configuration
st.set_page_config(page_title="Medical Image Analysis", page_icon=":robot:")

# Inject custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: #f9f9f9; /* Light background color */
        color: #333; /* Darker text color for contrast */
        font-family: 'Arial', sans-serif; /* Custom font family */
    }

    .stButton button {
        background-color: #39cfc3; /* Bootstrap blue for buttons */
        color: white; /* White text color */
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s, color 0.3s; /* Smooth transition for hover effect */
    }

    .stButton button:hover {
        background-color: #32b9ae; /* Darker blue on hover */
        color: white; /* White text color on hover */
    }

    .stFileUploader input[type="file"] {
        border: 2px solid #ccc; /* Default border color */
        color: #333; /* Default text color */
        background-color: #fff; /* Default background color */
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        transition: border-color 0.3s, color 0.3s; /* Smooth transition for hover effect */
    }

    .stFileUploader input[type="file"]:hover {
        border-color: #007bff; /* Blue border color on hover */
        color: #007bff; /* Blue text color on hover */
    }

    .stImage img {
        border-radius: 10px; /* Rounded corners for images */
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); /* Shadow effect for images */
    }

    .stTitle, .stSubheader {
        font-family: 'Arial', sans-serif; /* Custom font family */
    }

    .stMarkdown {
        font-family: 'Arial', sans-serif; /* Custom font family for markdown text */
    }

    .stExpanderHeader {
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Function to switch between pages
def switch_page(page_name):
    st.session_state.page = page_name

# Sidebar setup
st.sidebar.title("Medical Image Analysis")

# File uploader for medical images in the sidebar
uploaded_file = st.sidebar.file_uploader("Upload the medical image for analysis", type=['png', 'jpg', 'jpeg'])

# Button to generate the analysis in the sidebar
submit_button = st.sidebar.button("Generate Analysis")

# Function to upload the file to Gemini and get analysis
def upload_to_gemini(path, mime_type=None):
    """Uploads the given file to Gemini and returns the file URI."""
    file = genai.upload_file(path, mime_type=mime_type)
    return file

# Home page content
if st.session_state.page == 'home':
    # Create a row with two columns
    col1, col2 = st.columns([1, 3])  # Adjust the proportions as needed

    with col1:
        st.image("mcare-logo.png", width=130)  # Adjust width as needed

    with col2:
        st.title("M.Care: Your Companion in Medical Image Insights")

    st.markdown("""
        **M.Care** is an AI-powered tool designed to provide general information about visible conditions 
        in medical images. Upload your image in the sidebar, click the 'Generate Analysis' button, and get relevant educational 
        content about what might be visible in the image.
    """)

    if submit_button and uploaded_file is not None:
        # Save the uploaded file temporarily
        with open("temp_image.png", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Switch to the results page
        switch_page('results')

    elif submit_button:
        st.sidebar.write("Please upload an image before clicking the button.")


# Results page content
elif st.session_state.page == 'results':
    # Display the uploaded image
    st.image("temp_image.png", caption="Uploaded Medical Image", use_column_width=True)

    # Configure the Gemini API with the API key
    genai.configure(api_key=api_key)

    # Upload the image to Gemini
    file = upload_to_gemini("temp_image.png", mime_type="image/png")

    # Create the generation configuration
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    # Initialize the Gemini model
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    # Detailed prompt for educational information
    detailed_prompt = (
        "Analyze the visible condition in this medical image and provide general information about it. "
        "Please include the following details:\n"
        "1. Possible causes or factors that might lead to the condition seen in the image.\n"
        "2. General symptoms or characteristics associated with the visible condition.\n"
        "3. Recommendations for further actions or what might be done next. "
        "Avoid any disclaimers or mentions of the AI model's limitations."
    )

    # Start a chat session with the uploaded file and the detailed prompt
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    file,
                    detailed_prompt,
                ],
            }
        ]
    )

    # Send a message to the model and get the response
    response = chat_session.send_message(detailed_prompt)
    
    # Display the analysis results
    st.subheader("Information About the Condition")
    st.write(response.text)
    
    # Back button to return to home page
    if st.button("Back to Home"):
        switch_page('home')
