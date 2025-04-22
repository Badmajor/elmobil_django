import os.path
import re
import sqlite3

from bs4 import BeautifulSoup, Comment
from django.core.exceptions import FieldError
from django.core.management import BaseCommand
from django.db import models

from catalog.models import (
    AccelerationTo,
    ArchitectureBattery,
    Battery,
    BatteryType,
    Car,
    CarBody,
    Charging,
    Cathode,
    Drive,
    DimensionsWeight,
    Manufacturer,
    Miscellaneous,
    NominalVoltage,
    PackConfiguration,
    RangeEstimation,
    Performance,
    Platform,
    PortCharge,
    PortLocation,
    Segment,
    TypeElectric,
)

from catalog.management.commands.utils import normalize_time, normalize_data


def get_dict_from_soup(block: BeautifulSoup) -> dict:
    data = {}
    if block:
        tables = block.find_all("table")
        for table in tables:
            rows = table.find_all("tr")
            for row in rows:
                cells = row.find_all("td")
                if len(cells) == 2:
                    key = cells[0].text.strip()
                    value = cells[1].text.strip()
                    data[key] = value
    return normalize_data(data)


def yes_no_bool(string):
    if "yes" in string.lower():
        return True
    elif "no" in string.lower():
        return False
    return None


def get_dict_into_block_without_id(soup, string):
    block = soup.find("h2", string=string).find_parent("div", class_="data-table")
    if not block:
        return None
    data = {}
    if block:
        tables = block.find_all("table")
        for table in tables:
            rows = table.find_all("tr")

            for row in rows:
                cells = row.find_all("td")
                if len(cells) == 2:
                    key = cells[0].text.strip()
                    value = cells[1].text.strip()
                    data[key] = value
    return normalize_data(data)


def _get_or_create_obj(klass: models.Model, value):
    if value and ("No" not in value) and ("-" not in value):
        try:
            obj, _ = klass.objects.get_or_create(title=value)
            return obj
        except FieldError:
            obj, _ = klass.objects.get_or_create(time=value)
            return obj
    return


def _get_or_create_segment(value):
    if value:
        char_class, title = value.split(" - ")
        obj, _ = Segment.objects.get_or_create(title=title, char_class=char_class)
        return obj
    return


def _check_digit_and_split(value):
    if value:
        value = value.replace(",", "").split(" ")[0]
        try:
            float(value)
            return value
        except ValueError:
            return


def update_html_code(path_db, id_car):
    query = """
    UPDATE pages_code
    SET is_added = 1
    WHERE id_car = ?
    """
    with sqlite3.connect(path_db) as conn:
        cursor = conn.cursor()
        cursor.execute(query, (id_car,))
        conn.commit()


def _get_html_code(path_db):
    query = """
    SELECT id_car, code_page
    FROM pages_code
    WHERE is_added = 0
    ORDER BY id_car
    LIMIT 1
    """
    with sqlite3.connect(path_db) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
    return data


def _get_manufacturer(title):
    manufacturer = title.split(" ")[0]
    obj, _ = Manufacturer.objects.get_or_create(title=manufacturer)
    return obj


def _get_drive(value):
    if value:
        obj, _ = Drive.objects.get_or_create(title=value)
        return obj
    return


def _get_performance(performance_block: BeautifulSoup):
    data = get_dict_from_soup(performance_block)
    acceleration_to_100 = _get_or_create_obj(
        AccelerationTo, _check_digit_and_split(data.get("Acceleration 0 - 100 km/h"))
    )
    drive = _get_drive(data.get("Drive"))
    obj, _ = Performance.objects.get_or_create(
        acceleration_to_100=acceleration_to_100,
        top_speed=_check_digit_and_split(data.get("Top Speed")),
        electric_range=_check_digit_and_split(data.get("Electric Range")),
        total_power=_check_digit_and_split(data.get("Total Power")),
        total_torque=_check_digit_and_split(data.get("Total Torque")),
        drive=drive,
    )
    return obj


def _get_battery(block: BeautifulSoup):
    data = get_dict_from_soup(block)
    obj, _ = Battery.objects.get_or_create(
        nominal_capacity=_check_digit_and_split(data.get("Nominal Capacity")),
        usable_capacity=_check_digit_and_split(data.get("Useable Capacity")),
        battery_type=_get_or_create_obj(BatteryType, data.get("Battery Type")),
        number_of_cells=_check_digit_and_split(data.get("Number of Cells")),
        architecture=_get_or_create_obj(
            ArchitectureBattery, _check_digit_and_split(data.get("Architecture"))
        ),
        cathode=_get_or_create_obj(Cathode, data.get("Cathode Material")),
        pack_configuration=_get_or_create_obj(
            PackConfiguration, data.get("Pack Configuration")
        ),
        nominal_voltage=_get_or_create_obj(
            NominalVoltage, _check_digit_and_split(data.get("Nominal Voltage"))
        ),
        warranty_period=_check_digit_and_split(data.get("Warranty Period")),
        warranty_mileage=_check_digit_and_split(data.get("Warranty Mileage")),
    )
    return obj


