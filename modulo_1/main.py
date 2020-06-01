from datetime import datetime

records = [
    {
        "source": "48-996355555",
        "destination": "48-666666666",
        "end": 1564610974,
        "start": 1564610674,
    },
    {
        "source": "41-885633788",
        "destination": "41-886383097",
        "end": 1564506121,
        "start": 1564504821,
    },
    {
        "source": "48-996383697",
        "destination": "41-886383097",
        "end": 1564630198,
        "start": 1564629838,
    },
    {
        "source": "48-999999999",
        "destination": "41-885633788",
        "end": 1564697158,
        "start": 1564696258,
    },
    {
        "source": "41-833333333",
        "destination": "41-885633788",
        "end": 1564707276,
        "start": 1564704317,
    },
    {
        "source": "41-886383097",
        "destination": "48-996384099",
        "end": 1564505621,
        "start": 1564504821,
    },
    {
        "source": "48-999999999",
        "destination": "48-996383697",
        "end": 1564505721,
        "start": 1564504821,
    },
    {
        "source": "41-885633788",
        "destination": "48-996384099",
        "end": 1564505721,
        "start": 1564504821,
    },
    {
        "source": "48-996355555",
        "destination": "48-996383697",
        "end": 1564505821,
        "start": 1564504821,
    },
    {
        "source": "48-999999999",
        "destination": "41-886383097",
        "end": 1564610750,
        "start": 1564610150,
    },
    {
        "source": "48-996383697",
        "destination": "41-885633788",
        "end": 1564505021,
        "start": 1564504821,
    },
    {
        "source": "48-996383697",
        "destination": "41-885633788",
        "end": 1564627800,
        "start": 1564626000,
    },
]

CALL_RATE = 0.36

# create phone bill and ordenate by higher values


def classify_by_phone_number(records):
    phone_bill = []
    phone_calls = []
    for call in records:
        if call["source"] not in phone_calls:
            phone_calls.append(call["source"])
    for number in phone_calls:
        rate = 0
        total_rate = 0
        for each_record in records:
            if each_record["source"] == number:
                rate = phone_rates(each_record)
                if isinstance(rate, float):
                    total_rate += rate
                    total_rate = round(total_rate, 2)

        phone_bill.append({"source": number, "total": total_rate})
        phone_bill = sorted(phone_bill, key=lambda k: k["total"], reverse=True)
    return phone_bill


# calculate call rates between ranges in daytime, night or mixed periods


def phone_rates(item):

    total_time = item["end"] - item["start"]
    get_start_date = datetime.fromtimestamp(item["start"])
    get_end_date = datetime.fromtimestamp(item["end"])
    start_date = datetime.date(get_start_date)
    end_date = datetime.date(get_end_date)

    if start_date == end_date:
        if get_start_date.hour >= 6 and get_end_date.hour < 22:
            daytime_rate = ((total_time // 60) * 0.09) + CALL_RATE
            rate = round(daytime_rate, 2)
            return rate

        elif (get_start_date.hour >= 0 and get_end_date.hour < 6) or (
            get_start_date.hour >= 22 and get_end_date.hour <= 23
        ):
            nightly_rate = (total_time * 0) + CALL_RATE
            rate = round(nightly_rate, 2)
            return rate

        elif (
            get_start_date.hour >= 6
            and get_end_date.hour >= 22
            and get_end_date.hour <= 23
        ):
            reset_end_hour = get_end_date.replace(hour=22, minute=0, second=0)
            night_until_ten_rate = (
                round((reset_end_hour - get_start_date).total_seconds() / 60) * 0.09
            )
            mixed_call_rate = night_until_ten_rate + 0.36
            rate = round(mixed_call_rate, 2)
            return rate

        elif (
            get_start_date.hour >= 22
            or get_start_date.hour < 6
            and get_end_date.hour >= 6
            or get_end_date.hour < 22
        ):
            reset_start_hour = get_start_date.replace(hour=6, minute=0, second=0)
            hour_from_six = (
                round((reset_start_hour - get_end_date).total_seconds() / 60) * 0.09
            )
            mixed_call_rate = hour_from_six + 0.36
            rate = round(mixed_call_rate, 2)
            return rate
