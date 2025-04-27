🏡 RealEstateGenie: Your AI-Powered Home Finder


🚀 Key Features
Personalized AI Suggestions: Powered by Groq’s Llama 3.

Smart Search (RAG): Retrieves top property matches using ChromaDB embeddings.

Clear, Friendly Prompts: Guides AI to generate accurate results.

Streamlit Interface: Simple, intuitive, and responsive design.

📂 Project Structure
RealEstateGenie/
├── app/                # Streamlit app
├── data/               # Dataset (original + cleaned)
├── scripts/            # Data processing script
├── docs/               # Architecture & documentation
├── README.md
└── requirements.txt

🛠️ Setup Instructions


1.Clone Repo:
git clone <your-repo-url>
cd RealEstateGenie

2.Create Virtual Environment:
python -m venv venv
venv\Scripts\activate  # Windows


3.Install Packages:
pip install -r requirements.txt


4.Configure API Key: Create .env with:
GROQ_API_KEY=your_groq_api_key_here


5.Run the App:
streamlit run app/RealEstateGenie.py
✅ The app will open at http://localhost:8501.

📊 Dataset
real_estate_utah.csv: Original listings.

real_estate_cleaned.csv: Cleaned data for optimized retrieval.

📖 Documentation
Full technical details and system architecture are available in docs/documentation.pdf.

🎯 Future Enhancements
Fine-tune LLM with real estate-specific queries.

Broaden dataset across regions.

Add advanced search filters and interactive dialogues.

⚠️ Ethics & Privacy
No personal data collected.

Bias-checked, transparent AI recommendations.

Designed for informational use only.

📬 Contact
Developer: Sijoy Almeida

Email: almeida.si@northeastern.edu

Thanks for exploring RealEstateGenie! 🚀🏠