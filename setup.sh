mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"22f3001919@ds.study.iitm.ac.in\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = 8501\n\
" > ~/.streamlit/config.toml