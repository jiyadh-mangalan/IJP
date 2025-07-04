import os

def count_words_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
        return len(text.split())

def main():
    markdown_files = []
    total_words = 0

    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                markdown_files.append(filepath)
                total_words += count_words_in_file(filepath)

    print(f"📝 Found {len(markdown_files)} markdown file(s)")
    print(f"📊 Total words: {total_words}")

if __name__ == "__main__":
    main()
