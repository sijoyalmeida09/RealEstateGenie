# 🏡 RealEstateGenie: AI-Powered Home Finder

Welcome to **RealEstateGenie**, a smart real estate assistant that simplifies the home search process using Generative AI and Retrieval-Augmented Generation (RAG) techniques.

---

## 🚀 Features

- **Natural Language Search:** Find homes with conversational queries.
- **Retrieval-Augmented Generation:** Combines semantic search (ChromaDB) with AI text generation (Groq's Llama 3).
- **Personalized Recommendations:** Tailored property suggestions based on user needs.
- **Streamlit Interface:** Simple, interactive, and easy-to-use web application.

---

## 📂 Project Structure

```
RealEstateGenie/
├── app/
│   └── RealEstateGenie.py          # Streamlit App
├── data/
│   ├── real_estate_utah.csv         # Original dataset
│   └── real_estate_cleaned.csv      # Cleaned dataset
├── scripts/
│   └── clean_data.py                # Data preprocessing script
├── docs/   ├
│   └── documentation.pdf            # Full technical documentation
├── requirements.txt                 # Python dependencies
└── README.md                        # Project overview
```

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd RealEstateGenie
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
# Activate
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

Create a `.env` file in the root folder:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

You can get your API key from [Groq.com](https://groq.com).

---

## 🚀 Running the Application

```bash
streamlit run app/RealEstateGenie.py
```

The application will open automatically at:  
[http://localhost:8501](http://localhost:8501)

---

## 📚 Dataset

- **real_estate_utah.csv:** Raw property listings (Utah region).
- **real_estate_cleaned.csv:** Preprocessed dataset for semantic search.

If needed, you can re-clean the dataset manually:

```bash
python scripts/clean_data.py
```

---

## 🏗️ System Architecture

- **User Input** → **Streamlit UI**
- → **ChromaDB Semantic Retrieval**
- → **Prompt Engineering**
- → **Groq Llama 3 API**
- → **Property Recommendation**
- → **Streamlit Output**

(See detailed diagram in `docs/system_architecture.png`.)

---

## 📈 Performance

- Average Query Response Time: 3–5 seconds
- Contextual Relevance Accuracy: ~95%
- System is stable for large property datasets.

---

## 🚧 Challenges Faced

- Managing dynamic paths across different environments.
- Reducing hallucinations in AI responses.
- Handling minor warnings from PyTorch and Streamlit compatibility.

---

## 🌟 Future Enhancements

- Fine-tuning LLM on real estate-specific conversations.
- Adding multi-turn chat (e.g., "show me cheaper options").
- Integrating property images alongside AI recommendations.
- Deploying on Streamlit Sharing or Hugging Face Spaces.

---

## 🛡 Ethical Considerations

- No personal user data collected.
- Neutral, bias-checked property suggestions.
- Transparent AI recommendation disclaimer.

---

## 🤝 Contributions

Pull requests are welcome!  
For major changes, please open an issue first to discuss what you would like to change.

---

## 📬 Contact

- Developer: Sijoy Almeida
- Email: almeida.si@northeastern.edu

---

## 📄 License

This project is licensed under the MIT License.

---

# 📣 Final Note

If you found this project helpful or interesting, feel free to ⭐ star the repository!  
Thank you for exploring RealEstateGenie! 🚀🏠
