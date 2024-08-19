import streamlit as st
# Title of the app
st.title('Simple Streamlit App for Teaching Purposes')

# Description of the app
st.write("""
This is a basic Streamlit app that demonstrates how to take user inputs, 
apply transformations, and display the results.
""")

# Sidebar for user inputs
st.sidebar.header('User Input')

# Text input
user_text = st.sidebar.text_input('Enter some text:', 'Hello, Streamlit!')

# Slider input
number = st.sidebar.slider('Select a number:', min_value=1, max_value=100, value=50)

# Checkbox input
reverse_text = st.sidebar.checkbox('Reverse the text?')

# Radio button input
case = st.sidebar.radio(
    'Choose the text case:',
    ('Original', 'Uppercase', 'Lowercase')
)

# Apply transformations based on user input
# 1. Text case transformation
if case == 'Uppercase':
    transformed_text = user_text.upper()
elif case == 'Lowercase':
    transformed_text = user_text.lower()
else:
    transformed_text = user_text

# 2. Reverse the text if checkbox is selected
if reverse_text:
    transformed_text = transformed_text[::-1]

# Display the transformed text
st.write('### Transformed Text')
st.write(transformed_text)

# Multiply the number by 2 and display the result
result = number * 2
st.write(f'### The number {number} multiplied by 2 is {result}')

# Concluding remarks
st.write("""
This app is a simple demonstration of how you can use Streamlit to create 
interactive applications with user inputs and display the results dynamically.
""")