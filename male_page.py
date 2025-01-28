import streamlit as st
from helpers import generate_response
def display_prompt_result():
    number1 = st.session_state['numbers'][0]
    number2 = st.session_state['numbers'][1]
    number3 = st.session_state['numbers'][2]
    number4 = st.session_state['numbers'][3]
    selected_position = st.session_state['numbers'][4]
    prompt = f"""
    Please give me a male football player that fits the following data (or is close to it): 
    Age: {number1} years old
    Size: {number2} cm tall
    Weight: {number3} kilograms 
    Top Speed min. {number4} kilometers per hour
    Plays the position of {selected_position}. 
    Please give me only one player. It can be any player that fits the data. It also does not necessarily have to be a world-class player. 
    I know that you can not give me the exact up-to-date data, but just shout me a player anyways. 
    Could you give me the results in a listed format: """

    with st.spinner("Thinking..."):
        response = generate_response(prompt)
        st.write(response)
def function_male():
    tabs1, tabs2, tabs3 = st.tabs(["Search players", "Search clubs", "Search Coaches"])

    with tabs1:
        st.write("Here you can enter the data profile you are looking for:")

        names = ["Age", "Height (cm)", "Weight (kg)", "Speed (km/h)", "Position"]
        initial_values = [27, 180, 75, 29, "Goalkeeper"]
        min_values = [16, 160, 60, 26, None]
        max_values = [40, 205, 95, 38, None]

        positions = [
            "Goalkeeper", "Right Back", "Left Back", "Central Defender",
            "Central Midfielder", "Striker", "Winger"
        ]

        if 'numbers' not in st.session_state:
            st.session_state['numbers'] = initial_values[:]
        if 'response' not in st.session_state:
            st.session_state['response'] = ""

        for i in range(5):
            if names[i] == "Position":
                st.session_state['numbers'][i] = st.selectbox(
                    f"{names[i]}:",
                    options=positions,
                    index=positions.index(st.session_state['numbers'][i]),
                    key=f"selectbox_{i}"
                )
            else:
                col1, col2, col3 = st.columns([0.05, 0.05, 0.5])
                with col1:
                    if st.button(f"▲", key=f"up{i}"):
                        if st.session_state['numbers'][i] < max_values[i]:
                            st.session_state['numbers'][i] += 1

                with col2:
                    if st.button(f"▼", key=f"down{i}"):
                        if st.session_state['numbers'][i] > min_values[i]:
                            st.session_state['numbers'][i] -= 1

                with col3:
                    st.write(f"{names[i]}: {st.session_state['numbers'][i]}")

        search = st.button("Search")
        if search:
            display_prompt_result()

    with tabs2:
        leagues = {
            "Germany": {
                "Bundesliga": ["FC Bayern München", "Borussia Dortmund", "RB Leipzig", "Bayer 04 Leverkusen"],
                "2. Bundesliga": ["Hamburger SV", "Fortuna Düsseldorf", "Hannover 96", "1. FC Nürnberg"]
            },
            "France": {
                "Ligue 1": ["Paris Saint-Germain", "Olympique de Marseille", "LOSC Lille", "AS Monaco"],
                "Ligue 2": ["AJ Auxerre", "SM Caen", "Le Havre AC", "Dijon FCO"]
            },
            "Spain": {
                "La Liga": ["Real Madrid CF", "FC Barcelona", "Atlético de Madrid", "Sevilla FC"],
                "Segunda División": ["Levante UD", "Real Zaragoza", "Real Sporting de Gijón", "CD Tenerife"]
            },
            "Italy": {
                "Serie A": ["Juventus FC", "AC Milan", "SSC Napoli", "AS Roma"],
                "Serie B": ["Brescia Calcio", "US Cremonese", "Frosinone Calcio", "Pisa SC"]
            },
            "England": {
                "Premier League": ["Manchester City FC", "Liverpool FC", "Chelsea FC", "Manchester United FC"],
                "EFL Championship": ["Norwich City FC", "Watford FC", "Sheffield United FC", "West Bromwich Albion FC"]
            }
        }

        country_container = st.empty()
        league_container = st.empty()
        club_container = st.empty()

        country = country_container.selectbox("Select a country:", [""] + list(leagues.keys()), key="country")
        if country:
            league = league_container.selectbox("Select a league:", [""] + list(leagues[country].keys()), key="league")
            if league:
                club = club_container.selectbox("Select a club:", [""] + leagues[country][league], key="club")
                if club:
                    st.write(f"In a future version of this app you will be able to see the player list of {club} here:")


    with tabs3:
        st.write("In a future version of this app you can use this page to find football coaches :)")

