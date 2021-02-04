import requests
from furl import furl

regional_datasets = [US, Europe, Japan, emerg, China, India, Global]
regional_datasets_topics = [inshold, beta, totalbeta, mktcaprisk]
datasets_topics = [histretSP, histimpl, ctryprem, countrytaxrates]

base_path = "http://www.stern.nyu.edu/~adamodar/pc/datasets/{}.xls"
# f = furl(http://www.stern.nyu.edu/~adamodar/pc/datasets/{}.xls)

for f in datasets_topics:
    path = base_path.format(f)
    response = requests.get(path)
    if response.status_code == 200:
        response = response.content
    else:
        raise ValueError("Error Downloadning File")
