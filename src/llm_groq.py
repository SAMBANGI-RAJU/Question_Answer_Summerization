from groq import Groq
import json

def generate_summary(final_data, model="llama3-8b-8192"):
    context = "Summarize the following answers based on the provided question."
    summarized_data = {}

    api = "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"
    # Initialize Groq client
    client = Groq(api_key=api)

    for question, answer_list in final_data.items():
        # Combine the list of answers into a single string
        answers_combined = " ".join(answer_list)

        # Create the prompt
        prompt = f"Question: {question}\nAnswers: {answers_combined}\nSummarize the answers."

        # Call Groq API for summarization
        response = client.chat.completions.create(
            messages=[
                {"role": "user", "content": f"Context: {context}\nPrompt: {prompt}"}
            ],
            model=model,
            stream=False,
        )

        # Extract the summary from the API response
        summary = response.choices[0].message.content.strip()

        # Add the summarized response to the dictionary
        summarized_data[question] = summary

    # # Save the summarized data to a JSON file
    # with open("summarized_responses.json", "w") as file:
    #     json.dump(summarized_data, file, indent=4)

    return summarized_data