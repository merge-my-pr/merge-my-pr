import os
import json


event_path = os.getenv('GITHUB_EVENT_PATH')


if not event_path:
    print("GitHub event data not found.")
    exit(1)


with open(event_path, 'r') as file:
    event_data = json.load(file)


def printBoard(matrix):
    markdown_content = "## HELLO THIS IS MERGE\n## Hey Lets Play :\n|   | 0 | 1 | 2 | 3 | 4 | 5 |\n| - | - | - | - | - | - | - |\n"
    for i, row in enumerate(matrix):
        markdown_content += f"| {i} | "
        for j, cell in enumerate(row):
            if cell == "HangryHunger":
                markdown_content += "![](https://github.com/merge-my-pr/merge-my-pr/blob/main/files/HangryHunger.png) | "
            elif cell == "HangryHungerBody":
                markdown_content += "![](https://github.com/merge-my-pr/merge-my-pr/blob/main/files/HangryHubgerBody.png) | "
            elif cell == "HangryHungerTail":
                markdown_content += "![](https://github.com/merge-my-pr/merge-my-pr/blob/main/files/HangryHungerTail.png) | "
            elif cell == "Tile":
                markdown_content += "![](https://github.com/merge-my-pr/merge-my-pr/blob/7311931b11cdacc8bb992244a5bb4aedbd8520a3/files/GrayTile.png) | "
            elif cell == "HangryHungerCurvedBody":
                markdown_content += "![](https://github.com/merge-my-pr/merge-my-pr/blob/7311931b11cdacc8bb992244a5bb4aedbd8520a3/files/HangryHungerCurvedBody.png)"
            elif cell == "HangryHungerHeadUp":
                markdown_content += "![](https://github.com/merge-my-pr/merge-my-pr/blob/7311931b11cdacc8bb992244a5bb4aedbd8520a3/files/HangryHungerHeadUp.png)"
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

def defaultPosition():
    matrix[4][3]="HangryHunger"
    matrix[4][4]="HangryHungerBody"
    matrix[4][5]="HangryHungerTail"



defaultPosition()

issue_author = event_data['issue']['user']['login']
issue_name =event_data['issue']['title']



if issue_name =="MOVE|UP":
        matrix[3][3]="HangryHungerHeadUp"
        matrix[4][3]="HangryHungerCurvedBody"
        matrix[4][4]="HangryHungerTail"
        print("snake moved up")
        generatedBoard=printBoard(matrix)


with open('Readme.md', 'w') as file:
    file.write(generatedBoard)

print("done")
