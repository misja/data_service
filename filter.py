from datetime import date


def filter_place(events, place=None, **kwargs):
    """Filter by place name

    Returns events filtererd by case insensitive place match.
    """
    # TODO create an empty list for adding filtered events

    # TODO if place is not None, loop through all events (else just return all events)

    # TODO if event location contains place, add event to list

    # TODO and return the list of filtered items

    return events  # just return all events for now ...


def filter_year(data, min_year=None, max_year=None, **kwargs):
    """Filter by year

    Returns events filtered by year (inclusive).
    """
    # TODO create an empty list for adding filtered events

    # TODO if min_year and/or max_year are not None, convert to int

    # TODO loop through all events

    # TODO for each event, get the year as integer

    # TODO for each event, check min_year and max_year (if not None) against year and if valid add to list

    # TODO and return the list of filtered events

    return data  # just return all events for now ...


def filter_magnitude(events, min_mag=None, max_mag=None, **kwargs):
    """Filter by magnitude

    Returns data entries filtered by magnitude (inclusive).
    """
    # TODO create an empty list for adding filtered events

    # TODO if min_mag and/or max_mag are not None, convert to float

    # TODO loop through all events

    # TODO for each event, get the magnitude as float

    # TODO for each event, check min_mag and max_mag (if not None) against event magnitude and if valid add to list

    # TODO and return the list of filtered events

    return events  # just return all events for now ...
