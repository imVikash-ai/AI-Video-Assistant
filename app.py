import streamlit as st
import time

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MeetMind AI",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --bg:       #0a0a0f;
    --surface:  #111118;
    --border:   #1e1e2e;
    --accent:   #6c63ff;
    --accent2:  #00d4aa;
    --accent3:  #ff6b6b;
    --text:     #e8e8f0;
    --muted:    #6b6b80;
    --card:     #13131c;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background: var(--bg);
    color: var(--text);
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem; max-width: 1280px; }

/* ── Hero header ── */
.hero {
    display: flex;
    align-items: center;
    gap: 1.2rem;
    padding: 2.5rem 0 1.5rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 2rem;
}
.hero-icon {
    font-size: 2.8rem;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1;
}
.hero h1 {
    font-family: 'Syne', sans-serif;
    font-size: 2.2rem;
    font-weight: 800;
    margin: 0;
    background: linear-gradient(120deg, #fff 40%, var(--accent2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero p {
    margin: 0.2rem 0 0;
    color: var(--muted);
    font-size: 0.9rem;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.04em;
}

/* ── Cards ── */
.card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.5rem;
    margin-bottom: 1.2rem;
    transition: border-color 0.2s;
}
.card:hover { border-color: var(--accent); }
.card-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 0.8rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.card-title span { color: var(--accent2); font-size: 1rem; }

/* ── Pill badge ── */
.pill {
    display: inline-block;
    padding: 0.22rem 0.7rem;
    border-radius: 99px;
    font-size: 0.72rem;
    font-family: 'DM Mono', monospace;
    font-weight: 500;
    letter-spacing: 0.04em;
}
.pill-purple { background: rgba(108,99,255,0.15); color: var(--accent); border: 1px solid rgba(108,99,255,0.3); }
.pill-teal   { background: rgba(0,212,170,0.12);  color: var(--accent2); border: 1px solid rgba(0,212,170,0.25); }
.pill-red    { background: rgba(255,107,107,0.12); color: var(--accent3); border: 1px solid rgba(255,107,107,0.25); }

/* ── Step indicator ── */
.steps {
    display: flex;
    align-items: center;
    gap: 0;
    margin-bottom: 2rem;
    overflow-x: auto;
    padding-bottom: 0.5rem;
}
.step {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    flex-shrink: 0;
}
.step-num {
    width: 28px; height: 28px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-family: 'DM Mono', monospace;
    font-size: 0.75rem;
    font-weight: 500;
    border: 1.5px solid var(--border);
    color: var(--muted);
    background: var(--surface);
    transition: all 0.3s;
}
.step-num.active {
    background: var(--accent);
    border-color: var(--accent);
    color: #fff;
    box-shadow: 0 0 12px rgba(108,99,255,0.4);
}
.step-num.done {
    background: var(--accent2);
    border-color: var(--accent2);
    color: #000;
}
.step-label {
    font-size: 0.78rem;
    color: var(--muted);
    font-family: 'DM Mono', monospace;
}
.step-label.active { color: var(--text); }
.step-connector {
    width: 40px; height: 1px;
    background: var(--border);
    margin: 0 0.4rem;
    flex-shrink: 0;
}

/* ── Input area ── */
.stTextInput > div > div > input,
.stSelectbox > div > div {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    color: var(--text) !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.88rem !important;
}
.stTextInput > div > div > input:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 2px rgba(108,99,255,0.2) !important;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, var(--accent), #8b5cf6) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.6rem 2rem !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.9rem !important;
    letter-spacing: 0.04em !important;
    transition: all 0.2s !important;
    box-shadow: 0 4px 20px rgba(108,99,255,0.3) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 28px rgba(108,99,255,0.45) !important;
}
.stButton > button:disabled {
    background: var(--border) !important;
    box-shadow: none !important;
    transform: none !important;
}

