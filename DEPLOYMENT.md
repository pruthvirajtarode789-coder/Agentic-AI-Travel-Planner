# 🚀 Deployment Guide - Render

This guide will help you deploy your Agentic AI Travel Planner to Render.

## 📋 Prerequisites

1. ✅ Git repository initialized (Done!)
2. ✅ GitHub account
3. ✅ Render account (free tier available)
4. ✅ Anthropic API key

---

## Step 1: Create GitHub Repository

### Option A: Using GitHub Website

1. Go to https://github.com/new
2. Repository name: `agentic-ai-travel-planner`
3. Description: `AI-powered travel planning assistant using LangChain, Claude AI, and Streamlit`
4. Set as **Public** (required for free Render deployment)
5. **DO NOT** initialize with README (we already have one)
6. Click "Create repository"

### Option B: Using GitHub CLI (if installed)

```bash
gh repo create agentic-ai-travel-planner --public --source=. --remote=origin --push
```

---

## Step 2: Push to GitHub

After creating the repository, run these commands:

```bash
# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/agentic-ai-travel-planner.git

# Push to GitHub
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

---

## Step 3: Deploy to Render

### A. Sign Up / Log In

1. Go to https://render.com/
2. Sign up or log in (you can use GitHub account)

### B. Create New Web Service

1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository:
   - Click **"Connect repository"**
   - Find `agentic-ai-travel-planner`
   - Click **"Connect"**

### C. Configure Web Service

Fill in these settings:

**Basic Settings:**
- **Name**: `agentic-ai-travel-planner`
- **Region**: `Singapore` (or nearest to you)
- **Branch**: `main`
- **Root Directory**: (leave blank)
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `streamlit run ui/app.py --server.port=$PORT --server.address=0.0.0.0`

**Instance Type:**
- Select **"Free"** (or paid if you prefer)

### D. Add Environment Variables

Click **"Advanced"** → **"Add Environment Variable"**

Add this variable:
- **Key**: `ANTHROPIC_API_KEY`
- **Value**: `your_actual_api_key_here`

**Get API Key:** https://console.anthropic.com/

### E. Deploy

1. Click **"Create Web Service"**
2. Wait 5-10 minutes for deployment
3. Once deployed, you'll get a URL like: `https://agentic-ai-travel-planner.onrender.com`

---

## Step 4: Verify Deployment

1. Open your Render URL
2. Test the application:
   - Enter "Delhi" → "Goa"
   - Set trip duration to 3 days
   - Click "Generate My Dream Trip"
3. Verify all features work:
   - ✅ AI reasoning
   - ✅ Flight search
   - ✅ Hotel recommendations
   - ✅ Weather forecast
   - ✅ Interactive map
   - ✅ Budget calculation

---

## 🛠️ Troubleshooting

### Issue: Build Fails

**Solution:** Check `requirements.txt` has all dependencies

```bash
# Update requirements if needed
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update requirements"
git push
```

### Issue: App Shows Error

**Solution:** Check Environment Variables
- Go to Render Dashboard → Your Service → Environment
- Verify `ANTHROPIC_API_KEY` is set correctly
- Click "Manual Deploy" → "Deploy latest commit"

### Issue: App is Slow

**Solution:** Free tier has limitations
- App sleeps after 15 minutes of inactivity
- First load after sleep takes ~30 seconds
- Consider upgrading to paid tier for better performance

### Issue: Can't Find Repository

**Solution:** Make sure repository is public
- Go to GitHub → Repository Settings
- Scroll to "Danger Zone"
- Change visibility to Public

---

## 📱 Render Dashboard Features

### View Logs
- Go to your service → **"Logs"** tab
- See real-time application logs
- Helpful for debugging

### Manual Deploy
- Go to **"Manual Deploy"**
- Click "Deploy latest commit"
- Useful after pushing updates

### Metrics
- View CPU and Memory usage
- Monitor requests and response times

---

## 🔄 Updating Your Deployment

When you make changes:

```bash
# Make your changes
git add .
git commit -m "Describe your changes"
git push

# Render auto-deploys on push!
```

Render will automatically detect the push and redeploy.

---

## 💡 Pro Tips

### 1. Custom Domain (Optional)
- Go to Settings → Custom Domains
- Add your own domain (e.g., travelplanner.yourdomain.com)

### 2. Health Checks
Render automatically monitors:
- HTTP status codes
- Response times
- App availability

### 3. Environment Groups
For multiple services:
- Create environment groups
- Share API keys across services

### 4. Free Tier Limitations
- App sleeps after 15 minutes
- 750 hours/month free
- Slower build times
- Shared resources

### 5. Upgrade for Production
Consider paid tier for:
- No sleep time
- Better performance
- More resources
- Priority support

---

## 📊 Cost Estimate

**Free Tier:**
- ✅ Perfect for development/testing
- ✅ Share with friends
- ✅ Portfolio projects
- ❌ Sleeps after inactivity

**Starter ($7/month):**
- ✅ Always running
- ✅ Better performance
- ✅ Production-ready

---

## 🎯 Quick Reference

**Render Dashboard:** https://dashboard.render.com/  
**GitHub Repo:** https://github.com/YOUR_USERNAME/agentic-ai-travel-planner  
**Live App:** https://agentic-ai-travel-planner.onrender.com  

---

## ✅ Deployment Checklist

- [ ] Created GitHub repository
- [ ] Pushed code to GitHub
- [ ] Created Render account
- [ ] Connected GitHub to Render
- [ ] Configured build settings
- [ ] Added ANTHROPIC_API_KEY
- [ ] Deployed successfully
- [ ] Tested all features
- [ ] App is accessible via URL
- [ ] Shared link with others

---

## 🆘 Need Help?

**Render Documentation:** https://render.com/docs  
**Streamlit Deployment:** https://docs.streamlit.io/deploy  
**LangChain Docs:** https://docs.langchain.com/  

**Common Issues:**
- Check Render logs for errors
- Verify environment variables
- Ensure requirements.txt is updated
- Test locally first

---

**🎉 Congratulations! Your AI Travel Planner is now live and accessible worldwide!**
