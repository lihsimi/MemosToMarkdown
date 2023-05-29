# Memos to Markdown

Export the database of Memos to Markdown.

> Export of attachments not supported yet.

1. Retrieve the database file

```
docker cp memos:/var/opt/memos/memos_prod.db ~/
```

2. Download Export.py

```
cd ~
curl -O https://raw.githubusercontent.com/lihoneymi/MemosToMarkdown/master/Export.py
```

3. Run Export.py

Confirmed that the `sqlite3` module is installed for Python, or
```
pip install sqlite3
```

After that,
```
python Export.py
```

4. Now you get the `memos_export.md` at the same position.
