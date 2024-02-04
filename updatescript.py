import os
import json


event_path = os.getenv('GITHUB_EVENT_PATH')


if not event_path:
    print("GitHub event data not found.")
    exit(1)
def printBoard(matrix):
    markdown_content = "## HELLO THIS IS MERGE\n## Hey Lets Play :\n|   | 1 | 2 | 3 | 4 | 5 | 6 |\n| - | - | - | - | - | - | - |\n"
    for i, row in enumerate(matrix):
        markdown_content += f"| {i+1} | "
        for j, cell in enumerate(row):
            if cell == "HangryHunger":
                markdown_content += "![](https://github.com/merge-my-pr/merge-my-pr/blob/main/files/HangryHunger.png) | "
            elif cell == "HangryHungerBody":
                markdown_content += "![](https://github.com/merge-my-pr/merge-my-pr/blob/main/files/HangryHubgerBody.png) | "
            elif cell == "HangryHungerTail":
                markdown_content += "![](https://github.com/merge-my-pr/merge-my-pr/blob/main/files/HangryHungerTail.png) | "
            elif cell == "Tile":
                markdown_content += "![](https://github.com/merge-my-pr/merge-my-pr/blob/7311931b11cdacc8bb992244a5bb4aedbd8520a3/files/GrayTile.png) | "
            else:
                print("Invalid space")
        markdown_content += "\n"
    return markdown_content


matrix = [
    ["Tile"] * 7,
    ["Tile"] * 7,
    ["Tile"] * 7,
    ["Tile"] * 7,
    ["Tile"] * 7,
    ["Tile"] * 7,
]


matrix[4][3]="HangryHunger"
matrix[4][4]="HangryHungerBody"
matrix[4][5]="HangryHungerTail"


generatedBoard=printBoard(matrix)


with open(event_path, 'r') as file:
    event_data = json.load(file)


issue_author = event_data['issue']['user']['login']
issue_name =event_data['issue']['title']

if issue_name=="MOVE|UP":
        pass  

with open('Readme.md', 'w') as file:
    file.write(generatedBoard)

print("done")
