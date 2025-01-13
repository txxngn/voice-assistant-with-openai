1. Phải Install Flask từ python virtual environment thì mới include dependencies cần thiết để chạy.
c:\Users\thain\OneDrive\Desktop\voice-assistant-with-openai\.venv\Scripts\python.exe -m pip install flask

2. Run
docker build . -t voice-chatapp-powered-by-openai
docker run -p 8000:8000 voice-chatapp-powered-by-openai
