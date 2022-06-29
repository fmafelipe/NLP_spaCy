import pandas as pd
import numpy as np 
import streamlit as st 
import spacy_streamlit 
from spacy_streamlit import visualize_parser
from pathlib import Path
import srsly
import importlib
import random 

MODELS = srsly.read_json(Path(__file__).parent / "models.json")
DEFAULT_MODEL = "en_core_web_sm" 
DEFAULT_TEXT = "David Bowie moved to the US in 1974, initially staying in New York City before settling in Los Angeles."
DESCRIPTION = """**Explore trained [spaCy v3.0](https://nightly.spacy.io) pipelines**"""


def get_default_text(nlp):
    # Comprueba si spacy tiene texto de ejemplo para el idioma escogido
    try:
        examples = importlib.import_module(f".lang.{nlp.lang}.examples","spacy")
        return examples.sentences[0]
    except:
        return ""
    
spacy_streamlit.visualize(
    MODELS,
    default_model= DEFAULT_MODEL,
    visualizers=["parser","ner","similarity","tokens","textcat"],
    show_visualizer_select=True,
    sidebar_description = DESCRIPTION,
    get_default_text= get_default_text
    )