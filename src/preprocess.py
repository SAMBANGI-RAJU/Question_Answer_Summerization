import os
import fitz
import json


def get_qa_pairs(doc):
    current_question = None
    font_size_threshold = None  # To determine the font size of questions

    # Define keywords for detecting questions
    question_keywords = ["What", "How", "When", "Why", "Where", "Who", "Which"]

    qa_pairs = {}
    for page_num in range(1, len(doc)):  # Start from page 2 (index 1)
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]  # Extract text blocks as dictionaries

        for block in blocks:
            for line in block["lines"]:
                line_text = " ".join([span["text"] for span in line["spans"]]).strip()
                font_size = line["spans"][0][
                    "size"
                ]  # Assume uniform font size in a line

                # Detect font size threshold for questions (only if not already determined)
                if font_size_threshold is None:
                    font_size_threshold = font_size

                # Detect if the line is a question based on keywords and font size
                if font_size >= font_size_threshold and any(
                    line_text.startswith(kw) for kw in question_keywords
                ):
                    # If there's an ongoing question, finalize it
                    if current_question:
                        qa_pairs[current_question] = qa_pairs[current_question].strip()

                    # Start a new question
                    current_question = line_text
                    qa_pairs[current_question] = ""
                elif current_question:  # Otherwise, treat as part of the current answer
                    qa_pairs[current_question] += " " + line_text

    return qa_pairs


def fix_json_structure(data):
    fixed_data = {}
    for key, value in data.items():
        if "?" in key:
            # Split the key at '?' and ensure it's at the end
            key_parts = key.split("?", 1)
            if len(key_parts) > 1:
                key = key_parts[0] + "?"  # Ensure the question mark is at the end

        # If '?' is in the value, split content before '?' and append to key
        if "?" in value:
            value_parts = value.split("?", 1)
            key = (
                key + " " + value_parts[0] + " " + "?"
            )  # Append the content before '?' to the key
            value = value_parts[1].strip()  # Remove that content from the value

        # Add the key-value pair to the fixed dictionary
        fixed_data[key] = value
    return fixed_data


def transform_data(qa_list):
    transformed_data = {}
    for entry in qa_list:
        for key, value in entry.items():
            if key not in transformed_data:
                transformed_data[key] = []  # Initialize list if key doesn't exist
            transformed_data[key].append(value)

    return transformed_data

def main():

    pds_dir = "Documents_belgium"
    qa_list = []
    for pdf in os.listdir(pds_dir):
        doc = fitz.open(os.path.join(pds_dir, pdf))
        qa_pairs = get_qa_pairs(doc)
        updated_json = fix_json_structure(qa_pairs)
        qa_list.append(updated_json)
        final_data = transform_data(qa_list)

    
    with open("final_check_transform.json", 'w') as file:
        json.dump(final_data, file, indent=4)


if __name__ == "__main__":
    main()
