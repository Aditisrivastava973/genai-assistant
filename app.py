import gradio as gr
from backend.utils import extract_text_from_file
from backend.summarizer import summarize_document
from backend.qa_engine import answer_question
from backend.question_generator import generate_questions
from backend.evaluator import evaluate_answers

uploaded_doc_text = ""
chat_history = []

def handle_upload(file):
    global uploaded_doc_text
    uploaded_doc_text = extract_text_from_file(file.name)
    summary = summarize_document(uploaded_doc_text)
    return summary

def handle_ask(question):
    global chat_history
    if not question.strip():
        return chat_history
    answer = answer_question(uploaded_doc_text, question)
    chat_history.append((f"🧑‍💻 <b>You:</b> {question}", f"🤖 <b>Assistant:</b> {answer}"))
    return chat_history

def handle_challenge():
    return generate_questions(uploaded_doc_text)

def handle_evaluation(q1, a1, q2, a2, q3, a3):
    return evaluate_answers(uploaded_doc_text, [q1, q2, q3], [a1, a2, a3])

with gr.Blocks(css="""
    * {
        font-family: 'Poppins', sans-serif !important;
    }

    body {
        background: linear-gradient(to bottom right, #f3f4f6, #ffffff);
    }

    h1 {
        font-size: 40px;
        background: linear-gradient(to right, #2F80ED, #1ABC9C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 10px;
    }

    .gr-container {
        max-width: 1000px;
        margin: 0 auto;
        padding: 30px;
        border-radius: 16px;
        background: white;
        box-shadow: 0 4px 18px rgba(0,0,0,0.06);
    }

    .gr-button {
        background: linear-gradient(to right, #2F80ED, #1ABC9C) !important;
        color: white !important;
        font-weight: 600;
        border-radius: 8px;
        padding: 12px 20px;
        font-size: 16px;
        transition: transform 0.2s ease;
    }

    .gr-button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 12px rgba(47, 128, 237, 0.3);
    }

    .gr-textbox textarea, .gr-textbox input {
        background-color: #f9fafb !important;
        border-radius: 8px;
        font-size: 15px;
    }

    .chatbox {
        background: #f4f6fb;
        border-radius: 12px;
        padding: 16px;
        height: 360px;
        overflow-y: auto;
        box-shadow: inset 0 1px 4px rgba(0,0,0,0.05);
    }

    .footer {
        text-align: center;
        font-size: 13px;
        color: #7f8c8d;
        margin-top: 40px;
    }
""") as demo:

    with gr.Column(elem_classes=["gr-container"]):
        gr.HTML("<h1>✨ GenAI Research Assistant</h1>")
        gr.Markdown("Upload, summarize, interact and learn with beautifully integrated AI features.")

        with gr.Tab("📤 Upload Document"):
            file_input = gr.File(label="Upload PDF or TXT file", file_types=[".pdf", ".txt"])
            summary_output = gr.Textbox(label="📄 Summary", lines=8, interactive=False)
            file_input.change(fn=handle_upload, inputs=[file_input], outputs=[summary_output])

        with gr.Tab("💬 Chat with Document"):
            chatbot = gr.Chatbot(elem_classes=["chatbox"])
            question_input = gr.Textbox(label="Ask something from the document...", placeholder="e.g. What is the abstract about?", lines=2)
            ask_button = gr.Button("🔍 Ask")

            ask_button.click(fn=handle_ask, inputs=[question_input], outputs=[chatbot])
            question_input.submit(fn=handle_ask, inputs=[question_input], outputs=[chatbot])

        with gr.Tab("🧠 Challenge Me"):
            gr.Markdown("Let AI quiz you! Answer 3 questions and get feedback.")

            challenge_btn = gr.Button("🎲 Generate Questions")

            q1 = gr.Textbox(label="Q1")
            a1 = gr.Textbox(label="Your Answer 1", lines=2)
            q2 = gr.Textbox(label="Q2")
            a2 = gr.Textbox(label="Your Answer 2", lines=2)
            q3 = gr.Textbox(label="Q3")
            a3 = gr.Textbox(label="Your Answer 3", lines=2)

            eval_btn = gr.Button("✅ Evaluate My Answers")
            feedback = gr.Textbox(label="📋 AI Feedback", lines=10, interactive=False)

            challenge_btn.click(fn=handle_challenge, inputs=[], outputs=[q1, q2, q3])
            eval_btn.click(fn=handle_evaluation, inputs=[q1, a1, q2, a2, q3, a3], outputs=[feedback])

        gr.HTML('<div class="footer">Made by Aditi | Powered by Together.ai</div>')

demo.launch()
