import openai


def setup_openai_api(api_key):
    openai.api_key = api_key


def ask_openai(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
    )
    return response.choices[0].text.strip()
