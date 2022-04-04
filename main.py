
try:
    import streamlit as st
except ImportError:
    print("No module named 'streamlit' found")


try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

import time



st.title('Fake Review detector')
st.header('detect fake reviews using this tools')
st.text('made by students of class 12 AM JAIN SCHOOL')
review = st.text_area("Review To Check")

time.sleep(1)

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
# to search
res = ''
 
for j in search(review, tld="co.in", num=10, stop=10, pause=2):
    res = ''
    res = res + j

if review.strip() == '':
    st.subheader('Review is empty')
elif res == '':
    st.subheader('This review is NOT FAKE')
else:
    st.subheader('this review  is Potentially fake and has been found in the following websites')
    st.write(res)

