# 📢 Sentiment Analysis — Amazon Alexa Reviews

A machine learning project to classify sentiments (Positive 😊, Neutral 😐, Negative 😠) from Amazon Alexa product reviews using Natural Language Processing (NLP) and Support Vector Machine (SVM). The project also includes an interactive and colorful Streamlit web app with emojis to visualize predictions.

---

## 📌 Project Highlights

- ✅ Text preprocessing with tokenization, stemming, stopword removal, and TF-IDF vectorization
- ✅ Sentiment classification into 3 categories (Positive, Neutral, Negative)
- ✅ Trained using Logistic Regression, Decision Tree, and SVM (SVM chosen as final model)
- ✅ Interactive and emoji-enhanced Streamlit UI
- ✅ Model saved using `pickle` for deployment

---

## 🧠 Machine Learning Workflow

1. **Data Loading**: Amazon Alexa reviews dataset (CSV format)
2. **Preprocessing**:
   - Clean text: remove punctuation, lowercase, remove stopwords
   - Stemming using NLTK’s PorterStemmer
3. **TF-IDF Vectorization** for feature extraction
4. **Label Encoding**: Map sentiment to numeric (0 = Negative, 1 = Neutral, 2 = Positive)
5. **Modeling**: Train models using Logistic Regression, Decision Tree, and SVM
6. **Evaluation**: Accuracy and F1 Score
7. **Deployment**: Streamlit app for real-time predictions

---

## 🚀 Streamlit App Features

- 🎨 Color-coded sentiment display
- 😊 Emojis to enhance prediction output
- 💬 Text area for user input
- 📊 Live model prediction using saved SVM model

---

## 🛠️ Tech Stack

| Component           | Technology           |
|--------------------|----------------------|
| Programming Lang.  | Python               |
| Data Handling      | Pandas, NumPy        |
| NLP                | NLTK, re, string     |
| ML Models          | Scikit-learn         |
| Web App            | Streamlit            |
| Model Storage      | Pickle               |
| Visualization      | Emojis + Color Blocks|

---

## 📂 Folder Structure

Sentiment-Analysis---Amazon-Alexa-Reviews/
│
├── app.py # Streamlit app

├── data.csv # Raw dataset

├── tfidf_vectorizer.pkl # Saved TF-IDF vectorizer

├── svm_model.pkl # Trained SVM model

├── README.md # Project documentation

└── requirements.txt # All dependencies


---




![Screenshot 2025-05-31 165025](https://github.com/user-attachments/assets/7d6bd380-cca9-439c-8c1f-0ea80fa70b51)

## ✍️ Author
HARIPRAKASH.N
LinkedIn - linkedin.com/in/hariprakash015/
Email - hariprakash3004@gmail.com


