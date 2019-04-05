import logging
from .wrapper import PipelineWrapper
import os
import json
logging.basicConfig(level=logging.INFO)

def main():
    wrapper = PipelineWrapper()
    config = wrapper.get_config()
    output = wrapper.run(json.dumps({"data": "hello"}))
    with open(os.path.join(config["output_path"], "output.txt"), 'w') as f:
        f.write(output["output"])
    logging.info(output)

if __name__ == "__main__":
    main()
