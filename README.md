# Task Manager CLI

A simple command-line task manager built with Python. Track your tasks through todo, in progress, and done states.

## Features

- Add, update, and delete tasks
- Mark tasks as in progress or done
- List all tasks, todo items, or completed tasks
- Lightweight — runs with Python only (no external dependencies)

## Requirements

- Python 3.8+

## Installation

Clone the repository and run the script directly:

```bash
git clone https://github.com/YOUR_USERNAME/task-manager-cli.git
cd task-manager-cli
```

## Usage

Run the task manager:

```bash
python Todo.py
```

Or, if installed as a package:

```bash
task-cli
```

## Commands

| Command | Description | Example |
|---------|-------------|---------|
| `add <text>` | Add a new task | `add Buy groceries` |
| `update <id> <text>` | Update a task | `update 1 Buy milk` |
| `delete <id>` | Delete a task | `delete 1` |
| `mark_in_progress <id>` | Mark task as in progress | `mark_in_progress 1` |
| `mark_done <id>` | Mark task as done | `mark_done 1` |
| `list` | List all tasks | `list` |
| `list_done` | List completed tasks | `list_done` |
| `list_todo` | List todo tasks | `list_todo` |
| `quit` | Exit the CLI | `quit` |

## Example Session

```
Welcome to Task Manager CLI!
Available commands: add, update, delete, mark_in_progress, mark_done, list, list_done, list_todo
Type 'quit' or press Ctrl+C to exit
--------------------------------------------------
add Study Python
Task added successfully (ID: 1)
add Read documentation
Task added successfully (ID: 2)
list
your all tasks are:
Study Python
Read documentation
mark_in_progress 1
task ID 1 added in in_progress list
mark_done 1
task ID 1 added in did list
list_done
your dided tasks are:
Study Python
quit
Have a good day!
```

## Project Structure

```
.
├── README.md      # This file
├── Todo.py        # Main application
├── Todo.md        # Command reference
└── Todo.toml      # Project configuration (pyproject.toml)
```

*My first GitHub project — built with Python*
https://roadmap.sh/projects/task-tracker