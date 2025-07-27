
## Dubai Trip Assistant App - Chatbot
This is a Streamlit-based chatbot that helps you plan your trip to Dubai. The assistant provides expert recommendations on locations, hotels, and tourism activities.

### Features
- Chatbot powered by OpenAI GPT-4 API
- Loads API key securely from `.env` file
- Interactive chat interface using Streamlit

### Setup Instructions
1. **Clone the repository**
2. **Create and activate a Python virtual environment**
   - Windows PowerShell:
     ```powershell
     python -m venv venv0
     .\venv0\Scripts\activate
     ```
3. **Install dependencies**
   ```powershell
   pip install streamlit openai python-dotenv
   ```
4. **Get your OpenAI API key**
   - Sign up at [OpenAI](https://platform.openai.com/)
   - Copy your API key
5. **Create a `.env` file in the project folder**
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```
6. **Run the app**
   ```powershell
   streamlit run chatbot.py
   ```

### Usage
- Enter your travel questions in the chat input box.
- The assistant will reply with Dubai-specific recommendations.

