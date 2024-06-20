import os
import sqlite3
import shutil

def get_iridium_urls():
    # Path to the Iridium 'History' SQLite database on Windows
    history_db_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Iridium', 'User Data', 'Default', 'History')

    # Temporary copy of the History file to avoid database lock issues
    temp_history_db = os.path.join(os.getenv('TEMP'), 'History')
    shutil.copy2(history_db_path, temp_history_db)

    # Connect to the copied database
    conn = sqlite3.connect(temp_history_db)
    cursor = conn.cursor()

    # Query to get the URLs from the 'urls' table
    cursor.execute('SELECT url FROM urls')

    urls = [row[0] for row in cursor.fetchall()]

    conn.close()

    return urls

def save_urls_to_file(urls, file_path='active_current_urls.txt'):
    with open(file_path, 'w') as file:
        for url in urls:
            file.write(f"{url}\n")

if __name__ == "__main__":
    urls = get_iridium_urls()
    save_urls_to_file(urls)
    print(f"Active URLs saved to active_current_urls.txt")
