import streamlit as st
import plotly.express as px

def category_chart(df):

    fig = px.pie(
        df,
        values="amount",
        names="category",
        hole=0.7,

        color_discrete_sequence=[
            "#8B5CF6",
            "#06B6D4",
            "#22C55E",
            "#F59E0B"
        ]
    )

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        height=420
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )

def monthly_chart(df):

    fig = px.area(
        df,
        x="date",
        y="amount",
        template="plotly_dark"
    )

    fig.update_traces(
        line_color="#8B5CF6"
    )

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        height=420
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )