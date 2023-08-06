from fpdf import FPDF


class FileGenerator:
    '''
    Class for handling file generation from given path
    '''
    def __init__(self, pdf_path, html_path, data):
        if all([pdf_path, html_path]):
            raise AttributeError('You need to specify only 1 file path')
        
        self.pdf_path = pdf_path
        self.html_path = html_path
        self.data = data

    def write_html(self):
        '''
        Method for generating html file
        '''
        with open(self.html_path, 'w') as f:
            result = f'<h2>{self.data["Feed"]}</h2>'
            for entry in self.data['Entries']:
                result += f'''
                <div>
                <p>Title: {entry['Title']}</p>
                <p>Date: {entry['Date']}</p>
                <p>Link: <a href="{entry['Link']}">Link</a></p>
                </div>
                '''
            f.write(result)

    def write_pdf(self):
        '''
        Method for generating pdf file
        '''
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 15)
        pdf.cell(200, 10, txt=self.data['Feed'], ln=1, align='C')

        line_counter = 3

        for entry in self.data['Entries']:
            for key, item in entry.items():
                if key == 'Link':
                    continue
                txt = f'{key}: {item}'.encode('latin-1')
                pdf.cell(200, 10, txt=txt, ln=line_counter, align='L')
                line_counter += 1
            line_counter += 1

        pdf.output(self.pdf_path)

    def generate(self):
        '''
        Client interface method that controls format of generated file
        '''
        print(self.pdf_path)
        if self.pdf_path:
            self.write_pdf()
        else:
            self.write_html()
