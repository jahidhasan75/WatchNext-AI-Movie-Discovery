"""
ML developer owns this module.

Required public interface:
    load_model()
    search_movies(query: str, limit: int = 10) -> list[dict]
    recommend_movies(movie_title: str, genre: str | None = None,
                     year: int | None = None, top_n: int = 5) -> list[dict]

Each result dictionary must contain:
movie_id, title, genres, overview, poster_path, similarity_score, reason

Replace these placeholder functions with the real dataset-backed implementation.
Do not return fabricated recommendations in the final demo.
"""

def load_model():
    """Load/preprocess data and prepare the recommender once at backend startup."""
    raise NotImplementedError("ML developer: implement load_model()")


def search_movies(query: str, limit: int = 10) -> list[dict]:
    """Return matching dataset-backed movies using the shared schema."""
    raise NotImplementedError("ML developer: implement search_movies()")


def recommend_movies(
    movie_title: str,
    genre: str | None = None,
    year: int | None = None,
    top_n: int = 5,
) -> list[dict]:
    """Return up to top_n similar movies using the shared schema."""
    raise NotImplementedError("ML developer: implement recommend_movies()")
