import os
import json


event_path = os.getenv('GITHUB_EVENT_PATH')


if not event_path:
    print("GitHub event data not found.")
    exit(1)


with open(event_path, 'r') as file:
    event_data = json.load(file)

head_row, head_col=-1,-1
def printBoard(matrix):
    markdown_content = "## HELLO THIS IS MERGE\n## Hey Lets Play :\n|   | 0 | 1 | 2 | 3 | 4 | 5 |\n| - | - | - | - | - | - | - |\n"
    for i, row in enumerate(matrix):
        markdown_content += f"| {i} | "
        for j, cell in enumerate(row):
            if cell == "HangryHunger":
                global head_row,head_col
                head_row, head_col = i, j
                markdown_content += "![](https://github.com/merge-my-pr/merge-my-pr/blob/main/files/HangryHunger.png) | "
            elif cell == "HangryHungerBody":
                markdown_content += "![](https://github.com/merge-my-pr/merge-my-pr/blob/main/files/HangryHubgerBody.png) | "
            elif cell == "HangryHungerTail":
                markdown_content += "![](https://github.com/merge-my-pr/merge-my-pr/blob/main/files/HangryHungerTail.png) | "
            elif cell == "Tile":
                markdown_content += "![](https://github.com/merge-my-pr/merge-my-pr/blob/main/files/GrayTile.png) | "
            elif cell == "HangryHungerCurvedBody":
                markdown_content += "![](https://github.com/merge-my-pr/merge-my-pr/blob/main/files/HangryHungerCurvedBody.png) | "
            elif cell == "HangryHungerHeadUp":
                markdown_content += "![](https://github.com/merge-my-pr/merge-my-pr/blob/main/files/HangryHungerHeadUp.png) | "
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



issue_author = event_data['issue']['user']['login']
issue_name =event_data['issue']['title']

def move_snake(matrix, direction):
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == "HangryHunger": #[1,3]
                head_row, head_col = i, j  # head_row =1 ,head_col=3
                break
    new_head_row, new_head_col = head_row, head_col #1,3
    print(f"[{head_row}][{head_col}]")
    if direction == "UP":
        new_head_row -= 1 #new_head_row=0
        
        # matrix[3][3] = "HangryHungerHeadUp"
        # matrix[4][3] = "HangryHungerCurvedBody"
        # matrix[4][4] = "HangryHungerTail"
        matrix[new_head_row][new_head_col] = "HangryHungerHeadUp"
        matrix[head_row][head_col+1] = "HangryHungerTail"  #[1,4]
        matrix[head_row][head_col]="HangryHungerCurvedBody"
        print("Snake moved up")
    else:
        print("Invalid direction")

def resetSnake(matrix):
    matrix[1][3]="HangryHunger"
    matrix[1][4]="HangryHungerBody"
    matrix[1][5]="HangryHungerTail"


if issue_name == "Move|UP":
        move_snake(matrix,"UP")
        with open('Readme.md', 'r') as file:
            readme_content = file.read()

        generatedBoard=printBoard(matrix)
        start_index = readme_content.find("## HELLO THIS IS MERGE")
        end_index = readme_content.find("## Make a move:")
        updated_readme_content = readme_content[:start_index] + generatedBoard + readme_content[end_index:]


        with open('Readme.md', 'w') as file:
            file.write(updated_readme_content)


elif issue_name == "Reset":
    resetSnake(matrix)
    with open('Readme.md', 'r') as file:
            readme_content = file.read()

    generatedBoard=printBoard(matrix)
    start_index = readme_content.find("## HELLO THIS IS MERGE")
    end_index = readme_content.find("## Make a move:")
    updated_readme_content = readme_content[:start_index] + generatedBoard + readme_content[end_index:]

    with open('Readme.md', 'w') as file:
        file.write(updated_readme_content)


print("done")
