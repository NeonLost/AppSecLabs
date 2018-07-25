# Improper Neutralization of CRLF Sequences ('CRLF Injection')

This lab shows how to easy achieve unexpected behavior. The software receives input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could be interpreted as line delimiters when they are sent to a downstream component.

## Core idea
You have single account **`jdoe:1234`**. You must log in with admin privileges and capture the flag.
