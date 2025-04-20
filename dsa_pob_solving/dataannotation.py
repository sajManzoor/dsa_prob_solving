import requests
from bs4 import BeautifulSoup

def fetch_google_doc_table_content(url):
    url = url + "?output=html"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')

        if not table:
            return "No table found in the document."

        rows = table.find_all('tr')
        table_data = []

        for row in rows[1:]:  # skip header
            columns = row.find_all('td')

            if len(columns) == 3:  # 3 column check
                # Extract the x-coordinate, character, and y-coordinate
                x_coord = int(columns[0].get_text(strip=True))
                character = columns[1].get_text(strip=True)
                y_coord = int(columns[2].get_text(strip=True))

                table_data.append((x_coord, character, y_coord))

        return table_data
    else:
        return f"Error: {response.status_code}"


def print_code(table_data):
    max_x = max([x for x, _, _ in table_data])
    max_y = max([y for _, _, y in table_data])

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, character, y in table_data:
        grid[max_y - y][x] = character

    for row in grid:
        print(''.join(row))

def main():
    doc_url = 'https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub'

    table_data = fetch_google_doc_table_content(doc_url)

    if isinstance(table_data, str) and table_data.startswith("Error"):
        print(table_data)
    else:
        print_code(table_data)

if __name__ == '__main__':
    main()
