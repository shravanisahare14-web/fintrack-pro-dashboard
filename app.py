import streamlit as st

from config import APP_NAME

from components.sidebar import render_sidebar

from views.dashboard import render_dashboard
from views.transactions import render_transactions
from views.analytics import render_analytics
from views.budgets import render_budgets
from views.goals import render_goals
from views.reports import render_reports
from views.settings import render_settings

st.set_page_config(
    page_title=APP_NAME,
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# LOAD CSS

with open("styles/main.css") as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

selected = render_sidebar()

if selected == "Dashboard":

    render_dashboard()

elif selected == "Transactions":

    render_transactions()

elif selected == "Analytics":

    render_analytics()

elif selected == "Budgets":

    render_budgets()

elif selected == "Goals":

    render_goals()

elif selected == "Reports":

    render_reports()

elif selected == "Settings":

    render_settings()