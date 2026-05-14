# 🎥 YouTube → Article & Website Generator

An AI-powered application that converts YouTube videos into professional articles and fully responsive websites automatically using **Python**, **LangChain**, **Google Gemini AI**, and **Streamlit**.

---

# 🚀 Features

- ✅ Extract YouTube transcripts automatically  
- ✅ Convert transcripts into professional Medium/LinkedIn-style articles  
- ✅ Remove unnecessary promotional content such as:
  - Subscribe messages
  - Sponsorships
  - Affiliate links
  - Channel introductions
- ✅ Generate complete frontend files:
  - HTML
  - CSS
  - JavaScript
- ✅ Create downloadable ZIP website packages  
- ✅ Responsive modern UI  
- ✅ Dark/Light theme support  
- ✅ SEO-friendly webpage generation  
- ✅ Intelligent handling of both short and long transcripts  

---

# 🛠 Tech Stack

- Python  
- Streamlit  
- LangChain  
- Google Gemini AI  
- HTML5  
- CSS3  
- JavaScript  
- YouTube Transcript Loader  

---

# 📂 Project Structure

```bash
project/
│
├── app.py
├── .env
├── requirements.txt
├── index.html
├── style.css
├── script.js
├── website.zip
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/youtube-article-generator.git

cd youtube-article-generator
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root folder:

```env
gemini_key=YOUR_GEMINI_API_KEY
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 🧠 How It Works

## Step 1: Extract Transcript

The application fetches the YouTube transcript using the YouTube Transcript Loader.

---

## Step 2: AI Article Generation

Gemini AI transforms the transcript into a professional article by:

- Removing unnecessary promotional content
- Structuring content with headings and lists
- Generating readable technical explanations

---

## Step 3: Frontend Generation

The AI automatically generates:

- Responsive HTML
- Modern CSS
- Interactive JavaScript

---

## Step 4: ZIP Packaging

All generated files are automatically packaged into a downloadable ZIP file.

---

# ✨ AI Workflow

```text
YouTube URL
     ↓
Transcript Extraction
     ↓
AI Summarization
     ↓
Article Generation
     ↓
Frontend Code Generation
     ↓
Website ZIP Download
```

---

# 📸 Screenshots

## Home Page

> Add Screenshot Here

---

## Generated Website

> Add Screenshot Here

---

# 📦 Example Output

Generated files include:

```bash
index.html
style.css
script.js
website.zip
```

---

# 🔥 Key LangChain Concepts Used

- RunnableBranch  
- RunnableLambda  
- RunnablePassthrough  
- Prompt Templates  
- Output Parsers  
- Summarization Middleware  

---

# 🎯 Future Improvements

- Multi-language support  
- Blog export to Medium/Dev.to  
- PDF article generation  
- AI-generated thumbnails  
- Voice narration support  
