from setuptools import setup, find_packages

setup(
    name='toxic_comment_classifier',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={'toxic_classifier': ['toxic_comment_model.pkl', 'tfidf_vectorizer.pkl']},
    install_requires=[
        'joblib',
        'scikit-learn',
        'pandas'
    ],
  
)
