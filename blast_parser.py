
import json


def parse_blast_json(blast_file):
    json_data = open(blast_file)
    parsed = json.load(json_data)
    json_data.close()
    return parsed