def _get_charging(block: BeautifulSoup):
    data = get_dict_from_soup(block)
    if charge_power_type := data.pop("Charge Power"):
        charge_power = charge_power_type.split(" ")[0]
        type_electric = _get_or_create_obj(
            TypeElectric, charge_power_type.split(" ")[-1]
        )
    else:
        charge_power, type_electric = (None, None)
    charge_speed = _check_digit_and_split(data.get("Charge Speed"))
    charge_time = None
    for key, value in data.items():
        if "Charge Time " in key:
            charge_time = normalize_time(value)
            break
    type_port = _get_or_create_obj(PortCharge, data.get("Charge Port"))
    qs = Charging.objects.filter(
        type_port=type_port,
        charge_power=charge_power,
        type_electric=type_electric,
        charge_time=charge_time,
        charge_speed=charge_speed,
    )
    port_locations = []
    for key, value in data.items():
        if "Port Location" in key and "FC" not in key:
            value = value.replace("-", "/")
            obj = _get_or_create_obj(PortLocation, value)
            port_locations.append(obj)
            qs.filter(port_location=obj)
    if qs:
        return qs.first()
    charging = Charging.objects.create(
        type_port=type_port,
        charge_power=charge_power,
        type_electric=type_electric,
        charge_time=charge_time,
        charge_speed=charge_speed,
    )
    for port in port_locations:
        charging.port_location.add(port)
    return charging


def _get_charging_fast(block: BeautifulSoup):
    data = get_dict_from_soup(block)
    if charge_power_type := data.get("Fastcharge Power (10-80%)"):
        charge_power = _check_digit_and_split(charge_power_type)
        type_electric = _get_or_create_obj(
            TypeElectric, charge_power_type.split(" ")[-1]
        )
    else:
        charge_power, type_electric = (None, None)
    charge_speed = _check_digit_and_split(data.get("Fastcharge Speed"))
    charge_time = None
    for key, value in data.items():
        if "Fastcharge Time" in key:
            charge_time = normalize_time(value)
            break
    type_port = _get_or_create_obj(PortCharge, data.get("Fastcharge Port"))
    charging_data = dict(
        type_port=type_port,
        charge_power=charge_power,
        type_electric=type_electric,
        charge_time=charge_time,
        charge_speed=charge_speed,
    )
    qs = Charging.objects.filter(**charging_data)
    port_locations = []
    for key, value in data.items():
        if "FC Port Location" in key:
            value = value.replace("-", "/")
            obj = _get_or_create_obj(PortLocation, value)
            port_locations.append(obj)
            qs.filter(port_location=obj)
    if qs:
        return qs.first()
    charging = Charging.objects.create(**charging_data)
    for port in port_locations:
        charging.port_location.add(port)
    return charging


def _get_real_range_estimation(block: BeautifulSoup):
    data = get_dict_from_soup(block)
    obj, _ = RangeEstimation.objects.get_or_create(
        city_cold=data.get("City - Cold Weather").split(" ")[0],
        highway_cold=data.get("Highway - Cold Weather").split(" ")[0],
        combined_cold=data.get("Combined - Cold Weather").split(" ")[0],
        city_mild=data.get("City - Mild Weather").split(" ")[0],
        highway_mild=data.get("Highway - Mild Weather").split(" ")[0],
        combined_mild=data.get("Combined - Mild Weather").split(" ")[0],
    )
    return obj


def _get_dimensions_weight(data: dict):
    obj, _ = DimensionsWeight.objects.get_or_create(
        length=_check_digit_and_split(data.get("Length")),
        width=_check_digit_and_split(data.get("Width")),
        width_with_mirrors=_check_digit_and_split(data.get("Width with mirrors")),
        height=_check_digit_and_split(data.get("Height")),
        wheelbase=_check_digit_and_split(data.get("Wheelbase")),
        weight_unladen=_check_digit_and_split(data.get("Weight Unladen (EU)")),
        gross_weight=_check_digit_and_split(data.get("Gross Vehicle Weight (GVWR)")),
        payload=_check_digit_and_split(data.get("Max. Payload")),
        cargo_volume=_check_digit_and_split(data.get("Cargo Volume")),
        cargo_volume_frunk=_check_digit_and_split(data.get("Cargo Volume Frunk")),
        tow_hitch=yes_no_bool(data.get("Tow Hitch Possible")),
    )
    return obj


