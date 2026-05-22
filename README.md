# 🎙️ MeetMind AI — AI Video Meeting Assistant

## ✨ What It Does

MeetMind AI is an end-to-end autonomous meeting intelligence pipeline that transforms any video or audio source into structured, actionable insights — with zero manual effort.

| Feature | Description |
|---|---|
| 🔗 **YouTube + Local file** | Paste any YouTube URL or upload MP3/MP4/WAV/M4A |
| 🗣️ **Bilingual Transcription** | English via Whisper · Hinglish via Sarvam AI |
| 📋 **Auto Summary** | Professional bullet-point meeting summary |
| ✅ **Action Items** | Extracts tasks with owner & deadline |
| 🔑 **Key Decisions** | Identifies all decisions made |
| ❓ **Open Questions** | Flags unresolved topics needing follow-up |
| 💬 **RAG Chat** | Ask anything about your meeting — powered by ChromaDB |
| ⬇️ **Download** | Export full transcript as `.txt` |

---

## 🏗️ System Architecture
┌─────────────────────────────────────────────────────────────────┐
│                        MeetMind AI Pipeline                     │
└─────────────────────────────────────────────────────────────────┘

  YouTube URL / Local File
          │
          ▼
  ┌───────────────────┐
  │  Audio Processor  │  yt-dlp · pydub · FFmpeg
  │                   │  → Downloads, converts to WAV
  │                   │  → Chunks into 10-min pieces
  └────────┬──────────┘
           │
           ▼
  ┌───────────────────┐
  │    Transcriber    │  English  → OpenAI Whisper (local)
  │                   │  Hinglish → Sarvam AI STT-Translate
  │                   │  → Validates chunks, skips empty
  └────────┬──────────┘
           │
           ▼
  ┌───────────────────────────────────────────────┐
  │              Analyser (3 parallel chains)     │
  │                                               │
  │  summarize.py  → Map-Reduce summary           │
  │  extractor.py  → Action items + decisions +   │
  │                  open questions               │
  │                                               │
  │  LLM: Mistral AI (mistral-small-latest)       │
  │  Framework: LangChain LCEL                    │
  └────────┬──────────────────────────────────────┘
           │
           ▼
  ┌───────────────────┐
  │   Vector Store    │  RecursiveCharacterTextSplitter
  │                   │  Embeddings: all-MiniLM-L6-v2
  │                   │  DB: ChromaDB (local persist)
  └────────┬──────────┘
           │
           ▼
  ┌───────────────────┐
  │   RAG Chat Engine │  Top-4 similarity retrieval
  │                   │  Mistral AI generation
  │                   │  Strict context grounding
  └───────────────────┘
           │
           ▼
  ┌─────────────────────────────────────────────┐
  │           Streamlit UI (Production)         │
  │  Step indicator · Tabs · Metrics · Chat     │
  └─────────────────────────────────────────────┘

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **LLM** | Mistral AI `mistral-small-latest` |
| **Transcription (EN)** | OpenAI Whisper `small` (local inference) |
| **Transcription (HI)** | Sarvam AI `saaras:v3` STT-Translate API |
| **Framework** | LangChain + LangChain LCEL |
| **Vector Database** | ChromaDB |
| **Embeddings** | `all-MiniLM-L6-v2` (HuggingFace) |
| **Audio Processing** | yt-dlp, pydub, FFmpeg |
| **UI** | Streamlit |
| **Deployment** | Streamlit Community Cloud |

---

## 📁 Project Structure

```
ai-video-assistant/
│
├── streamlit_app.py          # Production Streamlit UI
├── main.py                   # CLI entry point + pipeline orchestrator
│
├── core/
│   ├── transcriber.py        # Whisper + Sarvam AI routing
│   ├── summarize.py          # Map-Reduce summarisation chain
│   ├── extractor.py          # Action items, decisions, questions
│   ├── rag_engine.py         # RAG pipeline + chat interface
│   └── vector_store.py       # ChromaDB + MiniLM embeddings
│
├── utils/
│   └── audio_processor.py    # yt-dlp download, WAV convert, chunking
│
├── requirements.txt          # Python dependencies
├── packages.txt              # System dependencies (FFmpeg for Streamlit Cloud)
└── .env                      # API keys (never commit this)
```

---

## ⚡ Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/imVikash-ai/ai-video-assistant.git
cd ai-video-assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> **Note:** First run downloads the Whisper `small` model (~244MB) and `all-MiniLM-L6-v2` embeddings automatically.

