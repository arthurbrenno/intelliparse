# 🧠 Intelliparse

**Smart File Parsing & Content Extraction Made Simple**

Intelliparse is your all-in-one solution to extract text, images, tables, and metadata from **various file formats** - from common documents to complex CAD drawings. Powered by AI for intelligent content understanding. 🚀

```python
from intelliparse.parsers import FileParser
from intelliparse.types import RawFile

# Parse any file with AI-powered insights
file = RawFile.from_path("contract.pdf")
parser = FileParser()
parsed_file = parser.parse(file)

print(f"🔍 Found {len(parsed_file.sections)} sections!")
print(f"📄 Text: {parsed_file.sections[0].text[:200]}...")
```

## 🌟 Features

- **Common File Formats** supported (PDF, DOCX, PPT, Images, Audio, Video, CAD, and more)
- **AI-Powered Insights** - Automatic image descriptions, audio transcriptions, and content analysis
- **Military-Grade Extraction (WIP)** - Text, tables, images, metadata, and document structure
- **Easy Extension** - Add custom parsers in <10 lines of code

## 📦 Installation

```bash
# Install core library
pip install intelliparse

# Install system dependencies (choose your OS)
# Ubuntu/Debian
sudo apt-get install libmagic1
# macOS
brew install libmagic
# Windows (via Chocolatey)
choco install magic
```

## 🚀 Basic Usage

### Parse Any File
```python
file = RawFile.from_bytes(b"file content", "secret_data.xlsx")
parsed = await FileParser().parse_async(file) # ParsedFile

for section in parsed.sections:
    print(f"Section {section.number}:")
    print(f"- Text: {section.text[:100]}...")
    print(f"- Found {len(section.images)} images!")
```

### Extract Tables
```python
table_data = parsed.sections[0].items[0]
if isinstance(table_data, TablePageItem):
    print("📊 Perfect Table Found!")
    print("\n".join(table_data.csv.split("\n")[:3]))
```

## 🔍 Advanced Usage

### AI-Powered Parsing
```python
from intellibricks.agents import Agent
from intellibricks.llms import TextTranscriptionSynapse, Synapse
from intellibricks.llms.types import (
    GenerationConfig,
    ChainOfThought,
    VisualMediaDescription,
    AudioDescription
)

# Use AI to describe images and transcribe audio
parser = FileParser(
    strategy="high",
    visual_description_agent=Agent(
        task="Detailed description of visual elements.",
        instructions=[
            "Describe the provided visual elements in a"
            "detailed manner, following the instructions."
            "Descriptions must be in Portuguese.",
        ],
        metadata={
            "name": "Visual Elements Descriptor",
            "description": "Description of visual elements in Portuguese.",
        },
        synapse=Synapse.of("google/genai/gemini-1.5-flash"),
        response_model=ChainOfThought[VisualMediaDescription],
        output_language="en",
        generation_config=GenerationConfig(timeout=60, max_retries=1),
    ),
    audio_description_agent=Agent(
        task="Audio transcription",
        instructions=[
            "Transcribe the provided audio in a"
            "clear and precise manner, following the instructions."
            "Transcriptions must be in Portuguese.",
        ],
        metadata={
            "name": "Audio Transcriber",
            "description": "Audio transcription in Portuguese.",
        },
        synapse=Synapse.of("google/genai/gemini-1.5-flash"),
        audio_transcriptions_synapse=TextTranscriptionSynapse.of(
            "groq/api/whisper-large-v3-turbo"
        ),
        response_model=ChainOfThought[AudioDescription],
    ),
)

parsed = await parser.parse_async(RawFile.from_path("presentation.mp4"))
print(f"📽 Video Description: {parsed.md}")
```

## 📚 Supported Formats

| Category       | Formats                                                                 |
|----------------|-------------------------------------------------------------------------|
| **Documents**  | PDF, DOCX, PPTX, XLSX, TXT, XML                              |
| **Images**     | PNG, JPG, TIFF, BMP, GIF, SVG, WEBP,                            |
| **Audio/Video**| MP3, WAV, FLAC, AAC, MP4, AVI, MOV,                               |
| **CAD/Design** | DWG                                    |
| **Archives**   | ZIP, RAR, 7Z, TAR, GZ                                                  |
| **Specialized**| PKT (Cisco - TODO),             |

## 🤝 Contributing

We welcome contributors! To get started:
```bash
git clone https://github.com/arthurbrenno/intelliparse.git
cd intelliparse
uv sync
```

Run tests (TODO. Will work like this):
```bash
pytest tests/ --verbose
```

## 📜 License

Apache 2.0 - Made with ❤️ by Arthur Brenno

---
