import PyPDF2

def main():
    """
    main loops through an econ test bank file, parses the contents, and writes it to econ.txt.
    """

    # Open the PDF file in read-binary mode
    pdf_file = open("test_test_test_bank.pdf.pdf", "rb")

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    f = open('econ.txt', 'w')

    # Iterate through all the pages
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        lines = text.split("\n")
        objective = False
        for line in lines:
            if line.startswith("Chapter 4"):
                break
            if (len(line) < 3):
                continue
            if ((line[0].isdigit() and line[1] == ")") or (line[0].isdigit() and line[1].isdigit() and line[2] == ")")):
                print('\n')
            if (objective):
                objective = False
                if not((line[0].isdigit() and line[1] == ")") or (line[0].isdigit() and line[1].isdigit() and line[2] == ")")):
                    continue
            if (line.startswith("Objective")):
                objective = True
            if not(line.startswith("Answer") or line.startswith("Diff") or line.startswith("Skill") or line.startswith("Objective")):
                print(line)
                
        if line.startswith("Chapter 4"):
            break

    # Close the PDF file
    pdf_file.close()

if __name__ == "__main__":
    main()
