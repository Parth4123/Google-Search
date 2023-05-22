import webbrowser
import sys

url = 'https://www.google.com/search?q='

valid_websites=[
    'reddit.com',
    'stackoverflow.com',
    'stackexchange.com',
    'github.com',
    'geeksforgeeks.org',
    'medium.com',
    'tutorialspoint.com',
]


#linux 
# Brave_path = '/usr/bin/brave-browser %s'

def create_fliter():
    filter = '('
    for index, website in enumerate (valid_websites):
        filter+= 'site:' + website
        if index == len(valid_websites) - 1:
            filter+= ')'
        else:
            filter+= ' OR '

    return filter


def create_query():
    query = sys.argv[1:]
    return ' '.join(query)

def create_url():
    if len(sys.argv[1:]) == 0:
        print('Error: Please enter a valid Search query') 
    else:
        final_url = url + create_query() + create_fliter()
        # webbrowser.get(Brave_path).open(final_url)
        webbrowser.open_new_tab(final_url)

create_url()
