import numpy as np
import pandas as pd
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from openai import OpenAI
from rich import print
from rich.table import Table

from text_explorer import PDFExtractor, TextProcessor


def embedding_function(texts):
    client = OpenAI()
    return client.embeddings.create(input=texts, model="text-embedding-3-small").data[0].embedding

# Step 3: Initialize the PDF extractor
pdf_extractor = PDFExtractor()

# Step 4: Extract text from PDF
text = pdf_extractor.extract_text("dev_data/input.pdf")

# Step 5: For this text, find the most common nouns and verbs using textacy
text_processor = TextProcessor(model_name="en_core_web_sm", text=text)

def print_as_table(df, title):
    df = pd.DataFrame(df)
    df.columns = ["word", "count"]
    t = Table(title=title)
    for _, row in df.iterrows():
        # Convert any spaCy Span objects to strings
        word = str(row["word"])
        t.add_row(word, str(row["count"]))
    print(t)


print_as_table(text_processor.extract_top_oov_words(k=10), "Out of Vocabulary words")
print("Also useful for finding pdf parsing errors")
print_as_table(text_processor.extract_top_noun_phrases(k=10), "Noun phrases")
print_as_table(text_processor.extract_top_words(k=10), "Most common words")
print_as_table(text_processor.extract_keywords(k=10), "Keywords using textrank")
print({"Flesch-Kincaid grade level": [text_processor.flesch_kincaid_grade()]})
print({"Type-token ratio": [text_processor.type_token_ratio()]})