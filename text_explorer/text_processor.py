# pdf_text_explorer/text_processor.py

from collections import Counter

import numpy as np
import pandas as pd
import spacy
import textacy
import textacy.text_stats
from loguru import logger


class TextProcessor:
    def __init__(self, text: str, model_name: str = "en_core_web_lg"):
        try:
            self.spacy_nlp = spacy.load(model_name)
        except Exception as e:
            logger.error(f"Error loading spacy model: {e}. Please install the model using `python -m spacy download {model_name}`")
        self.text = text
        self.doc = textacy.make_spacy_doc(text, lang=self.spacy_nlp)

    def extract_top_noun_phrases(self, k: int = 10) -> dict:
        """Extract the top K noun phrases from text using textacy.

        Args:
            text: Input text to analyze
            k: Number of top noun phrases to return (default: 10)

        Returns:
            Dictionary of noun phrases and their counts
        """
        # Extract noun chunks using textacy
        noun_chunks = list(textacy.extract.noun_chunks(self.doc, drop_determiners=True))
        # Get top K by length using heapq.nlargest
        phrase_lengths = Counter({phrase: len(phrase) for phrase in noun_chunks})
        # Convert spans to strings
        return phrase_lengths.most_common(k)
    
    def extract_top_oov_words(self, k: int = 10) -> dict:
        """Extract the top K OOV words from text using spaCy.

        Args:
            text: Input text to analyze
            k: Number of top OOV words to return (default: 10)

        Returns:
            Dictionary of OOV words and their counts
        """
        # Create spacy doc

        # Extract OOV words using spaCy's vocabulary
        oov_counter = Counter(
            token.text
            for token in self.doc
            if token.lemma_ not in self.spacy_nlp.vocab and token.is_alpha and not token.is_stop
        )
        return oov_counter.most_common(k)
    
    def extract_top_words(self, k: int = 10) -> dict:
        """Extract the top K words from text using spaCy.
        """
        word_counter = Counter(
            token.text.lower() for token in self.doc if token.is_alpha and not token.is_stop
        )
        return word_counter.most_common(k)
    
    def extract_keywords(self, k: int = 10, method: str = "textrank") -> dict:
        """Extract the top K keywords from text using textacy.

        Args:
            k: Number of top keywords to return (default: 10)
            method: Keyword extraction method to use (default: "textrank")

        Returns:
            Dictionary of keywords and their scores
        """
        keyterms = textacy.extract.keyterms.textrank(
            self.doc,
            topn=k,
            normalize="lemma",
            window_size=10,
            edge_weighting="count"
        )
        # Count occurrences of each keyword in the document and create dictionary
        keyterm_counts = {}
        for term, score in keyterms:
            count = len([token for token in self.doc if token.lemma_.lower() == term.lower()])
            keyterm_counts[term] = count
        keyterms = keyterm_counts.items()
        # Convert to list of tuples instead of dict
        keyterms = sorted(keyterms, key=lambda x: x[1], reverse=True)
        return keyterms
    
    def flesch_kincaid_grade(self) -> float:
        """Calculate the Flesch-Kincaid grade level of the text.
        """
        return textacy.text_stats.readability.flesch_kincaid_grade_level(self.doc)

    def type_token_ratio(self) -> float:
        """Compute the Type-Token Ratio (TTR) of doc_or_tokens, a direct ratio of the number of unique words (types) to all words (tokens)."""
        return textacy.text_stats.diversity.ttr(self.doc)
