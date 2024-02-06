from setuptools import find_packages, setup

setup(
    name='mcq_generatore',
    version='0.0.1',
    author="dushyant",
    author_email="dushyantdchss@gmail.com",
    install_requires = ["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)