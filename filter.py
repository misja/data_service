from datetime import date


def filter_place(events, place=None, **kwargs):
    """Filter by place name

    Returns events filtererd by case insensitive place match.
    """
    places = []
    if place != None:
        for x in events:
            location = x['place']
            if place.lower() in location.lower():
                places += [x]
        return places
    return events  # just return all events for now ...

def filter_year(events, min_year=None, max_year=None, **kwargs):
    """Filter by year

    Returns events filtered by year (inclusive).
    """
    events_year = []

    if min_year:
        min_year = int(min_year)
    if max_year:
        max_year = int(max_year)

    if not min_year or not max_year:
        return events

    for event in events:
        year = event["date"]

        year = int(year[:4])

        if min_year and year < min_year:
            continue

        if max_year and year > max_year:
            continue

        events_year.append(event)

    return events_year


def filter_magnitude(events, min_mag=None, max_mag=None, **kwargs):
    """Filter by magnitude

    Returns data entries filtered by magnitude (inclusive).
    """
    data = []

    if min_mag == None:
        min_mag = 0.0
    if max_mag == None:
        max_mag = 99.9

    for event in events:
        if float(event["mag"]) >= float(min_mag) and float(event["mag"]) <= float(max_mag):
            data.append(event)

    return data  # just return all events for now ...



