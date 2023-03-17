import openai
import pandas as pd
import os

# Set up OpenAI API credentials
openai.api_key = os.environ["OPENAI_KEY"]

# Read in the CSV file
try:
    df = pd.read_csv("review.csv")
except pd.errors.ParserError as e:
    print(f"Error parsing CSV file: {e}")
    exit()


# Define a function to get the excitement rating for a given review
def get_excitement(review):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Rate the excitement level of the following review on a scale of 1 to 10, where 1 is not at all excited and 10 is extremely excited:\n{review}\nRating:",
        temperature=0.5,
        max_tokens=1,
    )
    excitement = int(response.choices[0].text)
    return excitement


# Apply the get_excitement function to each review in the DataFrame
df["excitement"] = df["Review"].apply(get_excitement)

# Save the DataFrame to a new CSV file with the excitement ratings included
filename = "input_data_analyzed.csv"
df.to_csv(filename, index=False)

print(f"Data saved to {filename}")
