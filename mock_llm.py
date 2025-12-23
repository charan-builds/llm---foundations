def mock_llm(prompt: str) -> str:
    """
    Mock LLM function.
    Used when API credits are not available.
    """

    if "dictionary" in prompt.lower():
        return (
            "A Python dictionary is like a real dictionary. "
            "It stores data as key-value pairs, where each key has a value."
        )
    return "This is a mock response."

 
user_prompt = "Explain Python dictionaries in very simple words."
response = mock_llm(user_prompt)

print("LLM Response:")
print(response)
