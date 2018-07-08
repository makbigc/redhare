from table import ResultTable
from exception import MatchNotFoundError


def ensure_match_held(date, venue):
    for i in range(20):
        result_tbl = ResultTable(date, venue, '1')
        if result_tbl.is_valid_link():
            return True

    raise MatchNotFoundError(date, venue)


def get_result_tbl(date, venue, race_no):

    while True:
        result_tbl = ResultTable(date, venue, race_no)
        if result_tbl.is_valid_link():
            return result_tbl


def capture_result(date, venue):
    ensure_match_held(date, venue)

    first_table = get_result_tbl(date, venue, '1')
    no_of_race = first_table.get_no_of_race()

    tables = [get_result_tbl(date, venue, str(i))
              for i in range(1, no_of_race+1)]

    for table in tables:
        output_string = 'Date:{}\tVenue:{}\tRace No.:{}'
        print(output_string.format(table.date, table.venue, table.race_no))
        table.print_result()
