import ply.yacc as yacc
from ah_lex import tokens

participants = []
meetings_info = []
error_msg = ""


class Testimony:
    def __init__(self, testimony_type, member_from, member_to):
        self.testimony_type = testimony_type
        self.member_from = member_from
        self.member_to = member_to


class Meeting:
    def __init__(self, dead_info, testimonies, conclusion):
        self.dead_info = dead_info
        self.testimonies = testimonies
        self.conclusion = conclusion


def p_data(p):
    """
    data : participants SEMI meetings SEMI
    """
    global participants
    participants = p[1]
    global meetings_info
    meetings_info = p[3]


def p_participants(p):
    """
    participants : members
    """
    p[0] = p[1]


def p_members(p):
    """
    members : MEMBER
            | members COMMA MEMBER
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_meetings(p):
    """
    meetings : meeting
             | meetings SEMI meeting
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_meeting(p):
    """
    meeting : dead_info SEMI conclusion
            | dead_info SEMI testimonies SEMI conclusion
    """
    if len(p) == 4:
        p[0] = Meeting(p[1], None, p[3])
    else:
        p[0] = Meeting(p[1], p[3], p[5])


def p_dead_info(p):
    """
    dead_info : DEAD NONE
              | DEAD MEMBER
    """
    if p[2] == "none":
        p[0] = None
    else:
        p[0] = p[2]


def p_testimonies(p):
    """
    testimonies : testimony
                | testimonies SEMI testimony
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_testimony(p):
    """
    testimony : members TRUST members
              | members DOUBT members
    """
    p[0] = Testimony(p[2], p[1], p[3])


def p_conclusion(p):
    """
    conclusion : SKIP
               | EJECT MEMBER
    """
    if len(p) == 2:
        p[0] = None
    else:
        p[0] = p[2]


def p_error(p):
    global error_msg
    error_msg = f"Error occured at {p}"


start = "data"
parser = yacc.yacc()


def parse(input_str):
    global participants, meetings_info, error_msg
    participants = []
    meetings_info = []
    error_msg = None
    yacc.parse(input_str)
    return participants, meetings_info, error_msg
