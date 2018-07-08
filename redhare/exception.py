class MatchNotFoundError(Exception):
    def __init__(self, date, venue):
        self.date = date
        self.venue = venue
        msg = "The link is not ready. No match held on %s in %s" % (date, venue)
        super().__init__(msg)
