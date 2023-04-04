from owlready2 import *
from owlready2.reasoning import sync_reasoner_pellet
import streamlit as st

def load_ontology(ontology_file):
    # Load the OWL file
    onto = get_ontology(ontology_file).load()
    return onto


def infer(ontology_file):
    onto = load_ontology(ontology_file)
    with onto:
        sync_reasoner_pellet(infer_data_property_values=True, infer_property_values=True)
        onto.save(f"{ontology_file.split('.')[0].strip()}_inferred.owl", format='rdfxml')


def get_actors(loaded_ontology):
    with loaded_ontology:
        list_ = loaded_ontology.search(is_a=loaded_ontology.myActor)
        actors = []
        for item_ in list_:
            actors.append(item_)
    return actors


def get_movies(loaded_ontology):
    with loaded_ontology:
        list_ = loaded_ontology.search(is_a=loaded_ontology.myMovie)
        movies = []
        for item_ in list_:
            movies.append(item_)
    return movies


def get_actors_name(loaded_ontology, reasoner=False):
    with loaded_ontology:
        actors = get_actors(loaded_ontology)
        names_list = []
        for item_ in actors:
            name = item_.myName
            if name:
                names_list.append(item_.myName[0])
    return names_list


def get_movies_title(loaded_ontology, reasoner=False):
    with loaded_ontology:
        movies = get_movies(loaded_ontology)
        title_list = []
        for item_ in movies:
            title = item_.myTitle
            if title:
                title_list.append(item_.myTitle[0])
    return title_list

"""
if __name__ == '__main__':

    onto3 = load_ontology("movies_project.owl")
    with onto3:
        sync_reasoner_pellet(infer_property_values=True, infer_data_property_values=True)
        actors = onto3.search(is_a=onto3.myMovie)

        \"\"\"for actor in actors:
            try:
                print(actor.iri, actor.age, actor.birthday, actor.name)
            except:
                print("One annotation doesn't exist")\"\"\"

        for movie in actors:
            print(movie.iri, movie.hasGenre, movie.myTitle, movie.myYear, movie.myName, movie.myPoster, movie.myPlot)"""
