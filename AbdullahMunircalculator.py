import streamlit as st

st.title('Abdullah Munir Calulator HCCD-AI')
st.set_page_config( layout="centered")

# Store expression
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Symbol → Python operator
symbol_map = {
    "➕": "+",
    "➖": "-",
    "✖️": "*",
    "➗": "/",
    "=": "=",
    "C": "C"
}

# Callback function
def handle_click(symbol):
    val = symbol_map.get(symbol, symbol)
    if val == "C":
        st.session_state.expression = ""
    elif val == "=":
        try:
            result = eval(st.session_state.expression)
            st.session_state.expression = str(result)
        except:
            st.session_state.expression = "Error"
    else:
        st.session_state.expression += val

# Custom style
st.markdown("""
    <style>
        .calc-display {
            background-color: #808080;
            font-size: 36px;
            padding: 20px;
            border-radius: 10px;
            text-align: right;
            margin-bottom: 20px;
            border: 2px solid #ccc;
        }
        .orange-btn > button {
            background-color: orange !important;
            color: white !important;
            font-size: 28px !important;
            height: 70px !important;
            width: 100% !important;
            border-radius: 10px !important;
            margin-top: 5px;
        }
        .grey-btn > button {
            background-color: grey !important;
            color: white !important;
            font-size: 28px !important;
            height: 70px !important;
            width: 100% !important;
            border-radius: 10px !important;
            margin-top: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Display expression
st.markdown(f"<div class='calc-display'>{st.session_state.expression}</div>", unsafe_allow_html=True)

# Button layout
buttons = [
    ["7", "8", "9", "➗"],
    ["4", "5", "6", "✖️"],
    ["1", "2", "3", "➖"],
    ["0", "C", "=", "➕"]
]

# Render buttons with safe styling and callbacks
for row in buttons:
    cols = st.columns(4)
    for i, btn in enumerate(row):
        css_class = "orange-btn" if btn.isdigit() else "grey-btn"
        with cols[i]:
            st.markdown(f"<div class='{css_class}'>", unsafe_allow_html=True)
            st.button(btn, key=f"{btn}_{i}", on_click=handle_click, args=(btn,))
            st.markdown("</div>", unsafe_allow_html=True)
