# pdf_text_explorer/cluster_visualizer.py

import hdbscan
import plotly.express as px
import umap
from litellm import completion
from loguru import logger


class ClusterVisualizer:
    """
    Clusters text data and visualizes them.
    """

    def __init__(self):
        """
        Initializes the ClusterVisualizer.
        """
        pass

    def project_embeddings(self, embeddings):
        """
        Reduces high-dimensional embeddings to 2D coordinates using UMAP.

        Args:
            embeddings (numpy.ndarray): High-dimensional embeddings.

        Returns:
            numpy.ndarray: 2D coordinates.
        """
        try:
            logger.info("Projecting embeddings to 2D using UMAP")
            umap_model = umap.UMAP(n_components=2, random_state=42)
            coordinates = umap_model.fit_transform(embeddings)
            logger.info("Projection complete")
            return coordinates
        except Exception as e:
            logger.error(f"Error during embedding projection: {e}")
            raise

    def cluster_embeddings(self, coordinates):
        """
        Clusters the 2D coordinates using HDBSCAN.

        Args:
            coordinates (numpy.ndarray): 2D coordinates from UMAP projection.

        Returns:
            numpy.ndarray: Cluster labels.
        """
        try:
            logger.info("Clustering coordinates using HDBSCAN")
            clusterer = hdbscan.HDBSCAN(min_cluster_size=5)
            labels = clusterer.fit_predict(coordinates)
            logger.info("Clustering complete")
            return labels
        except Exception as e:
            logger.error(f"Error during clustering: {e}")
            raise

    def label_clusters(self, df):
        """
        Assigns labels to clusters using an LLM to generate 2-3 word summaries.

        Args:
            df (pd.DataFrame): DataFrame containing texts and cluster labels.

        Returns:
            pd.DataFrame: DataFrame with assigned cluster names.
        """
        try:
            logger.info("Labeling clusters using LLM")
            cluster_labels = df["cluster"].unique()
            cluster_names = {}

            for cluster in cluster_labels:
                if cluster == -1:
                    # Noise cluster
                    cluster_names[cluster] = "Noise"
                    continue
                # Get texts in this cluster
                cluster_texts = df[df["cluster"] == cluster]["text"].tolist()
                # Concatenate texts to form the cluster content
                cluster_content = " ".join(cluster_texts)
                # Limit the content size to avoid exceeding context length
                cluster_content = cluster_content[:2000]

                # Generate a cluster label using litellm
                prompt = f"Provide a concise 2-3 word label that summarizes the following texts:\n\n{cluster_content}\n\nLabel:"
                response = completion(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                )
                cluster_name = response.strip()
                cluster_names[cluster] = cluster_name
            df["cluster_name"] = df["cluster"].map(cluster_names)
            logger.info("Clusters labeled successfully")
            return df
        except Exception as e:
            logger.error(f"Error labeling clusters: {e}")
            raise

    def visualize_clusters(self, df):
        """
        Visualizes clusters using Plotly.

        Args:
            df (pd.DataFrame): DataFrame containing texts, coordinates, and cluster labels.
        """
        try:
            logger.info("Visualizing clusters")
            fig = px.scatter(
                df,
                x="x",
                y="y",
                color="cluster_name",
                hover_data=["text"],
                title="Clusters of Text Chunks",
            )
            fig.show()
            logger.info("Clusters visualized successfully")
        except Exception as e:
            logger.error(f"Error visualizing clusters: {e}")
            raise
