import streamlit as st
from google import genai
from google.genai import types
import os
import random
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    client = genai.Client(api_key=api_key)
else:
    st.error("API Key not found. Please check your .env file or environment variables.")
    st.stop()

PERSONAS = {
    # 1. The Architects & Philosophers (AI Ethics & Existential Risk)
    "Geoffrey Hinton": "Computer scientist and 'Godfather of AI', pioneer of neural networks who now warns of the potential dangers of superintelligence.",
    "Nick Bostrom": "Philosopher and polymath, author of Superintelligence, focused on existential risks and the long-term future of humanity.",
    "Sam Harris": "Neuroscientist and philosopher, rationalist, atheist, focuses on ethics, AI risks, meditation, and honest conversation.",
    
    # 2. The Techno-Visionaries (Innovation & Acceleration)
    "Elon Musk": "Tech visionary, free speech advocate, innovation and long-termism focused, optimistic about AI and space.",
    "Marc Andreessen": "Techno-optimist venture capitalist, advocates for accelerationism, believes technology is the primary driver of human progress.",
    
    # 3. The Social & Political Critics (Power & Equality)
    "Noam Chomsky": "Linguist and social critic, skeptical of current AI, focuses on human cognition, power structures, and ethics.",
    "Bernie Sanders": "Progressive politician, focuses on economic inequality, corporate power, healthcare, and workers' rights.",
    
    # 4. The Foundations (Individualism & Economics)
    "Thomas Sowell": "Conservative economist, emphasizes empirical evidence, unintended consequences of policies, and free markets.",
    "Jordan Peterson": "Psychologist, emphasizes personal responsibility, critiques radical progressivism and identity politics."
}

