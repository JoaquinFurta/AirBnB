#!/usr/bin/python3
"""console"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt ="(hbnb) "


    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """End of file"""
        print()
        return True

    def emptyline(self):
        """emptyline"""
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
            return
        if arg != "BaseModel":
            print("** class doesn't exist **")
            return
        else:
            inst = BaseModel()
            storage.save()
            print(inst.id)

    def do_show(self, arg):
        argg = arg.split()
        if not argg:
            print("** class name missing **")
            return
        if argg[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(argg) == 1:
            print("** instance id missing **")
            return
        strr = str(argg[0]) + "." + str(argg[1])
        print(strr)
        print("-------------------------")
        if strr in storage.all():
            print(storage.all()[strr])
        else:
            print("** no instance found **")





if __name__ == '__main__':
    HBNBCommand().cmdloop()
