import streamlit as st

def main():
    st.title("Uno Reverse Project Details")
    
    # Textbox for entering the title
    title = st.text_input("Enter Title")
    
    # Textbox for entering the target industry
    target_industry = st.text_input("Enter Target Industry")
    
    # Textbox for entering the problems solved
    problems_solved = st.text_area("Enter Problems Solved", height=200)
    
    if st.button("Submit"):
        # You can add your backend logic here to process the input data
        # For example, you can save the input data to a database or perform calculations
        
        # Display the input data for confirmation
        st.write("Title:", title)
        st.write("Target Industry:", target_industry)
        st.write("Problems Solved:", problems_solved)

if __name__ == "__main__":
    main()
