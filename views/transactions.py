import streamlit as st
import pandas as pd
import plotly.express as px


def render_transactions():

    # HEADER

    st.title("💳 Transactions Center")

    st.caption(
        "Smart tracking for your recent financial activity."
    )

    st.markdown("##")

    # FILTERS

    f1, f2, f3 = st.columns([2,2,1])

    with f1:

        category = st.selectbox(
            "Category",
            [
                "All",
                "Food",
                "Shopping",
                "Travel",
                "Entertainment"
            ]
        )

    with f2:

        status = st.selectbox(
            "Status",
            [
                "All",
                "Completed",
                "Pending",
                "Auto Debit"
            ]
        )

    with f3:

        st.markdown("<br>", unsafe_allow_html=True)

        st.button(
            "Export"
        )

    st.markdown("##")

    # TRANSACTIONS DATA

    transactions = [

        {
            "icon": "🛒",
            "merchant": "Amazon",
            "category": "Shopping",
            "amount": "₹2,450",
            "status": "Completed"
        },

        {
            "icon": "🍔",
            "merchant": "Zomato",
            "category": "Food",
            "amount": "₹850",
            "status": "Completed"
        },

        {
            "icon": "🚕",
            "merchant": "Uber",
            "category": "Travel",
            "amount": "₹320",
            "status": "Completed"
        },

        {
            "icon": "🎬",
            "merchant": "Netflix",
            "category": "Entertainment",
            "amount": "₹499",
            "status": "Auto Debit"
        },

        {
            "icon": "🍕",
            "merchant": "Swiggy",
            "category": "Food",
            "amount": "₹780",
            "status": "Completed"
        }
    ]

    # FILTERING

    filtered = []

    for tx in transactions:

        category_match = (
            category == "All"
            or tx["category"] == category
        )

        status_match = (
            status == "All"
            or tx["status"] == status
        )

        if category_match and status_match:

            filtered.append(tx)

    # TRANSACTION CARDS

    for tx in filtered:

        card = st.container()

        with card:

            left, middle, right = st.columns([1,4,2])

            with left:

                st.markdown(
                    f"# {tx['icon']}"
                )

            with middle:

                st.subheader(
                    tx["merchant"]
                )

                st.caption(
                    tx["category"]
                )

            with right:

                st.markdown(
                    f"## {tx['amount']}"
                )

                if tx["status"] == "Completed":

                    st.success(
                        tx["status"]
                    )

                elif tx["status"] == "Pending":

                    st.warning(
                        tx["status"]
                    )

                else:

                    st.info(
                        tx["status"]
                    )

        st.markdown("---")

    st.markdown("##")

    # SPENDING CHART

    st.subheader(
        "📈 Spending Breakdown"
    )

    chart_data = pd.DataFrame({

        "Category": [
            "Food",
            "Shopping",
            "Travel",
            "Entertainment"
        ],

        "Amount": [
            1630,
            2450,
            320,
            499
        ]
    })

    chart = px.bar(

        chart_data,

        x="Category",

        y="Amount",

        color="Category",

        template="plotly_dark",

        color_discrete_sequence=[
            "#8B5CF6",
            "#06B6D4",
            "#22C55E",
            "#F59E0B"
        ]
    )

    chart.update_layout(

        paper_bgcolor='rgba(0,0,0,0)',

        plot_bgcolor='rgba(0,0,0,0)',

        font_color='white',

        height=500
    )

    st.plotly_chart(
        chart,
        width='stretch'
    )