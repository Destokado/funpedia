from collections import Counter

from pywikibot import Site, User, APISite


## Function to get the editing buddy of a username and a language edition given a username and a langcode
#
#  Returns the editors the user has coincided the most in the pages of the last 100 edits
def get_editing_buddy(username, langcode,namespaces =[0]):
    username = username.capitalize()
    langcode = langcode.lower()
    site = Site(langcode, 'wikipedia')
    user = User(site, username)
    contributed_pages = set()
    for page, oldid, ts, comment in user.contributions(total=100, namespaces=namespaces):
        contributed_pages.add(page)

    return get_contributor_ocurrences(contributed_pages,site, username)

    # return get_all_contributors(contributed_pages, username)


def get_contributor_ocurrences(contributed_pages, site,username):
    contributors = []
    for page in contributed_pages:

        for editor in page.contributors():
            if APISite.isBot(self= site,username=editor) or editor==username:
                continue
            contributors.append(editor)

    return Counter(contributors).items()

if __name__ == "__main__":
    import timeit

    t = timeit.Timer(lambda: print(get_editing_buddy('Paucabot', 'ca')))
    print(t.timeit(1))
