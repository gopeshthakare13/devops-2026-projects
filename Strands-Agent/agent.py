from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import http_request

ollama_model = OllamaModel(
    host="http://localhost:11434/",
    model_id="gemma3:1b"
)

system_prompt = " you are repectful agent"\
                " U can answer in kind and humbal way"\
                " You can use tools wherever neeeded and "\
                " make api calls to free api that doesnt need api key"
                    
                 
agent = Agent(model=ollama_model,system_prompt=system_prompt,tools=[http_request])

user_input = input("you")
agent(user_input)

