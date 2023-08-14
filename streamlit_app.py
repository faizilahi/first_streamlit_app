import streamlit
import pandas
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list= my_fruit_list.set_index('Fruit')
options=list(my_fruit_list.index)
default=['Avocado','Strawberries']
streamlit.multiselect("pick some fruits:",options,default)
streamlit.dataframe(my_fruit_list)
fruits_selected=streamlit.multiselect("pick some fruits:",options,default)
fruits_to_show=my_fruits_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
