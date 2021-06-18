duel_app = Dash(__name__, server=application, url_base_pathname="/duel/",
                 external_stylesheets=external_stylesheets)
duel_app.config['suppress_callback_exceptions'] = True
title = 'Duel '
duel_app.title = title + title_addenda

duel_app.layout = html.Div([
    navbar,
    html.H3(title, style={'textAlign': 'center'}),
    dcc.Markdown("""This page allows you to challenge another editor to contribute. 
    You can establish a metric (rule to measure the duel), an objective, the language edition, the duration and the namespaces in which the duel will take place. **You can also agree on themes and even bet tokens!**   
    Remember: whoever reaches the goal first or whoever is closest to it when the final date arrives, wins the duel and gets the tokens from the bet, if any."""),
    dcc.Markdown("* **Do you have what it takes?**"),
    footbar, ])