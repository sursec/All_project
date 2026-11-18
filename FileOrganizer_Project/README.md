# Python File Organizer

A beginner-friendly Python project that sorts files into folders based on their file extensions. It uses the `os` and `shutil` modules and an object-oriented `FileOrganizer` class.

## Features

- Accepts a folder path from the user.
- Scans files using Python's `os` module.
- Organizes files into `Images`, `Documents`, `Videos`, `Python_Files`, and `Others`.
- Creates category folders automatically.
- Counts files moved into each category.
- Prevents overwriting: if a filename already exists, it creates a name such as `photo_copy1.jpg`.
- Writes every successful move or skipped/error item to `organizer_log.txt`.
- Shows a preview before moving anything.
- Asks for confirmation before making changes.

## Categories

| Category | Extensions |
|---|---|
| Images | `.jpg`, `.jpeg`, `.png` |
| Documents | `.pdf`, `.docx`, `.txt` |
| Videos | `.mp4`, `.mkv` |
| Python_Files | `.py` |
| Others | All other file extensions |

## Requirements

- Python 3.8 or newer
- No third-party packages are required.

## Installation

1. Download or clone this project from GitHub.
2. Open the `FileOrganizer_Project` folder in VS Code.
3. Open the VS Code terminal.
4. Check Python is installed:

   ```bash
   python --version
   ```

## Safe testing (important)

Do not test this tool on your real Downloads folder first.

1. Make a copy of a few unimportant sample files.
2. Put those copies in a separate test folder.
3. Run the program and enter the path to that test folder.
4. Read the preview carefully. Preview mode does not move anything.
5. Type `no` to cancel, or type `yes` only when the planned moves look correct.

The tool only scans files directly inside the selected folder; it does not recursively scan subfolders. It does not delete files. It avoids overwriting existing destination files by choosing a unique filename.

## How to run

From the project folder, run:

**Windows:**
```bash
python main.py
```

**macOS / Linux:**
```bash
python3 main.py
```

Then:
1. Enter the path of your test folder.
2. Review the preview list.
3. Type `yes` to organize or `no` to cancel.

Example Windows path:
```text
C:\Users\YourName\Downloads\file_test
```

Example macOS/Linux path:
```text
/home/yourname/Downloads/file_test
```


## How the code works

### `FileOrganizer` class

The class keeps the organizing logic in one place.

- `__init__()` stores the selected folder path and initializes report counters.
- `validate_folder()` checks that the path exists and is a folder.
- `get_category()` chooses a category from the file extension.
- `scan_files()` gets files from the selected folder using `os.listdir()` and `os.path.isfile()`.
- `get_unique_destination()` checks whether a destination filename already exists and adds `_copy1`, `_copy2`, etc. when needed.
- `plan_movements()` prepares the list of planned file moves.
- `preview()` displays the plan without moving files.
- `organize()` creates folders and moves files using `shutil.move()`.
- `write_log()` records file actions with timestamps.
- `show_summary()` prints the final count for each category.

### Duplicate filename handling

If `report.pdf` already exists in the Documents folder, the program does not replace it. It tries `report_copy1.pdf`, then `report_copy2.pdf`, and so on until it finds an unused name.

**Note:** This project handles duplicate *filenames* safely. It does not compare file contents to identify identical files with different names.



## Safety reminder

Always use a test folder containing copied sample files first. Review the preview before confirming. The program moves files, so only type `yes` when you are certain the selected folder is the correct test folder.
