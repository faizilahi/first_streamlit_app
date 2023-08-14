import st as st
import pandas
import requests

st.title('My Parents New Healthy Diner')

st.header('Breakfast Favourites')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list= my_fruit_list.set_index('Fruit')
options=list(my_fruit_list.index)
default=['Avocado','Strawberries']
fruits_selected=st.multiselect("pick some fruits:",options,default)
fruits_to_show=my_fruits_list.loc[fruits_selected]
st.write(fruits_selected)
st.write(type(fruits_selected))
st.write(my_fruit_list.head())
st.dataframe(fruits_to_show)

# st.header("Fruityvice Fruit Advice!")
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# st.text(fruityvice_response)
