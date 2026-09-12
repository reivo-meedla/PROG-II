class Diary:
    def __init__(self):
        self.entries = []

    def add_entry(self, text):
        self.entries.append(text)

    def remove_entry(self, index):
        if 0 <= index < len(self.entries):
            del self.entries[index]
        else:
            raise IndexError("Entry index out of range.")

    def get_entries(self):
        return self.entries

    def __str__(self):
        if not self.entries:
            return ""
        return "\n".join(self.entries)


class DiaryPersistence:
    @staticmethod
    def save_to_file(diary, filename):
        with open(filename, "w") as file:
            for entry in diary.entries:
                file.write(entry + "\n")

    @staticmethod
    def load_from_file(filename):
        diary = Diary()
        with open(filename, "r") as file:
            diary.entries = [line.strip() for line in file]
        return diary
            
            
class DiaryStatistics:
    @staticmethod
    def print_statistics(diary):
        total_entries = len(diary.entries)
        avg_length = (
            sum(len(entry) for entry in diary.entries) / total_entries
            if total_entries > 0
            else 0
        )
        print(f"Total entries: {total_entries}")
        print(f"Average entry length: {avg_length:.2f}")