import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px


def render_reports():

    st.markdown("""
    <div class="page-title">
        📊 Financial Reports
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="page-subtitle">
        Premium insights into your financial performance.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # KPI REPORT CARDS

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Income",
            "₹1,20,000",
            "+12%"
        )

    with c2:
        st.metric(
            "Expenses",
            "₹54,000",
            "-3%"
        )

    with c3:
        st.metric(
            "Savings",
            "₹66,000",
            "+18%"
        )

    with c4:
        st.metric(
            "Investments",
            "₹18,000",
            "+9%"
        )

    st.markdown("<br><br>", unsafe_allow_html=True)

    # CHARTS

    left, right = st.columns(2)

    with left:

        st.markdown("""
        <div class="section-title">
            💰 Expense Distribution
        </div>
        """, unsafe_allow_html=True)

        pie = go.Figure(

            data=[
                go.Pie(

                    labels=[
                        "Food",
                        "Shopping",
                        "Bills",
                        "Travel"
                    ],

                    values=[
                        12000,
                        22000,
                        14000,
                        6000
                    ],

                    hole=0.72
                )
            ]
        )

        pie.update_layout(

            paper_bgcolor='rgba(0,0,0,0)',

            font_color='white',

            height=420
        )

        st.plotly_chart(
            pie,
            width='stretch'
        )

    with right:

        st.markdown("""
        <div class="section-title">
            📈 Savings Growth
        </div>
        """, unsafe_allow_html=True)

        growth = pd.DataFrame({

            "Month": [
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May"
            ],

            "Savings": [
                12000,
                18000,
                22000,
                35000,
                66000
            ]
        })

        line = px.area(

            growth,

            x="Month",

            y="Savings",

            template="plotly_dark"
        )

        line.update_traces(
            line_color="#8B5CF6"
        )

        line.update_layout(

            paper_bgcolor='rgba(0,0,0,0)',

            plot_bgcolor='rgba(0,0,0,0)',

            font_color='white',

            height=420
        )

        st.plotly_chart(
            line,
            width='stretch'
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # AI SUMMARY

    st.markdown("""
    <div class="section-title">
        🧠 AI Financial Summary
    </div>
    """, unsafe_allow_html=True)

    summaries = [

        "Your savings increased by 18% this month.",

        "Shopping expenses are your highest spending category.",

        "Food spending reduced compared to last month.",

        "Investment consistency improved significantly."
    ]

    for item in summaries:

        st.markdown(f"""
        <div class="insight-card">
            {item}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.button("⬇ Download Premium Report")