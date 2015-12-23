def pre_process(serie):
    if serie.startswith("marvels_daredevil"):
        return serie.replace("marvels_", "")
    elif serie.startswith("marvels_"):
        return serie.replace("marvels", "marvel's")
    elif serie == "the_flash_2014":
        return "the_flash_(2014)"
    elif serie == "mr_robot":
        return "mr._robot"
    elif serie == "house_of_cards_2013":
        return "house_of_cards_(2013)"
    elif serie == "doctor_who_2005":
        return "doctor_who"
    elif serie == "ash_vs_evil_dead":
        return "ash_vs._evil_dead"
    else:
        return serie


def post_process(serie):
    if serie.startswith("Daredevil -"):
        return serie.replace("Daredevil -", "Marvel's Daredevil -")
    elif serie.startswith("Doctor Who -"):
        return serie.replace("Doctor Who -", "Doctor Who (2005) -")
    else:
        return serie
