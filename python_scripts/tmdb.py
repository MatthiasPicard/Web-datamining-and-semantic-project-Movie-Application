import requests
import json

import reasoner

API_KEY = "e437ba8ad56648958471ed221119622e"
iri = 'https://schema.org/'

import rdflib

if __name__ == '__main__':

    g = rdflib.Graph()
    g.parse('../ontologies/movies_project.owl')

    for i in range(1, 2):
        if i%10==0:
            print(i)
        response = requests.get(f"https://api.themoviedb.org/3/person/{i}?api_key={API_KEY}&language=en-US")

        if response.ok:
            d = json.loads(response.text)
            name = d['name']

            # Check if exists in Ontology
            sparql = f"""SELECT ?p {{ ?p <{iri}myName> \"{name}\"}}"""
            res = g.query(sparql)
            if len(res) == 0:
                continue
            person = None
            for row in res:
                person = row.p

            if 'profile_path' in d.keys():
                if d['profile_path'] is not None:
                    bio = d['biography'].replace('\"', '')
                    bio = bio.replace("\n", " ")
                    sparql_bio = f"""INSERT DATA {{ <{person}> <{iri}biography> \"{bio}\" }}"""
                    g.update(sparql_bio)

            if 'profile_path' in d.keys():
                if d['profile_path'] is not None:
                    photo_url = "https://image.tmdb.org/t/p/w500" + d['profile_path']
                    sparql_photo = f"""INSERT DATA {{ <{person}> <{iri}photo> \"{photo_url}\" }}"""
                    g.update(sparql_photo)

            if 'death_day' in d.keys():
                if d['death_day'] is not None:
                    sparql_deathday = f"""INSERT DATA {{ <{person}> <{iri}deathday> \"{d['deathday']}\" }}"""
                    g.update(sparql_deathday)

            if 'birthday' in d.keys():
                if d['birthday'] is not None:
                    sparql_birthday = f"""INSERT DATA {{ <{person}> <{iri}birthday> \"{d['birthday']}\" }}"""
                    age = 2023 - int(d['birthday'][:4])
                    sparql_age = f"""INSERT DATA {{ <{person}> <{iri}age> {age} }}"""
                    g.update(sparql_birthday)
                    g.update(sparql_age)

    file = "../ontologies/movies_project.owl"
    g.serialize(file, format="xml")
    reasoner.infer(file)
