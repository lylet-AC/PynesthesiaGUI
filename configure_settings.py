import utilities


def configure_settings(file_name):

    # list containing the new file to be written
    new_lines = []

    try:
        print("[confset] Loading the file: ", file_name, "...\n")

        with open(file_name) as reader:
            file = reader.readlines()

            for line in file:
                # check if the first character is "#" or " " "
                if line[0] == "#" or line[0] == "\"" or "import" in line or "FOLDER" in line:
                    new_lines.append(line)

                # check if the line is blank
                elif "\n" == line:
                    new_lines.append(line)

                # for TITLES, quotes need to be placed around the lines
                elif "TITLE" in line:
                    line = line.replace("\n", "")
                    value = input("{} = ".format(line[:line.index(" ")]))
                    temp_line = line[:line.index(
                        " ")] + " = \"" + value + "\"\n"

                    new_lines.append(temp_line)

                # all else should be values containing integers
                else:
                    line = line.replace("\n", "")
                    value = input("{} = ".format(line[:line.index(" ")]))
                    temp_line = line[:line.index(" ")] + " = " + value + "\n"

                    new_lines.append(temp_line)

    except IOError:
        print(
            "\n[confset] An IOError occured.  Perhaps the settings file has been removed.\n")

    # print(new_lines)
    utilities.write_file(new_lines, file_name)
