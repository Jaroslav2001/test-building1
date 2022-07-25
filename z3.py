from typing import TypedDict, List, Tuple, Literal, TypeAlias, Dict, Optional

Operations: TypeAlias = Tuple[Literal['lesson', 'pupil', 'tutor'], bool]


class IsLesson(TypedDict):
    lesson: int
    pupil: int
    tutor: int


class Lesson(TypedDict):
    lesson: List[int]
    pupil: List[int]
    tutor: List[int]


class LessonTest(TypedDict):
    data: Lesson
    answer: int


def appearance(intervals: Lesson) -> int:
    result = 0
    content: List[int] = []
    content_table: Dict[int, List[Operations]] = dict()

    for i_, j_ in intervals.items():
        i_: Literal['lesson', 'pupil', 'tutor']
        for index, j in enumerate(j_):
            if not(j in content):
                content.append(j)
                content_table[j] = []
            content_table[j].append((i_, not bool(index % 2),))

    content.sort()

    start: Optional[int] = None
    is_lesson: IsLesson = {'lesson': 0, 'pupil': 0, 'tutor': 0}
    for time in content:
        for op in content_table[time]:
            if op[1]:
                is_lesson[op[0]] += 1
            else:
                is_lesson[op[0]] -= 1
        if is_lesson['lesson'] > 0 and is_lesson['pupil'] > 0 and is_lesson['tutor'] > 0 and start is None:
            start = time
        elif (is_lesson['lesson'] == 0 or is_lesson['pupil'] == 0 or is_lesson['tutor'] == 0) and not(start is None):
            result += time - start
            start = None
    return result


tests: List[LessonTest] = [
    {
        'data': {
             'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
        },
        'answer': 3117
    },
    {
        'data': {
            'lesson': [1594702800, 1594706400],
            'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513,
                      1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009,
                      1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773,
                      1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                      1594706524, 1594706524, 1594706579, 1594706641],
            'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]
        },
        'answer': 3577
    },
    {
        'data': {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594692033, 1594696347],
            'tutor': [1594692017, 1594692066, 1594692068, 1594696341]
        },
        'answer': 3565
    },
]


if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
