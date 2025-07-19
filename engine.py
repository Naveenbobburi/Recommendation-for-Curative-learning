from openai import OpenAI

# Replace this with your real A4F API key
a4f_api_key = "ddc-a4f-a14a028c03b24b4b8f96a1a5e788263c"
a4f_base_url = "https://api.a4f.co/v1"

client = OpenAI(
    api_key=a4f_api_key,
    base_url=a4f_base_url,
)

# User input
user_input = "I am interested in tech entrepreneurship and Elon Musk's thinking."

# System prompt to guide the assistant
system_prompt = (
    "You are a highly knowledgeable AI assistant that helps users discover high-quality learning and information resources. "
    "Based on the user's interests, recommend:\n"
    "- 3 specific YouTube videos (with titles and links)\n"
    "- 2 books (with title, author, and link if available)\n"
    "- 2 free online courses (from trusted platforms with links)\n"
    "Ask 1–2 clarifying questions if the user input is vague. Tailor the suggestions to the topic specifically. "
    "Always prefer reputable sources like Coursera, edX, MIT OCW, Khan Academy, YouTube EDU channels, etc."
)

completion = client.chat.completions.create(
    model="provider-3/gpt-4",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ],
    temperature=0.8,
    max_tokens=1000,
)

# Output the assistant's response
print(completion.choices[0].message.content)
