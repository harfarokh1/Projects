import openai

# Enter your openAI API key below
API_KEY = 'OPENAI API KEY HERE'

openai.api_key = API_KEY
model = 'text-davinci-003'

prompt = input("Please enter a question: ")

# you can modify the below to suit your specifications such as max tokens etc
response = openai.Completion.create(
    prompt=prompt,
    model=model,
    max_tokens=4000,
    temperature=0.9,
    n=3,
    stop=['---']
)

# Prints response to question
print(response.choices[0].text)