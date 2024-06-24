
#
#
# dict_ = {'a': [11, 21, 31], 'b': [12, 22, 32]}
#
# df = pd.DataFrame(dict_)
#
# print(type(df))

import pandas as pd
from nba_api.stats.static import teams
# import matplotlib.pyplot as plt

def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

nba_teams = teams.get_teams()
nbaTeams = nba_teams[0:3]
teams = one_dict(nbaTeams)

teamsDf = pd.DataFrame(teams)

celtics_df = teamsDf[teamsDf['nickname'] == 'Celtics']

print(celtics_df)


