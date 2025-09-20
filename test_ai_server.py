#!/usr/bin/env python3
"""
Test script for the local AI server
Run this to verify your AI server is working correctly
"""

import requests
import json

def test_ai_server():
    """Test the local AI server with sample questions"""
    
    # Test questions
    test_questions = [
        "Hello, how are you?",
        "What does your company do?",
        "What are your products?",
        "How can I contact you?",
        "What makes you different from competitors?",
        "Do you offer support?"
    ]
    
    print("Testing Local AI Server...")
    print("=" * 50)
    
    for question in test_questions:
        try:
            # Prepare the request
            payload = {
                "model": "local-company-ai",
                "messages": [
                    {"role": "user", "content": question}
                ],
                "temperature": 0.7
            }
            
            # Send request to local server
            response = requests.post(
                "http://localhost:8001/v1/chat/completions",
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                result = response.json()
                ai_response = result["choices"][0]["message"]["content"]
                print(f"Q: {question}")
                print(f"A: {ai_response}")
                print("-" * 50)
            else:
                print(f"Error: {response.status_code} - {response.text}")
                
        except requests.exceptions.ConnectionError:
            print("Error: Could not connect to AI server.")
            print("Make sure the server is running on port 8001")
            print("Run: py local_ai_server.py")
            break
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    test_ai_server()

