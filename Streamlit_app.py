import streamlit

streamlit.title("My Parents New Healthy Dinner")
streamlit.header("Breakfast Favorites")
streamlit.text("🥣 Omega 3 and Blueberry Oat meal")
streamlit.text("🥗 Kale Spinach and Rocket Smoothie")
streamlit.text("🐔 Hard boiled free range-egg")
streamlit.text("🥑🍞 Avocado Toast")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index(["Fruit"])
streamlit.multiselect("pick some fruits: ",list(my_fruit_list.index),["Avocado","Strawberries"])
streamlit.dataframe(my_fruit_list)

