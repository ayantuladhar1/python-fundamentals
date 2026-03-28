# Python Fundamentals Practice

## Overview
A web-based viewer for a collection of Python learning materials. The app serves Markdown documentation files as a formatted web interface using a simple Python HTTP server.

## Tech Stack
- **Language**: Python 3 (stdlib only, no external dependencies)
- **Server**: Python's built-in `http.server` module
- **Content**: Markdown files in `python_collections/`

## Project Structure
```
app.py                    # Web server entry point
python_collections/       # All documentation content
  *.md                    # Core concept files (01-variables.md, etc.)
  dictionary/             # Dictionary guides
  functions/              # Function guides
  if-else/                # Conditional logic guides
  list/                   # List operation guides
  loops/                  # Loop guides (for_loop/, while/)
  reference/              # Built-in functions, keywords, exceptions
  sets/                   # Set guides
  tuples/                 # Tuple guides
README.md                 # Project overview
```

## Running the App
```bash
python app.py
```
Serves on `http://0.0.0.0:5000`

## Architecture Notes
- No external dependencies required
- The server parses and renders Markdown to HTML on-the-fly
- Sidebar navigation is auto-generated from the file structure
- All topics are browsable from the left sidebar
