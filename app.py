import os
from dotenv import load_dotenv

from langchain_community.document_loaders import YoutubeLoader

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_core.runnables import chain, RunnablePassthrough, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware

import zipfile 
import streamlit as st
import re

load_dotenv()

GEMINI_API_KEY = st.secrets["gemini_key"]

os.environ["GEMINI_API_KEY"] = os.getenv("gemini_key")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

system_message = 'You are an Professional Article Writer specializing in writing articles for Medium, LinkedIn, and tech blogs.'

human_message = '''
Transform YouTube transcript into **engaging, professional articles** with:

**CRITICAL INSTRUCTIONS**:
- **IGNORE** Introductionary notes like welcome, In this video
- **IGNORE** all channel names, "subscribe", "like", "comment", "follow", "check description" 
- **IGNORE** marketing phrases: "my course", "my discord", "affiliate links", "sponsors"
- **FOCUS ONLY** on technical content, code, tutorials, actionable insights

**MANDATORY ARTICLE STRUCTURE** (exact Medium/LinkedIn format):
- Write in **first-person professional tone** 
- Use **bold subheadings**, **numbered lists**.
- Include **code snippets** for technical videos
- Make **Actionable Steps** copy-paste ready
- End with **short summary of the article**
{transcript}
'''
# Prompt Template
summarizer_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_message),
    HumanMessagePromptTemplate.from_template(human_message)
])

# Create transcript tool
def extract_transcript(link: str):
    """
    Extract YouTube transcript using YoutubeLoader
    Input: YouTube URL → Output: Transcript text
    """
    loader = YoutubeLoader.from_youtube_url(link)
    doc = loader.load()
    return doc[0].page_content

# BASE SUMMARIZER (short transcripots < 1000 tokens)
base_summarizer = RunnablePassthrough() | RunnableLambda(extract_transcript) | summarizer_prompt | llm | StrOutputParser()

# Summarizing Long Transcripts # Agent
agent = create_agent(
    model=llm,
    tools=[],   # NO tools - summarization ONLY
    system_prompt = system_message,
    middleware=[
        SummarizationMiddleware(
            model=llm,
            trigger=("tokens", 1000),     # Summarize when conversation hits 1000 tokens
            keep=("tokens", 200)        # Preserve last 200 tokens verbatim
        )
    ]
)

# Postprocess the output of agent
def clean_output(output):
    return output.content

long_summarizer = RunnablePassthrough() | RunnableLambda(extract_transcript) | summarizer_prompt | llm | RunnableLambda(clean_output)

# RUNNABLE BRANCH - Routes automatically based on transcript length
def estimate_transcript_length(link: str) -> bool:
    """Quick length estimator (characters → tokens)."""
    transcript = extract_transcript(link)
    return len(transcript) >= 1000  # Returns True for long transcripts

system_message = """You are a Senior Frontend Web Developer with 10+ years experience in HTML5, CSS3, and modern JavaScript (ES6+).

Your task: Generate COMPLETE, PRODUCTION-READY frontend code based on user requirements.

**MANDATORY OUTPUT FORMAT** (exact delimiters):
--html--
[html code here]
--html--

--css--
[css code here]
--css--

--js--
[java script code here]
--js--
"""


human_message = '''
Create a **production-ready article webpages** in the style of **Medium, Dev.to, Hashnode, and Substack**.

**MANDATORY REQUIREMENTS**:
- **Mobile-first responsive design** (perfect on all devices)
- **Clean, modern typography** (system fonts + readability first)
- **Medium-like article layout** with card-based design
- **Dark/light theme toggle**
- **Smooth animations** and **scroll effects**
- **SEO optimized** with proper meta tags
- **Accessibility compliant** (ARIA labels, keyboard navigation)

**CONTENT TO USE**: {article_content}
'''

web_dev_template = ChatPromptTemplate.from_messages([system_message, human_message])

smart_summarizer = RunnableBranch(
    # Condition: if transcript ≥ 1000 words → long handler
    (RunnableLambda(estimate_transcript_length), long_summarizer),

    # Else: base summarizer for short transcripts
    base_summarizer) | web_dev_template | llm | StrOutputParser()

st.set_page_config(page_title="YouTube → Article Generator", layout="wide")

st.title("🎥 YouTube to Article & Website Generator")
st.markdown("Convert any YouTube video into a **professional article + full webpage**")

# -------------------------------
# Input
# -------------------------------
user_input = st.text_input("Enter YouTube URL")

def is_valid_youtube_url(url):
    pattern = r"(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+"
    return re.match(pattern, url)

# -------------------------------
# Generate Button
# -------------------------------
if st.button("🚀 Generate Article & Website"):

    if not user_input:
        st.warning("⚠️ Please enter a YouTube URL")
    
    elif not is_valid_youtube_url(user_input):
        st.error("❌ Invalid YouTube URL")
    
    else:
        with st.spinner("⏳ Processing video... This may take some time"):

            try:
                article = smart_summarizer.invoke(user_input)

                # -------------------------------
                # Extract code blocks
                # -------------------------------
                html_code = article.split('--html--')[1]
                css_code = article.split('--css--')[1]
                js_code = article.split('--js--')[1]

                # -------------------------------
                # Save files
                # -------------------------------
                with open('index.html', 'w', encoding='utf-8') as f:
                    f.write(html_code)

                with open('style.css', 'w', encoding='utf-8') as f:
                    f.write(css_code)

                with open('script.js', 'w', encoding='utf-8') as f:
                    f.write(js_code)

                # -------------------------------
                # Create ZIP
                # -------------------------------
                with zipfile.ZipFile('website.zip', 'w') as zipf:
                    zipf.write('index.html')
                    zipf.write('style.css')
                    zipf.write('script.js')

                # -------------------------------
                # UI Output
                # -------------------------------
                st.success("✅ Website Generated Successfully!")

                st.download_button(
                    label="📥 Download Website ZIP",
                    data=open("website.zip", "rb"),
                    file_name="website.zip",
                    mime="application/zip"
                )

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
