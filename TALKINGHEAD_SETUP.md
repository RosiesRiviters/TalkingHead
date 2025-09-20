    
    
    
    # TalkingHead Setup with Local AI

Your local AI server is now running! Here's how to configure TalkingHead to use it.

## 🚀 Current Status

✅ **Local AI Server**: Running on port 8001  
✅ **TalkingHead Web Server**: Running on port 8000  
✅ **AI Testing**: Working correctly  

## 🌐 Access TalkingHead

1. **Open your web browser**
2. **Go to**: `http://localhost:8000`
3. **You should see the TalkingHead interface**

## ⚙️ Configure AI Integration

### Step 1: Open Settings
1. Click the **☰ (menu)** button in the top-right corner
2. Look for **"AI"** or **"Settings"** section

### Step 2: Configure AI Endpoint
1. Find the **AI endpoint** or **API URL** field
2. Set it to: `http://localhost:8001/v1/chat/completions`
3. **Remove any API key** (leave it blank)

### Step 3: Set AI Model
1. Find the **AI model** dropdown
2. Set it to: `local-company-ai`
3. If that option doesn't exist, try: `gpt-3.5-turbo` or similar

### Step 4: Configure Voice
1. Find the **Voice** section
2. Set **Voice Type** to: `Google` (for built-in TTS)
3. Set **Language** to: `en-GB` or `en-US`
4. Set **Voice ID** to: `en-GB-Standard-A` or similar

## 🧪 Test the Integration

1. **Type a question** in the input field, such as:
   - "What does your company do?"
   - "What are your products?"
   - "How can I contact you?"

2. **Press Enter** or click **Send**

3. **Watch your avatar** speak the AI-generated response!

## 🔧 Troubleshooting

### Avatar Not Speaking
- Check that the AI endpoint is correct
- Verify the AI model is set properly
- Ensure the voice settings are configured

### No AI Response
- Check that the local AI server is running (port 8001)
- Verify the endpoint URL in TalkingHead
- Check browser console for errors

### Voice Issues
- Try different Google TTS voices
- Check that lipsync language matches voice language
- Ensure voice type is set to "Google"

## 📝 Example Questions to Try

- "Hello, how are you?"
- "What does TechCorp Solutions do?"
- "Tell me about your products"
- "What services do you offer?"
- "What makes you different from competitors?"
- "Do you provide support?"
- "How can I get in touch?"

## 🌟 Customization

### Change Company Information
Edit `company_config.py` to update:
- Company name and details
- Products and services
- Custom Q&A pairs

### Add More Knowledge
Add new questions and answers to `CUSTOM_QA` in `company_config.py`:

```python
CUSTOM_QA = {
    "what are your pricing plans": "We offer flexible pricing plans including...",
    "do you have a free trial": "Yes, we offer a 30-day free trial...",
    # Add more here
}
```

### Restart After Changes
After editing `company_config.py`:
1. Stop the AI server (Ctrl+C)
2. Restart it: `py local_ai_server.py`

## 🎯 Next Steps

Once everything is working:
1. **Customize your avatar** appearance
2. **Add more company knowledge** to the AI
3. **Test with different questions**
4. **Share with your team** for feedback
5. **Deploy to company network** if needed

## 🆘 Need Help?

If you encounter issues:
1. Check both servers are running (ports 8000 and 8001)
2. Verify the configuration settings
3. Test the AI server separately first
4. Check browser console for error messages

**Happy chatting with your AI avatar! 🎉**

