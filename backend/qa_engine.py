import openai

# ✅ Setup API
openai.api_key = "bd694cf39d025dcdaa6be4f4dbefa45281af00eb664c0ca804ed339ff5dc09c0"
openai.api_base = "https://api.together.xyz/v1"

def answer_question(document_text, user_question):
    try:
        print("💬 [qa_engine] Answering question:", user_question)
        if not document_text.strip():
            return "⚠️ Document is empty. Please upload a readable file."
        if not user_question.strip():
            return "⚠️ Please enter a question."

        prompt = (
            f"Use only the document below to answer the question. Justify your answer if possible.\n\n"
            f"Document:\n{document_text[:12000]}\n\n"
            f"Question: {user_question}\n\n"
            f"Answer:"
        )

        response = openai.ChatCompletion.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            messages=[{"role": "user", "content": prompt}]
        )

        answer = response['choices'][0]['message']['content'].strip()
        print("✅ [qa_engine] Answer retrieved.")
        return answer

    except Exception as e:
        print("❌ [qa_engine] Error:", e)
        return f"⚠️ Error: {str(e)}"
