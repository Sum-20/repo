import streamlit as st
num_1 = st.number_input('Insert a number')
num_2= st.number_input('Insert a number')
num_3 = st.number_input('Insert a number')
st.write('The current number is ', number)
if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3

st.write("The largest number is", largest)
