import sqlite3
from datetime import datetime

def convert_unix_to_datetime(unix_timestamp):
    return datetime.fromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')

def export_to_markdown(database_file, table_name, output_file):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT created_ts, content FROM {table_name}")
    results = cursor.fetchall()
    
    with open(output_file, 'w') as file:
        for row in results:
            created_ts = row[0]
            content = row[1]
            
            # Convert the time stamp
            created_datetime = convert_unix_to_datetime(created_ts)
            
            # Markdown
            file.write(f"## {created_datetime}\n\n")
            file.write(content)
            file.write('\n\n---\n\n')
    
    print(f"Successed! Save as {output_file}")


database_file = "memos_prod.db"
table_name = "memo"
output_file = "memos_export.md"

export_to_markdown(database_file, table_name, output_file)
