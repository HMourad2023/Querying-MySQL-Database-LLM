from groq import Groq

def query_data(data_json, question, model_name, api_key):
    client = Groq(api_key=api_key)
    prompt = f"Based on the following relational data, answer the question:\n{data_json}\nQuestion: {question}"
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        model=model_name,
    )
    response = chat_completion.choices[0].message.content
    return response
