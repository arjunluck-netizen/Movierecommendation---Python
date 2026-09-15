🔄 Project Workflow
                  Kaggle Dataset
                       │
                       ▼
                Data Loading
                       │
                       ▼
               Data Cleaning
                       │
                       ▼
            Metadata Extraction
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Genres       Keywords      Cast
          │            │            │
          └────────────┼────────────┘
                       │
                       ▼
                  Director
                       │
                       ▼
                Create "Tags"
                       │
                       ▼
              CountVectorizer
                       │
                       ▼
                Movie Vectors
                       │
                       ▼
              Cosine Similarity
                       │
                       ▼
             Similarity Ranking
                       │
                       ▼
              Top 5 Recommendations
                       │
                       ▼
                Streamlit App
