import inquirer

def confirm_prompt(msg: str = "Are you sure?", opts: list = ["Yes", "No"]) -> bool:
    """Confirm a yes/no statement."""
    questions = [inquirer.List("confirm", message=msg, choices=opts)]
    ans = inquirer.prompt(questions)
    return ans["confirm"] == "Yes"

def text_input(msg: str = "Enter information:") -> str:
    """Collect text info from user."""
    prompt = inquirer.prompt([inquirer.Text("text", message=msg)])
    return prompt["text"]

def confirm(msg: str = "Continue?") -> bool:
    prompt = inquirer.Confirm("confirm", message=msg, default=True)
    ans = inquirer.prompt([prompt])
    return ans["confirm"]
