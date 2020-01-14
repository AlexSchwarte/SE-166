import requests

cookies = {
    '_dtlrde_visitor_id': 'eb68caa3-6ac7-46f7-9320-e956b15235b9',
    '_ga': 'GA1.2.729570989.1566914203',
    'optimizelyEndUserId': 'oeu1569088854377r0.6776164682254544',
    '_vwo_uuid_v2': 'DEB5E5E35DB73B549F202DEBF94B81BCF|47e2711eb3ba7563f6431af9ffb26acb',
    '_vis_opt_s': '1%7C',
    '_vwo_uuid': 'DEB5E5E35DB73B549F202DEBF94B81BCF',
    '_4c_': 'dVFda9s8GP0rQxe7ShXLli0rUMboWMnN3sHodllk63Ei5lRGktOGkv%2FeI68NvPvwhdF5Ps45Onpmj3t6YBtRN7qsKyHrUooV%2B0mnyDbPrJ%2Fy%2F5h%2Fn32gSMQ2l9OK3UUKt8HPmGLOxDTfp%2BDMiM7X4O3cp61F57%2Fv2xuU5jAC7FOa4ma93vmrnRnpqvcHPgX%2FdOKj63gmMYk42Xk9xbXj1n%2BYrjPB%2B%2FlN64s50PX%2F1XpvszGhueQFsHWx90cKp28Ujq6n7Sd0Ue%2BCfwQNwM0%2B%2BAO9Uw2qQ7avSl2rQreaI4pGC1kWFXoeMbAf7sFiETDQQCEsDEDRpSyb77HLzjgug3KicMhrOE6IjgkcRt9jCgBhr9jtx%2Fu7xdNfVc8r9vTrRapK17JqqwakCem1jSzyh4ngEO3yNKyrO6UktdQOsiGyg5HaDq0QhRx0YzsILnxKFSUkhNIKBBP4ln0896tc2ahairasXuWEvMjli%2Fw2vZjDtP7TnDXJdCbSv7eqN43L1vn8Ag%3D%3D',
    'oup-cookie': '1_23-9-2019',
    'AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg': '-1712354808%7CMCIDTS%7C18163%7CMCMID%7C90036397354918203941462032067790417237%7CMCAAMLH-1569858326%7C9%7CMCAAMB-1569858326%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1569260726s%7CNONE%7CMCAID%7CNONE%7CMCCIDH%7C-210853576%7CvVersion%7C4.3.0',
    's_pers': '%20c19%3Dsd%253Aproduct%253Ajournal%253Aarticle%7C1569255326800%3B%20v68%3D1569253521080%7C1569255326829%3B%20v8%3D1569253527285%7C1663861527285%3B%20v8_s%3DFirst%2520Visit%7C1569255327285%3B',
    'CID': 'AgAAAHyJvrF3Q9b/JQLXnNbwzLk=',
    'AMCV_1B6E34B85282A0AC0A490D44%40AdobeOrg': '-1303530583%7CMCIDTS%7C18181%7CMCMID%7C82089378510552103481825494631972022611%7CMCAAMLH-1571414688%7C9%7CMCAAMB-1571414688%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1570817088s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.3.0',
    'amplitude_id_9f6c0bb8b82021496164c672a7dc98d6_edmiastate.edu': 'eyJkZXZpY2VJZCI6IjVhOWM5OTQ2LTlkOGMtNDhiNC04YzA3LThlMjBmNmU0NDI4ZFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU3NDM2NDgwOTA3NSwibGFzdEV2ZW50VGltZSI6MTU3NDM2NDgwOTA3OSwiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6MzksInNlcXVlbmNlTnVtYmVyIjozOX0=',
    'amplitude_id_408774472b1245a7df5814f20e7484d0iastate.edu': 'eyJkZXZpY2VJZCI6ImE1OTJhYTI3LTRkZjYtNDRiZi1iNTIwLWRlODkwMGQxZGJkOVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU3NDM2NDgwOTEzMCwibGFzdEV2ZW50VGltZSI6MTU3NDM2NDgxNjQ1MywiZXZlbnRJZCI6MjY3LCJpZGVudGlmeUlkIjoxNzgsInNlcXVlbmNlTnVtYmVyIjo0NDV9',
    'PHPSESSID': 'lv1kpgfb6knlfvvsuhvkk05vi3',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Sec-Fetch-User': '?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

params = (
    ('y', '2019'),
    ('m', '11'),
    ('d', '20'),
    ('mode', 'month'),
)

response = requests.get('https://events-stuorg.sws.iastate.edu/events/', headers=headers, params=params, cookies=cookies)

responseText = response.content

#print(responseText)

for x in range(0, len(responseText)):
    if(str(responseText[x:x+9]).lower() == 'b\'free food\''):
        print('Found at ' + str(x))
        for i in range(x-500,x):
            location = x - i
            if(responseText[x-i] == '\\'):
                print(i)
            print(responseText[location])

