import streamlit as st
from streamlit_option_menu import option_menu

def render_sidebar():

    with st.sidebar:

        st.markdown("# 💸 FinTrack Pro")
        st.caption("AI-Powered Expense Intelligence")

        selected = option_menu(

            menu_title=None,

            options=[
                "Dashboard",
                "Transactions",
                "Analytics",
                "Budgets",
                "Goals",
                "Reports",
                "Settings"
            ],

            icons=[
                "speedometer2",
                "wallet2",
                "graph-up-arrow",
                "pie-chart",
                "bullseye",
                "file-earmark-bar-graph",
                "gear"
            ],

            default_index=0,

            styles={

                "container": {
                    "padding": "0!important",
                    "background-color": "transparent"
                },

                "icon": {
                    "color": "#C4B5FD",
                    "font-size": "18px"
                },

                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "8px 0",
                    "padding": "14px",
                    "border-radius": "14px",
                    "color": "white",
                    "--hover-color": "rgba(139,92,246,0.15)"
                },

                "nav-link-selected": {
                    "background":
                    "linear-gradient(90deg,#8B5CF6,#06B6D4)",

                    "box-shadow":
                    "0 0 20px rgba(139,92,246,0.35)"
                }
            }
        )

    return selected