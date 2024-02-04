import os
import PyPDF2

def get_pdf_page_counts(directory):
    pdf_data = []
    error_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'rb') as pdf_file:
                    pdf_reader = PyPDF2.PdfReader(pdf_file)
                    num_pages = len(pdf_reader.pages)
                    pdf_data.append((filename, num_pages))
            except Exception as e:
                error_files.append((filename, str(e)))  
                print(f"Error processing {filename}: {e}")

    sorted_data = sorted(pdf_data, key=lambda x: x[1])
    create_error_report(error_files)  
    return sorted_data

def create_txt_report(sorted_data, output_filename="pdf_page_counts.txt"):
    with open(output_filename, "w", encoding="utf-8") as output_file:
        output_file.write("PDF Page Counts:\n\n")
        output_file.write("----\n")  
        for filename, num_pages in sorted_data:
            output_file.write(f"•  {filename:<23} {num_pages} pages\n")
            output_file.write("----\n")  
        output_file.write(f"\n{len(sorted_data)} files processed.\n") 

def create_error_report(error_files, output_filename="error_report.txt"):
    with open(output_filename, "w", encoding="utf-8") as output_file:
        output_file.write("Error Report:\n\n")
        output_file.write("----\n")  
        for filename, error_message in error_files:
            if "incorrect startxref pointer" in error_message or "PdfReadError" in error_message:
                output_file.write(f"•  {filename}: {error_message}\n")
                output_file.write("----\n") 
            else:
                output_file.write(f"•  {filename}: {error_message}\n")
                output_file.write("----\n") 
			
if __name__ == "__main__":
    directory = "Books" 
    sorted_data = get_pdf_page_counts(directory)
    create_txt_report(sorted_data)