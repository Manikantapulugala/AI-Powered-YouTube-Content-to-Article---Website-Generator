<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>YouTube → Article & Website Generator</title>

    <style>
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
        }

        body{
            font-family: Arial, Helvetica, sans-serif;
            background:#0f172a;
            color:#f8fafc;
            line-height:1.7;
        }

        .container{
            width:90%;
            max-width:1100px;
            margin:auto;
            padding:40px 0;
        }

        h1,h2,h3{
            margin-bottom:20px;
            color:#38bdf8;
        }

        h1{
            font-size:42px;
            text-align:center;
            margin-bottom:30px;
        }

        p{
            margin-bottom:16px;
        }

        .card{
            background:#1e293b;
            padding:25px;
            border-radius:14px;
            margin-bottom:25px;
            box-shadow:0 4px 10px rgba(0,0,0,0.3);
        }

        ul{
            padding-left:20px;
        }

        li{
            margin-bottom:10px;
        }

        code{
            background:#334155;
            padding:3px 6px;
            border-radius:5px;
            color:#facc15;
        }

        pre{
            background:#020617;
            padding:20px;
            overflow-x:auto;
            border-radius:10px;
            margin-top:15px;
        }

        .highlight{
            color:#facc15;
            font-weight:bold;
        }

        .footer{
            text-align:center;
            margin-top:40px;
            color:#94a3b8;
        }

        @media(max-width:768px){
            h1{
                font-size:30px;
            }

            .container{
                width:95%;
            }
        }
    </style>
</head>

<body>

    <div class="container">

        <h1>🎥 YouTube → Article & Website Generator</h1>

        <div class="card">
            <p>
                An AI-powered application that converts YouTube videos into
                professional articles and fully responsive websites automatically
                using <span class="highlight">Python, LangChain, Gemini AI, and Streamlit</span>.
            </p>
        </div>

        <div class="card">
            <h2>🚀 Features</h2>

            <ul>
                <li>✅ Extract YouTube transcripts automatically</li>
                <li>✅ Convert transcripts into Medium/LinkedIn-style articles</li>
                <li>✅ Remove promotional content like sponsors and subscribe messages</li>
                <li>✅ Generate HTML, CSS, and JavaScript automatically</li>
                <li>✅ Download website as ZIP file</li>
                <li>✅ Mobile responsive design</li>
                <li>✅ Dark/Light theme support</li>
                <li>✅ SEO-friendly webpage generation</li>
                <li>✅ Smart handling for short and long transcripts</li>
            </ul>
        </div>

        <div class="card">
            <h2>🛠 Tech Stack</h2>

            <ul>
                <li>Python</li>
                <li>Streamlit</li>
                <li>LangChain</li>
                <li>Google Gemini AI</li>
                <li>HTML5</li>
                <li>CSS3</li>
                <li>JavaScript</li>
                <li>YouTube Transcript Loader</li>
            </ul>
        </div>

        <div class="card">
            <h2>📂 Project Structure</h2>

<pre>
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
</pre>

        </div>

        <div class="card">
            <h2>⚙️ Installation</h2>

            <h3>1️⃣ Clone Repository</h3>

<pre>
git clone https://github.com/your-username/youtube-article-generator.git

cd youtube-article-generator
</pre>

            <h3>2️⃣ Create Virtual Environment</h3>

<pre>
python -m venv venv
</pre>

            <h3>3️⃣ Activate Environment</h3>

            <p><strong>Windows</strong></p>

<pre>
venv\Scripts\activate
</pre>

            <p><strong>Mac/Linux</strong></p>

<pre>
source venv/bin/activate
</pre>

            <h3>4️⃣ Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

        </div>

        <div class="card">
            <h2>🔑 Environment Variables</h2>

            <p>Create a <code>.env</code> file:</p>

<pre>
gemini_key=YOUR_GEMINI_API_KEY
</pre>

        </div>

        <div class="card">
            <h2>▶️ Run Application</h2>

<pre>
streamlit run app.py
</pre>

        </div>

        <div class="card">
            <h2>🧠 How It Works</h2>

            <ul>
                <li><strong>Step 1:</strong> Extract transcript from YouTube video</li>
                <li><strong>Step 2:</strong> AI generates professional article</li>
                <li><strong>Step 3:</strong> Frontend webpage is generated</li>
                <li><strong>Step 4:</strong> Files are packed into ZIP</li>
            </ul>
        </div>

        <div class="card">
            <h2>✨ AI Workflow</h2>

<pre>
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
</pre>

        </div>

        <div class="card">
            <h2>🔥 LangChain Concepts Used</h2>

            <ul>
                <li>RunnableBranch</li>
                <li>RunnableLambda</li>
                <li>RunnablePassthrough</li>
                <li>Prompt Templates</li>
                <li>Output Parsers</li>
                <li>Summarization Middleware</li>
            </ul>
        </div>

        <div class="card">
            <h2>🎯 Future Improvements</h2>

            <ul>
                <li>Multi-language support</li>
                <li>Medium/Dev.to publishing</li>
                <li>PDF article generation</li>
                <li>AI-generated thumbnails</li>
                <li>Voice narration support</li>
            </ul>
        </div>

        <div class="card">
            <h2>🤝 Contributing</h2>

<pre>
Fork the repository
Create your feature branch
Commit your changes
Push to the branch
Open a Pull Request
</pre>

        </div>

        <div class="card">
            <h2>📜 License</h2>

            <p>
                This project is licensed under the MIT License.
            </p>
        </div>

        <div class="card">
            <h2>👨‍💻 Author</h2>

            <p>
                Developed by Saikrishna 🚀
            </p>
        </div>

        <div class="card">
            <h2>⭐ Support</h2>

            <p>
                If you like this project:
            </p>

            <ul>
                <li>⭐ Star the repository</li>
                <li>🍴 Fork the project</li>
                <li>📢 Share with others</li>
            </ul>
        </div>

        <div class="card">
            <h2>📬 Contact</h2>

            <ul>
                <li>LinkedIn: Your LinkedIn Profile</li>
                <li>GitHub: Your GitHub Profile</li>
            </ul>
        </div>

        <div class="footer">
            <p>Made with ❤️ using AI & LangChain</p>
        </div>

    </div>

</body>
</html>
