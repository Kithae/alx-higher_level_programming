#!/usr/bin/python3
"""module defining class base model."""
import json
import turtle
import csv


class Base:
    """base model representation.
    This is the "base" for all project 0x0C classes.
    Attributes:
        __nb_objects (int): total instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """new Base initialization.
        Args:
            id (int): new Base identity.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return dictionaries list with a JSON serialization.
        Args:
            list_dictionaries (list): dictionaries list.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes an objects list with a JSON serialization to a file.
        Args:
            list_objs (list): inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [a.to_dictionary() for a in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return JSON string deserialization.
        Args:
            json_string (str): dictionaries list represented by JSON string.
        Returns:
            empty list, else a json_string python list.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return attribute dictionary class.
        Args:
            **dictionary (dict): attributes values to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                curr = cls(1, 1)
            else:
                curr = cls(1)
            curr.update(**dictionary)
            return curr

    @classmethod
    def load_from_file(cls):
        """Return JSON strings instantiated classes list.
        Reads from `<cls.__name__>.json`.
        Returns:
            an empty list, else, instantiated classes list
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**a) for a in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write objects list CSV serialization to file.
        Args:
            list_objs (list): Base instances list - inherited.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for item in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([a, int(b)] for a, b in c.items())
                              for c in list_dicts]
                return [cls.create(**c) for c in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """uses turtle mode to draw square and rectangle.
        Args:
            list_rectangles (list): Rectangle objects list.
            list_squares (list): Square objects list.
        """
        ntur = turtle.Turtle()
        ntur.screen.bgcolor("#b7312c")
        ntur.pensize(3)
        ntur.shape("turtle")

        ntur.color("#ffffff")
        for nrec in list_rectangles:
            ntur.showturtle()
            ntur.up()
            ntur.goto(rect.x, rect.y)
            ntur.down()
            for a in range(2):
                ntur.forward(rect.width)
                ntur.left(90)
                ntur.forward(rect.height)
                ntur.left(90)
            ntur.hideturtle()

        ntur.color("#b5e3d8")
        for nsq in list_squares:
            ntur.showturtle()
            ntur.up()
            ntur.goto(sq.x, sq.y)
            ntur.down()
            for a in range(2):
                ntur.forward(sq.width)
                ntur.left(90)
                ntur.forward(sq.height)
                ntur.left(90)
            ntur.hideturtle()

        turtle.exitonclick()
