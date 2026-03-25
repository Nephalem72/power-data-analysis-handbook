from __future__ import annotations

from html import escape

import pandas as pd
from IPython.display import HTML, Markdown, display


def _callout_palette(tone: str) -> tuple[str, str]:
    palette = {
        "info": ("#eef5ff", "#1f4b99"),
        "warning": ("#fff5e8", "#8a4b00"),
        "success": ("#eef8f2", "#146c43"),
        "accent": ("#f4f1fb", "#5f3dc4"),
    }
    return palette.get(tone, palette["info"])


def display_callout(title: str, body: str, tone: str = "info") -> None:
    """Render a compact HTML callout for notebook conclusions or warnings."""
    background, border = _callout_palette(tone)
    html = f"""
    <div style="border-left: 4px solid {border}; background: {background}; padding: 12px 14px; margin: 14px 0; border-radius: 6px;">
      <strong>{escape(title)}</strong><br/>
      <span>{escape(body)}</span>
    </div>
    """
    display(HTML(html))


def display_stage_note(title: str, body: str) -> None:
    """Render a stage intro block for notebook steps."""
    html = f"""
    <div style="margin: 14px 0 10px; padding: 10px 12px; background: #f7f8fb; border: 1px solid #d8deea; border-radius: 6px;">
      <div style="font-weight: 700; color: #1f4b99; margin-bottom: 4px;">{escape(title)}</div>
      <div>{escape(body)}</div>
    </div>
    """
    display(HTML(html))


def _styled_frame(frame: pd.DataFrame, decimals: int = 3) -> pd.io.formats.style.Styler:
    formats: dict[str, object] = {}
    numeric_columns = frame.select_dtypes(include="number").columns
    for column in numeric_columns:
        formats[column] = lambda x, d=decimals: f"{x:.{d}f}"

    return (
        frame.style.format(formats)
        .hide(axis="index")
        .set_table_styles(
            [
                {
                    "selector": "th",
                    "props": [
                        ("background-color", "#1f3556"),
                        ("color", "white"),
                        ("font-weight", "600"),
                        ("text-align", "left"),
                    ],
                },
                {
                    "selector": "td",
                    "props": [("padding", "6px 10px"), ("border-bottom", "1px solid #e5e7eb")],
                },
                {
                    "selector": "table",
                    "props": [("border-collapse", "collapse"), ("width", "100%")],
                },
            ]
        )
    )


def display_frame(frame: pd.DataFrame, decimals: int = 3) -> None:
    """Display a dataframe with a consistent course style."""
    display(_styled_frame(frame, decimals=decimals))


def display_metric_table(metrics: dict[str, float], decimals: int = 3) -> None:
    """Show a small metric table with consistent formatting."""
    frame = pd.DataFrame(
        {"Показатель": list(metrics.keys()), "Значение": list(metrics.values())}
    )
    display(_styled_frame(frame, decimals=decimals))


def display_markdown_list(title: str, items: list[str]) -> None:
    """Render a markdown heading with a flat bullet list."""
    bullet_text = "\n".join(f"- {item}" for item in items)
    display(Markdown(f"### {title}\n\n{bullet_text}"))