### 4. Set up environment variables

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_mistral_api_key_here
SARVAM_API_KEY=your_sarvam_api_key_here       # Only needed for Hinglish
WHISPER_MODEL=small                            # Options: tiny, base, small, medium, large
```

### 5. Run the app

```bash
streamlit run streamlit_app.py
```

Or use the CLI:

```bash
python main.py
```

---

## 🔑 Getting API Keys

| Service | Get Key | Used For |
|---|---|---|
| **Mistral AI** | [console.mistral.ai](https://console.mistral.ai) | Summarisation, extraction, RAG |
| **Sarvam AI** | [dashboard.sarvam.ai](https://dashboard.sarvam.ai) | Hinglish transcription only |

> Whisper runs **locally** — no API key needed for English transcription.

---

## 🚀 Deploying to Streamlit Cloud

### 1. Push to GitHub (without `.env`)

```bash
git add .
git commit -m "deploy"
git push origin main
```

### 2. Create `packages.txt` in repo root

```
ffmpeg
```

### 3. Deploy on [share.streamlit.io](https://share.streamlit.io)

- Repository: `imVikash-ai/ai-video-assistant`
- Branch: `main`
- Main file: `streamlit_app.py`

### 4. Add secrets

Go to **App Settings → Secrets** and add:

```toml
MISTRAL_API_KEY = "your_key_here"
SARVAM_API_KEY = "your_key_here"
```

---

## 🎯 Usage Examples

### YouTube Video
```
Input:  https://www.youtube.com/watch?v=your_video_id
Output: Summary + Action Items + Key Decisions + RAG Chat
```

### Local File
```
Input:  /path/to/meeting_recording.mp3
Output: Full transcript + structured analysis + downloadable report
```

### RAG Chat Examples
```
You: Who was assigned the marketing campaign task?
AI:  Based on the transcript, Sarah was assigned the marketing campaign...

You: What budget was approved for Q3?
AI:  The team approved a budget of $50,000 for Q3 as discussed at 14:32...

You: What are the unresolved issues?
AI:  Two open questions remain: the vendor selection and the launch timeline...
```

---

## 🌐 Language Support

| Language | Engine | Notes |
|---|---|---|
| **English** | OpenAI Whisper (local) | No API needed, runs offline |
| **Hinglish** | Sarvam AI `saaras:v3` | Hindi + English mixed, auto-translates to English |

---

## ⚙️ Configuration

| Variable | Default | Description |
|---|---|---|
| `WHISPER_MODEL` | `small` | Whisper model size: `tiny` · `base` · `small` · `medium` · `large` |
| `SARVAM_STT_MODEL` | `saaras:v3` | Sarvam model version |
| `CHROMA_DIR` | `vector_db` | ChromaDB persistence directory |
| `EMBEDDING_MODEL` | `all-MiniLM-L6-v2` | HuggingFace sentence embedding model |

**Whisper model trade-offs:**

| Model | Size | Speed | Accuracy |
|---|---|---|---|
| tiny | 75MB | ⚡⚡⚡⚡ | ⭐⭐ |
| base | 145MB | ⚡⚡⚡ | ⭐⭐⭐ |
| small | 244MB | ⚡⚡ | ⭐⭐⭐⭐ |
| medium | 769MB | ⚡ | ⭐⭐⭐⭐⭐ |

---

## 🐛 Troubleshooting

### `cannot reshape tensor of 0 elements`
Whisper received an empty audio chunk. Fixed in `transcriber.py` with `_is_valid_chunk()` guard — ensure you're using the latest version.

### `No pyproject.toml found` on Streamlit Cloud
Remove `uv.lock` from your repo — Streamlit Cloud detects it and tries to use `uv` instead of `requirements.txt`.
```bash
rm uv.lock
git add . && git commit -m "remove uv.lock" && git push
```

### `ModuleNotFoundError: torchvision`
Install CPU-only version:
```bash
pip install torchvision --index-url https://download.pytorch.org/whl/cpu
```

### FFmpeg not found
```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# Mac
brew install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html and add to PATH
```

---

## 🗺️ Roadmap

- [ ] Speaker diarization (who said what)
- [ ] PDF export of full report
- [ ] Multi-language support (beyond Hinglish)
- [ ] Meeting comparison across sessions
- [ ] Slack / Teams integration for auto-upload
- [ ] Streaming transcription (real-time)

---

## 👨‍💻 Author

**Vikash Kumar** — Gen AI Engineer

[LinkedIn] = (https://linkedin.com/in/vikashkumar-ai)
[GitHub] = (https://github.com/imVikash-ai)

---
