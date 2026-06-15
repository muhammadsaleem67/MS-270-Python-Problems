import datetime
def write_diary_entry(entry_text):
    # Get current date and time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("diary.txt", "a")  as diary:
        diary.write(f"[{timestamp}]\n")
        diary.write(f"[{entry_text}]\n")
        diary.write(f"-"*30 + "\n")

        print("Diary entry saved")
write_diary_entry("Today I learned about Python file handling. It was awesome!")
"""
	1. The datetime Module: We import Python's built-in time module. .now() gets the exact current second, and .strftime() formats it to look nice (Year-Month-Day Hour:Minute:Second).
	2. Append Mode: We open diary.txt in 'a' mode.
	3. Structuring: We write the timestamp, then the actual text, then a row of dashes ("-" * 30) to visually separate this entry from tomorrow's entry.

"""