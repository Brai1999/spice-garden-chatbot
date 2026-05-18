from groq import Groq

client = Groq(api_key="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")

business_info = """
You are a customer support assistant 
for a restaurant called Spice Garden.

Opening hours: 11am to 11pm daily
Location: MG Road, Bangalore
Phone: 9876543210
Speciality: North Indian food
Average cost: 500 rupees for two people
Only answer questions about this restaurant.
If you don't know something say 
"Please call us at 9876543210"
"""

def ask_bot(question):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": business_info},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

print("Bot is ready! Type your question.")
print("Type 'quit' to exit")
print("-" * 40)

while True:
    question = input("you: ")
    if question.lower() == "quit":
        break
    answer = ask_bot(question)
    print(f"Bot: {answer}")
    print("-" * 40)