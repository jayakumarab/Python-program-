# Let me read the files directly to get the complete code
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

with open('app.html', 'r', encoding='utf-8') as f:
    app_content = f.read()

print("INDEX.HTML LENGTH:", len(index_content))
print("APP.HTML LENGTH:", len(app_content))