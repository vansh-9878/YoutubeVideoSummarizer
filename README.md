# 🎥 YouTube Transcript Summarizer 

This project fetches transcripts from YouTube videos using the `youtube-transcript-api` and generates a summary using `spaCy` and word frequency analysis.

## ✨ Features
✅ Extracts transcripts from YouTube videos 🎬  
✅ Supports **English** 📖  
✅ Summarizes the transcript based on word frequency analysis 🧠  

## 📥 Installation

### Prerequisites
Make sure you have **Python** installed. Then, install the required dependencies:

```bash
pip install youtube-transcript-api spacy
```

For **English support** in `spaCy`, download the English language model:
```bash
python -m spacy download en_core_web_sm
```

## 🚀 How to Run

1. **Open** `main.py` and enter the YouTube **video link** inside it.
2. **Run the script** using the command:

```bash
python main.py
```

## 📜 Example Output
```
Summary:
This is an example summary generated from the most frequent words in the transcript.
```

## 🔍 Notes
- Ensure that the video has **captions enabled** in English.
- `spaCy` is used for **NLP processing**, and the `n_core_web_sm` model is required.

## 📜 License
This project is licensed under the **GNU License**.

