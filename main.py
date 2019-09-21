import sys
from database_tools import connect_to_database
from site_parser import parse_page

url_parse = "https://minecraft-inside.ru/mods/page/1/"


if len(sys.argv) == 1:
    print("Enter your password: <script_name> <password>")
    exit(1)
else:
    connect_to_database(sys.argv[1])

if __name__ == '__main__':
    parse_page(url_parse)