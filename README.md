# Text Case Converter 🔤

**Completed:** September 27, 2025

A Python command-line application designed to convert and modify text capitalization. The program supports four different conversion modes, including full uppercase, full lowercase, and character-based capitalization changes after periods.

I developed this project to practice Python programming concepts such as string manipulation, loops, conditional statements, Boolean variables, and ASCII character processing.

## Features

- **Uppercase conversion:** Convert all letters in a text to uppercase.
- **Lowercase conversion:** Convert all letters in a text to lowercase.
- **Capitalization after periods:** Convert the first lowercase English letter after a period and space into uppercase.
- **Lowercase after periods:** Convert the first uppercase English letter after a period and space into lowercase.
- **Input validation:** Reject invalid commands and ask the user to try again.
- **Character-by-character processing:** Analyze individual characters and modify them using custom algorithms.
- **No external dependencies:** Runs using standard Python functionality.

## Requirements

- Python 3
- No additional libraries required.

## Installation

1. Download `Lower_Upper Letters.py` from this repository.
2. Make sure Python 3 is installed on your computer.
3. Open a terminal in the folder containing the Python file.
4. Run:

   ```bash
   python "Lower_Upper Letters.py"
   ```

## How to Use

When the program starts, enter the text you want to modify.

The program then displays four available conversion modes:

| Command | Description |
|---|---|
| `UP` | Convert all letters to uppercase |
| `LOW` | Convert all letters to lowercase |
| `DOT` | Capitalize the first lowercase letter following a period and space |
| `DOTS` | Lowercase the first uppercase letter following a period and space |

Commands are case-insensitive.

### Mode 1 — Uppercase (UP)

Converts all letters in the input text to uppercase.

**Example:**

```text
Input:  Hello, my name is Nik!
Mode:   UP
Output: HELLO, MY NAME IS NIK!
```

The program processes every character using Python's `.upper()` method.

### Mode 2 — Lowercase (LOW)

Converts all letters in the input text to lowercase.

**Example:**

```text
Input:  HELLO, MY NAME IS NIK!
Mode:   LOW
Output: hello, my name is nik!
```

The program uses Python's `.lower()` method to perform the conversion.

### Mode 3 — Capitalization After Periods (DOT)

This mode searches for periods followed by spaces and converts the first eligible lowercase English letter into uppercase.

**Example:**

```text
Input:  hello. how are you? i am fine.
Mode:   DOT
Output: hello. How are you? i am fine.
```

Only letters following periods are considered. The first letter of the entire text is not automatically capitalized.

### Mode 4 — Lowercase After Periods (DOTS)

This mode performs the opposite operation, converting the first eligible uppercase English letter following a period and space into lowercase.

**Example:**

```text
Input:  Hello. HOW are you? GREAT!
Mode:   DOTS
Output: Hello. hOW are you? GREAT!
```

Only the first eligible letter following a period is modified, rather than the entire word.

## How It Works

### 1. Text Input

The program begins by asking the user to enter text:

```python
word = input("Give your text:\n")
```

The entered text is stored in the `word` variable for processing.

### 2. Character-by-Character Processing

The program uses a `for` loop to examine each character individually.

For example, uppercase conversion uses:

```python
for i in range(len(word)):
    new_word += word[i].upper()
```

Each modified character is appended to a new string.

### 3. ASCII Character Detection

The period-based conversion modes use Python's `ord()` function to retrieve the numerical character value.

```python
letter = ord(word[i])
```

The algorithms check for specific ASCII values:

| ASCII value | Character |
|---|---|
| `46` | Period (`.`) |
| `32` | Space |
| `65–90` | Uppercase English letters (A–Z) |
| `97–122` | Lowercase English letters (a–z) |

These values help the program decide when a letter should be converted.

### 4. Period and Space Detection

The program uses Boolean variables to track periods and spaces:

```python
dot = False
space = False
```

When a period is detected, the program checks whether spaces and an eligible character follow.

If a matching letter is found, the program removes the previously appended character and replaces it with its converted version.

For example:

```python
new_word = new_word[:-1]
new_word += word[i].upper()
```

The tracking variables are then reset so the algorithm can search for another period.

### 5. Input Validation

The program verifies that the selected mode matches one of the supported commands.

If an invalid command is entered, an error message appears and the program asks for another selection.

After completing a valid conversion, the result is displayed and the program ends.

## Known Limitations

- **ASCII-based sentence conversion:** The `DOT` and `DOTS` algorithms work with English letters A–Z and do not fully support special characters such as Slovenian `č`, `š`, and `ž`.
- **Period-based detection:** Sentence conversion requires a period followed by a space or spaces. Other punctuation patterns are not handled.
- **First-letter conversion:** The period-based modes modify only the first matching character after a period, not an entire word or sentence.
- **Single text input:** The application processes one line of text per execution.
- **No graphical interface:** All interactions take place in the terminal.
- **No file support:** Text must be entered manually and cannot be loaded directly from a document.

## Development Note

This project was created as a personal Python programming exercise to improve my understanding of string manipulation and character processing.

Instead of relying entirely on Python's built-in capitalization functions, I experimented with custom algorithms that detect punctuation, track character positions, and modify text using ASCII values.

The project demonstrates practical use of loops, conditional statements, strings, Boolean variables, and input validation.


**Author:** [Nik Berginc](https://github.com/nikberginc)
