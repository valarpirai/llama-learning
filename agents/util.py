import ollama
import os
import re


def llm_call(prompt: str, system_prompt: str = "", model="llama3.2") -> str:
    """
    Calls the model with the given prompt and returns the response.

    Args:
        prompt (str): The user prompt to send to the model.
        system_prompt (str, optional): The system prompt to send to the model. Defaults to "".
        model (str, optional): The model to use for the call. Defaults to "llama3.2".

    Returns:
        str: The response from the language model.
    """
    # Create a new session with the specified model
    output = ollama.generate(
        model="llama3.2",
        prompt=f"{system_prompt}. {prompt}"
    )
    
    return output['response']

def extract_xml(text: str, tag: str) -> str:
    """
    Extracts the content of the specified XML tag from the given text. Used for parsing structured responses 

    Args:
        text (str): The text containing the XML.
        tag (str): The XML tag to extract content from.

    Returns:
        str: The content of the specified XML tag, or an empty string if the tag is not found.
    """
    match = re.search(f'<{tag}>(.*?)</{tag}>', text, re.DOTALL)
    return match.group(1) if match else ""
