import json
import ruamel.yaml

new_source = "kafka_source_qms"
yaml = ruamel.yaml.YAML()
with open("experiment.yaml", "r") as data:
    data = yaml.load(data)
    if new_source not in data['vector']['sources'].keys():
        data['vector']['sources'][new_source] = {
            "type": 'kafka',
            "topic": new_source
        }
    print(data)