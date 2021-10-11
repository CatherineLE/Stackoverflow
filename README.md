# Stackoverflow
Multi-Labels Classification on Text with SVC on LDA  \
Deployed with Flask or Streamlit

Final Model Deployed : SVC on LDA labels

## Flask  

On bash: \
        $ export FLASK_APP=app_flask.py \
        $ flask run \
        $ to quit : Ctrl + C \
        
Then run the cell on jupyter notebook to verify that the prediction is working well.

## Streamlit  

`pip install streamlit`

On Bash: \
        $ python3 -m venv venv \
        $ source venv/bin/activate \
        $ python   YOUR_APP.py \
        - if command not find : \
        $ export PATH="$HOME/.local/bin:$PATH" \
        $ streamlit run YOUR_APP.py 
        
Then go the the  Local URL: http://localhost:8501 for exemple to test the app.

### Play Button
[![Streamlit App](https://static.streamlit.io/badges/stramlit_badge_black_white.svg)](https://share.streamlit.io/catherinele/stackoverflow/app_streamlit.py)
