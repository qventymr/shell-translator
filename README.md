# Shell Translator

A simple command-line translation tool written in Python that automatically detects the source language and translates text to the target language.

## Features

- 🌐 **Automatic language detection** - detects the source language automatically
- 🔄 **Multi-language support** - supports translation between multiple languages
- 🚀 **Easy to use** - simple command-line interface
- ⚡ **Fast translation** - quick response times

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Install dependencies

```bash
pip install translate langdetect
```

### Download the script
```bash
git clone https://github.com/qventymr/shell-translator.git
cd shell-translator
mv main.py translator
```

### Make Executable
```bash
chmod +x translator
```

## Adding to PATH
```bash
sudo mv translator /usr/local/bin/
```

```bash
mkdir -p ~/.local/bin
mv translator ~/.local/bin/
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

## Usage
```bash
translator "Hello world" -l es
```
