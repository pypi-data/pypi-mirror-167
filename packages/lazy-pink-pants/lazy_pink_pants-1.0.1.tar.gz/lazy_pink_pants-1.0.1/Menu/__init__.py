#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class LazyBalikaMenu:

    def __init__(self, options:list) -> None:

        """
        Print options from the options list and ask for select one by the number in the beginning of the line.
        
        If an option is selected it executes its the function.

        If there is no option selected or selected option not exists it ask selecting again.

        Example options list:

            options = [
                {
                    "text": "Print Hello World",
                    "function": print_hello_world,
                },
                {
                    "text": "Kilépés",
                    "function": exit,
                },
            ]
        """

        self.options = options
        option_number = 1
        
        try:
            print("\nKérlek válassz az alábbi lehetőségek közül:")
            for option in options:
                print(f"{str(option_number)}) {option['text']}")
                option_number = option_number + 1 
            selected_query = input("> ")
            index_of_selected_query = int(selected_query) - 1
            options[index_of_selected_query]["function"]()
        except IndexError:
            self.error_handler(error_message="[!] Hiba: Választásod nincs a lehetőségek között!")
        except ValueError:
            self.error_handler(error_message="[!] Hiba: Nem választottál!")


    def error_handler(self, error_message) -> None:

        """
        It handels wrong selections.

        It prints what the problem is than a manual about how to use the menu app.

        After all it asks again for select an option for options list and the cicle starts again.
        """

        how_to_use_message = "[*] Kérlek írd be a használni kívánt funkció előtti számot, majd üss Enter-t!\n"
        print(f"\n{error_message}")
        print(how_to_use_message)
        LazyBalikaMenu(options=self.options)
