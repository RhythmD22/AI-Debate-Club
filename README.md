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
- [Design System](#design-system)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

---

## Features

| Feature | Description |
|---------|------------|
| Formal Debate Structure | Stage-based moderation engine (Opening Statements → Rebuttals → Closing Statements) for coherent, phased discourse |
| User-as-Moderator | Real-time interventions, topic pivots, and direct challenges to AI participants from the chat input |
| Curated Persona Roster | 9 distinct contemporary figures across 4 categories — Architects/Philosophers, Techno-Visionaries, Social Critics, and Foundations |
| Persona Orchestration | Strict one-turn-at-a-time enforcement via system instructions and round-robin turn logic |
| Tone Control | Four debate tones (Civil, Balanced, Fiery, Humorous) with custom system-instruction modifiers |
| Multi-Model Engine | 7 Gemini and Gemma model variants — benchmark different AI intellects in real-time |
| Dark Mode | Automatic light/dark theming via CSS `light-dark()` — no Python-side theme detection |
| Surface Elevation | Two-tier surface system (`#1a1a1a` → `#242424`) for alternate backgrounds in dark mode |
| Shadow System | Four shadow levels that activate exclusively in dark mode to replace border-based elevation |
| Curated Typography | Inter (UI), Playfair Display (headings), Merriweather (body) loaded via Google Fonts |
| Responsive Layout | Mobile-first responsive design with sticky header release, fluid chat bubbles, and compressed hero card |

---

## Demo

**[ai-debate-club.streamlit.app](https://ai-debate-club.streamlit.app)**

Hosted on Streamlit Community Cloud. A Gemini API key is configured server-side — no local setup needed to try the app.

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
├── .gitignore              # Git ignore rules
├── .python-version         # Pinned Python version (3.13+)
├── .env.example            # Environment variable template
├── app.py                  # Streamlit application, debate engine, and session logic
├── styles.css              # Custom styling with light-dark() theming
├── requirements.txt        # Python dependencies
└── README.md
```

The app is a single-file Streamlit application. Debate state is managed entirely through Streamlit's `session_state`, which orchestrates persona turn-taking, stage progression, and user interventions. The Gemini API is called per-turn with structured system prompts that enforce debate role, tone, and format. Styling is loaded from an external `styles.css` file injected via `st.markdown`. All theme values use CSS custom properties with `light-dark()` — no Python-side dark mode detection required.

---

## Design System

AI Debate Club uses CSS custom properties with `light-dark()` for automatic light/dark theming:

### Colors

| Token | Light | Dark | Usage |
|-------|-------|------|-------|
| `--color-primary` | `#064e3b` | `#10b981` | Accents, borders, labels, focus rings, buttons |
| `--color-primary-hover` | `#0a6950` | `#34d399` | Button hover, interactive states |
| `--color-primary-border` | `rgba(6,78,59,0.2)` | `rgba(16,185,129,0.25)` | Sidebar header underline |
| `--color-on-primary` | `#ffffff` | `#022c22` | Text on primary-colored backgrounds (tags, buttons) |
| `--color-surface` | `#ffffff` | `#1a1a1a` | Page background |
| `--color-surface-alt` | `#f9faf9` | `#242424` | Alternate background (hero-card-inner) |
| `--color-surface-raised` | `#ffffff` | `#1a1a1a` | Elevated containers (hero card, chat bubbles) |
| `--color-surface-transparent` | `rgba(255,255,255,0.85)` | `rgba(26,26,26,0.88)` | Sticky header with backdrop blur |
| `--color-border` | `rgba(128,128,128,0.2)` | `#3a3a3a` | Primary borders (sidebar, selects) |
| `--color-border-light` | `rgba(128,128,128,0.1)` | `#2e2e2e` | Subtle borders (chat bubbles, sticky header) |
| `--color-text` | `inherit` | `#e8e8e8` | Primary text |
| `--color-text-secondary` | `#555555` | `#999999` | Secondary descriptions |
| `--color-text-muted` | `#777777` | `#777777` | Muted meta text |

### Shadows

| Token | Light | Dark | Usage |
|-------|-------|------|-------|
| `--shadow-hero` | `none` | `0 20px 25px -5px rgba(0,0,0,0.65)` | Hero card elevation |
| `--shadow-bubble` | `none` | `0 1px 2px rgba(0,0,0,0.35)` | Chat bubble elevation (lift on hover) |
| `--shadow-sticky` | `none` | `0 4px 6px -2px rgba(0,0,0,0.45)` | Sticky topic header |
| `--shadow-button` | `0 4px 6px rgba(0,0,0,0.1)` | `0 2px 4px rgba(0,0,0,0.35)` | Initialize Debate button |
| `--shadow-button-hover` | `0 6px 12px rgba(0,0,0,0.2)` | `0 10px 15px -3px rgba(0,0,0,0.55)` | Button hover state |

### Typography

| Element | Font | Weight | Size | Line Height |
|---------|------|--------|------|-------------|
| Headings | Playfair Display | 700 | `1.2rem`–`3rem` | `1.15`–`1.35` |
| Body text | Merriweather | 400 | `1.2rem` | `1.5` |
| UI labels | Playfair Display | 700 | `0.8rem` | `1.6` |
| Chat bubbles | Inter | 400 | `0.95rem` | `1.55` |
| Controls | Inter | 400–600 | `0.85rem`–`1rem` | `1.5` |

Line-heights are proportional — larger text gets tighter leading, smaller text gets looser.

**Key design decisions:**
- **`light-dark()` theming** — every color and shadow uses the CSS `light-dark()` function; the browser resolves values based on `color-scheme` with no Python-side detection
- **Borders in light, shadows in dark** — elements keep their original borders in light mode (preserving the original UI) and gain shadows in dark mode where borders alone don't provide enough depth
- **Saturation-matched dark accent** — `#10b981` (emerald-500) was chosen for dark mode to match the light mode's `#064e3b` at the same saturation level (88%)
- **Streamlit specificity** — many selectors require `!important` to override Streamlit's aggressive default styles; custom properties isolate theme values from selector wars
- **Single CSS file** — all styling consolidated in `styles.css` with no build step or preprocessor

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

4. Run the app:

```bash
streamlit run app.py
```

5. Open `http://localhost:8501` in your browser

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