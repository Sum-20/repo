import streamlit as st
def largest_num(num_1,num_2,num_3):
   if (num_1 > num_2) and (num_1 > num_3):
     largest = num_1
   elif (num_2 > num1) and (num_2 > num_3):
     largest = num_2
   else:
     largest = num_3
   return largest
num_1= st.number_input('Insert a number')
num_2= st.number_input('Insert a number')
num_3 = st.number_input('Insert a number')
st.write("The largest number is", largest_num)
