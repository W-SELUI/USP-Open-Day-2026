"""A tiny Streamlit component used to receive real completion events from games.

The hand and camera activities are HTML pages inside Streamlit. A normal
``st.iframe`` can display those pages, but it cannot pass their completion
state back to Python. This bridge hosts the page and returns a completion ID
only when the page's final result button sends one.
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


_completion_listener = st.components.v2.component(
    "questpass_completion_listener",
    js="""
const instances = new WeakMap();

export default function(component) {
  const { data, parentElement, setTriggerValue } = component;
  const activity = data?.activity || "";
  const previous = instances.get(parentElement);

  if (previous) {
    window.removeEventListener("message", previous);
  }

  const onMessage = (event) => {
    const message = event.data;

    if (
      message &&
      message.type === "questpass:completed" &&
      message.activity === activity
    ) {
      setTriggerValue("completed", activity);
    }
  };

  instances.set(parentElement, onMessage);
  window.addEventListener("message", onMessage);

  return () => {
    window.removeEventListener("message", onMessage);
    instances.delete(parentElement);
  };
}
""",
)

# Hand Puzzle is a complete web build, rather than one self-contained HTML
# file.  Give it its own Streamlit component so it has a single iframe and
# can load its JavaScript modules, MediaPipe files, and model directly.
_hand_puzzle = components.declare_component(
    "hand_puzzle_activity",
    path=str(Path(__file__).with_name("questpass_bridge") / "hand-puzzle"),
)

_gravity_thief = components.declare_component(
    "gravity_thief_activity",
    path=str(Path(__file__).with_name("questpass_bridge") / "gravity-thief"),
)


def render_hand_puzzle_activity(*, key: str):
    """Render Hand Puzzle and return its completion ID, if it is completed."""
    return _hand_puzzle(default=None, key=key)


def render_gravity_thief_activity(*, key: str):
    """Render Gravity Thief and return its back/completion event."""
    return _gravity_thief(default=None, key=key)


def render_static_iframe(url: str, height: int | str = 760) -> None:
    """Show a page from Streamlit's ``static`` folder inside an iframe.

    ``st.iframe("/app/static/...")`` uses an absolute path. That works
    locally, but on Streamlit Community Cloud the app itself runs under
    ``/~/+/``, so ``/app/static/...`` points at the Cloud wrapper page
    instead of the game and the frame just keeps loading. A relative
    ``app/static/...`` address resolves correctly in both places.
    """
    relative_src = url.lstrip("/")
    css_height = f"{height}px" if isinstance(height, int) else "100vh"
    st.markdown(
        f'''<iframe title="st.iframe" class="nv-static-frame" src="{relative_src}"
            allow="camera; microphone; autoplay; fullscreen; clipboard-write"
            allowfullscreen
            style="display:block;width:100%;height:{css_height};border:0;"></iframe>''',
        unsafe_allow_html=True,
    )


def render_questpass_activity(
    html_file: Path | None,
    activity: str,
    *,
    key: str,
    game_url: str | None = None,
):
    """Render a trusted activity and return its completion ID, if any.

    Self-contained HTML activities display through Streamlit's built-in
    iframe renderer. A tiny component only listens for the final completion
    message, so a display issue in the listener cannot blank the activity.
    """
    if game_url:
        render_static_iframe(game_url, height=760)
    else:
        if html_file is None:
            raise ValueError("html_file is required when game_url is not provided")

        st.iframe(html_file, height=760, width="stretch")

    result = _completion_listener(
        data={"activity": activity},
        default=None,
        height=1,
        key=f"{key}_completion_listener",
        on_completed_change=lambda: None,
    )

    return result.completed
