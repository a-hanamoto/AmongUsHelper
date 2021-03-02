import itertools

from ah_yacc import parse


class InferenceResult:
    def __init__(self, innocent, guilty, candidates):
        self.innocent = innocent
        self.guilty = guilty
        self.candidates = candidates

    def get_output_str(self):
        ret_list = []
        innocent_str = ", ".join(self.innocent) if self.innocent else "NONE"
        guilty_str = ", ".join(self.guilty) if self.guilty else "NONE"
        ret_list.append(f"CLEARLY CREWMATE: {innocent_str}")
        ret_list.append(f"CLEARLY IMPOSTER: {guilty_str}")
        ret_list.append("POSSIBLE IMPOSTERS:")
        for imps, dead_list in self.candidates:
            ret_list.append(
                f"{', '.join(imps)} -> {', '.join(map(dead_info_to_str, dead_list))}"
            )
        return "\n".join(ret_list)


def dead_info_to_str(dead_info):
    return f"{' or '.join(sorted(dead_info[1]))} killed {dead_info[0]}"


def check_trust(alive_imps, crews, killer, non_killer, member_from, member_to):
    if member_from & crews:
        non_killer.update(non_killer | (member_to & alive_imps))
        if len(alive_imps) == len(non_killer) or killer & non_killer:
            return False
    return True


def check_doubt(alive_imps, crews, killer, non_killer, member_from, member_to):
    if member_from & crews:
        if len(member_to) > 1:
            return False
        if (crews | non_killer) & member_to:
            return False
        if killer and not (killer & member_to):
            return False
        killer.update(member_to)
    return True


def check(imps, crews, meetings_info):
    num_left = len(imps) + len(crews)
    ejected = set()
    alive_imps = imps.copy()
    killer_info = []
    for meeting in meetings_info:
        killer = set()
        non_killer = set()
        if meeting.dead_info is not None:
            if meeting.dead_info in imps:
                return False
            num_left -= 1
            if num_left <= 4 and len(ejected & imps) == 0:
                return False
        if meeting.testimonies is not None:
            for testimony in meeting.testimonies:
                member_from = set(testimony.member_from)
                member_to = set(testimony.member_to)
                if testimony.testimony_type == "trust":
                    if not check_trust(
                        alive_imps, crews, killer, non_killer, member_from, member_to
                    ):
                        return False
                else:
                    if not check_doubt(
                        alive_imps, crews, killer, non_killer, member_from, member_to
                    ):
                        return False
        if meeting.dead_info is not None:
            killer_candidate = killer if killer else alive_imps - non_killer
            killer_info.append((meeting.dead_info, killer_candidate))
        if meeting.conclusion is not None:
            ejected.add(meeting.conclusion)
            alive_imps -= set(meeting.conclusion)
            num_left -= 1
            if num_left <= 4 and len(ejected & imps) == 0:
                return False
    return killer_info


def infer(input_data):
    participants, meetings_info = parse(input_data)
    participants_set = set(sorted(participants))
    num_participants = len(participants)
    innocent = participants_set.copy()
    guilty = participants_set.copy()
    candidates = []
    for imps in itertools.combinations(participants, 2):
        imps_set = set(imps)
        crews_set = participants_set - imps_set
        killer_info = check(imps_set, crews_set, meetings_info)
        if killer_info:
            innocent = innocent & (participants_set - imps_set)
            guilty = guilty & imps_set
            candidates.append((imps, killer_info))
    res = InferenceResult(innocent, guilty, candidates)
    return res.get_output_str()


if __name__ == "__main__":
    with open("./data.txt") as f:
        input_data = f.read()
    print(infer(input_data))
