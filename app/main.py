import streamlit as st
from services.write_rx.service import generate_response


def main():
    """
    The main function of the Streamlit app that renders the WriteRx Medical Note-Taking App's user interface.
    """

    # Set Streamlit page configuration
    st.set_page_config(
        page_title="WriteRx - Medical Note-Taking App",
        page_icon="🏥",
        layout="centered",
        initial_sidebar_state="collapsed",
    )

    # Page title and subtitle
    st.title("WriteRx - Medical Note-Taking App")
    st.write(
        "An intuitive and efficient medical note-taking app with smart data-entry features, customizable templates, "
        "and automated billing codes."
    )

    # Instructions expander
    with st.expander("Instructions"):
        st.write(
            """
            1. Enter the patient's Chief Complaint in the mandatory field.
            2. Click on the "OLDCART" expander and fill in any relevant information.
            3. Click on the "Generate Medical Note" button to create a well-structured medical note in the SOAP format.
            4. The generated note will appear below the button.
            """
        )

    # Input fields
    st.write("## Enter your medical notes")

    # 1. Chief Complaint (Mandatory)
    chief_complaint = st.text_input("1. Chief Complaint (Mandatory):")

    # OLDCART subsection
    st.subheader("OLDCART")
    with st.expander("Click to expand"):

        # 2a. Onset
        onset = st.text_input("2a. Onset:")

        # 2b. Location
        location = st.text_input("2b. Location:")

        # 2c. Duration
        duration = st.text_input("2c. Duration:")

        # 2d. Characteristics
        characteristics = st.text_input("2d. Characteristics:")

        # 2e. Aggravated By
        aggravated_by = st.text_input("2e. Aggravated By:")

        # 2f. Relieved By
        relieved_by = st.text_input("2f. Relieved By:")

        # 2g. Therapeutics
        therapeutics = st.text_input("2g. Therapeutics:")

    # Generate Medical Note button
    if st.button("Generate Medical Note"):

        # Check if Chief Complaint is provided
        if chief_complaint:

            # Generate the medical note using the provided information
            prompt = f"Generate a SOAP format medical note for the following patient information: Chief Complaint: {chief_complaint}, Onset: {onset}, Location: {location}, Duration: {duration}, Characteristics: {characteristics}, Aggravated By: {aggravated_by}, Relieved By: {relieved_by}, Therapeutics: {therapeutics}"
            response = generate_response(prompt)

            # Display the generated medical note
            st.success("Medical Note generated successfully!")
            st.write("## Generated Medical Note in SOAP Format")
            st.write(response)

        # Display a warning message if Chief Complaint is missing
        else:
            st.warning("Please enter a Chief Complaint before generating the note.")


if __name__ == "__main__":
    main()
