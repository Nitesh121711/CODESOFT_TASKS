import re

FILE = "vulnerable_code.py"

with open(FILE, "r", encoding="utf-8") as file:
    code = file.read()

issues = []

patterns = {
    "Hardcoded Password": r'password\s*=\s*["\'].*?["\']',
    "Use of eval()": r'\beval\s*\(',
    "Use of os.system()": r'\bos\.system\s*\(',
}

for issue, pattern in patterns.items():
    if re.search(pattern, code):
        issues.append(issue)

print("\n=== Secure Code Assessment Report ===\n")

for i, issue in enumerate(issues, 1):
    print(f"{i}. {issue}")

print("\nRecommended Fixes:")
print("- Do not store passwords directly in source code.")
print("- Avoid eval() with user input.")
print("- Avoid os.system() with untrusted input.")
print("- Validate and sanitize user input.")