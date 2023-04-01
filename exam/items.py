from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum


class Difficulty(StrEnum):
    """Difficulty enum."""

    easy: str = "Fácil"
    medium: str = "Média"
    hard: str = "Difícil"


class Matter(StrEnum):
    """Matter enum."""

    mathematics: str = "Matemática"
    portuguese: str = "Português"
    physics: str = "Física"


@dataclass
class ExerciseItem:
    """Item exercise."""

    matter: Matter = Matter.mathematics
    topic: str | None = None
    difficulty: Difficulty = Difficulty.exercise
    enunciation: str | None = None
    alternatives: list[str] | None = None
    multiple_choice: bool = False
    enunciation_image: str | None = None
    image_answer: str | None = None
    answer: str | None = None
    origin: str | None = None
    release_date: datetime | None = None
