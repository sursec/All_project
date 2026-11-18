
import os
import shutil
from datetime import datetime


class FileOrganizer:
    
    CATEGORIES = {
        "Images": {".jpg", ".jpeg", ".png"},
        "Documents": {".pdf", ".docx", ".txt"},
        "Videos": {".mp4", ".mkv"},
        "Python_Files": {".py"},
    }

    def __init__(self, folder_path):
        self.folder_path = os.path.abspath(os.path.expanduser(folder_path))
        self.log_path = os.path.join(self.folder_path, "organizer_log.txt")
        self.report = {}
        self.moved_count = 0
        self.skipped_count = 0

    def validate_folder(self):
        
        if not os.path.exists(self.folder_path):
            raise FileNotFoundError("The folder path does not exist.")
        if not os.path.isdir(self.folder_path):
            raise NotADirectoryError("The provided path is not a folder.")

    def get_category(self, filename):
        
        extension = os.path.splitext(filename)[1].lower()
        for category, extensions in self.CATEGORIES.items():
            if extension in extensions:
                return category
        return "Others"

    def get_unique_destination(self, destination_folder, filename):
        
        name, extension = os.path.splitext(filename)
        destination = os.path.join(destination_folder, filename)
        counter = 1

        while os.path.exists(destination):
            new_name = f"{name}_copy{counter}{extension}"
            destination = os.path.join(destination_folder, new_name)
            counter += 1

        return destination

    def scan_files(self):
        
        files = []
        for filename in os.listdir(self.folder_path):
            full_path = os.path.join(self.folder_path, filename)
            if os.path.isfile(full_path) and filename != os.path.basename(self.log_path):
                files.append(filename)
        return sorted(files, key=str.lower)

    def plan_movements(self):
        
        plan = []
        for filename in self.scan_files():
            category = self.get_category(filename)
            destination_folder = os.path.join(self.folder_path, category)
            destination = self.get_unique_destination(destination_folder, filename)
            plan.append((filename, category, destination))
        return plan

    def preview(self, plan):
        
        print("\n========== PREVIEW MODE ==========")
        if not plan:
            print("No files found to organize.")
        for filename, category, destination in plan:
            print(f"{filename}  ->  {category}/{os.path.basename(destination)}")
        print(f"\nTotal files to organize: {len(plan)}")
        print("Preview complete. No files were moved.")
        print("==================================\n")

    def write_log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_path, "a", encoding="utf-8") as log_file:
            log_file.write(f"[{timestamp}] {message}\n")

    def organize(self, plan):
        
        self.report = {category: 0 for category in list(self.CATEGORIES) + ["Others"]}
        self.moved_count = 0
        self.skipped_count = 0

        for category in self.report:
            os.makedirs(os.path.join(self.folder_path, category), exist_ok=True)

        for filename, category, old_destination in plan:
            source = os.path.join(self.folder_path, filename)

            destination_folder = os.path.join(self.folder_path, category)
            destination = self.get_unique_destination(destination_folder, filename)

            if not os.path.isfile(source):
                self.skipped_count += 1
                self.write_log(f"SKIPPED (source missing): {filename}")
                continue

            try:
                shutil.move(source, destination)
                self.report[category] += 1
                self.moved_count += 1
                self.write_log(
                    f"MOVED: {filename} -> {category}/{os.path.basename(destination)}"
                )
            except OSError as error:
                self.skipped_count += 1
                self.write_log(f"ERROR: {filename} | {error}")

        self.show_summary()

    def show_summary(self):
        print("\n========== ORGANIZATION REPORT ==========")
        for category, count in self.report.items():
            print(f"{category:15} : {count} file(s)")
        print("-----------------------------------------")
        print(f"Total moved     : {self.moved_count}")
        print(f"Total skipped   : {self.skipped_count}")
        print(f"Log file        : {self.log_path}")
        print("=========================================\n")


def main():
    print("=" * 52)
    print("             PYTHON FILE ORGANIZER")
    print("=" * 52)
    print("Tip: First test this program with a COPY of your files.")
    folder_path = input("\nEnter the folder path to organize: ").strip().strip('"')

    try:
        organizer = FileOrganizer(folder_path)
        organizer.validate_folder()
        plan = organizer.plan_movements()

        print(f"\nFound {len(plan)} file(s).")
        organizer.preview(plan)

        choice = input("Do you want to move these files? (yes/no): ").strip().lower()
        if choice == "yes":
            organizer.organize(plan)
            print("Done! Your files have been organized.")
        else:
            print("Cancelled. No files were moved.")

    except (FileNotFoundError, NotADirectoryError) as error:
        print(f"\nError: {error}")
    except PermissionError:
        print("\nError: Permission denied. Try a folder you have access to.")
    except OSError as error:
        print(f"\nAn operating-system error occurred: {error}")


if __name__ == "__main__":
    main()
