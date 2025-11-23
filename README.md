# Translate API
Created by **@arifi_ios**

This project provides a simple API to translate text into any language you want.

## Features
- Automatically detects the source language.
- Translates any text into any language you want.
- Uses Google Translate Web UI internal API.
- Lightweight and easy to use via HTTP.

## Requirements
Install the required libraries:
```bash
pip install flask requests user_agent
```

## Example Response
```bash
{
  "status": "success",
  "Real_Text": "hello",
  "Translated_Text": "مرحبا",
  "Time": 1730000000
}

```
