from dotenv import load_dotenv
import os

from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables
load_dotenv()

def generate_pet_name(animal_type, pet_color):
    # Initialize the LLM
    llm = OpenAI(temperature=0.5)

    # Create the prompt template
    prompt_template_name = PromptTemplate(
        input_variables=["animal_type", "pet_color"],
        template="I have a {animal_type} as a pet. It is {pet_color} in color. Suggest five cool names."
    )

    # Create the chain
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)

    # Run the chain with inputs
    response = name_chain.invoke({'animal_type': animal_type, 'pet_color': pet_color})

    return response['text']

if __name__ == "__main__":
    result = generate_pet_name("dog", "black")
    print("Suggested Pet Names:\n", result)
