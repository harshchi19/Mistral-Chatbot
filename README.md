# AI Insurance Assistant Dashboard through Mistral-Chatbot

## Project Overview  
The **AI Insurance Assistant Dashboard** is an interactive platform that combines **machine learning**, **speech recognition**, and **dynamic chat capabilities** to provide personalized insurance and financial guidance.  

## Features  
- 🗨️ **Chat Assistant**: Offers personalized financial advice and discount predictions.  
- 🎤 **Speech-to-Text**: Converts audio input to text for seamless interaction.  
- 🧠 **AI-Powered Responses**: Utilizes fine-tuned models for context-aware replies.  
- 📉 **Fitness-Based Discounts**: Predicts discounts based on user fitness scores.  

## Tech Stack  
- **Framework**: Streamlit  
- **Speech Recognition**: `speech_recognition`, `pydub`, `streamlit-webrtc`  
- **Machine Learning**: Hugging Face Inference API  
- **Backend**: Python, Pandas, Environment Variables (`dotenv`)  
- **Frontend**: Custom CSS for chat UI  

## Setup Instructions  

1. **Install Dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  

2. **Environment Setup**:  
   - Create a `.env` file with your Hugging Face API token:  
     ```  
     HUGGINGFACE_API_TOKEN=your_api_token_here  
     ```  

3. **Run the Application**:  
   ```bash  
   streamlit run app.py  
   ```  

## Usage  
- **Chat Interface**: Type or speak queries for personalized insurance assistance.  
- **Discount Prediction**: Input your fitness score to get applicable discounts.  

## Future Enhancements  
- Expand fitness-based discounts.  
- Integrate real-time data sources for better predictions.  