def _get_miscellaneous(data: dict):
    isofix_count = None
    isofix_data = data.get("Isofix").split(", ")
    isofix = yes_no_bool(isofix_data[0])
    if len(isofix_data) > 1:
        isofix_count = _check_digit_and_split(isofix_data[1])
    obj, _ = Miscellaneous.objects.get_or_create(
        seats=data.get("Seats").split(" ")[0],
        isofix=isofix,
        isofix_count=isofix_count,
        turning_circle=_check_digit_and_split(data.get("Turning Circle")),
        platform=_get_or_create_obj(Platform, data.get("Platform")),
        car_body=_get_or_create_obj(CarBody, data.get("Car Body")),
        segment=_get_or_create_segment(data.get("Segment")),
        roof_rails=yes_no_bool(data.get("Roof Rails")),
        special_ev_platform=yes_no_bool(data.get("EV Dedicated Platform")),
    )
    return obj


def _get_article_related_car(comment, article=None):
    html_block = comment.find_next("a")
    match = re.search(r"/car/(\d+)", html_block.prettify())
    if match:
        article = match.group(1)
    return article


def _get_previous_car(soup, previous_car_article=None, preceding_car=None):
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    for comment in comments:
        if "section news" in comment:
            previous_car_article = _get_article_related_car(comment)
    if previous_car_article:
        if Car.objects.filter(article=previous_car_article).exists():
            preceding_car = Car.objects.get(article=previous_car_article)
    return preceding_car


def _get_data_car(html_page, article):
    html_page = html_page.decode("utf-8").replace(
        "<td>Fastcharge Time", "<tr><td>Fastcharge Time"
    )
    soup = BeautifulSoup(html_page, "html.parser")
    header = soup.find("header", class_="sub-header")
    years = re.sub(r"[a-zA-Z\s]", "", header.find("span").text)
    if len(years.split("-")) > 1:
        year_release = years.split("-")[0]
        year_until = years.split("-")[1]
    else:
        year_release = years
        year_until = None
    title = f'{header.find("h1").text}'
    manufacturer = _get_manufacturer(title)
    battery = _get_battery(soup.find("div", class_="data-table", id="battery"))
    performance = _get_performance(
        soup.find("div", class_="data-table", id="performance")
    )
    soup_charging = soup.find("div", class_="data-table", id="charging")
    charging = _get_charging(soup_charging)
    charging_fast = _get_charging_fast(soup_charging)
    real_range_estimation = _get_real_range_estimation(
        soup.find("div", class_="data-table", id="range")
    )
    dimensions_weight = _get_dimensions_weight(
        get_dict_into_block_without_id(soup, "Dimensions and Weight")
    )
    miscellaneous = _get_miscellaneous(
        get_dict_into_block_without_id(soup, "Miscellaneous")
    )
    preceding_car = _get_previous_car(soup)
    description = f"""
{title} - это {miscellaneous.segment} разработанный {manufacturer}
на платформе {miscellaneous.platform}
Поколение {year_release}
разгоняется до 100км/ч за {performance.acceleration_to_100} c..
Дальность хода на одном заряде ~ {performance.electric_range} км. """
    return {
        "article": article,
        "title": f"{title} {years}",
        "description": description,
        "manufacturer": manufacturer,
        "performance": performance,
        "battery": battery,
        "charging": charging,
        "charging_fast": charging_fast,
        "real_range_estimation": real_range_estimation,
        "dimensions_weight": dimensions_weight,
        "miscellaneous": miscellaneous,
        "year_release": year_release,
        "year_until": year_until,
        "preceding_car": preceding_car,
    }


class Command(BaseCommand):
    help = "add car"

    def handle(self, *args, **options):
        path_db = os.path.normpath(options["db_path"])
        count = 0
        while data_db := _get_html_code(path_db):
            count += 1
            self.stdout.write(f'{data_db["id_car"]}/{count}')
            data_car = _get_data_car(data_db["code_page"], data_db["id_car"])
            car_instance = Car(**data_car)
            try:
                car_instance.save()
                update_html_code(path_db, data_db["id_car"])
            except Exception as ex:
                self.stdout.write(f"{ex}")
                break
            self.stdout.write(f'{data_db["id_car"]} is added')

    def add_arguments(self, parser):
        parser.add_argument(
            "db_path", type=str, help="Path to the DB with table pages_code(SQLite)"
        )
