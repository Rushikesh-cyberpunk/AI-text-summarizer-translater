import google.generativeai as genai

API_KEY = GEMINI_API_KEY

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


def get_text():
    choice = input("Read from a file instead of pasting text? (y/n): ").lower()

    if choice == "y":
        filename = input("Enter file name: ")
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return f.read().strip()
        except FileNotFoundError:
            print("File not found, type your text instead.\n")

    print("Paste your text below. Type END when finished.\n")
    lines = []
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)
    return "\n".join(lines)


def main():
    text = get_text()
    language = input("Translate the summary into which language? ")

    prompt = f"""Summarize the following text in exactly 3 bullet points.
Then translate those same 3 bullet points into {language}.

Use this format:

SUMMARY:
- ...
- ...
- ...

TRANSLATION ({language}):
- ...
- ...
- ...

Text:
{text}
"""

    print("\nThinking...\n")

    response = model.generate_content(prompt)
    result = response.text

    print(result)

    save = input("\nSave result to summary_translated.md? (y/n): ").lower()
    if save == "y":
        with open("summary_translated.md", "w", encoding="utf-8") as f:
            f.write(result)
        print("Saved.")


main()