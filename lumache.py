"""
Lumache - Python library for cooks and food lovers.
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass


def rank_answers(df):
"""
Ranks answers based on their scores for each row in a DataFrame and adds the ranked answers and scores as new columns.

:param kind: A pandas DataFrame containing columns for scores and answers. 
           The score columns should have names containing the substring 'score_', 
           and the answer columns should have names containing the substring 'answers_'.
:type kind: pandas.DataFrame
:return: A modified DataFrame with two new columns:
         - 'ranked_answer': The answer corresponding to the highest score for each row.
         - 'ranked_score': The highest score for each row.
:rtype: pandas.DataFrame
"""
    # Identify columns containing scores and answers
    score_cols = [col for col in df.columns if 'score_' in col]
    answer_cols = [col for col in df.columns if 'answers_' in col]

    ranked_answers = []
    ranked_scores = []
    for index, row in df.iterrows():
        best_score = -1  # Initialize with a value lower than any possible score
        best_answer = None
        for score_col, answer_col in zip(score_cols, answer_cols):
            score = row[score_col]
            if score:
              score_value = score['score']
              if score_value > best_score:
                  best_score = score_value
                  best_answer = row[answer_col]
        ranked_answers.append(best_answer)
        ranked_scores.append(score_value if score_value > best_score else best_score)

    df['ranked_answer'] = ranked_answers
    df['ranked_score'] = ranked_scores
    return df


def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]
