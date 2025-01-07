# Subtle ZeroDivisionError in Python
This repository demonstrates a subtle bug that can lead to a `ZeroDivisionError` in a Python function.  The bug is not immediately apparent and highlights the importance of thorough input validation.

## The Bug
The `function_with_uncommon_bug` function aims to handle different input values (x). However, a subtle edge case is not properly handled, possibly leading to a `ZeroDivisionError`.

## Solution
The provided solution shows how to handle this edge case robustly, preventing the `ZeroDivisionError`.