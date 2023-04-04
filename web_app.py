import streamlit as st
import python_scripts.reasoner as reasoner

st.set_page_config(layout="wide")
choose = st.container()
title_container = st.container()
infos = st.columns(5)
plot = st.container()
rest = st.container()


iri = 'https://schema.org/'

#load_ontology
ontology = "ontologies/movies_project_inferred.owl"
onto = reasoner.load_ontology(ontology)


#get selectboxes // according to movie/actor option ?
movies = reasoner.get_movies(onto)
actors = reasoner.get_actors(onto)

movies_titles = reasoner.get_movies_title(onto)
actors_names = reasoner.get_actors_name(onto)

with choose:
    option = st.selectbox(label="Choose what to look for:", options=("Actors", "Movies"))
    if option == "Actors":
        name = st.selectbox(label="Choose actor's name:", options=tuple(actors_names))
        for _ in range(2):
            st.write("")
        for actor in actors:
            if actor.myName:
                if actor.myName[0] == name:
                    with title_container:
                        if actor.myName:
                            st.title(actor.myName[0])
                            for _ in range(3):
                                st.write("")
                        else:
                            st.write("No Name")
                    with infos[0]:
                        if actor.photo:
                            st.image(actor.photo[0])
                        else:
                            st.write("No Picture")
                    with infos[2]:
                        for _ in range(1):
                            st.write("")
                        st.header("Age:")
                        if actor.age:
                            st.write(str(actor.age[0]))
                        else:
                            st.write("No Age")
                    with plot:
                        for _ in range(2):
                            st.write("")
                        st.header("Biography:")
                        if actor.biography:
                            st.write(actor.biography[0])
                        else:
                            st.write("No biography")
                    with infos[1]:
                        for _ in range(1):
                            st.write("")
                        st.header("\tMovies:")
                        for movie in actor.isActor:
                            if movie.myTitle:
                                st.write(f"\t{movie.myTitle[0]}")
                            else:
                                st.write(f"\t{movie}")

        st.write()
    if option == "Movies":
        title = st.selectbox(label="Choose movie's title:", options=tuple(movies_titles))
        for _ in range(2):
            st.write("")
        for movie in movies:
            if movie.myTitle:
                if movie.myTitle[0] == title:
                    with title_container:
                        if movie.myTitle:
                            st.title(movie.myTitle[0])
                            for _ in range(3):
                                st.write("\n")
                        else:
                            st.write("No Title")
                    with infos[0]:
                        if movie.myPoster:
                            st.image(movie.myPoster[0])
                        else:
                            st.write("No Poster")
                    with infos[1]:
                        for _ in range(2):
                            st.write("\n")
                        st.header("Actors:")
                        if movie.hasActor:
                            for actor in movie.hasActor:
                                st.write(actor.myName[0])
                        else:
                            st.write("No Actors")
                    with infos[3]:
                        for _ in range(2):
                            st.write("")
                        st.header("Genres:")
                        if movie.hasGenre:
                            for genre in movie.hasGenre:
                                st.write(genre.name)
                        else:
                            st.write("No Genre")
                    with plot:
                        for _ in range(2):
                            st.write("")
                        st.header("Plot:")
                        if movie.myPlot:
                            st.write(movie.myPlot[0])
                        else:
                            st.write("No Plot")
                    with infos[2]:
                        for _ in range(2):
                            st.write("")
                        st.header("Year:")
                        if movie.myYear:
                            st.write(movie.myYear[0])
                        else:
                            st.write("No Year")



