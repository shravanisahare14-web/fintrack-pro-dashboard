import streamlit as st

def render_goals():

    st.markdown(
        """
        <div class="main-title">
            Financial Goals
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="sub-title">
            Track savings milestones and long-term targets.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("💻 MacBook Pro Fund")

    st.progress(0.72)

    st.caption("₹1,08,000 / ₹1,50,000")

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("✈ Europe Trip")

    st.progress(0.46)

    st.caption("₹92,000 / ₹2,00,000")