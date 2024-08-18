import streamlit as st

from streamlit_page_link_params import page_link, page_link_html

st.title("haha")

st.divider()

st.markdown("## Native:")

st.markdown("### basic")
st.page_link("pages/p1.py", label="go to p1")

st.markdown("### use_container_width=True")
st.page_link("pages/p1.py", label="go to p1", use_container_width=True)

st.divider()

st.header("Component:")

st.markdown("### basic, no params")
page_link("pages/p1.py", label="go to p1")

st.markdown("### basic, use_container_width=True, with params: use_container_width=true")
page_link("pages/p1.py", label="go to p1",
          use_container_width=True, query_params={"use_container_width": "true"})

st.markdown(f"""### use html, with params: html=true""")
page_link_html(f'<a href="/p1" style="font-size: 30px;">go to p1</a>', query_params={"html": "true"})

st.markdown('''### use html, with style, with params: html=true&with_style=color''')
page_link_html("""
<style>
.myPageLink {
    color: green !important;
}
</style>
<a href="/p1" class="myPageLink">go to p1</a>
""", query_params={"html": "true", "with_style": "color"})

st.divider()

st.write("Page end.")
