# M.Care

M.Care is an AI-powered tool designed to provide general information about visible conditions in medical images. By leveraging advanced generative AI models, M.Care offers educational insights into the possible causes, symptoms, and recommendations related to conditions visible in uploaded medical images.

![image](https://github.com/user-attachments/assets/e8c3b31d-38d1-40be-8e6a-c7d92b28fb29)


## Features

- **Image Upload**: Upload medical images in PNG, JPG, or JPEG format.
- **AI Analysis**: Uses Gemini's AI model to analyze the visible condition in the image.
- **Educational Information**: Provides detailed information about possible causes, symptoms, and recommendations based on the image analysis.
- **User-Friendly Interface**: Simple and intuitive interface for easy interaction and navigation.

![image](https://github.com/user-attachments/assets/bf539501-592a-4a29-8d4e-72e62ed28916)
![image](https://github.com/user-attachments/assets/367ef608-0c5c-4a39-8710-3b07701572c6)


## Installation

To run the M.Care application locally, follow these steps:
1. **Clone the Repository**:
   
```
git clone https://github.com/your-username/mcare.git
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
