# RAG-based PDF Chat Application

An AI-powered PDF chat application that allows you to upload PDF documents and ask questions about their content using Google's Gemini AI and Retrieval-Augmented Generation (RAG) technology.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🌟 Features

- 📄 **PDF Upload**: Upload any PDF document for analysis
- 🤖 **AI-Powered Q&A**: Ask questions and get intelligent answers based on PDF content
- 🧠 **RAG Technology**: Uses Retrieval-Augmented Generation for accurate, context-aware responses
- 💾 **Vector Storage**: Efficient document embedding storage using FAISS
- ⚡ **Fast Retrieval**: Quick similarity search for relevant document chunks
- 🔄 **Persistent Embeddings**: Save and reuse embeddings to avoid reprocessing

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) - Interactive web application framework
- **LLM**: [Google Gemini](https://ai.google.dev/) - Large Language Model (gemini-1.5-flash)
- **RAG Framework**: [LangChain](https://python.langchain.com/) - LLM application framework
- **Vector Database**: [FAISS](https://github.com/facebookresearch/faiss) - Facebook AI Similarity Search
- **PDF Processing**: [PyPDF2](https://pypdf2.readthedocs.io/) - PDF text extraction
- **Embeddings**: Google's `models/embedding-001`

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package installer (included with Python)
- **Google API Key** - Get it from [Google AI Studio](https://makersuite.google.com/app/apikey)

## 🚀 Installation

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/amanrajfr/rag-hosting.git
cd rag-hosting
```

### 2. Create a Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `streamlit` - Web application framework
- `PyPDF2` - PDF processing
- `python-dotenv` - Environment variable management
- `streamlit-extras` - Additional Streamlit components
- `langchain` - LLM framework
- `faiss-cpu` - Vector database
- `google-generativeai` - Google AI SDK
- `langchain-google-genai` - LangChain integration for Google AI
- `langchain-community` - Community integrations

### 4. Set Up Environment Variables

Create a `.env` file in the project root directory:

```bash
# Windows
copy NUL .env

# macOS/Linux
touch .env
```

Open the `.env` file and add your Google API key:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

> **🔑 How to Get a Google API Key:**
> 1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
> 2. Sign in with your Google account
> 3. Click "Create API Key"
> 4. Copy the generated key and paste it in your `.env` file

> **⚠️ Security Warning:**
> - Never commit your `.env` file to version control
> - The `.gitignore` file is already configured to exclude it
> - Never share your API key publicly

## 🌐 Deployment

Want to host this app online? Check out our **[Deployment Guide](DEPLOYMENT.md)** for detailed instructions on deploying to:

- 🚀 **Streamlit Community Cloud** (Recommended - Free & Easy)
- 🔧 **Render** (Free tier available)
- 🚄 **Railway** (Modern platform)
- 🐳 **Docker** (Self-hosting)

**Quick Deploy to Streamlit Cloud:**
1. Visit [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Select this repository
4. Add your `GOOGLE_API_KEY` to secrets
5. Deploy! 🎉

👉 **[Read Full Deployment Guide →](DEPLOYMENT.md)**

---

## 🎮 Usage

### Running the Application

Start the Streamlit application:

```bash
streamlit run rag.py
```

The application will:
- Launch a local web server (default: `http://localhost:8501`)
- Automatically open in your default web browser

### Using the Application

1. **Upload a PDF**
   - Click the "Upload your PDF" button
   - Select a PDF file from your computer
   - Wait for the PDF to be processed

2. **Ask Questions**
   - Type your question in the text input field
   - Press Enter or click outside the field
   - The AI will analyze the PDF and provide an answer

3. **View Embeddings Status**
   - First upload: Embeddings are computed and saved
   - Subsequent uploads of same file: Embeddings are loaded from disk (faster)

## 📁 Project Structure

```
rag-hosting/
├── rag.py                  # Main application file
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not in repo)
├── .gitignore             # Git ignore rules
├── README.md              # Project documentation
└── *.faiss                # FAISS index files (generated)
```

## 🧪 How It Works

1. **PDF Upload**: User uploads a PDF document
2. **Text Extraction**: PyPDF2 extracts text from all pages
3. **Text Chunking**: Text is split into manageable chunks (1000 chars, 200 overlap)
4. **Embedding Generation**: Each chunk is converted to vector embeddings using Google's model
5. **Vector Storage**: Embeddings are stored in FAISS vector database
6. **Query Processing**: User asks a question
7. **Similarity Search**: FAISS finds the 3 most relevant chunks
8. **Answer Generation**: Gemini generates an answer based on retrieved chunks

## 🔧 Configuration

You can modify these settings in `rag.py`:

```python
# Text splitting parameters
chunk_size=1000          # Size of each text chunk
chunk_overlap=200        # Overlap between chunks

# LLM parameters
model="gemini-1.5-flash"  # Gemini model to use
temperature=0            # Response randomness (0 = deterministic)

# Similarity search
k=3                      # Number of relevant chunks to retrieve
```

## 🐛 Troubleshooting

### Common Issues

**Issue: "ModuleNotFoundError"**
```bash
# Solution: Reinstall dependencies
pip install -r requirements.txt
```

**Issue: "API Key Error"**
```bash
# Solution: Check your .env file
# Ensure GOOGLE_API_KEY is set correctly
# No spaces around the = sign
# No quotes needed
```

**Issue: "FAISS not found"**
```bash
# Solution: Install FAISS
pip install faiss-cpu
```

**Issue: "Streamlit not opening in browser"**
```bash
# Solution: Manually open the URL
# Check terminal for the URL (usually http://localhost:8501)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

Created by **PBL GROUP** © 2025

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [LangChain](https://python.langchain.com/) for RAG implementation
- [Google](https://ai.google.dev/) for the Gemini AI model
- [Facebook AI Research](https://github.com/facebookresearch/faiss) for FAISS

## 📧 Support

If you have any questions or issues, please open an issue on GitHub.

---

**⭐ If you find this project useful, please consider giving it a star!**