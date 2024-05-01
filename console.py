#!/usr/bin/python3

"""this the entry point of the command interpreter"""

import cmd
import shlex
from models import storage, classes


class HBNBCommand(cmd.Cmd):
    """this class for the command interpreter"""
    prompt = '(hbnb)'
    file = None

    def do_EOF(self, arg):
        """EOF is command used to exit the program"""
        return True

    def do_quit(self, arg):
        """quit is command used to exit the program."""
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """create is command used to create a new instance."""
        if not arg:
            print("class name missing")
        elif arg in classes:
            for key, value in classes.items():
                if key == arg:
                    new_instance = classes[key]()
            storage.save()
            print(new_instance.id)
        else:
            print("class doesn't exist")

    def do_show(self, arg):
        """show is a command used for an existing instance."""
        my_arg = arg.split(" ")
        if not arg:
            print("class name missing")
        elif len(my_arg) < 2:
            print("instance id missing")
        elif my_arg[0] not in classes:
            print("class doesn't exist")
        else:
            try:
                my_objects = self.all(classes[my_arg[0]])
                my_key = "{}.{}".format(my_arg[0], my_arg[1])
                if my_key in my_objects:
                    print(my_objects[my_key])
                else:
                    print("no instance found")
            except IndexError:
                print("instance id missing")

    def do_destroy(self, arg):
        """This deletes an instance based on class and id."""

        my_arg = arg.split(" ")
        if not arg:
            print("class name missing")
        elif my_arg[0] not in classes:
            print("class doesn't exist")
        elif len(my_arg) >= 1:
            try:
                my_objects = storage.all(self)
                my_key = my_arg[0] + "." + my_arg[1]
                try:
                    my_objects.pop(my_key)
                    storage.save()
                except KeyError:
                    print("no instance found")
            except IndexError:
                print("instance id missing")

    def do_all(self, arg):
        """This shows all instances based on class name."""

        my_arg = arg.split(" ")
        if not arg:
            my_list = []
            my_objects = storage.all(self)
            for key, values in my_objects.items():
                my_list.append(str(values))
            print(my_list)
        elif my_arg[0] not in classes:
            print("class doesn't exist")
        else:
            my_list = []
            my_objects = storage.all(self)
            for key, values in my_objects.items():
                my_key = key.split(".")
                if my_key[0] == my_arg[0]:
                    my_list.append(str(values))
            print(my_list)

    def do_update(self, arg):
        """This updates the instances based on class name and id."""

        my_arg = shlex.split(arg)
        if len(my_arg) == 0:
            print("class name missing")
        elif len(my_arg) == 1:
            print("instance id missing")
        elif len(my_arg) == 2:
            print("attribute name missing")
        elif len(my_arg) == 3:
            print("value missing")
        elif my_arg[0] not in classes:
            print("class doesn't exist")
        else:
            my_objects = storage.all(self)
            my_key = my_arg[0] + "." + my_arg[1]
            flag = 0
            for key, values in my_objects.items():
                if key == my_key:
                    flag = 1
                    my_values = my_objects.get(key)
                    setattr(values, my_arg[2], my_arg[3])
                    values.save()
                    print(my_values)
            if flag == 0:
                print("no instance found")

    def do_count(self, arg):
        """This counts all instances based on class name."""
        count = 0
        my_arg = arg.split(" ")
        if not arg:
            my_objects = storage.all(self)
            for key, values in my_objects.items():
                my_list.append(str(values))
            print(my_list)
        elif my_arg[0] not in classes:
            print("class doesn't exist")
        else:
            my_list = []
            my_objects = storage.all(self)
            for key, values in my_objects.items():
                my_key = key.split(".")
                if my_key[0] == my_arg[0]:
                    count += 1
            print(count)

    def do_BaseModel(self, arg):
        """This sends command based on class BaseModel."""

        the_class = "BaseModel"
        my_arg = arg.split(".")
        if my_arg[1] == 'all()':
            HBNBCommand.do_all(HBNBCommand, the_class)
        elif my_arg[1] == 'count()':
            HBNBCommand.do_count(HBNBCommand, the_class)
        else:
            prim = my_arg[1].find('("')
            seco = my_arg[1].find('")')
            my_arg1 = my_arg[1][0:prim]
            my_arg2 = my_arg[1][prim + 2: seco]
            if my_arg1 == "show":
                param = the_class + " " + my_arg2
                HBNBCommand.do_show(HBNBCommand, param)
            elif my_arg1 == "destroy":
                param = the_class + " " + my_arg2
                HBNBCommand.do_destroy(HBNBCommand, param)
            else:
                my_arg3 = arg
                my_arg3 = my_arg3.replace('"', ' ')
                my_arg3 = my_arg3.split(',')
                if len(my_arg3) == 0:
                    print("instance id missing")
                elif len(my_arg3) == 1:
                    print("attribute name missing")
                elif len(my_arg3) == 2:
                    print("value missing")
                else:
                    param = ("{} {} {} {}".format(the_class, my_arg3[0][9:],
                             my_arg3[1], my_arg3[2][1:-1]))
                    HBNBCommand.do_update(HBNBCommand, param)

    def do_User(self, arg):
        """This sends command based on class user."""

        the_class = "User"
        my_arg = arg.split(".")
        if my_arg[1] == 'all()':
            HBNBCommand.do_all(HBNBCommand, the_class)
        elif my_arg[1] == 'count()':
            HBNBCommand.do_count(HBNBCommand, the_class)
        else:
            prim = my_arg[1].find('("')
            seco = my_arg[1].find('")')
            my_arg1 = my_arg[1][0:prim]
            my_arg2 = my_arg[1][prim + 2: seco]
            if my_arg1 == "show":
                param = the_class + " " + my_arg2
                HBNBCommand.do_show(HBNBCommand, param)
            elif my_arg1 == "destroy":
                param = the_class + " " + my_arg2
                HBNBCommand.do_destroy(HBNBCommand, param)
            else:
                my_arg3 = arg
                my_arg3 = my_arg3.replace('"', ' ')
                my_arg3 = my_arg3.split(',')
                if len(my_arg3) == 0:
                    print("instance id missing")
                elif len(my_arg3) == 1:
                    print("attribute name missing")
                elif len(my_arg3) == 2:
                    print("value missing")
                else:
                    param = ("{} {} {} {}".format(the_class, my_arg3[0][9:],
                             my_arg3[1], my_arg3[2][1:-1]))
                    HBNBCommand.do_update(HBNBCommand, param)

    def do_State(self, arg):
        """This sends command based on class Statei."""

        the_class = "State"
        my_arg = arg.split(".")
        if my_arg[1] == 'all()':
            HBNBCommand.do_all(HBNBCommand, the_class)
        elif my_arg[1] == 'count()':
            HBNBCommand.do_count(HBNBCommand, the_class)
        else:
            prim = my_arg[1].find('("')
            seco = my_arg[1].find('")')
            my_arg1 = my_arg[1][0:prim]
            my_arg2 = my_arg[1][prim + 2: seco]
            if my_arg1 == "show":
                param = the_class + " " + my_arg2
                HBNBCommand.do_show(HBNBCommand, param)
            elif my_arg1 == "destroy":
                param = the_class + " " + my_arg2
                HBNBCommand.do_destroy(HBNBCommand, param)
            else:
                my_arg3 = arg
                my_arg3 = my_arg3.replace('"', ' ')
                my_arg3 = my_arg3.split(',')
                if len(my_arg3) == 0:
                    print("instance id missing")
                elif len(my_arg3) == 1:
                    print("attribute name missing")
                elif len(my_arg3) == 2:
                    print("value missing")
                else:
                    param = ("{} {} {} {}".format(the_class, my_arg3[0][9:],
                             my_arg3[1], my_arg3[2][1:-1]))
                    HBNBCommand.do_update(HBNBCommand, param)

    def do_City(self, arg):
        """This sends command based on class City."""

        the_class = "City"
        my_arg = arg.split(".")
        if my_arg[1] == 'all()':
            HBNBCommand.do_all(HBNBCommand, the_class)
        elif my_arg[1] == 'count()':
            HBNBCommand.do_count(HBNBCommand, the_class)
        else:
            prim = my_arg[1].find('("')
            seco = my_arg[1].find('")')
            my_arg1 = my_arg[1][0:prim]
            my_arg2 = my_arg[1][prim + 2: seco]
            if my_arg1 == "show":
                param = the_class + " " + my_arg2
                HBNBCommand.do_show(HBNBCommand, param)
            elif my_arg1 == "destroy":
                param = the_class + " " + my_arg2
                HBNBCommand.do_destroy(HBNBCommand, param)
            else:
                my_arg3 = arg
                my_arg3 = my_arg3.replace('"', ' ')
                my_arg3 = my_arg3.split(',')
                if len(my_arg3) == 0:
                    print("instance id missing")
                elif len(my_arg3) == 1:
                    print("attribute name missing")
                elif len(my_arg3) == 2:
                    print("value missing")
                else:
                    param = ("{} {} {} {}".format(the_class, my_arg3[0][9:],
                             my_arg3[1], my_arg3[2][1:-1]))
                    HBNBCommand.do_update(HBNBCommand, param)

    def do_Amenity(self, arg):
        """This sends command based on class Amenity."""

        the_class = "Amenity"
        my_arg = arg.split(".")
        if my_arg[1] == 'all()':
            HBNBCommand.do_all(HBNBCommand, the_class)
        elif my_arg[1] == 'count()':
            HBNBCommand.do_count(HBNBCommand, the_class)
        else:
            prim = my_arg[1].find('("')
            seco = my_arg[1].find('")')
            my_arg1 = my_arg[1][0:prim]
            my_arg2 = my_arg[1][prim + 2: seco]
            if my_arg1 == "show":
                param = the_class + " " + my_arg2
                HBNBCommand.do_show(HBNBCommand, param)
            elif my_arg1 == "destroy":
                param = the_class + " " + my_arg2
                HBNBCommand.do_destroy(HBNBCommand, param)
            else:
                my_arg3 = arg
                my_arg3 = my_arg3.replace('"', ' ')
                my_arg3 = my_arg3.split(',')
            if len(my_arg3) == 0:
                print("instance id missing")
            elif len(my_arg3) == 1:
                print("attribute name missing")
            elif len(my_arg3) == 2:
                print("value missing")
            else:
                param = ("{} {} {} {}".format(the_class, my_arg3[0][9:],
                         my_arg3[1], my_arg3[2][1:-1]))
                HBNBCommand.do_update(HBNBCommand, param)

    def do_Place(self, arg):
        """This sends command based on class Placei."""

        the_class = "Place"
        my_arg = arg.split(".")
        if my_arg[1] == 'all()':
            HBNBCommand.do_all(HBNBCommand, the_class)
        elif my_arg[1] == 'count()':
            HBNBCommand.do_count(HBNBCommand, the_class)
        else:
            prim = my_arg[1].find('("')
            seco = my_arg[1].find('")')
            my_arg1 = my_arg[1][0:prim]
            my_arg2 = my_arg[1][prim + 2: seco]
            if my_arg1 == "show":
                param = the_class + " " + my_arg2
                HBNBCommand.do_show(HBNBCommand, param)
            elif my_arg1 == "destroy":
                param = the_class + " " + my_arg2
                HBNBCommand.do_destroy(HBNBCommand, param)
            else:
                my_arg3 = arg
                my_arg3 = my_arg3.replace('"', ' ')
                my_arg3 = my_arg3.split(',')
                if len(my_arg3) == 0:
                    print("instance id missing")
                elif len(my_arg3) == 1:
                    print("attribute name missing")
                elif len(my_arg3) == 2:
                    print("value missing")
                else:
                    param = ("{} {} {} {}".format(the_class, my_arg3[0][9:],
                             my_arg3[1], my_arg3[2][1:-1]))
                    HBNBCommand.do_update(HBNBCommand, param)

    def do_Review(self, arg):
        """This sends command based on class Review"""

        the_class = "Review"
        my_arg = arg.split(".")
        if my_arg[1] == 'all()':
            HBNBCommand.do_all(HBNBCommand, the_class)
        elif my_arg[1] == 'count()':
            HBNBCommand.do_count(HBNBCommand, the_class)
        else:
            prim = my_arg[1].find('("')
            seco = my_arg[1].find('")')
            my_arg1 = my_arg[1][0:prim]
            my_arg2 = my_arg[1][prim + 2: seco]
            if my_arg1 == "show":
                param = the_class + " " + my_arg2
                HBNBCommand.do_show(HBNBCommand, param)
            elif my_arg1 == "destroy":
                param = the_class + " " + my_arg2
                HBNBCommand.do_destroy(HBNBCommand, param)
            else:
                my_arg3 = arg
                my_arg3 = my_arg3.replace('"', ' ')
                my_arg3 = my_arg3.split(',')
                if len(my_arg3) == 0:
                    print("instance id missing")
                elif len(my_arg3) == 1:
                    print("attribute name missing")
                elif len(my_arg3) == 2:
                    print("value missing")
                else:
                    param = ("{} {} {} {}".format(the_class, my_arg3[0][9:],
                             my_arg3[1], my_arg3[2][1:-1]))
                    HBNBCommand.do_update(HBNBCommand, param)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
