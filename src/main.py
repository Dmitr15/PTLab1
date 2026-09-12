import argparse
import sys
from CalcRating import CalcRating
from TextDataReader import TextDataReader
from XmlDataReader import XmlDataReader
from CountDebtors import CountDebtors


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str,
                        required=True, help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    match path.split(".")[-1]:
        case "txt":
            reader = TextDataReader()
        case "xml":
            reader = XmlDataReader()
        case _:
            raise TypeError("Unknown file type")
    students = reader.read(path)
    print("Students: ", students)
    rating = CalcRating(students).calc()
    print("Rating: ", rating)
    debtors_count = CountDebtors(students).calc()
    print("Students with exactly 2 debts: ", debtors_count)


if __name__ == "__main__":
    main()
