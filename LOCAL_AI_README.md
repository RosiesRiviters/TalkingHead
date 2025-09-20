# Local AI Setup for TalkingHead

This guide will help you set up a local AI server that TalkingHead can use to answer company-specific questions without requiring external API keys.

## 🚀 Quick Start

### 1. Customize Company Information
Edit `company_config.py` with your company's details:
- Company name, industry, mission
- Products and services
- Company values and contact information
- Custom Q&A pairs

### 2. Start the Local AI Server
```bash
# Option 1: Double-click the batch file
start_local_ai.bat

# Option 2: Run from command line
py local_ai_server.py
```

The server will start on port 8001.

### 3. Test the AI Server
```bash
py test_ai_server.py
```

### 4. Configure TalkingHead
- Open TalkingHead in your browser
- Go to Settings (☰)
- In AI settings, set the endpoint to: `http://localhost:8001/v1/chat/completions`
- Set AI model to: `local-company-ai`

## 📁 Files Overview

- **`local_ai_server.py`** - Main AI server that handles requests
- **`company_config.py`** - Company information and custom Q&A
- **`start_local_ai.bat`** - Windows batch file to start the server
- **`test_ai_server.py`** - Test script to verify the server works
- **`LOCAL_AI_README.md`** - This file

## ⚙️ Configuration

### Company Information
Edit `company_config.py` to customize:

```python
COMPANY_CONFIG = {
    "name": "Your Company Name",
    "industry": "Your Industry",
    "founded": "2020",
    "mission": "Your mission statement",
    "products": [
        "Product 1 - Description",
        "Product 2 - Description"
    ],
    "services": [
        "Service 1 - Description",
        "Service 2 - Description"
    ],
    "values": [
        "Value 1",
        "Value 2"
    ],
    "contact": {
        "email": "info@yourcompany.com",
        "phone": "+1-555-0123",
        "website": "https://yourcompany.com"
    }
}
```

### Custom Q&A
Add your own questions and answers:

```python
CUSTOM_QA = {
    "what makes you special": "Your custom answer here",
    "do you have certifications": "Your certification information"
}
```

## 🔧 Troubleshooting

### Server Won't Start
- Make sure Python is installed: `py --version`
- Check if port 8001 is available
- Try a different port by editing `local_ai_server.py`

### Can't Connect to Server
- Verify the server is running on port 8001
- Check firewall settings
- Ensure TalkingHead is configured with the correct endpoint

### AI Responses Not Working
- Test with `test_ai_server.py` first
- Check browser console for errors
- Verify the AI model is set to `local-company-ai`

## 🌟 Features

- **No API Keys Required** - Runs completely locally
- **Company-Specific Knowledge** - Customizable for your business
- **OpenAI-Compatible API** - Works seamlessly with TalkingHead
- **Easy Customization** - Simple Python configuration
- **Fast Responses** - No network latency
- **Privacy-First** - All data stays on your machine

## 🔄 Integration with TalkingHead

1. **Start Local AI Server** (port 8001)
2. **Start TalkingHead Web Server** (port 8000)
3. **Configure TalkingHead** to use local AI endpoint
4. **Ask Questions** and watch your avatar respond!

## 📝 Example Usage

1. Start the local AI server
2. Open TalkingHead in your browser
3. Type: "What does your company do?"
4. Your avatar will respond with company information
5. Ask follow-up questions about products, services, etc.

## 🆘 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify all files are in the same directory
3. Ensure Python is properly installed
4. Check that ports 8000 and 8001 are available

## 🚀 Next Steps

Once you have the basic system working:
- Customize your avatar appearance
- Add more company-specific Q&A
- Integrate with your company's knowledge base
- Deploy to your company's internal network
- Add more sophisticated AI capabilities

Happy coding! 🎉

