import joblib
import pkg_resources
import pandas as pd

class ToxicCommentClassifier:
    def __init__(self):
        model_path = pkg_resources.resource_filename('toxic_classifier', 'toxic_comment_model.pkl')
        tfidf_path = pkg_resources.resource_filename('toxic_classifier', 'tfidf_vectorizer.pkl')
        self.model = joblib.load(model_path)
        self.tfidf = joblib.load(tfidf_path)

    def predict(self, comment):
        comment_tfidf = self.tfidf.transform([comment])
        prediction = self.model.predict(comment_tfidf).tolist()[0]
        categories = ["Toxic", "Severe Toxic", "Obscene", "Threat", "Insult", "Identity Hate"]
        result = {categories[i]: bool(prediction[i]) for i in range(len(categories))}
        return result
