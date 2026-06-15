# AI Debate Club - Multi-Persona Debate Simulator

## Overview

AI Debate Club is a high-fidelity interactive web application that simulates structured, high-stakes intellectual discourse. It orchestrates debates between a curated roster of contemporary figures, transitioning them through formal stages: **Opening Statements**, **Rebuttals**, and **Closing Statements**. 

The project demonstrates a mature approach to LLM orchestration, structured prompt engineering, and a cohesive UI/UX design.

## Getting Started

1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Create a `.env` file with `GEMINI_API_KEY=your_key`.
4. Run: `streamlit run app.py`.

## Key Features

- **Formal Debate Structure**: Unlike standard chatbots, this app implements a stage-based moderation engine that guides the LLM through distinct phases of argumentation, ensuring coherent and productive discourse.
- **Architectural Separation**: Presentation logic is isolated into an external `styles.css` file for cleaner maintainability.
- **Dynamic Persona Orchestration**: Multi-persona role-play that ensures one-turn-at-a-time responses, strictly enforced via system instructions and round-robin persona logic.
- **User-as-Moderator**: The interface empowers the user to act as the primary moderator, enabling real-time interventions, topic pivots, and direct challenges to the AI participants.
- **Engine Control**: Built-in support for multiple Gemini and Gemma model variants, allowing users to benchmark different AI "intellects" in real-time.

## Technology Stack

- **Core**: Python 3.13+, Streamlit.
- **AI Engine**: Google Gemini API (`google-genai` 2026 SDK).
- **Design**: Custom CSS, Google Fonts ('Inter', 'Playfair Display', 'Merriweather').
- **Orchestration**: Custom session state management to handle multi-persona turn-taking.
