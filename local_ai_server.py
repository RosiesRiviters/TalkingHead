#!/usr/bin/env python3
"""
Simple Local AI Server for TalkingHead
This provides a local AI backend that can answer company-specific questions
"""

import json
import random
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import re
import time

class CompanyAI:
    """Simple company AI that can answer questions about your company"""
    
    def __init__(self):
        # Import company configuration
        try:
            from company_config import COMPANY_CONFIG, CUSTOM_QA
            self.company_info = COMPANY_CONFIG
            self.custom_qa = CUSTOM_QA
        except ImportError:
            # Fallback configuration if config file not found
            self.company_info = {
                "name": "Your Company Name",
                "industry": "Your Industry",
                "founded": "2020",
                "mission": "To provide innovative solutions to our customers",
                "products": [
                    "Product A - Description of what it does",
                    "Product B - Description of what it does", 
                    "Product C - Description of what it does"
                ],
                "services": [
                    "Service 1 - What it provides",
                    "Service 2 - What it provides"
                ],
                "values": [
                    "Innovation",
                    "Customer Focus", 
                    "Quality",
                    "Integrity"
                ],
                "contact": {
                    "email": "info@yourcompany.com",
                    "phone": "+1-555-0123",
                    "website": "https://yourcompany.com"
                }
            }
            self.custom_qa = {}
        
        # Common questions and answers
        self.qa_pairs = {
            "what does your company do": f"We are {self.company_info['name']}, a company in the {self.company_info['industry']} industry. {self.company_info['mission']}",
            "what are your products": f"Our main products include: {', '.join(self.company_info['products'])}",
            "what services do you offer": f"We offer: {', '.join(self.company_info['services'])}",
            "what are your company values": f"Our core values are: {', '.join(self.company_info['values'])}",
            "how can I contact you": f"You can reach us at {self.company_info['contact']['email']}, call {self.company_info['contact']['phone']}, or visit {self.company_info['contact']['website']}",
            "when was your company founded": f"Our company was founded in {self.company_info['founded']}",
            "what industry are you in": f"We operate in the {self.company_info['industry']} industry"
        }
        
        # Add custom Q&A pairs
        self.qa_pairs.update(self.custom_qa)
    
    def generate_response(self, user_input):
        """Generate a response based on user input"""
        user_input_lower = user_input.lower().strip()
        
        # Check for exact matches first
        for question, answer in self.qa_pairs.items():
            if question in user_input_lower:
                return answer
        
        # Check for partial matches
        for question, answer in self.qa_pairs.items():
            if any(word in user_input_lower for word in question.split()):
                return answer
        
        # Check for company name mentions
        if self.company_info['name'].lower() in user_input_lower:
            return f"Yes, {self.company_info['name']} is our company. {self.company_info['mission']}"
        
        # Check for product mentions
        for product in self.company_info['products']:
            if product.split()[0].lower() in user_input_lower:
                return f"{product} is one of our flagship products. It's designed to help our customers achieve their goals."
        
        # Generic responses for common question types
        if any(word in user_input_lower for word in ['hello', 'hi', 'hey']):
            return f"Hello! Welcome to {self.company_info['name']}. I'm here to help you learn about our company, products, and services. How can I assist you today?"
        
        if any(word in user_input_lower for word in ['help', 'assist', 'support']):
            return f"I can help you with information about {self.company_info['name']}, including our products, services, company history, and how to contact us. What would you like to know?"
        
        if any(word in user_input_lower for word in ['thank', 'thanks']):
            return "You're welcome! I'm happy to help. Is there anything else you'd like to know about our company?"
        
        # Default response for unknown questions
        return f"I'm not sure about that specific question, but I'd be happy to tell you about {self.company_info['name']}. You can ask me about our products, services, company values, or how to contact us. What interests you?"

class AIRequestHandler(BaseHTTPRequestHandler):
    """HTTP request handler for AI chat completions"""
    
    def __init__(self, *args, **kwargs):
        self.ai = CompanyAI()
        super().__init__(*args, **kwargs)
    
    def do_POST(self):
        """Handle POST requests for chat completions"""
        if self.path == "/v1/chat/completions":
            self.handle_chat_completion()
        else:
            self.send_error(404, "Endpoint not found")
    
    def handle_chat_completion(self):
        """Handle chat completion requests"""
        try:
            # Read request body
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            request_data = json.loads(post_data.decode('utf-8'))
            
            # Extract messages
            messages = request_data.get('messages', [])
            if not messages:
                self.send_error(400, "No messages provided")
                return
            
            # Get the last user message
            user_message = None
            for msg in reversed(messages):
                if msg.get('role') == 'user':
                    user_message = msg.get('content', '')
                    break
            
            if not user_message:
                self.send_error(400, "No user message found")
                return
            
            # Generate AI response
            ai_response = self.ai.generate_response(user_message)
            
            # Format response in OpenAI-compatible format
            response_data = {
                "id": "local-ai-" + str(random.randint(1000, 9999)),
                "object": "chat.completion",
                "created": int(time.time()),
                "model": "local-company-ai",
                "choices": [
                    {
                        "index": 0,
                        "message": {
                            "role": "assistant",
                            "content": ai_response
                        },
                        "finish_reason": "stop"
                    }
                ],
                "usage": {
                    "prompt_tokens": len(user_message.split()),
                    "completion_tokens": len(ai_response.split()),
                    "total_tokens": len(user_message.split()) + len(ai_response.split())
                }
            }
            
            # Send response
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
            
        except Exception as e:
            print(f"Error processing request: {e}")
            self.send_error(500, f"Internal server error: {str(e)}")
    
    def do_OPTIONS(self):
        """Handle CORS preflight requests"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def log_message(self, format, *args):
        """Custom logging to avoid cluttering the console"""
        pass

def main():
    """Start the local AI server"""
    port = 8001  # Different from TalkingHead web server
    
    print(f"Starting Local Company AI Server on port {port}")
    print(f"Server will be available at: http://localhost:{port}")
    print("Configure TalkingHead to use: http://localhost:8001/v1/chat/completions")
    print("\nTo customize company information, edit the CompanyAI class in this file.")
    print("Press Ctrl+C to stop the server.")
    
    try:
        server = HTTPServer(('localhost', port), AIRequestHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.shutdown()

if __name__ == "__main__":
    main()
