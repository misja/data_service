import json
from flask import Flask, request, jsonify, render_template
from filter import filter_place, filter_year, filter_magnitude

app = Flask(__name__)


def get_events():
    """Read and return earthquake events"""
    with open("all_induced.json") as file:
        data = json.load(file)
    return data["events"]


@app.route("/")
def index():
    events = get_events()  # all events
    total = len(events)  # number of events
    return render_template("index.html", total=total)


@app.route("/filter")
def filter():
    events = get_events()  # all events
    kwargs = request.args.to_dict()  # request query parameters as dictionary

    for filter in [filter_magnitude, filter_place, filter_year]:
        events = filter(events, **kwargs)

    result = {"events": events}

    return jsonify(result)  # return filtered events


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
