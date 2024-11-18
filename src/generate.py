from fpdf import FPDF
import uuid
import os

def generate_pdf(response, file_path):
    """Generate a PDF file with the given response text."""
    try:
        # Create a PDF object
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        # Title: Change color and font style
        pdf.set_font("Arial", 'B', 18)  # Bold font with size 18 for the title
        pdf.set_text_color(0, 102, 204)  # Blue color for the title text
        pdf.cell(200, 10, txt="Answer to the Question", ln=True, align="C")  # Centered title

        pdf.ln(10)  # Add space after the title

        # Response Body: Change color and font style
        pdf.set_font("Arial", size=12)  # Normal font for the body
        pdf.set_text_color(0, 0, 0)  # Black color for the text

        # Titles and corresponding body text
        titles_and_responses = [
            ("Average Delay:", "394.56 minutes (approximately 6.57 hours)"),
            ("Response Body:", response),  # This can be any text passed as a response
            ("Next Title:", "Here is another section of content that follows the previous section.")
        ]

        for title, content in titles_and_responses:
            # Set the title in bold
            pdf.set_font("Arial", 'B', 12)  # Set bold font for the title
            pdf.multi_cell(0, 10, title)  # Print the title in bold

            # Set the content in normal font
            pdf.set_font("Arial", '', 12)  # Set normal font for the content
            pdf.multi_cell(0, 10, content)  # Print the content of the response

            pdf.ln(5)  # Add some space between sections

        # Add a footer with different text
        pdf.ln(10)  # Add space for the footer
        pdf.set_font("Arial", 'I', 10)  # Italic font for the footer
        pdf.set_text_color(128, 128, 128)  # Gray color for footer text
        pdf.cell(200, 10, txt="This document was generated automatically.", ln=True, align="C")

        # Save the file to the given path
        pdf.output(file_path)
        return file_path  # Return the path where the PDF was saved

    except Exception as e:
        print(f"Error generating PDF: {e}")
        return None  # Return None in case of an error

def generate_pdf_and_save(answer):
    """Create a PDF and save it in the 'responses' folder with sequential filenames."""
    try:
        # Ensure the 'responses' directory exists
        if not os.path.exists("responses"):
            os.makedirs("responses", exist_ok=True)  # Avoid error if folder already exists

        # Get the list of existing PDF files in the 'responses' directory
        existing_files = [f for f in os.listdir("responses") if f.startswith("response_") and f.endswith(".pdf")]

        # Generate the next sequential number for the filename
        next_index = len(existing_files) + 1
        unique_filename = f"responses/response_{next_index:02d}.pdf"  # Formats as response_01.pdf, response_02.pdf, etc.

        # Generate and save the PDF
        generated_pdf_path = generate_pdf(answer, unique_filename)

        if generated_pdf_path:
            return generated_pdf_path  # Return the path of the saved PDF
        else:
            print("Failed to generate PDF.")
            return None  # In case of failure

    except Exception as e:
        print(f"Error saving PDF: {e}")
        return None  # Return None if there was an error in the process
