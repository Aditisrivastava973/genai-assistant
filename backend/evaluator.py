import openai

# ✅ Configure Together API
openai.api_key = "bd694cf39d025dcdaa6be4f4dbefa45281af00eb664c0ca804ed339ff5dc09c0"  
openai.api_base = "https://api.together.xyz/v1"

def evaluate_answers(document_text, questions, answers):
    try:
        # ✅ Validate inputs
        if not document_text.strip():
            return "⚠️ Please upload a document first."

        if not all(questions) or not all(answers):
            return "⚠️ Please fill in all questions and answers before evaluation."

        # ✅ Build evaluation prompt
        prompt = (
            "You are an academic evaluator.\n"
            "Given the document and answers below, evaluate each student's answer out of 5.\n"
            "Also explain briefly why.\n\n"
            f"Document:\n{document_text[:10000]}\n\n"
        )

        for i, (q, a) in enumerate(zip(questions, answers), start=1):
            prompt += f"Q{i}: {q}\nA{i}: {a}\n\n"

        prompt += "Give feedback like this:\nQ1: 4/5 - Good coverage, slight inaccuracy.\nQ2: ...\n"

        # ✅ Call Together API
        response = openai.ChatCompletion.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            messages=[{"role": "user", "content": prompt}]
        )

        evaluation = response['choices'][0]['message']['content'].strip()
        print("✅ Evaluation result:", evaluation[:200], "...")
        return evaluation

    except Exception as e:
        print("❌ Evaluation error:", str(e))
        return f"⚠️ Error during evaluation: {e}"
