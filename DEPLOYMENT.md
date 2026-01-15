# Deployment Guide - RAG PDF Chat Application

This guide provides detailed instructions for deploying your RAG-based PDF Chat application to various cloud platforms.

## Table of Contents

- [Streamlit Community Cloud (Recommended)](#streamlit-community-cloud-recommended)
- [Render Deployment](#render-deployment)
- [Railway Deployment](#railway-deployment)
- [Docker Deployment](#docker-deployment)
- [Troubleshooting](#troubleshooting)

---

## Streamlit Community Cloud (Recommended)

**Best for:** Quick deployment, free hosting, automatic updates from GitHub

### Prerequisites

- ✅ GitHub account with your code pushed to a repository
- ✅ Google API key for Gemini
- ✅ Code must be in a public GitHub repository (or private with Streamlit Teams)

### Step-by-Step Deployment

#### 1. Sign Up / Sign In

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **"Continue with GitHub"**
3. Authorize Streamlit to access your GitHub repositories
4. Grant access to the `amanrajfr/rag-hosting` repository

#### 2. Create New App

1. On the Streamlit Cloud dashboard, click **"New app"**
2. You'll see a deployment configuration form

#### 3. Configure Deployment Settings

Fill in the following fields:

| Field | Value | Description |
|-------|-------|-------------|
| **Repository** | `amanrajfr/rag-hosting` | Your GitHub repository |
| **Branch** | `main` | The branch to deploy from |
| **Main file path** | `rag.py` | The entry point of your app |
| **App URL** | Custom (e.g., `rag-pdf-chat`) | Your app's subdomain |

#### 4. Add Secrets (Environment Variables)

> **⚠️ CRITICAL STEP:** Your app won't work without this!

1. Click **"Advanced settings"** at the bottom of the form
2. In the **"Secrets"** section, add your environment variables in **TOML format**:

```toml
# Streamlit secrets.toml format
GOOGLE_API_KEY = "AIzaSyAatSYH_unqI4k23XuZpKi7ws846PpQ-Qc"
```

**Important Notes:**
- Use the exact TOML format (key = "value")
- Include quotes around the API key
- Do NOT use `.env` format (won't work)
- These secrets are encrypted and secure

#### 5. Deploy Your App

1. Click the **"Deploy!"** button
2. Watch the build logs in real-time
3. Build process typically takes **2-5 minutes**

#### 6. Build Process

You'll see logs showing:
```
Cloning repository...
Installing dependencies from requirements.txt...
Starting Streamlit app...
```

#### 7. Access Your App

Once deployed, your app will be available at:
```
https://your-app-name.streamlit.app
```

Share this URL with anyone to let them use your app! 🎉

### Managing Your Deployed App

#### View Logs

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click on your app
3. Click **"Manage app"** → **"Logs"**

#### Update Secrets

1. Click **"Settings"** → **"Secrets"**
2. Edit your TOML configuration
3. Click **"Save"**
4. App will automatically restart

#### Update Code

**Automatic Updates:**
- Push changes to your GitHub repository
- Streamlit Cloud automatically detects changes
- App redeploys automatically (takes 2-3 minutes)

**Manual Reboot:**
1. Go to app settings
2. Click **"Reboot app"**

#### Delete App

1. Go to app settings
2. Click **"Delete app"**
3. Confirm deletion

### Streamlit Cloud Limits (Free Tier)

| Resource | Limit |
|----------|-------|
| **Apps** | Up to 3 public apps |
| **RAM** | 1 GB per app |
| **CPU** | 1 vCPU core |
| **Storage** | Temporary storage only |
| **Sleep** | Apps sleep after 7 days of inactivity |
| **Bandwidth** | Fair use policy |

### Best Practices

- ✅ Keep dependencies minimal in `requirements.txt`
- ✅ Use `@st.cache_data` and `@st.cache_resource` for better performance
- ✅ Monitor app usage in the dashboard
- ✅ Test locally before pushing updates
- ⚠️ Large PDF files may hit memory limits

---

## Render Deployment

**Best for:** More control, larger resource needs, free tier available

### Prerequisites

- GitHub account with your repository
- Render account (sign up at [render.com](https://render.com))

### Step-by-Step Deployment

#### 1. Create Render Account

1. Go to [render.com](https://render.com)
2. Click **"Get Started"**
3. Sign up with GitHub

#### 2. Create Web Service

1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub account if not already connected
3. Select `amanrajfr/rag-hosting` repository

#### 3. Configure Service

| Setting | Value |
|---------|-------|
| **Name** | `rag-pdf-chat` |
| **Region** | Choose closest to your users |
| **Branch** | `main` |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `streamlit run rag.py --server.port=$PORT --server.address=0.0.0.0` |

#### 4. Add Environment Variables

1. Scroll to **"Environment Variables"**
2. Click **"Add Environment Variable"**
3. Add:
   - **Key:** `GOOGLE_API_KEY`
   - **Value:** `AIzaSyAatSYH_unqI4k23XuZpKi7ws846PpQ-Qc`

#### 5. Select Plan

- **Free Tier**: 512 MB RAM, sleeps after inactivity
- **Paid Plans**: Starting at $7/month, always-on

#### 6. Deploy

1. Click **"Create Web Service"**
2. Wait for deployment (5-10 minutes first time)
3. Access your app at: `https://your-app-name.onrender.com`

### Render Free Tier Notes

⚠️ **Important Limitations:**
- Apps spin down after 15 minutes of inactivity
- Cold start takes 30-60 seconds
- 750 hours/month free (shared across all free services)

---

## Railway Deployment

**Best for:** Modern platform, generous free tier, easy setup

### Step-by-Step Deployment

#### 1. Create Railway Account

1. Go to [railway.app](https://railway.app)
2. Click **"Login"** → **"Login with GitHub"**
3. Authorize Railway

#### 2. Create New Project

1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Choose `amanrajfr/rag-hosting`

#### 3. Add Environment Variables

1. Click on your deployed service
2. Go to **"Variables"** tab
3. Click **"New Variable"**
4. Add:
   - **Key:** `GOOGLE_API_KEY`
   - **Value:** Your API key

#### 4. Configure Start Command

Railway auto-detects Streamlit apps, but you can customize:

1. Go to **"Settings"** tab
2. Under **"Deploy"**, set:
   - **Start Command:** `streamlit run rag.py --server.port=$PORT --server.address=0.0.0.0`

#### 5. Deploy

- Railway automatically builds and deploys
- Access your app at the generated Railway URL
- You can add a custom domain

### Railway Free Tier

- $5 free credits per month
- Pay-as-you-go after credits
- No sleep/cold start issues

---

## Docker Deployment

**Best for:** Self-hosting, custom infrastructure, advanced users

### Create Dockerfile

Create a file named `Dockerfile` in your project root:

```dockerfile
# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Set environment variables
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run the application
CMD ["streamlit", "run", "rag.py"]
```

### Create .dockerignore

Create `.dockerignore` file:

```
.env
.git
.gitignore
__pycache__
*.pyc
*.pyo
*.pyd
.Python
*.faiss
*.pkl
venv/
env/
```

### Build and Run Docker Container

```bash
# Build the image
docker build -t rag-pdf-chat .

# Run the container
docker run -p 8501:8501 \
  -e GOOGLE_API_KEY="your_api_key_here" \
  rag-pdf-chat
```

### Deploy to Docker Hosting

You can deploy your Docker container to:
- **AWS ECS/Fargate**
- **Google Cloud Run**
- **Azure Container Instances**
- **DigitalOcean App Platform**
- **Fly.io**

---

## Troubleshooting

### Common Issues and Solutions

#### Issue 1: App Won't Start

**Symptoms:** Build succeeds but app crashes on startup

**Solutions:**
```bash
# Check if all dependencies are in requirements.txt
pip freeze > requirements.txt

# Ensure port configuration is correct
# For Streamlit Cloud: No changes needed
# For Render/Railway: Use --server.port=$PORT

# Check logs for error messages
```

#### Issue 2: API Key Not Working

**Symptoms:** "API key error" or authentication failures

**Solutions:**
- ✅ Verify API key is correctly added to secrets/environment variables
- ✅ Check for extra spaces or quotes in the key
- ✅ Ensure TOML format for Streamlit Cloud: `GOOGLE_API_KEY = "key"`
- ✅ Test API key locally first
- ✅ Regenerate API key if necessary

#### Issue 3: Out of Memory Errors

**Symptoms:** App crashes when processing large PDFs

**Solutions:**
```python
# Reduce chunk size in rag.py
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,  # Reduced from 1000
    chunk_overlap=100,  # Reduced from 200
)

# Limit PDF file size
max_file_size = 10 * 1024 * 1024  # 10 MB
if pdf.size > max_file_size:
    st.error("File too large. Maximum size: 10 MB")
```

#### Issue 4: Slow Performance

**Solutions:**
- Use Streamlit caching for embeddings
- Upgrade to paid tier for more resources
- Optimize FAISS index settings
- Implement pagination for large documents

#### Issue 5: Dependencies Won't Install

**Symptoms:** Build fails during `pip install`

**Solutions:**
```bash
# Pin specific versions in requirements.txt
streamlit==1.31.0
PyPDF2==3.0.1
# ... etc

# For FAISS issues, try:
faiss-cpu==1.7.4  # Use specific version
```

#### Issue 6: App Sleeps on Free Tier

**Solutions:**
- Use a uptime monitoring service (e.g., UptimeRobot) to ping your app
- Upgrade to paid tier for always-on hosting
- Accept cold starts as part of free tier

### Getting Help

If you're still experiencing issues:

1. **Check Deployment Logs:** Most platforms show detailed build/runtime logs
2. **Test Locally:** Ensure app runs with `streamlit run rag.py` locally
3. **Streamlit Forum:** [discuss.streamlit.io](https://discuss.streamlit.io)
4. **GitHub Issues:** Check if others have similar issues
5. **Platform Support:** Contact platform-specific support

---

## Production Checklist

Before deploying to production:

- [ ] Remove hardcoded API keys from code
- [ ] Add API key to platform secrets/environment variables
- [ ] Test app thoroughly with sample PDFs
- [ ] Set up error monitoring (optional: Sentry, LogRocket)
- [ ] Configure custom domain (if needed)
- [ ] Add usage analytics (optional: Streamlit analytics)
- [ ] Set up automated backups (if storing data)
- [ ] Review and optimize `requirements.txt`
- [ ] Add rate limiting for API calls (if needed)
- [ ] Test with different PDF sizes and types
- [ ] Document any platform-specific configurations
- [ ] Set up GitHub branch protection (optional)

---

## Monitoring Your Deployed App

### Streamlit Cloud Analytics

1. Go to your app dashboard
2. Click **"Analytics"**
3. View:
   - Active users
   - Page views
   - Response times
   - Error rates

### Custom Monitoring

Add to your `rag.py`:

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Log user interactions
logger.info(f"PDF uploaded: {pdf.name}")
logger.info(f"Query asked: {query}")
```

---

## Updating Your Deployed App

### Streamlit Cloud

```bash
# Make changes locally
git add .
git commit -m "Update feature"
git push origin main

# Streamlit Cloud auto-deploys (2-3 minutes)
```

### Other Platforms

Most platforms (Render, Railway) also auto-deploy from GitHub:

1. Push changes to GitHub
2. Platform detects changes
3. Automatically rebuilds and redeploys

To disable auto-deploy, check platform-specific settings.

---

## Cost Comparison

| Platform | Free Tier | Paid Plans | Best For |
|----------|-----------|------------|----------|
| **Streamlit Cloud** | 3 apps, 1GB RAM | Teams: $250/month | Streamlit apps |
| **Render** | 750 hrs/month | $7/month+ | Flexibility |
| **Railway** | $5 credits/month | Pay-as-you-go | Modern UI |
| **Heroku** | ❌ (discontinued) | $7/month+ | Legacy apps |
| **Google Cloud Run** | Free tier available | Pay-per-use | Scalability |

---

## Security Best Practices

### Protecting Your API Keys

- ✅ **Always** use environment variables for secrets
- ✅ **Never** commit `.env` files to Git
- ✅ Add `.env` to `.gitignore`
- ✅ Rotate API keys regularly
- ✅ Use separate keys for development and production
- ✅ Monitor API usage in Google Cloud Console

### User Data Protection

- ✅ Don't store uploaded PDFs permanently (Streamlit clears session data)
- ✅ Don't log sensitive information
- ✅ Inform users about data processing
- ✅ Consider adding file size limits
- ✅ Validate and sanitize user inputs

---

## Next Steps

After successful deployment:

1. **Share Your App:** Send the URL to users
2. **Monitor Usage:** Check analytics regularly
3. **Gather Feedback:** Improve based on user input
4. **Update README:** Add live demo link
5. **Consider Upgrades:** Evaluate paid tiers if needed

---

## Additional Resources

- [Streamlit Deployment Docs](https://docs.streamlit.io/streamlit-community-cloud)
- [Render Documentation](https://render.com/docs)
- [Railway Documentation](https://docs.railway.app)
- [Streamlit Forum](https://discuss.streamlit.io)
- [LangChain Deployment Guide](https://python.langchain.com/docs/guides/deployment)

---

**📝 Document Version:** 1.0  
**Last Updated:** 2026-01-16  
**Author:** PBL Group

---

> **💡 Pro Tip:** Start with Streamlit Cloud for the easiest deployment. You can always migrate to other platforms later if you need more resources or features!
