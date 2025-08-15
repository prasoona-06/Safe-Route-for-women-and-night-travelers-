import openai

client = openai.OpenAI(api_key="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")

def generate_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

