# Improper Neutralization of CRLF Sequences ('CRLF Injection')

This lab shows how to easy return to 2000s, when databases were used not everywhere to store data. 
The software get user input, but does't sanitize it or sanitizes incorrectly. Special chars can be interpreted as line delimiters when they are sent to a internal component.

## Core idea
You have single account **`jdoe:1234`**. You have to log in with admin privileges and capture the flag.
