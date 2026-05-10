import streamlit as st
import pandas as pd
import plotly.express as px

def render_analytics():

    st.markdown(
        """
        <div class="main-title">
            Analytics
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="sub-title">
            AI-powered financial analytics and spending intelligence.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    data = pd.DataFrame({

        "Month": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May"
        ],

        "Expenses": [
            42000,
            51000,
            39000,
            62000,
            54000
        ]
    })

    chart = px.line(
        data,
        x="Month",
        y="Expenses",
        markers=True,
        template="plotly_dark"
    )

    chart.update_traces(
        line_color="#8B5CF6",
        line_width=5
    )

    chart.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )

    st.plotly_chart(
        chart,
        width='stretch'
    )