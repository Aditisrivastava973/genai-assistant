# ✨ GenAI Research Assistant

An interactive, AI-powered tool that helps you **summarize**, **ask questions**, and **challenge your understanding** from any uploaded PDF or text document — designed for students, researchers, and lifelong learners.

---

## 🚀 Features

- 📤 Upload `.pdf` or `.txt` documents
- 🧠 Get concise, 150-word AI-generated summaries
- 💬 Ask custom questions in a chat-like interface
- 📝 Auto-generate 3 comprehension questions
- ✅ Evaluate your own answers with AI-based feedback
- 🌙 Dark/light theme compatible
- 🎨 Beautiful, responsive and intuitive UI

---

## 🧠 Powered By

| Component      | Technology                        |
|----------------|------------------------------------|
| LLM Backend    | Together.ai — Mixtral-8x7B         |
| UI Framework   | Gradio                             |
| PDF Parsing    | PyMuPDF                            |
| Prompt Handling| OpenAI-compatible API              |
| Styling        | Custom CSS + Gradio themes         |

---

## 📸 Screenshots

### 📤 Upload Tab
![Upload Tab](https://github.com/user-attachments/assets/209563aa-feb4-41fd-851d-c42009b03ab1)


### 💬 Chat Inference
![Chat Interface](https://github.com/user-attachments/assets/c651539e-95c6-4828-acb9-1388bed0ea5e)


### 🧠 Challenge Section
![Challenge Section](https://github.com/user-attachments/assets/534d26a2-34a2-4b86-bb82-06a372069973)


---

## 🛠️ Installation & Setup

```bash
git clone https://github.com/Aditisrivastava973/genai-assistant.git
cd genai-assistant

# Setup virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