/* ── Chat bubble ── */
.chat-wrap { display: flex; flex-direction: column; gap: 0.8rem; }
.bubble {
    max-width: 80%;
    padding: 0.75rem 1.1rem;
    border-radius: 14px;
    font-size: 0.88rem;
    line-height: 1.55;
}
.bubble-user {
    align-self: flex-end;
    background: linear-gradient(135deg, var(--accent), #8b5cf6);
    color: #fff;
    border-bottom-right-radius: 4px;
}
.bubble-ai {
    align-self: flex-start;
    background: var(--surface);
    border: 1px solid var(--border);
    color: var(--text);
    border-bottom-left-radius: 4px;
}
.bubble-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    color: var(--muted);
    margin-bottom: 0.3rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}

/* ── Transcript box ── */
.transcript-box {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1rem 1.2rem;
    font-family: 'DM Mono', monospace;
    font-size: 0.8rem;
    line-height: 1.7;
    color: #a0a0b8;
    max-height: 200px;
    overflow-y: auto;
    white-space: pre-wrap;
}
.transcript-box::-webkit-scrollbar { width: 4px; }
.transcript-box::-webkit-scrollbar-thumb { background: var(--border); border-radius: 4px; }

/* ── Score badge ── */
.score-ring {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 56px; height: 56px;
    border-radius: 50%;
    border: 3px solid var(--accent2);
    font-family: 'Syne', sans-serif;
    font-size: 1.3rem;
    font-weight: 800;
    color: var(--accent2);
    box-shadow: 0 0 16px rgba(0,212,170,0.25);
    flex-shrink: 0;
}

/* ── Section divider ── */
.divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 1.5rem 0;
}

/* ── Status dot ── */
.status { display:flex; align-items:center; gap:0.4rem; font-size:0.78rem; color:var(--muted); font-family:'DM Mono',monospace; }
.dot { width:7px; height:7px; border-radius:50%; background:var(--accent2); box-shadow:0 0 6px var(--accent2); animation:pulse 2s infinite; }
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.4} }

/* ── Upload drag zone ── */
.stFileUploader > div {
    background: var(--surface) !important;
    border: 1.5px dashed var(--border) !important;
    border-radius: 12px !important;
}

/* ── Expander ── */
.streamlit-expanderHeader {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: var(--surface);
    border-radius: 10px;
    padding: 4px;
    gap: 4px;
    border: 1px solid var(--border);
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.8rem !important;
    color: var(--muted) !important;
    padding: 0.4rem 1rem !important;
}
.stTabs [aria-selected="true"] {
    background: var(--accent) !important;
    color: #fff !important;
}

/* ── Spinner override ── */
.stSpinner > div { border-top-color: var(--accent) !important; }

/* ── Metric ── */
[data-testid="metric-container"] {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1rem 1.2rem;
}
[data-testid="stMetricLabel"] { font-family:'DM Mono',monospace; font-size:0.72rem; color:var(--muted); }
[data-testid="stMetricValue"] { font-family:'Syne',sans-serif; font-weight:800; color:var(--text); }
</style>
""", unsafe_allow_html=True)


# ── Session state init ─────────────────────────────────────────────────────────
for key, default in {
    "result": None,
    "chat_history": [],
    "processing": False,
    "step": 0,
}.items():
    if key not in st.session_state:
        st.session_state[key] = default


# ── Hero header ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-icon">🎙️</div>
  <div>
    <h1>MeetMind AI</h1>
    <p>// transcribe · summarize · extract · chat with your meetings</p>
  </div>
</div>
""", unsafe_allow_html=True)


# ── Step indicator ─────────────────────────────────────────────────────────────
def render_steps(current: int):
    steps = ["Input", "Transcribe", "Analyse", "Chat"]
    html = '<div class="steps">'
    for i, label in enumerate(steps):
        num_cls = "done" if i < current else ("active" if i == current else "")
        lbl_cls = "active" if i == current else ""
        icon = "✓" if i < current else str(i + 1)
        html += f'<div class="step"><div class="step-num {num_cls}">{icon}</div><span class="step-label {lbl_cls}">{label}</span></div>'
        if i < len(steps) - 1:
            html += '<div class="step-connector"></div>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

