#%%
import requests
from xml.etree import ElementTree


class OptaAPI:
    def __init__(self, outletAuthKey, response_format="json"):
        self.baseURL = "http://api.performfeeds.com"
        self.feedResource = "soccerdata"
        self.format = response_format
        self.operatingMode = "b"
        self.outletAuthKey = outletAuthKey

    def _url(self, feed, *route, **params):
        return "{base}/{feedResource}/{feed}/{outletKey}/{route}".format(
            base=self.baseURL,
            feedResource=self.feedResource,
            feed=feed,
            outletKey=self.outletAuthKey,
            route="/".join(str(r) for r in route)
        )

    def _parse_response(self, response):
        if self.format == "json":
            return response.json()
        if self.format == "xml":
            return ElementTree.fromstring(response.content)

    def _get_feed_data(self, feed, *route, **params):
        params["_rt"] = self.operatingMode
        params["_fmt"] = self.format

        r = requests.get(self._url(feed, *route), params=params)
        return self._parse_response(r)

    # StatsPerform functions

    def get_tournament_calendar(self, *route):
        """(OT2) Get basic information about the tournament calendars - the individual seasons/editions of a competition.
        https://documentation.statsperform.com/docs/data/reference/soccer/opta-sdapi-soccer-api-tournament-calendars.htm

        Args:
            route (str): Use /active and /authorized endpoints

        Returns:
            str: Tournament id for 3F Superliga (the only tournament we have access to)
        """

        return self._get_feed_data("tournamentcalendar", *route)

    def get_tournament_schedule(self, tmcl=None):
        """(MA0) Get schedule information for a tournament, including individual matches split by day, including the coverage level for a match.
        https://documentation.statsperform.com/docs/data/reference/soccer/opta-sdapi-soccer-api-tournament-schedule.htm

        Args:
            tmcl (str): str: Tournament id for 3F Superliga (the only tournament we have access to)

        Returns:
            json: tournament information, including individual matches split by day
        """
        return self._get_feed_data("tournamentschedule", tmcl=tmcl)

    def get_fixtures(self, fx=None, tmcl=None, stg=None, comp=None, lineups=None, live=None):
        """(MA1) Get a fixture or fixture list with match details, such as date, start time, contestants, competition, season, score, result and lineups.

        Kwargs:
            fx (str, list): GET detailed information about one fixture or multiple fixtures.
            tmcl (str): GET information about fixtures and results only for the specified tournament calendar. Pass the tournament calendar UUID to the tmcl parameter.
            stg (str): GET information about fixtures and results only for a specific stage of a tournament calendar. Pass the stage UUID to the stg parameter
            comp (str): GET information about fixtures and results only for a specific competition. Pass the competition UUID to the comp parameter - you can pass one or up to 50 competition UUIDs in a comma-separated list.
            lineups (str): GET only lineups information (including substitutes) for contestants in fixtures - you must use this parameter in combination with the live parameter with a value of yes.
                           The available values for the live and lineups parameters are: no (default) and yes.
            live (str): GET live data (such as score, goals, cards, attendance, officials, and more) for fixtures. The available values for the live parameter are: no (default) and yes

        Returns:
            json: match details, such as date, start time, contestants, competition, season, score, result and lineups
        """
        return self._get_feed_data("match", fx=fx, tmcl=tmcl, stg=stg, comp=comp, lineups=lineups, live=live)

    def get_match_stats(self, fx=None):
        """(MA2) Get detailed match statistics for teams and each individual player, including passes, shots, crosses, tackles and more.

        Kwargs:
            fx (str): ID from a specific fixture.

        Returns:
            json: match statistics for teams and each individual player
        """
        return self._get_feed_data("matchstats", fx=fx)

    def get_events(self, fx=None, ctst=None, prsn=None, type=None):
        """(MA3) Get all events in a game - including the player, team, event, type, time (minute and second) - and qualifiers for each action.

        Kwargs:
            fx (str): Get match events for a match by the specified fixture UUID (query parameter method). Pass the fixture UUID to the fx parameter.
            ctst (str): Get match events only for the specified contestant in the fixture. Pass the contestant UUID to the ctst parameter.
            prsn (str): Get match events only for a specific person in the fixture. Pass the person UUID to the prsn parameter.
            type (str): Get match events only of a specific event type(s) in the fixture, such as shots, goals, and crosses.
                        Pass the event type ID(s) to the type parameter. You can specify multiple event typeId values to the type parameter in a comma-separated list (up to a maximum of 20 values)

        Returns:
            json: match events - including the player, team, event, type, time (minute and second) and qualifiers for each action
        """
        return self._get_feed_data("matchevent", fx=fx, ctst=ctst, prsn=prsn, type=type)

    def get_match_xg(self, fx=None):
        """(MA12) Get shot, 'expected goals' and 'expected goals on target' data, cumulative player and team totals, and general match details.

        Kwargs:
            fx (str): Get match information only for the specified fixture. Pass the fixture UUID to the fx parameter.

        Returns:
            json: match expected goals - including shot location, expected goals on target, team totals and more
        """
        return self._get_feed_data("matchexpectedgoals", fx=fx)

    def get_season_xg(self, **params):
        """(TM9) Get shot information, 'expected goals' and 'expected goals on target' data, cumulative player and team totals, in any match.

        Kwargs:
            comp + ctst (str): Get season expected goals for a specific contestant in a competition (of a competition). Pass the contestant UUID to the ctst parameter, and competition UUID to the comp parameter.
            tmcl + ctst (str): Get season expected goals only for a specific contestant in a tournament calendar (of a competition). Pass the contestant UUID to the ctst parameter, and tournament calendar UUID to the tmcl parameter.

        Returns:
            json: shot information, 'expected goals' and 'expected goals on target' data, cumulative player and team totals, in any match
        """
        return self._get_feed_data("seasonexpectedgoals", **params)

    def get_teams(self, ctry=None, ctst=None, tmcl=None, stg=None, srs=None):
        """(TM1) Get team details of all contestants within a specified tournament calendar or details for a single contestant.

        Kwargs:
            ctry (str): Get team information only for a specific country. Pass the contestant UUID to the ctry parameter.
            ctst (str): Get team information only for a specific contestant. Pass the contestant UUID to the ctst parameter.
            tmcl (str): Get team information only for the specified tournament calendar. Pass the tournament calendar UUID to the tmcl parameter.
            stg (str): Get team information only for a specific stage. Pass the stage UUID to the stg parameter.
            srs (str): Get team information only for a specific series. Pass the series UUID to the srs parameter.
            detailed (str): yes or no

        Returns:
            json: team details
        """
        return self._get_feed_data("team", ctry=ctry, ctst=ctst, tmcl=tmcl, stg=stg, srs=srs)

    def get_standings(self, tmcl=None):
        """(TM2) Get data to create a league table - position, points, matches won/lost/drawn, goals scored and conceded, and goal difference.

        Kwargs:
            tmcl (str): GET team standings information only for the specified tournament calendar. Pass the tournament calendar UUID to the tmcl parameter.

        Returns:
            json : position, points, matches won/lost/drawn, goals scored and conceded, and goal difference.
        """
        return self._get_feed_data("standings", tmcl=tmcl)

    def get_season_stats(self, **params):
        """(TM4) Get cumulative performance statistics for every player that has made an appearance in the specified tournament calendar.

        Kwargs:
            comp + ctst (str): Get seasonal statistics for a specific contestant in a competition (of a competition). Pass the contestant UUID to the ctst parameter, and competition UUID to the comp parameter.
            tmcl + ctst (str): Get seasonal statistics only for a specific contestant in a tournament calendar (of a competition). Pass the contestant UUID to the ctst parameter, and tournament calendar UUID to the tmcl parameter.
            detailed (str): yes or no

        Returns:
            json: performance statistics for every player
        """
        return self._get_feed_data("seasonstats", **params)
