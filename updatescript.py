import os
import json
event_path = os.getenv('GITHUB_EVENT_PATH')

if not event_path:
    print("GitHub event data not found.")
    exit(1)


with open(event_path, 'r') as file:
    event_data = json.load(file)


issue_author = event_data['issue']['user']['login']
issue_name =event_data['issue']['title']

if issue_name=="MOVE|UP":
        pass  
with open('Readme.md', 'a') as file:
    file.write(f"hellow {issue_author}\n")

print("done")
