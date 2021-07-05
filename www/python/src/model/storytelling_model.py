import pywikibot as pw
import wikitextparser as wtp
import pypandoc as pp

def get_content(langcode, title):
    page = pw.Page(pw.Site(langcode, 'wikipedia'), title)


    parsed = wtp.parse(page.get())
    for s in parsed.sections:
        print('**************SECTION***********')
        print(s)
    return pp.convert_text(page.get(),to='html',format='mediawiki')


if __name__ == "__main__":
   # get_content('ca', 'Usuari_Discussió:Bestiasonica')
   # expects an installed pypandoc: pip install pypandoc
   from pypandoc.pandoc_download import download_pandoc

   # see the documentation how to customize the installation path
   # but be aware that you then need to include it in the `PATH`
   download_pandoc()
