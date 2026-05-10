import streamlit as st

def render_budgets():

    st.markdown(
        """
        <div class="main-title">
            Budget Management
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="sub-title">
            Monitor category-wise budget allocation and usage.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Monthly Budget",
            "₹80,000",
            "+5%"
        )

        st.progress(0.68)

        st.caption("68% budget utilized")

    with col2:

        st.metric(
            "Remaining Budget",
            "₹26,000",
            "-8%"
        )

        st.progress(0.32)

        st.caption("32% remaining")