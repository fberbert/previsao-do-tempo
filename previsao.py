#!/usr/bin/env python3
"""
Autor: Fábio Berbert de Paula <fberbert@gmail.com>
Data : 27/11/2018
"""

def previsao():
    #pip install requests-html
    from requests_html import HTMLSession
    import re

    session = HTMLSession()

    #URL resultado da busca no Google por: previsao do tempo
    r = session.get('https://www.google.com.br/search?q=previsao+do+tempo&oq=previsao+do+tempo&ie=UTF-8')

    #abaixo defino os seletores CSS de cada elemento da pagina
    #e armazeno nas devidas variaveis
    selector_city = '#wob_loc'
    city = r.html.find(selector_city, first=True).text

    selector_date = '#wob_dts'
    date = r.html.find(selector_date, first=True).text

    selector_state = '#wob_dc'
    state = r.html.find(selector_state, first=True).text

    selector_temp = '#wob_tm'
    temp = r.html.find(selector_temp, first=True).text

    #regex para limpar informacoes irrelevantes
    regex = re.compile(r'\nTemperatura.*$', re.DOTALL)
    selector_dtl = 'div.wob-dtl'
    dtl = r.html.find(selector_dtl, first=True).text
    dtl = regex.sub("", dtl)

    return("%s\n%s\t%s°C (%s)\n\n%s" %(city, date, temp, state, dtl))

print(previsao())
