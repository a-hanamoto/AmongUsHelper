import itertools

from ah_yacc import yacc_input


def check(imps_set, crews_set, meetings_info):
    num_left = len(imps_set) + len(crews_set)
    ejected = set()
    for meeting in meetings_info:
        if meeting.dead_info is not None:
            if meeting.dead_info in imps_set:
                return False
            num_left -= 1
            if num_left <= 4 and len(ejected & imps_set) == 0:
                return False
        if meeting.testimonies is not None:
            for testimony in meeting.testimonies:
                member_from_set = set(testimony.member_from)
                member_to_set = set(testimony.member_to)
                if testimony.testimony_type == "trust":
                    if (
                        len(member_from_set & crews_set) != 0
                        and len(member_to_set & imps_set) != 0
                    ):
                        return False
                else:
                    if len(member_from_set & crews_set) != 0 and len(member_to_set & imps_set) != len(member_to_set):
                        return False
        if meeting.conclusion is not None:
            ejected.add(meeting.conclusion)
            num_left -= 1
            if num_left <= 4 and len(ejected & imps_set) == 0:
                return False
    return True


def main():
    participants, meetings_info = yacc_input()
    participants_set = set(participants)
    num_participants = len(participants)
    for imps in itertools.combinations(participants, 2):
        imps_set = set(imps)
        crews_set = participants_set - imps_set
        if check(imps_set, crews_set, meetings_info):
            print(imps_set)


if __name__ == "__main__":
    main()
