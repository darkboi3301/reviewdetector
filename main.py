
import streamlit as st


import time



st.title('Fake Review detector')
st.header('Detect fake reviews using this online tool')
st.text('Made by students of class 12 AM JAIN SCHOOL')
review = '"'+st.text_area("Review To Check")+'"'



from googlesearch import search
 
# to search
res = ''
with st.spinner('Hold on.... \U0001f600'): 
    for j in search(review, tld="co.in", num=10, stop=10, pause=2):
        res = res + j + '\n'
    
if review.strip() == '':
    st.warning('Review is empty')
elif res == '':
    st.info('This review is not made by a bot and therefore could be Reliable')
else:
    st.info('this review  is Potentially fake and has been found in the following websites')
    st.write(res)