render_steps(st.session_state.step)


# ════════════════════════════════════════════════════════════════════════════════
# PHASE 1 — INPUT
# ════════════════════════════════════════════════════════════════════════════════
if st.session_state.result is None:

    col_left, col_right = st.columns([3, 2], gap="large")

    with col_left:
        st.markdown('<div class="card-title"><span>📥</span> Source</div>', unsafe_allow_html=True)

        source_type = st.radio(
            "Input type",
            ["🔗 YouTube URL", "📁 Local File"],
            horizontal=True,
            label_visibility="collapsed",
        )

        source = None

        if source_type == "🔗 YouTube URL":
            url = st.text_input(
                "YouTube URL",
                placeholder="https://www.youtube.com/watch?v=...",
                label_visibility="collapsed",
            )
            if url:
                source = url
                st.markdown('<div class="status"><div class="dot"></div>URL ready</div>', unsafe_allow_html=True)
        else:
            uploaded = st.file_uploader(
                "Upload audio/video",
                type=["mp3", "mp4", "wav", "m4a", "webm", "mkv"],
                label_visibility="collapsed",
            )
            if uploaded:
                import tempfile, os
                tmp = tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded.name)[1])
                tmp.write(uploaded.read())
                tmp.flush()
                source = tmp.name
                st.markdown(f'<div class="status"><div class="dot"></div>{uploaded.name} · {uploaded.size // 1024} KB</div>', unsafe_allow_html=True)

        st.markdown("<hr class='divider'>", unsafe_allow_html=True)

        language = st.selectbox(
            "Language",
            ["english", "hinglish"],
            format_func=lambda x: "🇬🇧 English (Whisper)" if x == "english" else "🇮🇳 Hinglish (Sarvam AI)",
        )

        run = st.button("⚡ Analyse Meeting", disabled=source is None, use_container_width=True)

    with col_right:
        st.markdown("""
        <div class="card">
          <div class="card-title"><span>⚙️</span> Pipeline</div>
          <div style="display:flex;flex-direction:column;gap:0.7rem;margin-top:0.5rem;">
            <div style="display:flex;align-items:center;gap:0.7rem;">
              <div style="width:32px;height:32px;border-radius:8px;background:rgba(108,99,255,0.15);display:flex;align-items:center;justify-content:center;font-size:1rem;">🔍</div>
              <div><div style="font-size:0.82rem;font-weight:600;font-family:'Syne',sans-serif;">Audio Processor</div><div style="font-size:0.72rem;color:var(--muted);font-family:'DM Mono',monospace;">yt-dlp · pydub · chunking</div></div>
            </div>
            <div style="display:flex;align-items:center;gap:0.7rem;">
              <div style="width:32px;height:32px;border-radius:8px;background:rgba(0,212,170,0.12);display:flex;align-items:center;justify-content:center;font-size:1rem;">🗣️</div>
              <div><div style="font-size:0.82rem;font-weight:600;font-family:'Syne',sans-serif;">Transcriber</div><div style="font-size:0.72rem;color:var(--muted);font-family:'DM Mono',monospace;">Whisper (EN) · Sarvam AI (HI)</div></div>
            </div>
            <div style="display:flex;align-items:center;gap:0.7rem;">
              <div style="width:32px;height:32px;border-radius:8px;background:rgba(108,99,255,0.15);display:flex;align-items:center;justify-content:center;font-size:1rem;">✍️</div>
              <div><div style="font-size:0.82rem;font-weight:600;font-family:'Syne',sans-serif;">Analyser</div><div style="font-size:0.72rem;color:var(--muted);font-family:'DM Mono',monospace;">Mistral · LangChain LCEL</div></div>
            </div>
            <div style="display:flex;align-items:center;gap:0.7rem;">
              <div style="width:32px;height:32px;border-radius:8px;background:rgba(255,107,107,0.12);display:flex;align-items:center;justify-content:center;font-size:1rem;">💬</div>
              <div><div style="font-size:0.82rem;font-weight:600;font-family:'Syne',sans-serif;">RAG Chat</div><div style="font-size:0.72rem;color:var(--muted);font-family:'DM Mono',monospace;">ChromaDB · MiniLM embeddings</div></div>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card" style="margin-top:0;">
          <div class="card-title"><span>💡</span> Tips</div>
          <ul style="margin:0;padding-left:1.2rem;font-size:0.8rem;color:var(--muted);line-height:1.9;">
            <li>Works with any public YouTube URL</li>
            <li>Supports MP3, MP4, WAV, M4A, WEBM</li>
            <li>Choose Hinglish for Hindi + English mixed</li>
            <li>Long videos are auto-chunked (10 min each)</li>
          </ul>
        </div>
        """, unsafe_allow_html=True)

    # ── Run pipeline ────────────────────────────────────────────────────────────
    if run and source:
        st.session_state.step = 1

        progress_area = st.empty()

        stages = [
            ("🔊", "Processing audio...", 1),
            ("🗣️", "Transcribing with AI...", 2),
            ("✍️", "Summarising & extracting...", 3),
            ("🗃️", "Building vector store...", 3),
        ]

        progress_bar = st.progress(0)
        status_text = st.empty()

        try:
            from main import run_pipeline

            # Show live progress stages
            for i, (icon, msg, step) in enumerate(stages):
                status_text.markdown(f'<div class="status"><div class="dot"></div>{icon} {msg}</div>', unsafe_allow_html=True)
                progress_bar.progress((i + 1) * 20)
                st.session_state.step = step

            result = run_pipeline(source, language)
            st.session_state.result = result
            st.session_state.step = 3
            progress_bar.progress(100)
            status_text.markdown('<div class="status"><div class="dot"></div>✅ Done!</div>', unsafe_allow_html=True)
            time.sleep(0.5)
            st.rerun()

        except Exception as e:
            progress_bar.empty()
            status_text.empty()
            st.error(f"❌ Pipeline error: {e}")


