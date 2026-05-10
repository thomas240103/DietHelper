from datetime import datetime
from math import asin, cos, radians, sin, sqrt
from pathlib import Path
import xml.etree.ElementTree as ET

from .models import RunTrackPoint


def import_activity_file(run):
    if not run.activity_file:
        return

    suffix = Path(run.activity_file.name).suffix.lower()
    if suffix == ".gpx":
        import_gpx(run)


def import_gpx(run):
    path = run.activity_file.path
    tree = ET.parse(path)
    root = tree.getroot()
    namespace = {"gpx": root.tag.split("}")[0].strip("{")} if "}" in root.tag else {}
    point_path = ".//gpx:trkpt" if namespace else ".//trkpt"
    points = root.findall(point_path, namespace)

    RunTrackPoint.objects.filter(run=run).delete()

    previous = None
    total_distance = 0
    start_time = None

    for index, point in enumerate(points):
        lat = float(point.attrib["lat"])
        lon = float(point.attrib["lon"])
        elevation = _find_text(point, "ele", namespace)
        raw_time = _find_text(point, "time", namespace)
        parsed_time = _parse_time(raw_time) if raw_time else None

        if previous:
            total_distance += _distance_km(previous[0], previous[1], lat, lon)
        if parsed_time and start_time is None:
            start_time = parsed_time

        seconds_from_start = 0
        if parsed_time and start_time:
            seconds_from_start = int((parsed_time - start_time).total_seconds())

        RunTrackPoint.objects.create(
            run=run,
            index=index,
            distance_km=round(total_distance, 3),
            elevation_m=round(float(elevation), 2) if elevation else None,
            seconds_from_start=max(seconds_from_start, 0),
        )
        previous = (lat, lon)


def _find_text(element, name, namespace):
    query = f"gpx:{name}" if namespace else name
    child = element.find(query, namespace)
    return child.text if child is not None else None


def _parse_time(value):
    normalized = value.replace("Z", "+00:00")
    return datetime.fromisoformat(normalized)


def _distance_km(lat1, lon1, lat2, lon2):
    radius_km = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    return 2 * radius_km * asin(sqrt(a))
