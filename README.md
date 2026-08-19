# Secure Code Assessment

## CodSoft Cyber Security Internship - Task 3

### Objective
To identify common security vulnerabilities in source code using a simple Python-based static code scanner.

### Vulnerabilities Detected

1. Hardcoded Password
2. Use of eval()
3. Use of os.system()

### Recommended Fixes

- Do not store passwords directly in source code.
- Avoid using eval() with user-controlled input.
- Avoid os.system() with untrusted input.
- Validate and sanitize user input.

### Tools Used

- Python
- Visual Studio Code
- Regular Expressions (Regex)

### Result

The scanner successfully detected multiple common security issues in the sample source code and provided recommended fixes.