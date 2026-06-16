# AI Debate Club

> Multi-persona debate simulator — orchestrate structured, high-stakes discourse between AI-powered contemporary figures with you as the moderator.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.13+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/built%20with-Streamlit-FF4B4B?logo=streamlit)](https://streamlit.io)

---

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Install](#install)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

---

## Features

| Feature | Description |
|---------|------------|
| Formal Debate Structure | Stage-based moderation engine (Opening Statements → Rebuttals → Closing Statements) for coherent, phased discourse |
| User-as-Moderator | Real-time interventions, topic pivots, and direct challenges to AI participants from the UI |
| Dynamic Persona Orchestration | Multi-persona role-play with strict one-turn-at-a-time enforcement via system instructions and round-robin logic |
| Multi-Model Engine | Built-in support for Gemini and Gemma model variants — benchmark different AI intellects in real-time |
| Architectural Separation | Presentation logic isolated in external `styles.css` for clean maintainability |
| Custom UX | Curated typography (Inter, Playfair Display, Merriweather) and custom CSS for an immersive debate experience |

---

## Demo

Run the app locally with Streamlit — no hosted demo available.

---

## Install

```bash
git clone https://github.com/rhythmd22/AI-Debate-Club.git
cd "AI Debate Club"

pip install -r requirements.txt
```

---

## Architecture

```
AI Debate Club/
├── app.py                  # Streamlit application, debate engine, and session logic
├── styles.css              # Custom styling and typography
├── requirements.txt        # Python dependencies
├── .python-version         # Pinned Python version (3.13+)
├── .env.example            # Environment variable template
└── README.md
```

The app is a single-file Streamlit application with modular section functions. Debate state is managed entirely through Streamlit's `session_state`, which orchestrates persona turn-taking, stage progression, and user interventions. The Gemini API is called per-turn with structured system prompts that enforce debate role and format. Styling is loaded from an external `styles.css` file injected via `st.markdown`.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Core | Python 3.13+ |
| UI Framework | [Streamlit](https://streamlit.io) |
| AI Engine | [Google Gemini API](https://ai.google.dev) (`google-genai` SDK) |
| Environment | [python-dotenv](https://github.com/theskumar/python-dotenv) |
| Fonts | [Inter](https://fonts.google.com/specimen/Inter), [Playfair Display](https://fonts.google.com/specimen/Playfair+Display), [Merriweather](https://fonts.google.com/specimen/Merriweather) |

---

## Getting Started

### Prerequisites

- [Python 3.13+](https://python.org)
- A [Google Gemini API key](https://aistudio.google.com/apikey)

### Setup

1. Clone the repository and install dependencies (see [Install](#install))
2. Create your environment file:

```bash
cp .env.example .env
```

3. Edit `.env` with your Gemini API key:

```env
GEMINI_API_KEY=your_gemini_api_key
```

3. Run the app:

```bash
streamlit run app.py
```

4. Open `http://localhost:8501` in your browser

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## License

MIT © [Rhythm Desai](LICENSE)