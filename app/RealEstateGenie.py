# RealEstateGenie: Your AI Home Finder 🏡
# Developed for VSCode + Streamlit Deployment
# ----------------------------------------------------------

# 📚 Import necessary libraries
import pandas as pd # type: ignore
import chromadb # type: ignore
import streamlit as st # type: ignore
import os
from groq import Groq # type: ignore
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# ----------------------------------------------------------
# Step 1: Data Loading (assuming cleaned CSV is available)
# ----------------------------------------------------------

import os

# Dynamically find the path to data folder
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "real_estate_cleaned.csv")


# Check if the cleaned CSV exists
if not os.path.exists(DATA_FILE):
    st.error(f"❌ Required file '{DATA_FILE}' not found. Please upload or generate it first.")
    st.stop()

# Load the cleaned dataset
df = pd.read_csv(DATA_FILE)
print(f"✅ Loaded cleaned dataset with {len(df)} rows.")

# ----------------------------------------------------------
# Step 2: Initialize ChromaDB
# ----------------------------------------------------------

chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="real_estate")
print("✅ Initialized ChromaDB and loaded collection.")

# Prepare embeddings if needed
if len(collection.get()['ids']) == 0:
    docs = df['text'].fillna('').tolist()
    ids = [f"prop_{i}" for i in range(len(docs))]
    collection.add(documents=docs, ids=ids)
    print(f"🚀 Embedded and stored {len(docs)} documents into ChromaDB.")

# ----------------------------------------------------------
# Step 3: Connect to Groq API
# ----------------------------------------------------------

# ⚡ Replace with your real Groq API key
groq_api_key = "groq_api_key"
groq_client = Groq(api_key=groq_api_key)
print("✅ Connected to Groq API.")

# ----------------------------------------------------------
# Step 4: Retrieval and Answering Function
# ----------------------------------------------------------

def retrieve_and_answer(user_query):
    if not user_query.strip():
        return "⚠️ Please enter a valid search query."

    # Retrieve top 5 similar properties
    results = collection.query(query_texts=[user_query], n_results=5)

    context_docs = results['documents'][0] if 'documents' in results else []
    if not context_docs:
        return "❌ No matching properties found. Please refine your search."

    # Filter very small entries
    context_docs = [doc for doc in context_docs if len(doc.split()) > 10]
    if not context_docs:
        return "❌ Found entries are too short. Try a different query."

    # Combine for prompt
    context_combined = " ".join(context_docs)

    # Build professional prompt
    prompt = f"""
You are an expert real estate assistant helping clients find ideal homes.

Listings:
{context_combined}

Client Request:
{user_query}

🔹 Instructions:
- Select the best matching property.
- Mention price, bedrooms, bathrooms, area (sqft), location.
- Highlight 1-2 unique features (like garden, pool, etc).
- Be professional and friendly.
- Summarize within 3-5 sentences.
"""

    # Send prompt to Groq (Model: Llama-3 / Mixtral)
    response = groq_client.chat.completions.create(
        model="llama3-8b-8192",  
        messages=[
            {"role": "system", "content": "You are a smart real estate assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4,
        max_tokens=500
    )

    final_answer = response.choices[0].message.content
    return final_answer

# ----------------------------------------------------------
# Step 5: Streamlit UI
# ----------------------------------------------------------

# Page configuration
st.set_page_config(page_title="🏡 RealEstateGenie", layout="centered")

# Main Title
st.title("🏡 RealEstateGenie")
st.subheader("🔍 Find Your Dream Home with AI Assistance")

# Input field
user_query = st.text_input("Enter your home search query (e.g., 4BHK near park, under $600k):")

# Button action
if st.button("🔍 Search Home"):
    if user_query.strip() == "":
        st.warning("⚠️ Please enter a valid search query above.")
    else:
        with st.spinner("✨ Analyzing and finding the best matches..."):
            answer = retrieve_and_answer(user_query)

        st.success("🏡 Here’s the Best Match Recommendation:")
        st.write(answer)

# Footer
st.caption("Built with ❤️ using Streamlit, ChromaDB, and Groq's LLMs. by sijoy almeida")

