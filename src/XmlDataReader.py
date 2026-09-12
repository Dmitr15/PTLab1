# -*- coding: utf-8 -*-
import re
from Types import DataType
from DataReader import DataReader


class XmlDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            content = file.read()

        # убираем XML-декларацию и комментарии
        content = re.sub(r'<\?.*?\?>', '', content, flags=re.DOTALL)
        content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)

        # вытаскиваем содержимое <root> ... </root>
        root_m = re.search(r'<root>\s*(.*?)\s*</root>',
                           content, flags=re.DOTALL)
        body = root_m.group(1) if root_m else content

        # студент: <ФИО> ... </ФИО>
        student_re = re.compile(r'<([^/][^<>]*)>\s*(.*?)\s*</\1>',
                                re.DOTALL)
        # предмет: <предмет>оценка</предмет>
        subject_re = re.compile(r'<([^/][^<>]*)>([^<>]*)</\1>')

        for m in student_re.finditer(body):
            name = m.group(1).strip()
            subjects = []
            for sm in subject_re.finditer(m.group(2)):
                subject = sm.group(1).strip()
                score = int(sm.group(2).strip())
                subjects.append((subject, score))
            self.students[name] = subjects

        return self.students
