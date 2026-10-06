from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.llm import get_llm


def build_chain(prompt_template: str, input_variables: list, provider: str = "ollama", model: str = None):
    prompt = PromptTemplate(template=prompt_template, input_variables=input_variables)
    llm = get_llm(provider=provider, model=model)
    return prompt | llm | StrOutputParser()
