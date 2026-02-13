class CourseIterator:
    def __init__(self, courses):
        self._courses = courses
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._courses):
            raise StopIteration
        course = self._courses[self._index]
        self._index += 1
        return course


def student_batch_generator(students, batch_size=1):
    print("Fetching Student Records...")
    for i in range(0, len(students), batch_size):
        yield students[i:i + batch_size]
