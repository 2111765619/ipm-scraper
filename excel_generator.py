import pandas as pd

class ExcelGenerator:
    def __init__(self, data):
        self.data = data

    def generate_excel(self, file_name='trademark_data.xlsx'):
        df = pd.DataFrame(self.data)
        df.to_excel(file_name, index=False)

# Sample trademark data, replace with actual data as needed
trademark_data = [
    {'Application Date': '2021-01-01', 'Class': '25', 'Owner Name Persian': 'مالک 1', 'Owner Name English': 'Owner 1', 'Agent': 'Agent 1', 'Nationality': 'Iran', 'Mark-Logo': 'logo1.png', 'Mark in Latin': 'mark1', 'Mark in Persian': 'مارک 1', 'Text - full trademark clipping': 'Trademark Clip 1', 'Language Of The Mark': 'Persian'},
    {'Application Date': '2021-02-01', 'Class': '25', 'Owner Name Persian': 'مالک 2', 'Owner Name English': 'Owner 2', 'Agent': 'Agent 2', 'Nationality': 'Iran', 'Mark-Logo': 'logo2.png', 'Mark in Latin': 'mark2', 'Mark in Persian': 'مارک 2', 'Text - full trademark clipping': 'Trademark Clip 2', 'Language Of The Mark': 'Persian'}
]

if __name__ == '__main__':
    excel_generator = ExcelGenerator(trademark_data)
    excel_generator.generate_excel()