st.set_page_config(
    page_title="AI Debate Club", 
    page_icon="⚖️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("styles.css")

with st.sidebar:
    st.markdown('<div class="sidebar-header">AI Debate Club</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-section-header">Subject & Participants</div>', unsafe_allow_html=True)
    debate_topic = st.text_area(
        "Debate Topic", 
        value="Should AI be regulated to prevent existential risk?",
        height=60
    )

    selected_personas = st.multiselect(
        "Select Participants (Max 4)",
        options=list(PERSONAS.keys()),
        default=["Geoffrey Hinton", "Marc Andreessen"],
        max_selections=4,
        help="Select up to 4 participants for the debate simulation."
    )

    st.divider()
    
    st.markdown('<div class="sidebar-section-header">Settings</div>', unsafe_allow_html=True)
    tone = st.selectbox(
        "Debate Tone",
        options=["Civil", "Balanced", "Fiery", "Humorous"],
        index=1
    )
    
    st.markdown('<div class="sidebar-section-header">Engine</div>', unsafe_allow_html=True)
    model_choice = st.selectbox(
        "Select Model",
        options=[
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.1-flash-lite",
            "gemini-3.1-flash-lite-preview",
            "gemini-3-flash-preview",
            "gemma-4-31b-it",
            "gemma-4-26b-a4b-it"
        ],
        label_visibility="collapsed"
    )

    st.markdown("<div style='margin-top: 0.5rem;'></div>", unsafe_allow_html=True)
    start_debate = st.button("Initialize Debate")

# Session State Initialization
if "messages" not in st.session_state or start_debate:
    st.session_state.messages = []
    st.session_state.debate_active = False

if start_debate:
    if len(selected_personas) < 2:
        st.sidebar.error("Select at least 2 participants.")
    else:
        st.session_state.debate_active = True
        st.session_state.messages.append({"role": "system_marker", "content": "Debate started"})

# AI Logic (Formalized Debate Structure)
def get_gemini_response(messages, stage, next_persona):
    persona_descriptions = "\n".join([f"- {name}: {desc}" for name, desc in PERSONAS.items() if name in selected_personas])
    debate_momentum = random.randint(1000, 9999)

    tone_instructions = {
        "Civil": "Use formal, sophisticated vocabulary. Focus on logical structures and peer-reviewed concepts.",
        "Balanced": "Maintain a neutral, objective stance. Acknowledge multiple sides of an argument.",
        "Fiery": "Be provocative and assertive. Use strong rhetoric and call out logical fallacies.",
        "Humorous": "Incorporate wit, irony, and clever analogies. Be entertaining while maintaining core arguments."
    }

    selected_tone_instruction = tone_instructions.get(tone, "")

    system_instruction = f"""
    You are a Master Moderator conducting a formal debate.
    Topic: '{debate_topic}'
    Current Stage: {stage}
    Participants: {', '.join(selected_personas)}
    Debate Momentum Seed: {debate_momentum}
    
    STRICT GUIDELINES:
    - Tone: {selected_tone_instruction}
    - Stage: {stage}.
    - IDENTITY: You are ONLY playing the role of: {next_persona}.
    - Do NOT write responses for any other participant. 
    - Format: Start exactly with: "**{next_persona}**: "
    - Keep responses to 3-5 sentences.
    - Be unique and creative; avoid repeating past arguments.
    """

    history = [
        types.Content(role="user", parts=[types.Part.from_text(text=system_instruction)]),
        types.Content(role="model", parts=[types.Part.from_text(text=f"Moderator: Stage is {stage}. {next_persona}, you have the floor.")])
    ]
    
    for msg in messages:
        if msg["role"] == "system_marker":
            continue
        
        # Post-process message to ensure clean bold labels
        clean_content = msg["content"]
        if not clean_content.startswith("**"):
            for p in selected_personas:
                if clean_content.startswith(p):
                    clean_content = clean_content.replace(p, f"**{p}**", 1)
        
        role = "user" if msg["role"] == "user" else "model"
        history.append(types.Content(role=role, parts=[types.Part.from_text(text=clean_content)]))

    prompt = f"Moderator: {next_persona}, please provide your response for the {stage}."

    try:
        chat = client.chats.create(model=model_choice, history=history)
        response = chat.send_message(prompt)
        return response.text
    except Exception:
        try:
            chat = client.chats.create(model="gemini-2.0-flash", history=history)
            response = chat.send_message(prompt)
            return response.text
        except Exception as e2:
            return f"Critical Engine Failure: {str(e2)}"

if not st.session_state.get("debate_active"):
    st.markdown(f"""
    <div class="hero-card" style="border: 2px solid #064e3b !important;">
        <h1 style="font-size: 3rem; margin-bottom: 1rem;">The Arena Awaits</h1>
        <p class="serif-text" style="font-size: 1.2rem; margin-bottom: 2rem;">
            Step into a world of intellectual rigor. Orchestrate dialogues between history's most compelling minds on the topics that define our future.
        </p>
        <div style="text-align: left; padding: 1.5rem; border-radius: 10px; border: 2px solid #064e3b;">
            <p style="font-weight: 600; margin-bottom: 0.5rem; color: #064e3b;">HOW TO BEGIN:</p>
            <ul style="font-size: 0.9rem;">
                <li>Define a <b>Debate Subject</b> in the Command Center.</li>
                <li>Choose your <b>Participants</b> from our curated personas.</li>
                <li>Adjust the <b>Tone</b> and <b>Engine</b> for desired depth.</li>
                <li>Click <b>Initialize Debate</b> to start the simulation.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    stage = st.session_state.get("debate_stage", "Starting...")
    st.markdown(f"""
    <div class="sticky-topic">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <span style="color: #064e3b; font-size: 0.8rem; font-weight: 700; text-transform: uppercase;">Current Subject:</span>
                <h3 style="margin: 0; font-size: 1.2rem;">{debate_topic}</h3>
                <div style="font-size: 0.75rem; font-style: italic; margin-top: 0.2rem;">Tip: Direct the debate, challenge assumptions, or pivot the focus.</div>
            </div>
            <div style="text-align: right;">
                <span style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase;">Current Stage:</span>
                <div style="font-weight: 600;">{stage}</div>
            </div>
        </div>
    </div>
    <div class="main-content"></div>
    """, unsafe_allow_html=True)

    col_left, col_mid, col_right = st.columns([1, 10, 1])
    with col_mid:
        for i, message in enumerate(st.session_state.messages):
            if message["role"] == "system_marker":
                continue

            content = message["content"]
            if message["role"] == "user":
                st.markdown(f"""
                <div class="chat-row participant-b">
                    <div class="chat-bubble" style="border-left: 4px solid #064e3b;">
                        <div class="persona-label">Moderator (You)</div>
                        {content}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                if content.startswith("**"):
                    name_end = content.find("**", 2)
                    if name_end != -1 and content[name_end:name_end+3] == "**:":
                        persona_name = content[2:name_end]
                        display_content = content[name_end+3:].strip()
                    else:
                        persona_name = "AI Participant"
                        display_content = content
                else:
                    persona_name = "AI Participant"
                    display_content = content
                is_even = i % 2 == 0
                alignment_class = "participant-a" if is_even else "participant-b"

                st.markdown(f"""
                <div class="chat-row {alignment_class}">
                    <div class="chat-bubble">
                        <div class="persona-label">{persona_name}</div>
                        {display_content}
                    </div>
                </div>
                """, unsafe_allow_html=True)

    user_input = st.chat_input("Intervene as Moderator...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.rerun()

    if len(st.session_state.messages) > 0:
        last_msg = st.session_state.messages[-1]
        if last_msg["role"] == "system_marker" or last_msg["role"] == "user":
            with st.spinner("Moderator is crafting the next response..."):
                assistant_msgs = [m for m in st.session_state.messages if m["role"] == "assistant"]
                num_msgs = len(assistant_msgs)
                next_persona = selected_personas[num_msgs % len(selected_personas)]

                if num_msgs < len(selected_personas):
                    stage = "Opening Statements"
                elif num_msgs < len(selected_personas) * 2:
                    stage = "Rebuttal & Cross-Examination"
                else:
                    stage = "Closing Statements"

                st.session_state.debate_stage = stage
                response = get_gemini_response(st.session_state.messages, stage, next_persona)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()