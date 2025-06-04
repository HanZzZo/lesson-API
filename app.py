import streamlit as st
from countries_api import get_continents, get_countries_by_continent

st.title("🌍 Countries Explorer (GraphQL)")

continents = get_continents()
continent_map = {c["name"]: c["code"] for c in continents}
selected = st.selectbox("Выберите континент", list(continent_map.keys()))

if selected:
    code = continent_map[selected]
    countries = get_countries_by_continent(code)

    st.subheader(f"Страны в {selected}:")
    for c in countries:
        st.markdown(f"**{c['name']}** (столица: {c.get('capital', '—')})")
        langs = [l['name'] for l in c['languages']]
        st.markdown(f"Языки: {', '.join(langs) if langs else 'нет данных'}")
        st.markdown("---")
