# ML-Project-CT4101
## Can a Machine Learning Model Classify the credibility of a News Article?

The purpose of this project is to develop a multi-class logistic regression model trained on data from the [Fake News Corpus](https://github.com/several27/FakeNewsCorpus) to predict the news type (e.g. fake, satire, bias, conspiracy) based on the title and contents of the news article. 

**Do note that this is an ongoing project, and the work you see here is still in progress.**

**Target Variable:** `type` (multi-class classification with 12 classes)
**Input Features:** `title` and `content`

## Dataset
- **Name:** FakeNewsCorpus
- **Source:** GitHub
- **Licence:** Apache 2.0

The original dataset is approximately 27GB in size and contains over 9 million records with a serious class imbalance. To make the dataset more manageable, I have taken a balanced sample of 2500 records per class (totalling 30,000 altogether in my sample dataset).

*Note: The full raw dataset and the generated sample CSV are not committed to this repository due to GitHub file size limits. However, the notebook `balanced-sampler.ipynb` contains the code used to generate the sample.*

## Project Structure
- `notebooks/balanced-sampler.ipynb` contains the script used to draw a balanced sample from the original dataset.
- `notebooks/data-audit.ipynb` contains the data audit.
- `notebooks/preprocessing.ipynb` contains the baseline model setup, cross-validation and initial evaluation results.
- `requirements.txt` the Python dependencies required to run the project.

## Setup Instructions
1. Clone the repository and navigate into the folder:
```bash
git clone https://github.com/hestiiia/ML-Project-CT4101
```
2. [Download](https://github.com/several27/FakeNewsCorpus/releases/tag/v1.0) the full FakeNewsCorpus dataset from here.

3. Use an extraction tool such as 7-Zip, WinRAR, or Unarchiver to extract the full multi-part archive.

4. Once extracted, move `news_cleaned_2018_02_13.csv` into the `datasets/` sub-directory of the project.
5. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

6. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## How to Run:
To reproduce the results, run the notebooks in the following order: 

1. `balanced-sampler.ipynb`: Requires the raw `datasets/news_cleaned_2018_02_13.csv` file to be placed in the directory. This will output `news_sample_balanced.csv`.

2. `data-audit.ipynb` outputs `audited-data.csv`.

3. `preprocessing.ipynb` loads `audited-data.csv` and evaluates the baseline model.