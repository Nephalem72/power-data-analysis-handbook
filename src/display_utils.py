from __future__ import annotations

from html import escape

import pandas as pd
from IPython.display import HTML, Markdown, display


def display_callout(title: str, body: str, tone: str = "info") -> None:
    """Render a compact HTML callout for notebook conclusions or warnings."""
    palette = {
        "info": ("#e7f0ff", "#1f4b99"),
        "warning": ("#fff4e5", "#8a4b00"),
        "success": ("#e9f7ef", "#146c43"),
    }
    background, border = palette.get(tone, palette["info"])
    html = f"""
    <div style="border-left: 4px solid {border}; background: {background}; padding: 12px 14px; margin: 12px 0;">
      <strong>{escape(title)}</strong><br/>
      <span>{escape(body)}</span>
    </div>
    """
    display(HTML(html))


def display_metric_table(metrics: dict[str, float], decimals: int = 4) -> None:
    """Show a small metric table with consistent formatting."""
    frame = pd.DataFrame(
        {"metric": list(metrics.keys()), "value": list(metrics.values())}
    )
    styled = frame.style.format({"value": lambda x: f"{x:.{decimals}f}"})
    display(styled)


def display_markdown_list(title: str, items: list[str]) -> None:
    """Render a markdown heading with a flat bullet list."""
    bullet_text = "\n".join(f"- {item}" for item in items)
    display(Markdown(f"### {title}\n\n{bullet_text}"))
