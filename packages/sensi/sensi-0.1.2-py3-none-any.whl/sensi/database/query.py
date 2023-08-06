from functools import cache
from typing import Any

from sqlalchemy import desc

from .models import (
    Base,
    Likelihood,
    Prior,
    StopWords,
    Training,
    engine,
    session,
)


def create_db() -> None:
    """Create Database dataset.db"""
    Base.metadata.create_all(engine)


def insert_training(txt: str, lbl: int) -> None:
    """Insert text and label into training table"""
    local_session = session(bind=engine)
    new_training = Training(text=txt, label=lbl)
    local_session.add(new_training)
    local_session.commit()


@cache
def read_stop_words() -> set:
    """Read all stop words"""
    local_session = session(bind=engine)
    stops = local_session.query(StopWords).all()

    return {data.content for data in stops}


@cache
def read_all_training() -> dict:
    """Read all training dataset"""
    local_session = session(bind=engine)
    training = local_session.query(Training).yield_per(5).all()

    return {data.id: {"text": data.text, "label": data.label} for data in training}


@cache
def read_log_likelihood() -> dict:
    """Read all loglikelihoods. Returns dictionary."""
    local_session = session(bind=engine)
    loglikelihood = local_session.query(Likelihood).all()

    return {data.text: data.loglikelihood for data in loglikelihood}


@cache
def read_log_prior() -> Any:
    """Read all logprior. Returns dictionary."""
    local_session = session(bind=engine)
    prior = local_session.query(Prior).order_by(desc(Prior.id)).first()

    return prior.logprior  # type: ignore
