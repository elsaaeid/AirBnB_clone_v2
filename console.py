#!/usr/bin/python3
"""this the entry point of the command interpreter"""
import cmd
from models import storage, classes
import shlex
import models


class HBNBCommand(cmd.Cmd):
    """this class for the command interpreter"""
    prompt = '(hbnb)'

    def do_EOF(self, arg):
        """EOF is command used to exit the program"""
        return True

    def do_quit(self, arg):
        """quit is command used to exit the program."""
        return True

    def emptyline(self):
        pass

    def do_create(self, args):
        """ Create an object of any class"""
        if not args:
            print("** class name missing **")
            return
        elif args not in classes:
            print("** class doesn't exist **")
            return

        try:
            new_instance = classes[args]()
            storage.save()
            print(new_instance.id)
            storage.save()
        except Exception as e:
            print(f"Error creating instance: {str(e)}")

    def help_create(self):
        """put information for the create method"""
        help_text = """
        Creates an instance of a class.
        [Usage]: create <className>
        Example:
        create MyClass
        """
        print(help_text)

    def do_show(self, arg):
        """Prints the string representation
        of an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """This shows all instances based on class name."""
        my_arg = arg.split(" ")
        if not arg:
            my_list = []
            my_objects = storage.all()
            for value in my_objects.values():
                my_list.append(str(value))
            print(my_list)
        elif my_arg[0] not in classes:
            print("Class doesn't exist")
        else:
            my_list = []
            my_objects = storage.all()
            for value in my_objects.values():
                if value.__class__.__name__ == my_arg[0]:
                    my_list.append(str(value))
            print(my_list)

    def do_update(self, arg):
        """Update an instance based on the class name,
        ID, and dictionary representation"""
        args = shlex.split(arg)
        if len(args) < 3:
            print("** insufficient arguments **")
            return
        class_name, instance_id, *updates = args
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        instance = models.storage.get(class_name, instance_id)
        if instance is None:
            print("** no instance found **")
            return
        try:
            updates_dict = eval("{" + ", ".join(updates) + "}")
        except SyntaxError:
            print("** invalid dictionary representation **")
            return
        for key, value in updates_dict.items():
            if hasattr(instance, key):
                setattr(instance, key, value)
            else:
                print(f"** invalid attribute: {key} **")
                return
        instance.save()
        print("OK")

    def do_count(self, arg):
        """Counts all instances based on class name."""
        count = 0
        my_arg = arg.split(" ")
        if not arg:
            my_list = []
            my_objects = storage.all()
            for key, value in my_objects.items():
                my_list.append(str(value))
            print(my_list)
        elif my_arg[0] not in classes:
            print("** class doesn't exist **")
        else:
            my_objects = storage.all()
            for key, value in my_objects.items():
                my_key = key.split(".")
                if my_key[0] == my_arg[0]:
                    if value.__class__.__name__ == my_arg[0]:
                        count += 1
            print(count)

    def do_BaseModel(self, arg):
        """Sends a command based on the class BaseModel"""
        the_class = "BaseModel"
        my_arg = arg.split(".")
        if my_arg[1] == 'all()':
            self.do_all(the_class)
        elif my_arg[1] == 'count()':
            self.do_count(the_class)
        else:
            command = my_arg[1].split('(')[0]
            if command == "show":
                instance_id = my_arg[1].split('(')[1].split(')')[0]
                param = the_class + " " + instance_id
                self.do_show(param)
            elif command == "destroy":
                instance_id = my_arg[1].split('(')[1].split(')')[0]
                param = the_class + " " + instance_id
                self.do_destroy(param)
            elif command == "update":
                args = my_arg[1].split('(')[1].split(')')[0].split(',')
                if len(args) != 3:
                    print("Invalid update command format")
                else:
                    instance_id = args[0].strip().strip('"')
                    attribute_name = args[1].strip().strip('"')
                    attribute_value = args[2].strip().strip('"')
                    param = "{} {} {} {}".format(
                        the_class,
                        instance_id,
                        attribute_name,
                        attribute_value
                        )
                    self.do_update(param)
            else:
                print("Invalid command")

    def do_User(self, arg):
        """Sends a command based on the class User"""
        the_class = "User"
        my_arg = arg.split(".")
        if my_arg[1] == 'all()':
            self.do_all(the_class)
        elif my_arg[1] == 'count()':
            self.do_count(the_class)
        else:
            command = my_arg[1].split('(')[0]
            if command == "show":
                instance_id = my_arg[1].split('(')[1].split(')')[0]
                param = the_class + " " + instance_id
                self.do_show(param)
            elif command == "destroy":
                instance_id = my_arg[1].split('(')[1].split(')')[0]
                param = the_class + " " + instance_id
                self.do_destroy(param)
            elif command == "update":
                args = my_arg[1].split('(')[1].split(')')[0].split(',')
                if len(args) != 3:
                    print("Invalid update command format")
                else:
                    instance_id = args[0].strip().strip('"')
                    attribute_name = args[1].strip().strip('"')
                    attribute_value = args[2].strip().strip('"')
                    param = "{} {} {} {}".format(
                        the_class,
                        instance_id,
                        attribute_name,
                        attribute_value
                        )
                    self.do_update(param)
            else:
                print("Invalid command")

    def do_State(self, arg):
        """Sends a command based on the class State"""
        the_class = "State"
        my_arg = arg.split(".")
        if my_arg[1] == 'all()':
            self.do_all(the_class)
        elif my_arg[1] == 'count()':
            self.do_count(the_class)
        else:
            command = my_arg[1].split('(')[0]
            if command == "show":
                instance_id = my_arg[1].split('(')[1].split(')')[0]
                param = the_class + " " + instance_id
                self.do_show(param)
            elif command == "destroy":
                instance_id = my_arg[1].split('(')[1].split(')')[0]
                param = the_class + " " + instance_id
                self.do_destroy(param)
            elif command == "update":
                args = my_arg[1].split('(')[1].split(')')[0].split(',')
                if len(args) != 3:
                    print("Invalid update command format")
                else:
                    instance_id = args[0].strip().strip('"')
                    attribute_name = args[1].strip().strip('"')
                    attribute_value = args[2].strip().strip('"')
                    param = "{} {} {} {}".format(
                        the_class,
                        instance_id,
                        attribute_name,
                        attribute_value
                        )
                    self.do_update(param)
            else:
                print("Invalid command")

    def do_City(self, arg):
        """Sends a command based on the class City"""
        the_class = "City"
        my_arg = arg.split(".")
        if my_arg[1] == 'all()':
            self.do_all(the_class)
        elif my_arg[1] == 'count()':
            self.do_count(the_class)
        else:
            command = my_arg[1].split('(')[0]
            if command == "show":
                instance_id = my_arg[1].split('(')[1].split(')')[0]
                param = the_class + " " + instance_id
                self.do_show(param)
            elif command == "destroy":
                instance_id = my_arg[1].split('(')[1].split(')')[0]
                param = the_class + " " + instance_id
                self.do_destroy(param)
            elif command == "update":
                args = my_arg[1].split('(')[1].split(')')[0].split(',')
                if len(args) != 3:
                    print("Invalid update command format")
                else:
                    instance_id = args[0].strip().strip('"')
                    attribute_name = args[1].strip().strip('"')
                    attribute_value = args[2].strip().strip('"')
                    param = "{} {} {} {}".format(
                        the_class,
                        instance_id,
                        attribute_name,
                        attribute_value
                        )
                    self.do_update(param)
            else:
                print("Invalid command")

    def do_Amenity(self, arg):
        """Sends a command based on the class Amenity"""
        the_class = "Amenity"
        my_arg = arg.split(".")
        if my_arg[1] == 'all()':
            self.do_all(the_class)
        elif my_arg[1] == 'count()':
            self.do_count(the_class)
        else:
            command = my_arg[1].split('(')[0]
            if command == "show":
                instance_id = my_arg[1].split('(')[1].split(')')[0]
                param = the_class + " " + instance_id
                self.do_show(param)
            elif command == "destroy":
                instance_id = my_arg[1].split('(')[1].split(')')[0]
                param = the_class + " " + instance_id
                self.do_destroy(param)
            elif command == "update":
                args = my_arg[1].split('(')[1].split(')')[0].split(',')
                if len(args) != 3:
                    print("Invalid update command format")
                else:
                    instance_id = args[0].strip().strip('"')
                    attribute_name = args[1].strip().strip('"')
                    attribute_value = args[2].strip().strip('"')
                    param = "{} {} {} {}".format(
                        the_class,
                        instance_id,
                        attribute_name,
                        attribute_value
                        )
                    self.do_update(param)
            else:
                print("Invalid command")

    def do_Place(self, arg):
        """Sends a command based on the class Place"""
        the_class = "Place"
        my_arg = arg.split(".")
        if my_arg[1] == 'all()':
            self.do_all(the_class)
        elif my_arg[1] == 'count()':
            self.do_count(the_class)
        else:
            command = my_arg[1].split('(')[0]
            if command == "show":
                instance_id = my_arg[1].split('(')[1].split(')')[0]
                param = the_class + " " + instance_id
                self.do_show(param)
            elif command == "destroy":
                instance_id = my_arg[1].split('(')[1].split(')')[0]
                param = the_class + " " + instance_id
                self.do_destroy(param)
            elif command == "update":
                args = my_arg[1].split('(')[1].split(')')[0].split(',')
                if len(args) != 3:
                    print("Invalid update command format")
                else:
                    instance_id = args[0].strip().strip('"')
                    attribute_name = args[1].strip().strip('"')
                    attribute_value = args[2].strip().strip('"')
                    param = "{} {} {} {}".format(
                        the_class,
                        instance_id,
                        attribute_name,
                        attribute_value
                        )
                    self.do_update(param)
            else:
                print("Invalid command")

    def do_Review(self, arg):
        """Sends a command based on the class Review"""
        the_class = "Review"
        my_arg = arg.split(".")
        if my_arg[1] == 'all()':
            self.do_all(the_class)
        elif my_arg[1] == 'count()':
            self.do_count(the_class)
        else:
            command = my_arg[1].split('(')[0]
            if command == "show":
                instance_id = my_arg[1].split('(')[1].split(')')[0]
                param = the_class + " " + instance_id
                self.do_show(param)
            elif command == "destroy":
                instance_id = my_arg[1].split('(')[1].split(')')[0]
                param = the_class + " " + instance_id
                self.do_destroy(param)
            elif command == "update":
                args = my_arg[1].split('(')[1].split(')')[0].split(',')
                if len(args) != 3:
                    print("Invalid update command format")
                else:
                    instance_id = args[0].strip().strip('"')
                    attribute_name = args[1].strip().strip('"')
                    attribute_value = args[2].strip().strip('"')
                    param = "{} {} {} {}".format(
                        the_class,
                        instance_id,
                        attribute_name,
                        attribute_value
                        )
                    self.do_update(param)
            else:
                print("Invalid command")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
