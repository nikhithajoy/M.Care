# M.Care

M.Care is an AI-powered tool designed to provide general information about visible conditions in medical images. By leveraging advanced generative AI models, M.Care offers educational insights into the possible causes, symptoms, and recommendations related to conditions visible in uploaded medical images.

![image](https://github.com/user-attachments/assets/e8c3b31d-38d1-40be-8e6a-c7d92b28fb29)


## Features

- **Image Upload**: Upload medical images in PNG, JPG, or JPEG format.
- **AI Analysis**: Uses Gemini's AI model to analyze the visible condition in the image.
- **Educational Information**: Provides detailed information about possible causes, symptoms, and recommendations based on the image analysis.
- **User-Friendly Interface**: Simple and intuitive interface for easy interaction and navigation.

![image](https://github.com/user-attachments/assets/bf539501-592a-4a29-8d4e-72e62ed28916)
![image](https://github.com/user-attachments/assets/c030290c-bd7b-488a-9c25-20e3fc213b3f)

## Technology Stack

- **Streamlit:** For building the web interface.
- **Google Generative AI (Gemini API):** For generating insights based on the medical images.
- **PIL (Pillow):** For image handling and processing.

## Gemini API

The Gemini API by Google is used for analyzing medical images. It provides powerful AI models that can interpret the content of images and generate human-readable information about what is visible. In this project, the API is configured to analyze the uploaded medical images and provide insights such as:

- **Possible Causes:** Factors that might lead to the visible condition.
- **Symptoms and Characteristics:** General symptoms and characteristics associated with the condition.
- **Recommendations:** Suggested next steps or actions to take based on the analysis.

## How to Configure the API

The Gemini API is configured using an API key, which is imported from a separate `api_key` module. Ensure that your API key is correctly set up to interact with the Gemini API.

```python
import google.generativeai as genai
from api_key import api_key  # Ensure this imports the correct key

# Configure the Gemini API
genai.configure(api_key=api_key)
```

## Installation

To run the M.Care application locally, follow these steps:
1. **Clone the Repository**:
   
```
git clone https://github.com/nikhithajoy/M.Care.git
```

2. **Navigate to the Project Directory:**
```
cd mcare
```

3. **Install Dependencies:** Ensure you have Python installed. Then, install the required packages using pip:
```
pip install -r requirements.txt
```

4. **API Key Configuration:**

Obtain an API key from Gemini and save it in a file named api_key.py in the project directory.
The api_key.py file should contain the following code:

```
api_key = 'YOUR_API_KEY_HERE'
```

5. **Run the Application:**
```
streamlit run app.py
```

## Usage
1. Upload Image: Navigate to the sidebar and use the file uploader to upload your medical image (PNG, JPG, or JPEG).
2. Generate Analysis: Click the "Generate Analysis" button to initiate the analysis process.
3. View Results: After the analysis is complete, the results will be displayed on the results page with detailed information about the condition visible in the uploaded image.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any questions or inquiries, please reach out to nikhitha.joy.official@gmail.com

Read More on [Medium](https://medium.com/@nikhitha.joy.official/m-care-your-ai-powered-companion-in-medical-image-analysis-228e072eb1b9)
