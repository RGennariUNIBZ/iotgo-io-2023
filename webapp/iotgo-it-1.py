#this file was updated on Mon Oct 18 10:10:06 2021
import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="IoTgo",page_icon=None,layout="wide")
urlis="https://makecode.microbit.org/--docs?md=%0A%0A%60%60%60%20blocks%0Abasic.forever%28function%20%28%29%20%7B%0A%20%20%20%20if%20%28%21input.buttonIsPressed%28Button.A%29%29%7B%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%7D%20else%20%7B%0A%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%7D%0A%7D%29%0A%60%60%60%0A%0A"

cardWidth=100
pluscardwidht=100
missionCardWidth=160
vertiPaddingWidth=35

# st.markdown("""""")
applogo, empty1, empty2, mission,empty3, persona, thing, empty4,edit  = st.columns(9)

with applogo:
    st.image("http://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/applogo3.png",width=300)
#with mission:
#    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-mission-4.png", width=missionCardWidth)
#with persona:
#    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-noPersona.png", width=cardWidth)
#with thing:
#    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-noThing.png", width=cardWidth)
with edit:
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=60)
    st.markdown("[Modifica]("+urlis+")", unsafe_allow_html=True)

input_col, plus_col, output_col,  code_col, emptycol , emptycol , emptycol, emptycol,emptycol,emptycol,emptycol = st.columns(11)

with input_col:    
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)
    st.write("se...")
    # ("Input1:")
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-inputPhy-buttonNotpressed.png", width=cardWidth)
    # ("Input2:")
    #st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-noInput.png", width=cardWidth)
    # ("Input3:")
    #st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-noInput.png", width=cardWidth)

with plus_col:    
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth*2)
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht)
    #st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht)
    #st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/plus.png", width=pluscardwidht)    

with output_col:    
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)
    st.write("allora...")
    # ("Output1:")
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-noOutput.png", width=cardWidth)
    # ("Output2:")
    #st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-noOutput.png", width=cardWidth)
    # ("Output3:")
    #st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/cards/IT-noOutput.png", width=cardWidth)
    st.image("https://raw.githubusercontent.com/rizMehdi/IoTgo/main/images/blankcard.png", width=vertiPaddingWidth)

with code_col:
    # st.header("Il mio codice è:")
    components.iframe(urlis,width=900, height=1500, scrolling=True)

st.button("Refresh")
