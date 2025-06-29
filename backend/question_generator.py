import openai
import os

# Set Together API base and your API key
openai.api_base = "https://api.together.xyz/v1"
os.environ["OPENAI_API_KEY"] = "bd694cf39d025dcdaa6be4f4dbefa45281af00eb664c0ca804ed339ff5dc09c0"  # 🔁 Replace with your real key

def generate_questions(document_text):
    prompt = (
        f"Read the following document and generate three logic-based or comprehension-focused questions a user could answer after reading it.\n\n"
        f"Document:\n{document_text[:4000]}\n\n"
        f"Format:\nQ1: ...\nQ2: ...\nQ3: ..."
    )
    response = openai.ChatCompletion.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        messages=[{"role": "user", "content": prompt}]
    )
    content = response['choices'][0]['message']['content'].strip()
    lines = content.split("\n")
    return [line.split(": ", 1)[1] for line in lines if ": " in line][:3]
