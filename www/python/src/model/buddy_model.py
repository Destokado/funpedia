from pywikibot import Site, User
from collections import Counter
## Function to get the editing buddy of a username and a language edition given a username and a langcode
#
def get_editing_buddy(username, langcode):
    # Get the last 100 edits of that user
        # Get the page_id of each edit
            #Get the last 100 editors of that page
                #For each editor, get the last 100 edits
                    #For each edit, get the page_id
                        #See if that page_id is the same as one of the first user

    user = User(Site(langcode,'wikipedia'),username)
    contributed_pages = set()

    for page, oldid, ts, comment in user.contributions(total=500):
        contributed_pages.add(page)

    #return get_contributor_ocurrences(contributed_pages,username)

    return get_all_contributors(contributed_pages, username)

def get_contributor_ocurrences(contributed_pages, username):
    contributors = []
    for page in contributed_pages:

        for editor in page.contributors():
            contributors.append(editor)

    return Counter(contributors)

def get_all_contributors(contributed_pages, username):
    contributors = {}
    for page in contributed_pages:
        editors = []
        for editor in page.contributors():
            if editor != username:
                editors.append(editor)
        contributors[page.title] = editors
    return contributors


if __name__ == "__main__":
    import timeit
    t = timeit.Timer(lambda : get_editing_buddy('Marcmiquel','ca'))
    print(t.timeit(1))
