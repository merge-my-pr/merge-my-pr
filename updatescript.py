import os
import json

event_path = os.getenv('GITHUB_EVENT_PATH')

if not event_path:
    print("GitHub event data not found")
    exit(1)


with open(event_path, 'r') as file:
    event_data = json.load(file)

def printBoard(matrix):
    markdown_content = "## HELLO THIS IS MERGE\n## Hey Lets Play :\n|   | 0 | 1 | 2 | 3 |\n| - | - | - | - | - |\n"
    for i, row in enumerate(matrix):
        markdown_content += f"| {i} | "
        for j, cell in enumerate(row):
            if cell == "HangryHunger":
                markdown_content += "![](https://github.com/merge-my-pr/merge-my-pr/blob/main/files/HangryHunger.png) | "
            elif cell == "Tile":
                markdown_content += "![](https://github.com/merge-my-pr/merge-my-pr/blob/main/files/GrayTile.png) | "
            else:
                print("Invalid space")
        markdown_content += "\n"
    return markdown_content


matrix = [
    ["Tile"] * 7,
    ["Tile"] * 7,
    ["Tile"] * 7,
    ["Tile"] * 7
]

matrix[1][3]="HangryHunger"

issue_author = event_data['issue']['user']['login']
issue_name =event_data['issue']['title']

def move_snake(matrix):
    # head_row, head_col=-1,-1

    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == "HangryHunger": #[1,3]
                # head_row, head_col = i, j
                # print(f"[{head_row}][{head_col}]{i}{j}")# head_row =1 ,head_col=3
                # new_head_row, new_head_col = head_row, head_col #1,3
                # new_head_row -= 1
                matrix[i][j]="Tile"     
                print(i,j)          
                matrix[j-1][i]="HangryHunger"
                print(i,j)          

                # new_head_row, new_head_col = head_row, head_col #1,3
                # if direction == "UP":
                    # new_head_row -= 1 #new_head_row=0
                    
                    # matrix[3][3] = "HangryHungerHeadUp"
                    # matrix[4][3] = "HangryHungerCurvedBody"
                    # matrix[4][4] = "HangryHungerTail"
                    # matrix[new_head_row][new_head_col] = "HangryHungerHeadUp"
                    # matrix[head_row][head_col+1] = "HangryHungerTail" 
                    # matrix[head_row][head_col+2] = "Tile" 
                    # matrix[head_row][head_col]="HangryHungerCurvedBody"
                    # matrix[new_head_row][head_col]="HangryHunger"
                    # matrix[head_row][head_col]="Tile"
                print("Snake moved up")
                break
            else:
                print("Invalid direction")
                break

def resetHunger(matrix):
    matrix[1][3]="HangryHunger"

if issue_name == "Move|UP":
        move_snake(matrix)
        with open('Readme.md', 'r') as file:
            readme_content = file.read()

        generatedBoard=printBoard(matrix)
        start_index = readme_content.find("## HELLO THIS IS MERGE")
        end_index = readme_content.find("## Make a move:")
        updated_readme_content = readme_content[:start_index] + generatedBoard + readme_content[end_index:]


        with open('Readme.md', 'w') as file:
            file.write(updated_readme_content)

elif issue_name == "Reset":
    resetHunger(matrix)
    with open('Readme.md', 'r') as file:
            readme_content = file.read()

    generatedBoard=printBoard(matrix)
    start_index = readme_content.find("## HELLO THIS IS MERGE")
    end_index = readme_content.find("## Make a move:")
    updated_readme_content = readme_content[:start_index] + generatedBoard + readme_content[end_index:]

    with open('Readme.md', 'w') as file:
        file.write(updated_readme_content)


print("done")
