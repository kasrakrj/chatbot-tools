import io
import json
from snips_nlu import SnipsNLUEngine



if __name__ == "__main__":
    with io.open("dataset.json") as f:
        dataset = json.load(f)
    
    nlu_engine = SnipsNLUEngine()
    
    nlu_engine.fit(dataset)

    while(True):
        inp =  input("input: ")
        if inp != "exit":
            parsing = nlu_engine.parse(inp)
            print(json.dumps(parsing, indent=2))
        else:
            break
    
