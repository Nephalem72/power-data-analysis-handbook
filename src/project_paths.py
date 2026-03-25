from __future__ import annotations

from pathlib import Path


def project_root() -> Path:
    cwd = Path.cwd().resolve()
    return cwd.parent if cwd.name == "notebooks" else cwd


def sample_data_dir() -> Path:
    return project_root() / "data" / "sample"
