# 🐧 Penguin Classifier — Streamlit ML App

A machine learning web app that predicts the species of a Palmer's Penguin based on physical measurements. Built with Streamlit and scikit-learn, deployed on Streamlit Community Cloud.

---

## What This App Does

- Accepts 6 user inputs (island, sex, bill length, bill depth, flipper length, body mass)
- Predicts the penguin species — Adelie, Gentoo, or Chinstrap
- Shows feature importance so users understand *why* the model made its prediction
- Displays species distribution histograms with the user's input marked as a vertical line
- Supports uploading a custom penguin CSV to train a fresh model on the spot
- Password protected using Streamlit Secrets

---

## Project Structure

```
Chapter4/
├── peng_streamlit.py           # Main Streamlit app
├── Data_explore.py             # Model training script (run once)
├── penguins.csv                # Palmer's Penguins dataset
├── random_forest_peng.pickle   # Saved Random Forest model
├── ouput_penguin.pickle        # Species name mapping
├── feature_importance.png      # Feature importance bar chart
├── requirements.txt            # Python dependencies
├── .gitignore                  # Excludes venv, secrets, cache
└── .streamlit/
    └── secrets.toml            # Local secrets (NOT pushed to GitHub)
```

---

## How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/penguin-classifier.git
cd penguin-classifier
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create your local secrets file**
```bash
mkdir .streamlit
```

Create `.streamlit/secrets.toml` and add:
```toml
app_password = "penguins123"
```

**5. Generate the model files (if not already present)**
```bash
python Data_explore.py
```

This creates:
- `random_forest_peng.pickle`
- `ouput_penguin.pickle`
- `feature_importance.png`

**6. Run the app**
```bash
streamlit run peng_streamlit.py
```

Open your browser at `http://localhost:8501`

---

## How to Use the App

1. Enter the password when prompted
2. Fill in the penguin measurements using the form:
   - Select the island (Biscoe, Dream, or Torgerson)
   - Select the sex (Female or Male)
   - Enter bill length, bill depth, flipper length, and body mass
3. Click **Submit**
4. See the predicted species, feature importance chart, and distribution histograms

**Optional:** Upload your own penguin CSV file to train a custom model. The file must have the same column structure as `penguins.csv`.

---

## Dataset

The **Palmer's Penguins** dataset contains measurements for 344 penguins across 3 species collected from 3 islands in the Palmer Archipelago, Antarctica.

| Column | Description |
|---|---|
| species | Adelie, Gentoo, or Chinstrap |
| island | Biscoe, Dream, or Torgerson |
| bill_length_mm | Bill length in millimetres |
| bill_depth_mm | Bill depth in millimetres |
| flipper_length_mm | Flipper length in millimetres |
| body_mass_g | Body mass in grams |
| sex | Female or Male |

---

## Model Details

| Property | Value |
|---|---|
| Algorithm | Random Forest Classifier |
| Library | scikit-learn |
| Train/Test split | 20% / 80% |
| Random state | 15 |
| Features | island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex |
| Encoding | One-hot encoding via pd.get_dummies() |

---

## Deployment

This app is deployed on **Streamlit Community Cloud**.

### To deploy your own copy:

1. Push this repo to GitHub (public repository)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **New app**
4. Select your repository, branch `main`, and file `peng_streamlit.py`
5. Click **Deploy**
6. Go to **⋮ → Edit secrets** and add:(i ddi it in the advanced setting before pressing the deploy button )


## 🌐 Live App
<a href= "https://chapter4-book.streamlit.app">👉 [Open the Penguin Classifier]</a>

''' Password: `12345`'''

## Dependencies

```
streamlit
pandas
scikit-learn
matplotlib
seaborn
```

Install all with:
```bash
pip install -r requirements.txt
```

---

## What I Learned Building This

This project was built while working through *Getting Started with Streamlit for Data Science* by Tyler Richards (Packt, 2021).

Concepts practised:
- Saving and loading ML models with `pickle`
- Using `st.form()` and `st.form_submit_button()` to batch inputs
- Displaying images with `st.image()`
- Plotting with Seaborn inside Streamlit using `st.pyplot(fig)`
- Password protection with `st.secrets` and `st.stop()`
- Deploying to Streamlit Community Cloud
- Git and GitHub workflow for deployment

---

## Author

Built by **Victoria Theresa**
- GitHub: [@vicresagm-spec](https://github.com/vicresagm-spec)

---

## License

This project is for educational purposes. The Palmer's Penguins dataset is available under the CC0 public domain license.
