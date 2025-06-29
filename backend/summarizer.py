import openai
import os

# ✅ Configure Together.ai endpoint + key

openai.api_key = "bd694cf39d025dcdaa6be4f4dbefa45281af00eb664c0ca804ed339ff5dc09c0"
openai.api_base = "https://api.together.xyz/v1"


def summarize_document(text):
    try:
        print("📄 Preparing to summarize...")

        if len(text.strip()) == 0:
            raise ValueError("The document is empty or has no extractable text.")

        # Truncate to ~4000 tokens (~15k characters)
        trimmed_text = text[:12000]

        prompt = (
            f"Summarize the following document in no more than 150 words:\n\n{trimmed_text}"
        )

        print("🧠 Sending to Together.ai API...")

        response = openai.ChatCompletion.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            messages=[{"role": "user", "content": prompt}]
        )

        summary = response['choices'][0]['message']['content'].strip()
        print("✅ Summary received.")
        return summary

    except Exception as e:
        print("❌ Summary generation failed:", str(e))
        return f"⚠️ Error: {str(e)}"
