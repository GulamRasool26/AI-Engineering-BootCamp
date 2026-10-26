# Mini Task Tracker

## goal

A small command-line app for keeping track of tasks. Add tasks, check their status, mark them complete, and remove them when they are no longer needed.

## features

- Add tasks with a non-empty title.
- View tasks and their status (`Pending` or `Done`).
- Mark a task complete or delete it by its displayed number.
- Save tasks in `tasks.json` so they remain available the next time you run the app.
- Use Python's standard library; no additional packages are required.

## how to run

Open a terminal in the `AI_Engineering_BootCamp` folder and run:

```powershell
python mini_task_tracker.py
```

If your system uses the `py` launcher, you can run `py mini_task_tracker.py` instead. The app creates or updates `tasks.json` in the current working directory.

## sample interaction

```text
--- TASK TRACKER ---
1. Add  2. View  3. Complete  4. Delete  5. Exit
Choice: 1
Task title: Finish the project README
Task added.

--- TASK TRACKER ---
1. Add  2. View  3. Complete  4. Delete  5. Exit
Choice: 2
1. Finish the project README [Pending]

--- TASK TRACKER ---
1. Add  2. View  3. Complete  4. Delete  5. Exit
Choice: 3
Task number: 1
Task completed.

--- TASK TRACKER ---
1. Add  2. View  3. Complete  4. Delete  5. Exit
Choice: 2
1. Finish the project README [Done]

--- TASK TRACKER ---
1. Add  2. View  3. Complete  4. Delete  5. Exit
Choice: 5
Goodbye.
```
## Repo Link
[Repo](https://github.com/GulamRasool26/AI-Engineering-BootCamp/commits/main/)
