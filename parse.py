import google.generativeai as genai

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

genai.configure(api_key="YourAPIkey")

def parse_with_gemini(dom_chunks, parse_description):

    model=genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=f"{template}")

    parsed_result = []
    for i, chunk in enumerate(dom_chunks, start=1):
        response = model.generate_content(f"dom_content :{chunk},parse_description:{parse_description}" )
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        text_content=response.candidates[0].content.parts[0].text

        parsed_result.append(text_content)

    return "\n".join(parsed_result)