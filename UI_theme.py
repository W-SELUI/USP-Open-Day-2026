import streamlit as st


def apply_theme():
    st.markdown(
        """
        <style>
        :root {
            --lab-ink: #f7fbff;
            --lab-muted: #aabbd4;
            --lab-cyan: #67e8f9;
            --lab-blue: #3b82f6;
            --lab-violet: #a78bfa;
            --lab-panel: rgba(10, 25, 56, 0.78);
            --lab-line: rgba(148, 163, 184, 0.22);
        }

        [data-testid="stAppViewContainer"] {
            background:
                radial-gradient(circle at 10% 6%, rgba(14, 165, 233, 0.22), transparent 25%),
                radial-gradient(circle at 88% 12%, rgba(139, 92, 246, 0.20), transparent 28%),
                radial-gradient(circle at 53% 88%, rgba(37, 99, 235, 0.15), transparent 30%),
                #030712;
            color: var(--lab-ink);
        }

        [data-testid="stAppViewContainer"]::before {
            position: fixed;
            inset: 0;
            z-index: 0;
            pointer-events: none;
            content: "";
            opacity: 0.32;
            background-image:
                linear-gradient(rgba(103, 232, 249, 0.045) 1px, transparent 1px),
                linear-gradient(90deg, rgba(103, 232, 249, 0.045) 1px, transparent 1px);
            background-size: 38px 38px;
            mask-image: radial-gradient(ellipse at top, black, transparent 72%);
        }

        [data-testid="stHeader"] { background: transparent; }
        [data-testid="stSidebar"] { display: none; }
        #MainMenu, footer { visibility: hidden; }

        .block-container {
            position: relative;
            z-index: 1;
            max-width: 1140px;
            padding-top: 1.35rem;
            padding-bottom: 4rem;
        }

        .hero {
            position: relative;
            overflow: hidden;
            margin: 0.7rem 0 1.25rem;
            padding: clamp(3rem, 7vw, 5.8rem) clamp(1.25rem, 5vw, 4.5rem);
            border: 1px solid rgba(125, 211, 252, 0.24);
            border-radius: 30px;
            background:
                linear-gradient(115deg, rgba(8, 47, 73, 0.69), rgba(15, 23, 42, 0.57) 58%, rgba(49, 46, 129, 0.46));
            box-shadow: 0 28px 75px rgba(0, 0, 0, 0.30), inset 0 1px rgba(255, 255, 255, 0.07);
            text-align: center;
        }

        .hero::before,
        .hero::after {
            position: absolute;
            border: 1px solid rgba(103, 232, 249, 0.23);
            border-radius: 50%;
            content: "";
        }

        .hero::before {
            top: -90px;
            left: -55px;
            width: 230px;
            height: 230px;
            box-shadow: 0 0 70px rgba(34, 211, 238, 0.20);
        }

        .hero::after {
            right: -65px;
            bottom: -115px;
            width: 270px;
            height: 270px;
            border-color: rgba(167, 139, 250, 0.25);
        }

        .eyebrow,
        .hero h1,
        .hero p { position: relative; z-index: 1; }

        .eyebrow {
            margin-bottom: 0.9rem;
            color: var(--lab-cyan);
            font-size: 0.75rem;
            font-weight: 850;
            letter-spacing: 0.18rem;
        }

        .hero h1 {
            margin: 0;
            color: var(--lab-ink);
            font-size: clamp(3rem, 8vw, 5.9rem);
            letter-spacing: -0.065em;
            line-height: 0.90;
            text-shadow: 0 8px 36px rgba(103, 232, 249, 0.14);
        }

        .hero p {
            max-width: 620px;
            margin: 1.35rem auto 0;
            color: #c5d5eb;
            font-size: 1.06rem;
            line-height: 1.72;
        }

        .mode-card {
            position: relative;
            min-height: 252px;
            overflow: hidden;
            padding: 1.85rem;
            border: 1px solid var(--lab-line);
            border-radius: 22px;
            background:
                linear-gradient(145deg, rgba(27, 49, 90, 0.86), rgba(9, 19, 42, 0.82));
            box-shadow: 0 16px 44px rgba(0, 0, 0, 0.24), inset 0 1px rgba(255, 255, 255, 0.045);
            transition: transform 180ms ease, border-color 180ms ease, box-shadow 180ms ease;
        }

        .mode-card::after {
            position: absolute;
            right: -38px;
            bottom: -48px;
            width: 130px;
            height: 130px;
            border: 1px solid rgba(103, 232, 249, 0.13);
            border-radius: 50%;
            content: "";
        }

        .mode-card:hover {
            border-color: rgba(103, 232, 249, 0.52);
            box-shadow: 0 23px 54px rgba(0, 0, 0, 0.34), 0 0 0 1px rgba(103, 232, 249, 0.06);
            transform: translateY(-5px);
        }

        .mode-icon {
            display: grid;
            width: 58px;
            height: 58px;
            border: 1px solid rgba(103, 232, 249, 0.28);
            border-radius: 18px;
            background: linear-gradient(145deg, rgba(14, 116, 144, 0.34), rgba(30, 41, 89, 0.52));
            box-shadow: 0 10px 24px rgba(6, 182, 212, 0.10);
            font-size: 2rem;
            place-items: center;
        }

        .mode-card h2 {
            margin: 1.15rem 0 0.55rem;
            color: var(--lab-ink);
            font-size: 1.48rem;
            letter-spacing: -0.025em;
        }

        .mode-card p {
            margin: 0;
            color: var(--lab-muted);
            line-height: 1.62;
        }

        .questpass-card {
            display: grid;
            grid-template-columns: minmax(0, 1.05fr) minmax(280px, 0.95fr);
            gap: 1.5rem 2rem;
            align-items: center;
            position: relative;
            overflow: hidden;
            margin: 1.35rem 0 2rem;
            padding: clamp(1.5rem, 4vw, 2.2rem);
            border: 1px solid rgba(103, 232, 249, 0.42);
            border-radius: 24px;
            background:
                radial-gradient(circle at 88% 20%, rgba(139, 92, 246, 0.28), transparent 34%),
                linear-gradient(135deg, rgba(8, 47, 73, 0.92), rgba(30, 41, 88, 0.88));
            box-shadow: 0 24px 62px rgba(0, 0, 0, 0.32), inset 0 1px rgba(255, 255, 255, 0.06);
        }

        .questpass-eyebrow {
            margin: 0 0 0.55rem;
            color: #67e8f9;
            font-size: 0.74rem;
            font-weight: 800;
            letter-spacing: 0.14rem;
        }

        .questpass-copy h2 {
            margin: 0;
            color: var(--lab-ink);
            font-size: clamp(2rem, 5vw, 3rem);
        }

        .questpass-copy p:not(.questpass-eyebrow),
        .questpass-progress-area p {
            margin: 0.65rem 0 0;
            color: #c7d7ee;
            line-height: 1.55;
        }

        .questpass-progress-area {
            padding: 1.15rem;
            border: 1px solid rgba(125, 211, 252, 0.22);
            border-radius: 18px;
            background: rgba(2, 6, 23, 0.46);
        }

        .questpass-count {
            color: #f8fbff;
            font-size: 2.05rem;
            font-weight: 850;
        }

        .questpass-count span {
            color: #a9c2de;
            font-size: 0.95rem;
            font-weight: 700;
        }

        .questpass-track {
            height: 11px;
            overflow: hidden;
            margin-top: 0.7rem;
            border-radius: 999px;
            border: 1px solid rgba(103, 232, 249, 0.10);
            background: rgba(2, 6, 23, 0.74);
        }

        .questpass-track div {
            height: 100%;
            min-width: 0;
            border-radius: inherit;
            background: linear-gradient(90deg, #22d3ee, #3b82f6, #a78bfa);
            box-shadow: 0 0 16px rgba(103, 232, 249, 0.45);
            transition: width 0.35s ease;
        }

        .quest-stamp-row {
            display: flex;
            grid-column: 1 / -1;
            flex-wrap: wrap;
            gap: 0.65rem;
        }

        .quest-stamp {
            display: inline-flex;
            gap: 0.45rem;
            align-items: center;
            padding: 0.6rem 0.8rem;
            border: 1px solid rgba(148, 163, 184, 0.22);
            border-radius: 999px;
            background: rgba(2, 6, 23, 0.32);
            color: #8ba1bf;
            font-size: 0.82rem;
            font-weight: 700;
        }

        .quest-stamp.collected {
            border-color: rgba(103, 232, 249, 0.52);
            background: rgba(8, 145, 178, 0.18);
            color: #e0f7ff;
        }

        .quest-stamp.collected span {
            font-size: 1rem;
        }

        @media (max-width: 700px) {
            .questpass-card {
                grid-template-columns: 1fr;
            }
        }

        .stButton > button {
            width: 100%;
            min-height: 53px;
            margin-top: 0.15rem;
            border: 1px solid rgba(125, 211, 252, 0.62);
            border-radius: 14px;
            background: linear-gradient(120deg, #0e7490, #2563eb 58%, #4f46e5);
            box-shadow: 0 10px 23px rgba(37, 99, 235, 0.20);
            color: white;
            font-weight: 800;
            letter-spacing: 0.01em;
            transition: transform 180ms ease, filter 180ms ease, box-shadow 180ms ease;
        }

        .stButton > button:hover {
            border-color: #cffafe;
            filter: brightness(1.12);
            box-shadow: 0 15px 30px rgba(37, 99, 235, 0.32);
            transform: translateY(-3px);
        }

        div[data-testid="stTextInput"] input,
        div[data-testid="stTextArea"] textarea {
            border: 1px solid rgba(148, 163, 184, 0.34);
            border-radius: 14px;
            background: rgba(7, 16, 37, 0.78);
            color: var(--lab-ink);
            box-shadow: inset 0 1px rgba(255, 255, 255, 0.03);
        }

        div[data-testid="stTextInput"] input:focus,
        div[data-testid="stTextArea"] textarea:focus {
            border-color: var(--lab-cyan);
            box-shadow: 0 0 0 3px rgba(103, 232, 249, 0.12);
        }

        div[data-testid="stMetric"] {
            border: 1px solid rgba(103, 232, 249, 0.25);
            border-radius: 16px;
            background: linear-gradient(145deg, rgba(15, 35, 72, 0.78), rgba(8, 16, 37, 0.76));
            padding: 1rem;
            box-shadow: inset 0 1px rgba(255, 255, 255, 0.04);
        }

        div[data-testid="stMetricLabel"] {
            color: #a5f3fc;
        }

        /* Career Quest: scoped styles keep the choice buttons in the lab palette. */
        .st-key-career_subject_panel,
        .st-key-career_interest_panel {
            border-radius: 22px;
            border-color: rgba(103, 232, 249, 0.25);
            background: linear-gradient(145deg, rgba(15, 35, 72, 0.78), rgba(8, 16, 37, 0.76));
            padding: 1rem;
        }

        .st-key-career_picker h3 {
            font-size: 1.3rem;
            letter-spacing: -0.025em;
        }

        .st-key-career_picker button[aria-pressed] {
            min-height: 44px;
            padding: 0.55rem 0.85rem;
            border: 1px solid rgba(148, 163, 184, 0.38);
            border-radius: 999px;
            background: rgba(8, 20, 44, 0.9);
            color: #e2e8f0;
            transition: background 120ms ease, border-color 120ms ease;
        }

        .st-key-career_picker button[aria-pressed="true"] {
            color: #042036 !important;
            border-color: #a5f3fc !important;
            background: #67e8f9 !important;
            font-weight: 750;
            box-shadow: 0 0 0 1px rgba(103, 232, 249, 0.25);
        }

        .st-key-career_picker button[aria-pressed]:hover {
            border-color: #67e8f9;
        }

        .st-key-career_picker button:focus-visible {
            outline: 3px solid #a5f3fc;
            outline-offset: 3px;
        }

        .st-key-career_picker [data-testid="stExpander"] details {
            border-color: rgba(148, 163, 184, 0.28);
            background: rgba(8, 20, 44, 0.62);
            color: #e2e8f0;
            border-radius: 12px;
        }

        .st-key-career_clear button {
            background: rgba(15, 23, 42, 0.7);
            border-color: rgba(148, 163, 184, 0.38);
            box-shadow: none;
            color: #d8e7f8;
        }

        .career-scan-panel {
            position: relative;
            display: grid;
            grid-template-columns: auto 1fr;
            gap: 1.1rem;
            align-items: center;
            overflow: hidden;
            margin: 1.1rem 0 0.75rem;
            padding: 1.25rem;
            border: 1px solid rgba(103, 232, 249, 0.36);
            border-radius: 22px;
            background:
                radial-gradient(circle at 12% 20%, rgba(103, 232, 249, 0.20), transparent 24%),
                linear-gradient(135deg, rgba(8, 47, 73, 0.88), rgba(15, 23, 42, 0.82));
            box-shadow: 0 22px 55px rgba(0, 0, 0, 0.30), inset 0 1px rgba(255, 255, 255, 0.055);
        }

        .career-scan-orb {
            display: grid;
            width: 64px;
            height: 64px;
            border: 1px solid rgba(165, 243, 252, 0.42);
            border-radius: 22px;
            background: linear-gradient(145deg, rgba(14, 165, 233, 0.36), rgba(79, 70, 229, 0.36));
            box-shadow: 0 0 34px rgba(34, 211, 238, 0.25);
            font-size: 2rem;
            place-items: center;
            animation: careerPulse 1.35s ease-in-out infinite alternate;
        }

        .career-scan-eyebrow {
            margin: 0 0 0.25rem;
            color: #9be9ff;
            font-size: 0.72rem;
            font-weight: 850;
            letter-spacing: 0.17rem;
            text-transform: uppercase;
        }

        .career-scan-panel h3 {
            margin: 0;
            color: #f8fbff;
            font-size: clamp(1.35rem, 3vw, 2rem);
            letter-spacing: -0.035em;
        }

        .career-scan-panel p:not(.career-scan-eyebrow) {
            margin: 0.35rem 0 0;
            color: #b8c8e3;
        }

        .career-scan-beam {
            position: absolute;
            top: -30%;
            bottom: -30%;
            left: -18%;
            width: 95px;
            background: linear-gradient(90deg, transparent, rgba(103, 232, 249, 0.25), transparent);
            filter: blur(1px);
            transform: rotate(15deg);
            animation: careerScanSweep 1.25s ease-in-out infinite;
        }

        .career-result-stage {
            position: relative;
            overflow: hidden;
            margin: 1.25rem 0 1rem;
            padding: clamp(1.6rem, 5vw, 3rem);
            border: 1px solid rgba(103, 232, 249, 0.44);
            border-radius: 28px;
            background:
                radial-gradient(circle at 82% 18%, rgba(167, 139, 250, 0.26), transparent 28%),
                radial-gradient(circle at 12% 82%, rgba(34, 211, 238, 0.18), transparent 30%),
                linear-gradient(135deg, rgba(8, 47, 73, 0.92), rgba(15, 23, 42, 0.88) 54%, rgba(30, 41, 88, 0.86));
            box-shadow:
                0 28px 75px rgba(0, 0, 0, 0.36),
                0 0 45px rgba(37, 99, 235, 0.16),
                inset 0 1px rgba(255, 255, 255, 0.065);
            text-align: center;
            animation: careerRevealDrop 0.55s ease both;
        }

        .career-result-stage::before {
            position: absolute;
            inset: 0;
            pointer-events: none;
            content: "";
            background:
                linear-gradient(rgba(103, 232, 249, 0.065) 1px, transparent 1px),
                linear-gradient(90deg, rgba(103, 232, 249, 0.05) 1px, transparent 1px);
            background-size: 28px 28px;
            mask-image: radial-gradient(ellipse at center, black, transparent 78%);
        }

        .career-result-stage::after {
            position: absolute;
            top: 0;
            left: -40%;
            width: 38%;
            height: 100%;
            content: "";
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.12), transparent);
            transform: skewX(-16deg);
            animation: careerResultShine 1.6s ease 0.25s both;
        }

        .career-result-eyebrow,
        .career-result-owner,
        .career-result-stage h2,
        .career-match-score,
        .career-result-tagline {
            position: relative;
            z-index: 1;
        }

        .career-result-eyebrow {
            margin: 0 0 0.5rem;
            color: #b9f6ff;
            font-size: 0.75rem;
            font-weight: 900;
            letter-spacing: 0.2rem;
            text-transform: uppercase;
        }

        .career-result-owner {
            margin: 0;
            color: #b6c8e5;
            font-weight: 700;
        }

        .career-result-stage h2 {
            margin: 0.35rem 0 0.1rem;
            color: #f8fbff;
            font-size: clamp(2.8rem, 8vw, 5.6rem);
            letter-spacing: -0.065em;
            line-height: 0.95;
            text-shadow: 0 12px 36px rgba(103, 232, 249, 0.16);
        }

        .career-match-score {
            display: inline-flex;
            gap: 0.35rem;
            align-items: baseline;
            margin-top: 0.55rem;
            padding: 0.55rem 1rem;
            border: 1px solid rgba(103, 232, 249, 0.38);
            border-radius: 999px;
            background: rgba(2, 6, 23, 0.36);
            box-shadow: inset 0 1px rgba(255, 255, 255, 0.06);
        }

        .career-match-score strong {
            color: #67e8f9;
            font-size: clamp(2.1rem, 5vw, 3.3rem);
            line-height: 1;
        }

        .career-match-score span {
            color: #e2eefc;
            font-size: 1rem;
            font-weight: 850;
        }

        .career-result-tagline {
            max-width: 620px;
            margin: 1rem auto 0;
            color: #cad8ec;
            line-height: 1.6;
        }

        .career-backup-title {
            margin: 1.25rem 0 0.55rem;
            color: #a5f3fc;
            font-size: 0.78rem;
            font-weight: 900;
            letter-spacing: 0.14rem;
            text-transform: uppercase;
        }

        .career-path-card {
            min-height: 132px;
            padding: 1.15rem;
            border: 1px solid rgba(148, 163, 184, 0.26);
            border-radius: 20px;
            background: linear-gradient(145deg, rgba(15, 35, 72, 0.74), rgba(8, 16, 37, 0.78));
            box-shadow: inset 0 1px rgba(255, 255, 255, 0.05);
            animation: careerRevealDrop 0.55s ease both;
        }

        .career-path-card span {
            color: #88dff0;
            font-size: 0.72rem;
            font-weight: 900;
            letter-spacing: 0.13rem;
            text-transform: uppercase;
        }

        .career-path-card h3 {
            margin: 0.45rem 0 0.45rem;
            color: #f8fbff;
            font-size: 1.45rem;
            letter-spacing: -0.03em;
        }

        .career-path-card p {
            margin: 0;
            color: #b8c8e3;
            font-weight: 800;
        }

        .career-clue-card {
            margin-top: 1rem;
            padding: 1rem;
            border: 1px solid rgba(103, 232, 249, 0.22);
            border-radius: 18px;
            background: rgba(2, 6, 23, 0.34);
        }

        .career-clue-card p {
            margin: 0 0 0.7rem;
            color: #b6c8e5;
            font-size: 0.8rem;
            font-weight: 850;
            letter-spacing: 0.09rem;
            text-transform: uppercase;
        }

        .career-clue-card div {
            display: flex;
            flex-wrap: wrap;
            gap: 0.55rem;
        }

        .career-clue-card span {
            display: inline-flex;
            align-items: center;
            padding: 0.48rem 0.7rem;
            border: 1px solid rgba(103, 232, 249, 0.25);
            border-radius: 999px;
            background: rgba(14, 165, 233, 0.12);
            color: #e4f8ff;
            font-size: 0.82rem;
            font-weight: 750;
            animation: careerChipPop 0.45s ease both;
        }

        @keyframes careerPulse {
            from { transform: translateY(0) scale(1); }
            to { transform: translateY(-4px) scale(1.035); }
        }

        @keyframes careerScanSweep {
            from { left: -22%; opacity: 0; }
            20% { opacity: 1; }
            80% { opacity: 1; }
            to { left: 115%; opacity: 0; }
        }

        @keyframes careerRevealDrop {
            from {
                opacity: 0;
                transform: translateY(18px) scale(0.985);
            }
            to {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }

        @keyframes careerResultShine {
            from { left: -45%; }
            to { left: 125%; }
        }

        @keyframes careerChipPop {
            from {
                opacity: 0;
                transform: translateY(6px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .small-note {
            color: #7890b3;
            text-align: center;
            margin-top: 2.5rem;
        }

        [data-testid="stCaptionContainer"],
        [data-testid="stMarkdownContainer"] code {
            color: #b9cae2;
        }

        @media (max-width: 700px) {
            .block-container { padding-top: 0.8rem; }
            .hero { border-radius: 23px; }
            .mode-card { min-height: 220px; }
            .career-scan-panel { grid-template-columns: 1fr; }
            .career-result-stage { border-radius: 23px; }
        }

        /* ===== Game screens: slim top bar for "Back to NeuroVerse" =====
           The back button used to float on top of each game's own header.
           On game routes it now sits in a 52px bar and the game starts
           below it, so nothing is covered. Career Quest is a normal page
           and is not affected. */
        :root { --game-bar-h: 52px; }

        .st-key-back_from_puzzle,
        .st-key-back_from_hand_rush,
        .st-key-back_from_slice_club,
        .st-key-back_from_skyshot,
        .st-key-back_from_vibe_link,
        .st-key-back_from_vibe_oracle {
            position: fixed !important;
            inset: 0 0 auto 0 !important;
            z-index: 1000000 !important;
            display: flex !important;
            align-items: center !important;
            width: 100vw !important;
            height: var(--game-bar-h) !important;
            margin: 0 !important;
            padding: 0 14px !important;
            border-bottom: 1px solid rgba(148, 163, 184, 0.16);
            background: rgba(3, 7, 18, 0.88);
            backdrop-filter: blur(12px);
        }

        .st-key-back_from_puzzle button,
        .st-key-back_from_hand_rush button,
        .st-key-back_from_slice_club button,
        .st-key-back_from_skyshot button,
        .st-key-back_from_vibe_link button,
        .st-key-back_from_vibe_oracle button {
            width: auto !important;
            min-height: 36px !important;
            margin: 0 !important;
            padding: 0 16px !important;
            border: 1px solid rgba(148, 163, 184, 0.28) !important;
            border-radius: 999px !important;
            background: rgba(255, 255, 255, 0.06) !important;
            box-shadow: none !important;
            color: #e6edf6 !important;
            font-size: 0.88rem !important;
            font-weight: 700 !important;
        }

        .st-key-back_from_puzzle button:hover,
        .st-key-back_from_hand_rush button:hover,
        .st-key-back_from_slice_club button:hover,
        .st-key-back_from_skyshot button:hover,
        .st-key-back_from_vibe_link button:hover,
        .st-key-back_from_vibe_oracle button:hover {
            border-color: var(--lab-cyan) !important;
            background: rgba(103, 232, 249, 0.14) !important;
            transform: none !important;
        }

        /* Games that scroll with the page: start them below the bar */
        [data-testid="stMain"]:has(.st-key-back_from_puzzle, .st-key-back_from_hand_rush, .st-key-back_from_slice_club, .st-key-back_from_skyshot) .block-container {
            padding-top: var(--game-bar-h) !important;
        }

        [data-testid="stMain"]:has(.st-key-back_from_puzzle, .st-key-back_from_hand_rush, .st-key-back_from_slice_club, .st-key-back_from_skyshot) .block-container [data-testid="stVerticalBlock"] {
            gap: 0 !important;
        }

        [data-testid="stMain"]:has(.st-key-back_from_puzzle, .st-key-back_from_hand_rush, .st-key-back_from_slice_club, .st-key-back_from_skyshot) iframe {
            min-height: calc(100vh - var(--game-bar-h)) !important;
        }

        /* Games pinned to the viewport: move the frame down by the bar */
        [data-testid="stMain"]:has(.st-key-back_from_vibe_link, .st-key-back_from_vibe_oracle) iframe[title="st.iframe"],
        [data-testid="stMain"]:has(.st-key-back_from_vibe_link, .st-key-back_from_vibe_oracle) [data-testid="stIFrame"],
        [data-testid="stMain"]:has(.st-key-back_from_vibe_link, .st-key-back_from_vibe_oracle) [data-testid="stCustomComponentV1"],
        [data-testid="stMain"]:has(.st-key-back_from_vibe_link, .st-key-back_from_vibe_oracle) [data-testid="stCustomComponentV1"] iframe {
            top: var(--game-bar-h) !important;
            height: calc(100vh - var(--game-bar-h)) !important;
            min-height: 0 !important;
        }

        /* Ko-fi support link in the home footer */
        .support-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.6rem 0.9rem;
            align-items: center;
            justify-content: center;
            margin: 2rem 0 0.4rem;
        }

        .support-pill {
            display: inline-flex;
            gap: 0.5rem;
            align-items: center;
            padding: 0.6rem 1.1rem;
            border: 1px solid rgba(245, 220, 133, 0.55);
            border-radius: 999px;
            background: rgba(245, 220, 133, 0.10);
            color: #f8e7a6 !important;
            font-weight: 800;
            text-decoration: none !important;
            transition: background 160ms ease, border-color 160ms ease, transform 160ms ease;
        }

        .support-pill:hover {
            border-color: #f5dc85;
            background: #f5dc85;
            color: #1a1405 !important;
            transform: translateY(-2px);
        }

        .support-text {
            color: var(--lab-muted);
            font-size: 0.9rem;
        }

        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
            }
        }
        /* ===== Home page layout (compact hero + QuestPass, grouped game cards) ===== */
        .home-top {
            display: grid;
            grid-template-columns: minmax(0, 1.55fr) minmax(300px, 1fr);
            gap: 1.1rem;
            align-items: stretch;
            margin: 0.4rem 0 1.6rem;
        }

        .home-top .hero {
            margin: 0;
            padding: 2.3rem 2.5rem;
            text-align: left;
        }

        .home-top .hero h1 {
            font-size: clamp(2.3rem, 4.6vw, 3.7rem);
            line-height: 0.98;
        }

        .home-top .hero p {
            max-width: 520px;
            margin: 1rem 0 0;
            font-size: 1rem;
        }

        .home-top .questpass-card {
            display: flex;
            flex-direction: column;
            justify-content: center;
            gap: 0;
            margin: 0;
            padding: 1.5rem 1.6rem;
        }

        .home-top .questpass-count {
            font-size: 2.3rem;
            line-height: 1;
        }

        .questpass-message {
            margin: 0.7rem 0 1rem !important;
            color: #c7d7ee;
            font-size: 0.92rem;
            line-height: 1.5;
        }

        .home-top .quest-stamp-row {
            display: grid;
            grid-template-columns: repeat(7, minmax(0, 52px));
            gap: 0.45rem;
        }

        .home-top .quest-stamp {
            display: grid;
            aspect-ratio: 1;
            padding: 0;
            border-radius: 14px;
            place-items: center;
            font-size: 1.35rem;
        }

        .home-top .quest-stamp .quest-stamp-icon {
            filter: grayscale(1);
            opacity: 0.32;
            transition: opacity 200ms ease, filter 200ms ease;
        }

        .home-top .quest-stamp.collected {
            border-color: rgba(103, 232, 249, 0.7);
            background: rgba(8, 145, 178, 0.22);
            box-shadow: 0 0 18px rgba(103, 232, 249, 0.28);
        }

        .home-top .quest-stamp.collected .quest-stamp-icon {
            filter: none;
            opacity: 1;
        }

        .quest-stamp-name {
            position: absolute;
            width: 1px;
            height: 1px;
            overflow: hidden;
            clip: rect(0 0 0 0);
            white-space: nowrap;
        }

        /* Section headings above each group of games */
        .game-section-title {
            display: flex;
            flex-wrap: wrap;
            align-items: baseline;
            gap: 0.35rem 0.7rem;
            margin: 1.4rem 0 0.75rem;
            color: var(--lab-ink);
            font-size: 1.2rem;
            font-weight: 800;
            letter-spacing: -0.01em;
        }

        .game-section-title small {
            color: var(--lab-muted);
            font-size: 0.82rem;
            font-weight: 600;
        }

        /* Card grids */
        .st-key-game_grid_camera,
        .st-key-game_grid_other {
            display: grid !important;
            gap: 0.9rem !important;
        }

        .st-key-game_grid_camera {
            grid-template-columns: repeat(5, minmax(0, 1fr));
        }

        .st-key-game_grid_other {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }

        /* Game cards: each one uses its game's accent colour */
        .st-key-game_card_puzzle { --accent: #67e8f9; }
        .st-key-game_card_hand_rush { --accent: #a78bfa; }
        .st-key-game_card_slice_club { --accent: #fb7185; }
        .st-key-game_card_skyshot { --accent: #38bdf8; }
        .st-key-game_card_vibe_oracle { --accent: #6ee7b7; }
        .st-key-game_card_career { --accent: #f5dc85; }
        .st-key-game_card_vibe_link { --accent: #c4b5fd; }

        [class*="st-key-game_card_"] {
            position: relative;
            overflow: hidden;
            justify-content: space-between;
            gap: 0.9rem !important;
            height: 100%;
            padding: 1.15rem;
            border: 1px solid color-mix(in srgb, var(--accent) 26%, transparent);
            border-radius: 20px;
            background:
                radial-gradient(circle at 100% 0%, color-mix(in srgb, var(--accent) 20%, transparent), transparent 55%),
                linear-gradient(160deg, rgba(22, 40, 78, 0.9), rgba(8, 16, 36, 0.92));
            box-shadow: 0 14px 36px rgba(0, 0, 0, 0.26), inset 0 1px rgba(255, 255, 255, 0.05);
            transition: transform 180ms ease, border-color 180ms ease, box-shadow 180ms ease;
        }

        [class*="st-key-game_card_"]:hover {
            border-color: color-mix(in srgb, var(--accent) 70%, transparent);
            box-shadow: 0 20px 46px rgba(0, 0, 0, 0.34), 0 0 28px color-mix(in srgb, var(--accent) 22%, transparent);
            transform: translateY(-4px);
        }

        .game-card-body .game-icon {
            display: grid;
            width: 48px;
            height: 48px;
            border: 1px solid color-mix(in srgb, var(--accent) 45%, transparent);
            border-radius: 14px;
            background: color-mix(in srgb, var(--accent) 16%, rgba(2, 6, 23, 0.6));
            box-shadow: 0 0 22px color-mix(in srgb, var(--accent) 18%, transparent);
            font-size: 1.6rem;
            place-items: center;
        }

        .game-card-body h3 {
            margin: 0.85rem 0 0.15rem;
            padding: 0;
            color: var(--lab-ink);
            font-size: 1.15rem;
            letter-spacing: -0.02em;
        }

        .game-card-body .game-tag {
            margin: 0 0 0.5rem;
            color: var(--accent);
            font-size: 0.78rem;
            font-weight: 700;
            line-height: 1.35;
        }

        .game-card-body .game-desc {
            margin: 0;
            color: var(--lab-muted);
            font-size: 0.88rem;
            line-height: 1.5;
        }

        [class*="st-key-game_card_"] .stButton > button {
            min-height: 44px;
            margin: 0;
            border: 1px solid color-mix(in srgb, var(--accent) 60%, transparent);
            border-radius: 12px;
            background: color-mix(in srgb, var(--accent) 14%, rgba(2, 6, 23, 0.55));
            box-shadow: none;
            color: #ffffff;
            font-weight: 800;
        }

        [class*="st-key-game_card_"] .stButton > button:hover,
        [class*="st-key-game_card_"]:hover .stButton > button {
            border-color: var(--accent);
            background: var(--accent);
            color: #04101f;
            filter: none;
            transform: none;
        }

        .st-key-game_grid_other [class*="st-key-game_card_"] .game-card-body {
            display: grid;
            grid-template-columns: auto 1fr;
            column-gap: 1rem;
        }

        .st-key-game_grid_other .game-card-body .game-icon {
            grid-row: span 3;
            width: 56px;
            height: 56px;
            font-size: 1.9rem;
        }

        .st-key-game_grid_other .game-card-body h3 {
            margin-top: 0.1rem;
        }

        .home-top .questpass-card { text-align: left; align-items: stretch; }
        .home-top .questpass-track { width: 100%; }

        /* Equal-height cards with the button pinned to the bottom */
        .st-key-game_grid_camera,
        .st-key-game_grid_other { align-items: stretch !important; }
        .st-key-game_grid_camera > div,
        .st-key-game_grid_other > div { display: flex; height: auto !important; align-self: stretch !important; }
        .st-key-game_grid_camera > div > [class*="st-key-game_card_"],
        .st-key-game_grid_other > div > [class*="st-key-game_card_"] { flex: 1 1 auto; }
        [class*="st-key-game_card_"] { display: flex !important; flex-direction: column; }
        [class*="st-key-game_card_"] > div:first-child { flex: 1 1 auto; }
        .game-card-body { padding-bottom: 0.4rem; }

        @media (max-width: 1050px) {
            .st-key-game_grid_camera { grid-template-columns: repeat(3, minmax(0, 1fr)); }
        }

        @media (max-width: 860px) {
            .home-top { grid-template-columns: 1fr; }
            .home-top .hero { padding: 1.8rem 1.6rem; }
        }

        @media (max-width: 640px) {
            .st-key-game_grid_camera,
            .st-key-game_grid_other { grid-template-columns: 1fr 1fr; }
            .st-key-game_grid_other { grid-template-columns: 1fr; }
            .game-card-body .game-desc { display: none; }
            [class*="st-key-game_card_"] { padding: 0.95rem; }
            .home-top .quest-stamp { font-size: 1.15rem; border-radius: 11px; }
            .st-key-game_grid_camera > div:last-child:nth-child(odd) { grid-column: span 2; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
