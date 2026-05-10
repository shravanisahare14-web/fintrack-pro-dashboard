import streamlit as st

def render_settings():

    st.markdown(
        """
        <div class="main-title">
            Settings
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="sub-title">
            Personalize your financial dashboard experience.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.toggle("Enable AI Spending Alerts")

    st.toggle("Dark Mode", value=True)

    st.toggle("Monthly Email Summary")

    currency = st.selectbox(
        "Preferred Currency",
        [
            "INR ₹",
            "USD $",
            "EUR €"
        ]
    )

    st.success(
        f"Current Currency: {currency}"
    )