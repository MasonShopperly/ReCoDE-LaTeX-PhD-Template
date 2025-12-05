import re
from pathlib import Path

input_file = "phd-thesis/preamble.tex"
output_file = "docs/2_Explanation_Preamble.md"

SNIPPET_NAME = "preamble"

def extract_snippet(tex_lines, name):
    start_marker = f"% START SNIPPET: {name}"
    end_marker   = f"% END SNIPPET: {name}"

    inside_block = False
    lines = []

    for line in tex_lines:
        if start_marker in line:
            inside_block = True
            continue
        if end_marker in line:
            inside_block = False
            break
        if inside_block:
            lines.append(line)

    return "\n".join(lines)

def main():
    tex_lines = Path(input_file).read_text(encoding="utf-8").splitlines()
    snippet = extract_snippet(tex_lines, SNIPPET_NAME)

    if not snippet.strip():
        print(f"[WARN] No snippet found for '{SNIPPET_NAME}'")
        return

    print(f"[INFO] Snippet '{SNIPPET_NAME}' length: {len(snippet)}")

    md_path = Path(output_file)
    md_content = md_path.read_text(encoding="utf-8")

    # 1. Ensure there is a placeholder in the file
    placeholder = "<!-- SNIPPET: preamble -->"

    if placeholder not in md_content:
        # Strategy: strip any existing generated code block and reinsert placeholder
        # Remove old ```latex... ``` block that follows the placeholder (if present)
        pattern = re.compile(
            r"<!-- SNIPPET: preamble -->.*?```latex.*?```",
            re.DOTALL
        )
        md_content = re.sub(pattern, placeholder, md_content)

        # If still not present, append placeholder at end
        if placeholder not in md_content:
            md_content = md_content.rstrip() + "\n\n" + placeholder + "\n"

    # 2. Now replace the placeholder with the new code block
    def repl(_match, snippet_text=snippet):
        return "```latex\n" + snippet_text + "\n```"

    pattern_placeholder = re.escape(placeholder)
    new_md_content, count = re.subn(pattern_placeholder, repl, md_content, count=1)

    if count == 0:
        print("[WARN] Placeholder replacement failed.")
    else:
        print("[INFO] Placeholder replaced with new snippet.")

    md_path.write_text(new_md_content, encoding="utf-8")
    print(f"[DONE] Updated {output_file}")

if __name__ == "__main__":
    main()
