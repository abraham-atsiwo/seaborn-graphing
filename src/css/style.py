from streamlit import markdown


def index():
    markdown("""<style>
            .streamlit-expanderHeader{
            font-weight:bold; 
            border-radius: 50%;
        }
    </style>""", unsafe_allow_html=True)
    markdown("""<style>
            .streamlit-expanderHeader{
            font-weight:bold; 
            border-radius: 50%;
            color: black;
            font-size: 16px;
            font-style: italic;
        }
    </style>""", unsafe_allow_html=True)
    markdown("""<style>
            .stButton > button{
            font-weight:bold; 
            border-radius: 50%;
        }
    </style>""", unsafe_allow_html=True)
    markdown("""<style>
            .stDownloadButton > button{
            font-weight:bold; 
            border-radius: 50%;
        }
    </style>""", unsafe_allow_html=True)
    markdown("""<style>
            div.css-19nj2mc{
            display:flex; 
            flex-direction:row;
        }
    </style>""", unsafe_allow_html=True)
    markdown('<style>div.row-widget.stRadio> div{flex-direction:row;}</style>', 
            unsafe_allow_html=True)