# ════════════════════════════════════════════════════════════════════════════════
# PHASE 2 — RESULTS
# ════════════════════════════════════════════════════════════════════════════════
else:
    result = st.session_state.result

    # ── Top bar ──────────────────────────────────────────────────────────────
    top_col1, top_col2 = st.columns([5, 1])
    with top_col1:
        st.markdown(f"""
        <div style="margin-bottom:1.5rem;">
          <div style="font-family:'DM Mono',monospace;font-size:0.7rem;color:var(--muted);letter-spacing:0.1em;text-transform:uppercase;margin-bottom:0.3rem;">Meeting Title</div>
          <div style="font-family:'Syne',sans-serif;font-size:1.6rem;font-weight:800;color:var(--text);">{result.get('title','Untitled Meeting')}</div>
        </div>
        """, unsafe_allow_html=True)
    with top_col2:
        if st.button("↩ New", use_container_width=True):
            st.session_state.result = None
            st.session_state.chat_history = []
            st.session_state.step = 0
            st.rerun()

    # ── Metrics strip ─────────────────────────────────────────────────────────
    transcript = result.get("transcript", "")
    word_count = len(transcript.split())
    chunk_count = max(1, word_count // 150)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Words", f"{word_count:,}")
    m2.metric("~Minutes", f"{word_count // 130}")
    m3.metric("Chunks processed", chunk_count)
    m4.metric("Actions found", result.get("action_items", "").count("\n") + 1 if result.get("action_items") else 0)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    # ── Main tabs ─────────────────────────────────────────────────────────────
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📋 Summary", "✅ Actions", "🔑 Decisions", "❓ Questions", "📄 Transcript"])

    with tab1:
        st.markdown('<div class="card-title"><span>📋</span> Meeting Summary</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="font-size:0.9rem;line-height:1.8;color:var(--text);">{result.get("summary","No summary available.")}</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="card-title"><span>✅</span> Action Items</div>', unsafe_allow_html=True)
        items_text = result.get("action_items", "No action items found.")
        for line in items_text.strip().split("\n"):
            if line.strip():
                st.markdown(f"""
                <div style="display:flex;align-items:flex-start;gap:0.6rem;padding:0.55rem 0;border-bottom:1px solid var(--border);">
                  <span style="color:var(--accent2);font-size:0.9rem;margin-top:0.05rem;">→</span>
                  <span style="font-size:0.875rem;line-height:1.6;">{line.lstrip('0123456789.-) ')}</span>
                </div>
                """, unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="card-title"><span>🔑</span> Key Decisions</div>', unsafe_allow_html=True)
        decisions_text = result.get("key_decisions", "No key decisions found.")
        for line in decisions_text.strip().split("\n"):
            if line.strip():
                st.markdown(f"""
                <div style="display:flex;align-items:flex-start;gap:0.6rem;padding:0.55rem 0;border-bottom:1px solid var(--border);">
                  <span class="pill pill-purple">decision</span>
                  <span style="font-size:0.875rem;line-height:1.6;">{line.lstrip('0123456789.-) ')}</span>
                </div>
                """, unsafe_allow_html=True)

    with tab4:
        st.markdown('<div class="card-title"><span>❓</span> Open Questions</div>', unsafe_allow_html=True)
        questions_text = result.get("open_questions", "No open questions found.")
        for line in questions_text.strip().split("\n"):
            if line.strip():
                st.markdown(f"""
                <div style="display:flex;align-items:flex-start;gap:0.6rem;padding:0.55rem 0;border-bottom:1px solid var(--border);">
                  <span class="pill pill-red">?</span>
                  <span style="font-size:0.875rem;line-height:1.6;">{line.lstrip('0123456789.-) ')}</span>
                </div>
                """, unsafe_allow_html=True)

    with tab5:
        st.markdown('<div class="card-title"><span>📄</span> Raw Transcript</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="transcript-box">{transcript}</div>', unsafe_allow_html=True)
        st.download_button(
            "⬇️ Download Transcript",
            data=transcript,
            file_name="transcript.txt",
            mime="text/plain",
        )

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    # ── RAG Chat ──────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="display:flex;align-items:center;gap:0.7rem;margin-bottom:1.2rem;">
      <div style="font-family:'Syne',sans-serif;font-size:1.1rem;font-weight:800;">💬 Chat with your Meeting</div>
      <span class="pill pill-teal">RAG · ChromaDB</span>
    </div>
    """, unsafe_allow_html=True)

    # Render chat history
    if st.session_state.chat_history:
        chat_html = '<div class="chat-wrap">'
        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                chat_html += f'<div style="display:flex;flex-direction:column;align-items:flex-end;"><div class="bubble-label" style="text-align:right;">You</div><div class="bubble bubble-user">{msg["content"]}</div></div>'
            else:
                chat_html += f'<div style="display:flex;flex-direction:column;align-items:flex-start;"><div class="bubble-label">MeetMind AI</div><div class="bubble bubble-ai">{msg["content"]}</div></div>'
        chat_html += '</div>'
        st.markdown(chat_html, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

    # Input row
    chat_col1, chat_col2 = st.columns([5, 1])
    with chat_col1:
        question = st.text_input(
            "Ask anything about your meeting",
            placeholder="e.g. Who owns the marketing task? What was decided about the budget?",
            label_visibility="collapsed",
            key="chat_input",
        )
    with chat_col2:
        ask = st.button("Ask →", use_container_width=True)

    if ask and question.strip():
        from core.rag_engine import ask_question

        st.session_state.chat_history.append({"role": "user", "content": question})

        with st.spinner("Thinking..."):
            try:
                answer = ask_question(result["rag_chain"], question)
            except Exception as e:
                answer = f"Error: {e}"

        st.session_state.chat_history.append({"role": "assistant", "content": answer})
        st.rerun()

    if st.session_state.chat_history:
        if st.button("🗑️ Clear chat"):
            st.session_state.chat_history = []
            st.rerun()