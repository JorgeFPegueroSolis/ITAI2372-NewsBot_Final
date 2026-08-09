
def get_top_tfidf_terms(tfidf_df, category, top_n=10):

    category_df = tfidf_df[tfidf_df['category'] == category]

    mean_scores = category_df.drop('category', axis=1).mean().sort_values(ascending=False)

    return mean_scores.head(top_n)
