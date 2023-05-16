import pandas as pd
import pandas.io.formats.style

import os

def corr_to_html(filename: str, corr_styler: pd.io.formats.style.Styler):
    correlation_css_filepath = os.path.relpath("../static/correlation.css", os.path.dirname(filename)).replace(os.sep, '/')

    with open(filename, "w") as file:
        file.write(f'<link rel="stylesheet" type="text/css" href="{correlation_css_filepath}">')
        file.write(corr_styler.to_html())  # Open this file outside of Jupyter