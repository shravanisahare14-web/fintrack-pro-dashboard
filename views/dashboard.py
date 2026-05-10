import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def render_dashboard():

    # HERO SECTION

    st.markdown(
        """
        <div class="hero-heading">
            FinTrack Pro
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-subtext">
            AI-powered financial analytics, budgeting intelligence,
            smart expense tracking, and premium finance management.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # KPI SECTION

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "Total Balance",
            "₹4,25,000",
            "+12%"
        )

    with c2:

        st.metric(
            "Income",
            "₹1,20,000",
            "+8%"
        )

    with c3:

        st.metric(
            "Expenses",
            "₹54,000",
            "-3%"
        )

    with c4:

        st.metric(
            "Savings",
            "₹66,000",
            "+18%"
        )

    st.markdown("<br><br>", unsafe_allow_html=True)

    # AI INSIGHTS + HEALTH

    left, right = st.columns([2,1])

    with left:

        st.markdown(
            "## 🧠 AI Financial Insights"
        )

        insights = [

            "Spending decreased by 8% this month.",

            "Food delivery remains your highest expense category.",

            "Savings improved significantly compared to April.",

            "Subscription spending increased slightly this week."
        ]

        for item in insights:

            st.markdown(
                f"""
                <div class="insight-card">
                    {item}
                </div>
                """,
                unsafe_allow_html=True
            )

    with right:

        st.markdown(
            "## 📊 Financial Health"
        )

        gauge = go.Figure(

            go.Indicator(

                mode="gauge+number",

                value=82,

                number={
                    'font': {
                        'size': 42,
                        'color': "white"
                    }
                },

                gauge={

                    'axis': {
                        'range': [0,100]
                    },

                    'bar': {
                        'color': "#8B5CF6"
                    },

                    'bgcolor': "rgba(255,255,255,0.05)",

                    'borderwidth': 0,

                    'steps': [

                        {
                            'range': [0,50],
                            'color': "#EF4444"
                        },

                        {
                            'range': [50,75],
                            'color': "#F59E0B"
                        },

                        {
                            'range': [75,100],
                            'color': "#10B981"
                        }
                    ]
                }
            )
        )

        gauge.update_layout(

            paper_bgcolor='rgba(0,0,0,0)',

            font={
                'color': "white"
            },

            height=320
        )

        st.plotly_chart(
            gauge,
            width='stretch'
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # CHART DATA

    expense_data = pd.DataFrame({

        "Category": [
            "Food",
            "Shopping",
            "Bills",
            "Travel"
        ],

        "Amount": [
            12000,
            22000,
            14000,
            9000
        ]
    })

    monthly_data = pd.DataFrame({

        "Month": [
            "Jan",
            "Feb",
            "Mar",
            "Apr"
        ],

        "Amount": [
            45000,
            52000,
            41000,
            60000
        ]
    })

    # CHARTS

    chart1, chart2 = st.columns(2)

    with chart1:

        st.markdown(
            "## 💳 Expense Categories"
        )

        pie = px.pie(

            expense_data,

            values="Amount",

            names="Category",

            hole=0.72,

            color_discrete_sequence=[
                "#8B5CF6",
                "#06B6D4",
                "#22C55E",
                "#F59E0B"
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

    with chart2:

        st.markdown(
            "## 📈 Monthly Overview"
        )

        line = px.area(

            monthly_data,

            x="Month",

            y="Amount",

            template="plotly_dark"
        )

        line.update_traces(
            line_color="#8B5CF6"
        )

        line.update_layout(

            paper_bgcolor='rgba(0,0,0,0)',

            font_color='white',

            height=420
        )

        st.plotly_chart(
            line,
            width='stretch'
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # TRANSACTIONS

    st.markdown(
        "## 💰 Recent Transactions"
    )

    transactions = pd.DataFrame({

        "Merchant": [
            "Amazon",
            "Zomato",
            "Uber",
            "Netflix",
            "Swiggy"
        ],

        "Category": [
            "Shopping",
            "Food",
            "Travel",
            "Entertainment",
            "Food"
        ],

        "Amount": [
            "₹2,450",
            "₹850",
            "₹320",
            "₹499",
            "₹780"
        ]
    })

    st.dataframe(
        transactions,
        width='stretch',
        hide_index=True
    )