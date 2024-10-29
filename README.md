# textexplorer
Modern Text Exploration Library

A Python library for advanced text analysis and exploration, primarily focused on PDF documents. This library combines various NLP techniques to extract insights from text data.

> ⚠️ This is a work in progress and should not be used in production.

## Features

- PDF text extraction
- Advanced text analysis using spaCy
- Text statistics (Flesch-Kincaid grade level, type-token ratio)
- Extraction of:
  - Out of vocabulary words
  - Noun phrases
  - Common words
  - Keywords using TextRank
- Text clustering capabilities (with OpenAI embeddings)
- Visualization of text clusters

## Installation

```bash
uv pip install text_explorer
```

## Dependencies

- spaCy (with `en_core_web_lg` model)
- OpenAI API key (for embeddings)
- Other dependencies will be installed automatically

## Usage

### Basic Text Analysis

```python
from text_explorer import PDFExtractor, TextProcessor

# Extract text from PDF
pdf_extractor = PDFExtractor()
text = pdf_extractor.extract_text("your_document.pdf")

# Initialize text processor
text_processor = TextProcessor(model_name="en_core_web_lg", text=text)

# Get out of vocabulary words (useful for finding PDF parsing errors)
oov_words = text_processor.extract_top_oov_words(k=10)

# Extract noun phrases
noun_phrases = text_processor.extract_top_noun_phrases(k=10)

# Get most common words
common_words = text_processor.extract_top_words(k=10)

# Extract keywords using TextRank
keywords = text_processor.extract_keywords(k=10)

# Get readability metrics
grade_level = text_processor.flesch_kincaid_grade()
token_ratio = text_processor.type_token_ratio()
```

### Clustering (Work in Progress)

```python
from text_explorer import ClusterVisualizer
from sklearn.cluster import KMeans
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings

# Initialize components
text_splitter = SemanticChunker(OpenAIEmbeddings())
clustering_function = KMeans(n_clusters=5, random_state=42)
cluster_visualizer = ClusterVisualizer(clustering_function=clustering_function)

# Split text into chunks
docs = text_splitter.create_documents([text])

# Cluster and visualize
df_clusters = cluster_visualizer.cluster_texts(docs, embeddings)
df_labeled = cluster_visualizer.label_clusters(df_clusters)
cluster_visualizer.visualize_clusters(df_labeled, embeddings)
```

## License & Contributing

[Apache 2.0](LICENSE) & [Contributing](CONTRIBUTING.md) have more details.

Contributions are welcome!